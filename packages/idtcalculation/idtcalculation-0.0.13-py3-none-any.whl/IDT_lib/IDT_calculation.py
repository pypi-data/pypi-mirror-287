import sys
import numpy as np
import cantera as ct
import scipy.integrate as s
from species          import mech_substance_list_or_array
from thermo_real      import from_x_substance_to_composition
from thermo_structure import thermo_structure
from virial_structure import virial_structure, virial_structure_from_np, lambdify_list_generate
R = 8.3144

sys.setrecursionlimit(3000)
deep = sys.getrecursionlimit() 

#%% 

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

#%%
def mole_fraction_change_0toX(mech_name_np, mech_zero_np, substance_np, mole_fraction_np):
    
    loc = 0
    for substance in substance_np:        
        substance_index = np.where(mech_name_np == substance)   
        mech_zero_np[substance_index] = mole_fraction_np[loc]
        
        loc=loc+1
    
    return mech_zero_np

#%%
def ignition_delay_P(dpdt_np, t_np):
    
    dpdt_max       = max(dpdt_np)
    dpdt_max_index = np.where(dpdt_np == dpdt_max)
    IDT_P          = t_np[dpdt_max_index][0]

    return IDT_P

def ignition_delay_OH(substance, G_Xi, t_np):
    
    OH_index = np.where(substance == 'OH')
    OH_loc   = OH_index[0]
    OH_np    = G_Xi[:,OH_loc]
    OH_max       = max(OH_np)
    OH_max_index = np.where(OH_np == OH_max)
    IDT_OH       = t_np[OH_max_index][0]
    
    return IDT_OH

#%% 

def gas_reactor_generator(gas_solution, IG_or_RK, substance, dVdt_set, T_value, p_value, Xi_value):
    
    gas_solution.TPX = T_value, p_value, from_x_substance_to_composition(substance, Xi_value)   
    
    if dVdt_set == 0:
        if   IG_or_RK == 'IG':
            gas_reactor = ct.IdealGasReactor(contents=gas_solution, name="IG_Reactor")  
        elif IG_or_RK == 'RK':
            gas_reactor = ct.Reactor(contents=gas_solution, name="RK_Reactor")
    else:
        print('use other gas reactor')
    
    return gas_reactor

#%% 
    
def input_constant(gas_IG_solution, substance, dVdt_set, Xi_value, n_0):
    
    gas_IG_reactor    = gas_reactor_generator(gas_IG_solution, 'IG', substance, dVdt_set, 1000, 10**5, Xi_value)   
    species_name_list = gas_IG_reactor.thermo.species_names  
    species_name      = np.asarray(species_name_list)          
    species_number    = len(species_name)
    
    Mi     = gas_IG_reactor.thermo.molecular_weights     / 1000    
    ave_M  = gas_IG_reactor.thermo.mean_molecular_weight / 1000    
    m_0     = n_0 * ave_M                                          
        
    return species_name, species_number, m_0, Mi
   
#%% 

def unit_transfer(virial_order, Bn_np, dBdT1_np, dBdT2_np, dBdXi_np, dBdTXi_np):
    
    for order in range(2, virial_order+1):
        Bn_np[order-2]     = Bn_np[order-2]     / 10**(6*(order-1))
        dBdT1_np[order-2]  = dBdT1_np[order-2]  / 10**(6*(order-1))
        dBdT2_np[order-2]  = dBdT2_np[order-2]  / 10**(6*(order-1))
        dBdXi_np[order-2]  = dBdXi_np[order-2]  / 10**(6*(order-1))
        dBdTXi_np[order-2] = dBdTXi_np[order-2] / 10**(6*(order-1))
    
    return Bn_np, dBdT1_np, dBdT2_np, dBdXi_np, dBdTXi_np

#%% 

def virial_thermo(mech_name, virial_order, thermo_ref_set, substance, substance_rank, Bn_fun, dBdT1_fun, dBdT2_fun, dBdX_fun, dBdTX_fun, Xi_value, T_value, v__value):
    
    Bn_np, dBdT1_np, dBdT2_np, dBdXi_np, dBdTXi_np = virial_structure(substance, substance_rank, Bn_fun, dBdT1_fun, dBdT2_fun, dBdX_fun, dBdTX_fun, Xi_value, T_value) 
                                                         
    p_value, Z, h_dep, cp_dep, h_ig_, cp_ig_, h_, cp_ \
        = thermo_structure(mech_name, thermo_ref_set, Bn_np, dBdT1_np, dBdT2_np, substance, Xi_value, T_value, v__value)   
                      
    Bn_np, dBdT1_np, dBdT2_np, dBdXi_np, dBdTXi_np = unit_transfer(virial_order, Bn_np, dBdT1_np, dBdT2_np, dBdXi_np, dBdTXi_np)     
    
    return Bn_np, dBdT1_np, dBdT2_np, dBdXi_np, dBdTXi_np, p_value, Z, h_dep, cp_dep, h_ig_, cp_ig_, h_, cp_

#%% 

def input_ODE(mech_name, gas_IG_solution, gas_RK_solution, virial_order, thermo_ref_set, substance, substance_rank, Bn_fun, dBdT1_fun, dBdT2_fun, dBdX_fun, dBdTX_fun, dVdt_set, n, T, V, Xi, Mi):   

    v__   = V*10**6 / n    
    ave_M = sum(Xi*Mi)

    Bn_np, dBdT1_np, dBdT2_np, dBdXi_np, dBdTXi_np, p, Z, h_dep, cp_dep, h_ig_, cp_ig_, h_, cp_ = \
        virial_thermo(mech_name, virial_order, thermo_ref_set, substance, substance_rank, Bn_fun, dBdT1_fun, dBdT2_fun, dBdX_fun, dBdTX_fun, Xi, T, v__)

    gas_RK_reactor = gas_reactor_generator(gas_RK_solution, 'RK', substance, dVdt_set, T, p, Xi)      
    wi             = gas_RK_reactor.kinetics.net_production_rates * 1000  
    
    hi_ig_ = []
    for substance_i in substance:
        gas_IG_reactor_i = gas_reactor_generator(gas_IG_solution, 'IG', np.array([substance_i]), dVdt_set, T, p, np.array([1]))
        hi_ideal_        = gas_IG_reactor_i.thermo.enthalpy_mole / 1000      # J/mole
        hi_ig_.append(hi_ideal_)
    hi_ig_ = np.array(hi_ig_)
    
    return Bn_np, dBdT1_np, dBdXi_np, dBdTXi_np, ave_M, p, Z, h_dep, cp_dep, h_ig_, cp_ig_, h_, cp_, hi_ig_, wi

#%% 

def C_fun(virial_order, C8, dVdt_set, dQdt_set, dndt, dXidt, n, T, V, Bn_np, dBdT1_np, dBdXi_np, dBdTXi_np, h_, hi_ig_, wi):

    v_      = V/n
    mediate = dndt*V - n*dVdt_set
    dv_dt   = -mediate / n**2
    
    C6 = sum(hi_ig_*dXidt)
        
    C2    = 0
    C3    = mediate / V**2
    C5    = 0   
    C7_in = 0    
    for k in range(2,virial_order+1):       
        Bk     = Bn_np[k-2]
        dBkdX  = dBdXi_np[k-2]
        dBkdT1 = dBdT1_np[k-2]
        dBkdTX = dBdTXi_np[k-2]
            
        C2_loop  = dBkdT1 / v_**k
        C2       = C2 + C2_loop
        
        C3_loop1 = k*Bk*n**(k-1) * mediate        
        C3_loop2 = n**k*V*sum(dBkdX*dXidt)       
        C3       = C3 + (C3_loop1 + C3_loop2) / V**(k+1) 
        
        C5_loop  = (T*dBkdT1 - (k-1)*Bk) / v_**k
        C5       = C5 + C5_loop
        
        C7_loop  = (dBkdX - T/(k-1)*dBkdTX) / v_**(k-1)
        C7_in    = C7_in + C7_loop
    
    C7 = sum(dXidt*C7_in)
    C4 = R*T*dv_dt*C5 + C6 + R*T*C7
    C1 = C4/v_ + h_*C8 - 1/V*dQdt_set

    return float(C1), float(C2), float(C3), float(C4), float(C5), float(C6), float(C7), v_

#%% 

def virial_ODEs(t, y, mech_name, est_IDT, gas_IG_solution, gas_RK_solution, virial_order, thermo_ref_set, substance, substance_rank, Bn_fun, dBdT1_fun, dBdT2_fun, dBdX_fun, dBdTX_fun, dmdt_set, dVdt_set, dQdt_set, Mi, fuel):
    
    m  = y[0]
    V  = y[1]
    n  = y[2]
    Xi = y[3:56]
    T  = y[56]
    p  = y[57]
    
    dmdt = dmdt_set 
    dVdt = dVdt_set                   
                                                        
    Bn_np, dBdT1_np, dBdXi_np, dBdTXi_np, ave_M, p, Z, h_dep, cp_dep, h_ig_, cp_ig_, h_, cp_, hi_ig_, wi \
                = input_ODE(mech_name, gas_IG_solution, gas_RK_solution, virial_order, thermo_ref_set, substance, substance_rank, Bn_fun, dBdT1_fun, dBdT2_fun, dBdX_fun, dBdTX_fun, dVdt_set, n, T, V, Xi, Mi)
    C8 = sum(wi)
    
    dndt  = dmdt/ave_M + V*C8   
    dXidt = V/n * (wi - Xi*C8)     
    
    C1,C2,C3,C4,C5,C6,C7, v_ = C_fun(virial_order, C8, dVdt_set, dQdt_set, dndt, dXidt, n, T, V, Bn_np, dBdT1_np, dBdXi_np, dBdTXi_np, h_, hi_ig_, wi)  
    
    dTdt  = (C1 - R*T*C3) / (p/T + R*T*C2 - cp_/v_)    
    dpdt  = cp_/v_ * dTdt + C1
        
    fun_np1 = np.hstack([dmdt, dVdt, dndt])
    fun_np2 = np.hstack([dTdt, dpdt])
    fun_np  = np.hstack((fun_np1, dXidt, fun_np2)) 
    
    OH_index, O2_index, fuel_index, H2O_index = np.where(substance == 'OH'), np.where(substance == 'O2'), np.where(substance == fuel), np.where(substance == 'H2O')
    OH_X, O2_X, fuel_X, H2O_X = Xi[(OH_index[0]+3)], Xi[(O2_index[0]+3)], Xi[(fuel_index[0]+3)], Xi[(H2O_index[0]+3)]
    
    
    global  G_t, G_infer, G_dpdt, G_h_, G_cp_, \
            G_m, G_V, G_Xi, G_T, G_p, \
            G_OH, G_O2, G_fuel, G_H2O, G_progress
    
    G_infer = G_infer + 1
    if G_infer % 5 == 0:           
        G_t,   G_dpdt       = np.vstack((G_t, t)),       np.vstack((G_dpdt, dpdt))
        G_h_,  G_cp_        = np.vstack((G_h_, h_)),     np.vstack((G_cp_, cp_))
        G_m,   G_V,         = np.vstack((G_m, m)),       np.vstack((G_V, V))
        G_Xi,  G_T,  G_p    = np.vstack((G_Xi, Xi)),     np.vstack((G_T, T)),                np.vstack((G_p, p))
        G_OH,  G_O2, G_fuel = np.vstack((G_OH, OH_X)),   np.vstack((G_O2, O2_X)),            np.vstack((G_fuel, fuel_X))
        G_H2O, G_progress   = np.vstack((G_H2O, H2O_X)), np.vstack((G_progress, t/est_IDT*100))
    
    return fun_np  

#%% 

def calculate(mech_name, tolerance_setting, virial_order, substance, substance_rank, Bn_fun, dBdT1_fun, dBdT2_fun, dBdX_fun, dBdTX_fun, est_IDT, dmdt_set, dVdt_set, dQdt_set, Xi_0, T_0, p_0, V_0, n_0, fuel):
    
    est_IDT, dmdt_set, dVdt_set, dQdt_set, T_0, V_0, n_0 = float(est_IDT), float(dmdt_set), float(dVdt_set), float(dQdt_set), float(T_0), float(V_0), float(n_0)
    
    path_front =  'yaml/'
    path_mid  = str(mech_name)    
    path_mech  = path_front+path_mid+'.yaml'
    
    gas_IG_solution = ct.Solution(path_mech, 'Ideal')    
    gas_RK_solution = ct.Solution(path_mech, 'RK')    
    species_name, species_number, m_0, Mi = input_constant(gas_IG_solution, substance, dVdt_set, Xi_0, n_0)
 
    print(f'initial temperature: {T_0:3e}')
    print(f'initial pressure: {p_0:3e}')
    print(f'initial volume: {V_0:3e}')
    
    t_span = np.arange(0, est_IDT, 1e-7)
    
    thermo_ref_set     = 'ref_point_off'
    
    initial_cond1 = np.array([m_0, V_0, n_0])
    initial_cond2 = np.array([T_0, p_0])
    initial_cond  = np.hstack((initial_cond1, Xi_0, initial_cond2))
        
    res_ODE = s.odeint(virial_ODEs, initial_cond, t_span, rtol=tolerance_setting[0], atol=tolerance_setting[1], tfirst=True, full_output=True, \
            args=(mech_name, est_IDT, gas_IG_solution, gas_RK_solution, virial_order, thermo_ref_set, substance, substance_rank, Bn_fun, dBdT1_fun, dBdT2_fun, dBdX_fun, dBdTX_fun, dmdt_set, dVdt_set, dQdt_set, Mi, fuel,))

    return m_0, Mi, res_ODE, t_span, initial_cond, gas_IG_solution
    
#%% 

if __name__ == '__main__':

    # input set
    mech_name          = 'GRI30'    
    virial_folder_name = 'Virial_GRI30'   
    virial_order       = 6
    
    est_IDT            = 2*10**(-6)   # unit: s
    
    T_0  = 1800        # unit: K
    p_0  = 1000*10**5  # unit: Pa    
    V_0  = 1.0         # unit: m^3 
    v_0_ = 146.3795    # unit: cm^3
    n_0  = V_0*10**6 / v_0_    

    dmdt_value  = 0
    dVdt_value  = 0
    dQdt_value  = 0
    
    fuel     = 'H2'
    oxidizer = 'O2'
    diluent  = 'CO2'
    
    fuel_X     = 0.05
    oxidizer_X = 0.10
    diluent_X  = 0.85
    
    rtol_value = 10**(-13)
    atol_value = 10**(-13)

    substance     = np.array(mech_substance_list_or_array(mech_name, 'name_list'))  
    mech_zero_np  = np.array(mech_substance_list_or_array(mech_name, 'zero_list'))  
    substance_set = np.hstack((np.array(fuel), np.array(oxidizer),  np.array(diluent)))
    mole_frac_set = np.hstack((np.array(fuel_X), np.array(oxidizer_X),  np.array(diluent_X)))
    
    tolerance_setting = [rtol_value, atol_value]   
    Xi_0 = mole_fraction_change_0toX(substance, mech_zero_np, substance_set, mole_frac_set)    
    XT_tup_list = lambdify_list_generate('symbole', 0, Xi_0, substance, substance, T_0)
    
    substance_rank, Bn_fun, dBdT1_fun, dBdT2_fun, dBdX_fun, dBdTX_fun = virial_structure_from_np(virial_folder_name, XT_tup_list, virial_order)
    
    # set global parameter
    G_t,    G_infer      = np.zeros(1),  0
    G_dpdt, G_h_, G_cp_  = np.zeros(1),  np.zeros(1), np.zeros(1)
    G_m,    G_V          = np.zeros(1),  np.zeros(1)
    G_Xi,   G_T,  G_p    = np.zeros(53), np.zeros(1), np.zeros(1)    
    G_OH,   G_O2, G_fuel = np.zeros(1), np.zeros(1), np.zeros(1) 
    G_H2O,  G_progress   = np.zeros(1), np.zeros(1)  
    
    m0, Mi, res_ODE, t_span, initial_cond, gas_IG_solution = calculate(mech_name, tolerance_setting, virial_order, substance, substance_rank, Bn_fun, dBdT1_fun, dBdT2_fun, dBdX_fun, dBdTX_fun, est_IDT, dmdt_value, dVdt_value, dQdt_value, Xi_0, T_0, p_0, V_0, n_0, fuel)
     
    IDT_P  = ignition_delay_P(G_dpdt, G_t)*10**6
    IDT_OH = ignition_delay_OH(substance, G_Xi, G_t)*10**6
            
    print(f'IDT by max dP/dt is {IDT_P:3e}us')
    print(f'IDT by max [OH] is {IDT_OH:3e}us')
    
