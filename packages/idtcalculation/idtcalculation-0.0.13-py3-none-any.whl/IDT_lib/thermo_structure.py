from thermo_real import cal_thermo_real
R = 8.3144


#%%
def EOS_virial_p(Bn_np, T_value, v__value):  

    loop1 = 1

    for i, B_i in enumerate(Bn_np):
        order = i +2
        loop  = B_i / pow(v__value, order-1)
        loop1 = loop1 + loop
        
    p = R * T_value / v__value /pow(10,-6) * loop1
    Z = loop1
    return p, Z

#%%
def thermo_departure(Bn_np, dBdT1_np, dBdT2_np, Z, thermo, T_value, v__value):
    
    v_ = v__value / pow(10,6)   
    
    if thermo == 'h_':
        loop1 = 0
        
        for i, B_i in enumerate(Bn_np):
            order = i+2
            
            B_i     =         B_i / pow(10,6*(order-1))  
            dBdT1_i = dBdT1_np[i] / pow(10,6*(order-1))            
            loop    = (B_i -  T_value*dBdT1_i / (order-1)) / pow(v_, (order-1))
            loop1   = loop1 + loop
        
        h_gap = R * T_value * loop1
        return h_gap
    
    elif thermo == 'cp_':
        loop_nu1 = 1          
        loop_de1 = 1
        loop_cv1 = 0
        
        for i, B_i in enumerate(Bn_np):
            order = i+2
            
            B_i     =         B_i / pow(10,6*(order-1))
            dBdT1_i = dBdT1_np[i] / pow(10,6*(order-1)) 
            dBdT2_i = dBdT2_np[i] / pow(10,6*(order-1)) 
        
            loop_nu = (B_i + T_value * dBdT1_i) / pow(v_, order-1)
            loop_de = order * B_i / pow(v_, order-1)
            loop_cv = (2 * T_value * dBdT1_i + pow(T_value, 2) * dBdT2_i) / (order-1) / pow(v_, (order-1))
            
            loop_nu1 = loop_nu1 + loop_nu             
            loop_de1 = loop_de1 + loop_de               
            loop_cv1 = loop_cv1 + loop_cv
        
        loop_nu_final = pow(loop_nu1,2)
        cv_gap = -R * loop_cv1
        cp_gap = -R + R * loop_nu_final / loop_de1 + cv_gap   
        return cp_gap
      
#%%    
def thermo_structure(mech_name, thermo_ref_set, Bn_np, dBdT1_np, dBdT2_np, substance, X_value, T_value, v__value):
    
    p_value, Z = EOS_virial_p(Bn_np, T_value, v__value)
    
    h_dep  = thermo_departure(Bn_np, dBdT1_np, dBdT2_np, Z, 'h_',   T_value, v__value)    
    cp_dep = thermo_departure(Bn_np, dBdT1_np, dBdT2_np, Z, 'cp_',  T_value, v__value)

    h_ig_  = cal_thermo_real(mech_name, 'h_',   h_dep,  'Ideal',  substance, X_value, T_value, p_value, thermo_ref_set)    
    cp_ig_ = cal_thermo_real(mech_name, 'cp_',  cp_dep, 'Ideal',  substance, X_value, T_value, p_value, thermo_ref_set)
    h_     = h_ig_  + float(h_dep)
    cp_    = cp_ig_ + float(cp_dep)  

    return p_value, Z, h_dep, cp_dep, h_ig_, cp_ig_, h_, cp_
