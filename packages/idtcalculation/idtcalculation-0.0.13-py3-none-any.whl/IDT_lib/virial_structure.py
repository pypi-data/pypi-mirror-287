import sympy as sp
import numpy as np
import time
import os.path

#%% 

def X_substance_update(order_minus2, X_in, substance_in, substance_rank):
    
    if order_minus2 == 0: 
        X_out = X_in
        
    else:            
        X_out = np.zeros(len(substance_in))         
        substance_rank1 = substance_rank[order_minus2]
        for i, substance_rank_i in enumerate(substance_rank1):            
            substancei_index = np.where(substance_in==substance_rank_i)   
            X_out[i] = X_in[substancei_index]
    
    return X_out

#%% 

def lambdify_list_generate(generate_type, order_minus2, X_in, substance_in, substance_rank, T_value):
    
    if generate_type == 'symbole':         
        T      = sp.symbols('T')   
        lenth  = X_in.shape  
        X_tup =()         
        for i in range(0, lenth[0]):
            X_str    = 'X' + str(i+1)
            X_symbol = sp.symbols(X_str)
            X_tup   = X_tup + (X_symbol,)   
        XT_tup = X_tup + (T,)
        XT_tup_list  = [XT_tup]       
        return XT_tup_list
    
    elif generate_type == 'value':  
        X_np = X_substance_update(order_minus2, X_in, substance_in, substance_rank)
        XT_np = np.append(X_np, T_value)                
        return XT_np

#%% 

def function_transfer_to_lambdify(funciton_ensemble_np, XT_tup_list):   
    
    result_np = np.empty(funciton_ensemble_np.shape, dtype=object)
    
    iterate = np.nditer(result_np, ['multi_index', "refs_ok"], op_flags=["readwrite"])
    
    for result_function in iterate:

        index = np.array(iterate.multi_index)
        
        if len(index) == 1:               
            array_index = index[0]            
            function   = funciton_ensemble_np[array_index]           
            lambdify_f = sp.lambdify(XT_tup_list, function, "scipy")
            result_function[...] = lambdify_f
            
        elif len(index) == 2:               
            array_index, colum_index = index[0], index[1]            
            function   = funciton_ensemble_np[array_index][colum_index]            
            lambdify_f = sp.lambdify(XT_tup_list, function, "scipy")
            result_function[...] = lambdify_f
    
    return result_np
    
#%% 

def array_cal_to_array(funciton_np, X_in, substance_in, substance_rank, T_value):
    
    result_np = np.zeros(funciton_np.shape)
    
    iterate = np.nditer(result_np, ['multi_index', "refs_ok"], op_flags=["readwrite"])
    
    for result_value in iterate:

        index = np.array(iterate.multi_index)
        
        if len(index) == 1:               
            array_index = index[0]          
            XT_np = lambdify_list_generate('value', array_index, X_in, substance_in, substance_rank, T_value)
            function = funciton_np[array_index]
            result_value[...] = function(XT_np)
                               
        elif len(index) == 2:               
            array_index, colum_index = index[0], index[1]    
            XT_np = lambdify_list_generate('value', array_index, X_in, substance_in, substance_rank, T_value)
            function = funciton_np[array_index][colum_index]
            result_value[...] = function(XT_np)

    return result_np

#%% 

def virial_structure_from_np(virial_folder_name, XT_tup_list, virial_order):
    
    path_front =  str(virial_folder_name) + str('/')
    
    Bn_fun_path    = os.path.join(path_front, 'Bn_fun.npy')
    dBdT1_fun_path = os.path.join(path_front, 'dBdT1_fun.npy')
    dBdT2_fun_path = os.path.join(path_front, 'dBdT2_fun.npy')
    dBdX_fun_path  = os.path.join(path_front, 'dBdX_fun.npy')
    dBdTX_fun_path = os.path.join(path_front, 'dBdTX_fun.npy')
    substance_rank_path = os.path.join(path_front, 'Substance_rank.npy')

    Bn_fun    = np.load(Bn_fun_path,    allow_pickle=True, fix_imports=False)    
    
    dBdT1_fun = np.load(dBdT1_fun_path, allow_pickle=True, fix_imports=False)    
    
    dBdT2_fun = np.load(dBdT2_fun_path, allow_pickle=True, fix_imports=False)    
    
    dBdX_fun  = np.load(dBdX_fun_path,  allow_pickle=True, fix_imports=False)    

    dBdTX_fun = np.load(dBdTX_fun_path, allow_pickle=True, fix_imports=False)   

    substance_rank = np.load(substance_rank_path, allow_pickle=True, fix_imports=False)   

    Bn_fun    = Bn_fun[0:virial_order-1]    
    dBdT1_fun = dBdT1_fun[0:virial_order-1]    
    dBdT2_fun = dBdT2_fun[0:virial_order-1]    
    dBdX_fun  = dBdX_fun[0:virial_order-1]    
    dBdTX_fun = dBdTX_fun[0:virial_order-1]  
    substance_rank = substance_rank[0:virial_order-1] 
    
    Bn_fun    = function_transfer_to_lambdify(Bn_fun,    XT_tup_list)
    dBdT1_fun = function_transfer_to_lambdify(dBdT1_fun, XT_tup_list)
    dBdT2_fun = function_transfer_to_lambdify(dBdT2_fun, XT_tup_list)
    dBdX_fun  = function_transfer_to_lambdify(dBdX_fun,  XT_tup_list)
    dBdTX_fun = function_transfer_to_lambdify(dBdTX_fun, XT_tup_list)  

    return substance_rank, Bn_fun, dBdT1_fun, dBdT2_fun, dBdX_fun, dBdTX_fun

#%% 

def virial_structure(substance, substance_rank, Bn_fun, dBdT1_fun, dBdT2_fun, dBdX_fun, dBdTX_fun, X_value, T_value):

    Bn_np    = array_cal_to_array(Bn_fun,    X_value, substance, substance_rank, T_value)
    dBdT1_np = array_cal_to_array(dBdT1_fun, X_value, substance, substance_rank, T_value)
    dBdT2_np = array_cal_to_array(dBdT2_fun, X_value, substance, substance_rank, T_value)
    dBdX_np  = array_cal_to_array(dBdX_fun,  X_value, substance, substance_rank, T_value)
    dBdTX_np = array_cal_to_array(dBdTX_fun, X_value, substance, substance_rank, T_value)
    
    Bn_np    = Bn_np.astype(np.float64)         
    dBdT1_np = dBdT1_np.astype(np.float64)
    dBdT2_np = dBdT2_np.astype(np.float64) 
    dBdX_np  = dBdX_np.astype(np.float64)
    dBdTX_np = dBdTX_np.astype(np.float64)

    return Bn_np, dBdT1_np, dBdT2_np, dBdX_np, dBdTX_np