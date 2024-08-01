import cantera as ct

NA = 6.02214076 * pow(10,23)
kB = 1.380649 * pow(10,-23)
R = 8.3144

#%% 
def from_x_substance_to_composition(substance, X_value):
    
    X_value_dimension = len(X_value.shape)
    
    if X_value_dimension == 1:  
        X_value = X_value.reshape(1, X_value.shape[0])
    
    substance   = list(substance)  
    composition = ''
    
    for i, substance_i in enumerate(substance):

        if  i != (len(X_value[0])-1):
            composition = composition + substance_i + ':' + str(X_value[0][i]) + ',' 
        elif i == (len(X_value[0])-1):
            composition = composition + substance_i + ':' + str(X_value[0][i])
            
    return composition

#%% ideal gas thermodynamics 
def get_thermo(mech_name, composition, X_value, T_value, p_value, EOS_type, thermo_ref_set):
 
    path = 'yaml/' + mech_name + '.yaml'
    gas_1 = ct.Solution(path, EOS_type)
    gas_1.TPX = T_value, p_value, composition
    
    h_1_  = gas_1.enthalpy_mole / 1000    # J/mole
    s_1_  = gas_1.entropy_mole  / 1000    # J/(mole*K)
    cp_1_ = gas_1.cp_mole       / 1000    # J/(mole*K)
    cv_1_ = gas_1.cv_mole       / 1000    # J/(mole*K)
    g_1_  = gas_1.gibbs_mole    / 1000    # J/mol 
    
    if thermo_ref_set == 'ref_point_on':
        gas_0 = ct.Solution(path, EOS_type)
        gas_0.TPX = 273.153, 101325, composition   
    
        h_0_  = gas_0.enthalpy_mole / 1000      
        s_0_  = gas_0.entropy_mole  / 1000
        g_0_  = gas_0.gibbs_mole    / 1000
        h_1_  = h_1_  - h_0_             # based on standard state (300 K, 101325 Pa)
        s_1_  = s_1_  - s_0_
        g_1_  = g_1_  - g_0_ 
        return h_1_, s_1_, cp_1_, cv_1_, g_1_
    
    elif thermo_ref_set == 'ref_point_off':   
        return h_1_, s_1_, cp_1_, cv_1_, g_1_
    
#%% real gas thermodynamics 在计算IDT时候，热力学参数不需要额外基准点，此时选thermo_ref_set = 'ref_point_off'

def cal_thermo_real(mech_name, thermo, thermo_dep, EOS_type, substance, X_value, T_value, p_value, thermo_ref_set):
    
    composition = from_x_substance_to_composition(substance, X_value)
    
    if EOS_type == "Ideal":
       h_, s_, cp_, cv_, g_ = get_thermo(mech_name, composition, X_value, T_value, p_value, 'Ideal', thermo_ref_set)
       if   thermo == 'h_':
           return h_
       elif thermo == 's_':
           return s_
       elif thermo == 'cp_':
           return cp_
       elif thermo == 'cv_':
           return cv_
       elif thermo == 'g_':
           return g_
       else:
           print('input should be h_, cv_, cp_, s_, g_')
       
    elif EOS_type == 'Virial':        
       h_0, s_0, cp_0, cv_0, g_0 = get_thermo(mech_name, composition, X_value, T_value, p_value, 'Ideal', thermo_ref_set)       
       if   thermo == 'h_':
           h_  = h_0  + float(thermo_dep) 
           return h_
       elif thermo == 'cp_':
           cp_ = cp_0 + float(thermo_dep) 
           return cp_
       elif thermo == 'cv_':
           cv_ = cv_0 + float(thermo_dep) 
           return cv_
       elif thermo == 'g_':
           g_  = g_0  + float(thermo_dep)
           return g_
       else:
           print('input should be h_, cv_, cp_, s_, g_')
       
