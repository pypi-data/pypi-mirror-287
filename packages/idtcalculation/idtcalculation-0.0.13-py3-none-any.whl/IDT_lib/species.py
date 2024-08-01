import numpy as np

#%%

def mech_substance_list_or_array(mech_name, name_or_zero):
    if mech_name == 'GRI30' and name_or_zero == 'name_list':         
        list_or_array = \
            ['H2',     'H',      'O',     'O2',     'OH',     'H2O',    'HO2',     'H2O2',    'C',       'CH',   \
             'CH2',    'CH2(S)', 'CH3',   'CH4',    'CO',     'CO2',    'HCO',     'CH2O',    'CH2OH',   'CH3O', \
             'CH3OH',  'C2H',    'C2H2',  'C2H3',   'C2H4',   'C2H5',   'C2H6',    'HCCO',    'CH2CO',   'HCCOH',\
             'N',      'NH',     'NH2',   'NH3',    'NNH',    'NO',     'NO2',     'N2O',     'HNO',     'CN',   \
             'HCN',    'H2CN',   'HCNN',  'HCNO',   'HOCN',   'HNCO',   'NCO',     'N2',      'AR',      'C3H7', \
             'C3H8',   'CH2CHO', 'CH3CHO']       
    elif mech_name == 'GRI30' and name_or_zero == 'zero_list':
        list_or_array = np.zeros([53])

    
    elif mech_name == 'Glarborg2018' and name_or_zero == 'name_list':   
        list_or_array = \
            ['H2',       'O2',        'O3',        'H',          'O',          'OH',       'HO2',       'H2O',       'H2O2',     'CO',          \
             'CO2',      'CH4',       'CH3',       'CH2',        'CH2(S)',     'CH',       'C',         'CH3OH',     'CH3O',     'CH2OH',       \
             'CH2O',     'HCOH',      'HCO',       'HOCO',       'HOCHO',      'OCHO',     'HOCH2O',    'CH3OOH',    'CH3OO',    'CH2OOH',      \
             'C2H6',     'C2H5',      'C2H4',      'C2H3',       'C2H2',       'H2CC',     'C2H',       'CH3CH2OH',  'CH3CHO',   'CH2CHOH',     \
             'cC2H4O',   'CH2CHO',    'CH2CO',     'HCCOH',      'HCCO',       'C2O',      'OCHCHO',    'NO',        'HCN',      'NH3',         \
             'NH2',      'NH',        'N',         'NNH',        'N2H4',       'N2H3',     'N2H2',      'H2NN',      'NH2OH',    'H2NO',        \
             'HNOH',     'HNO',       'HON',       'NO2',        'HONO',       'HNO2',     'NO3',       'HONO2',     'N2O',      'HNC',         \
             'CN',       'HNCO',      'HOCN',      'HCNO',       'NCO',        'NCN',      'HNCN',      'NCNO',      'NCNOH',    'HNCNH',       \
             'NCCN',     'CH3NO',     'CH2NO',     'CH3NO2',     'CH2NO2',     'CH3ONO',   'CH3ONO2',   'CH3NH2',    'CH2NH2',   'CH3NH',       \
             'CH2NH',    'H2CN',      'HCNH',      'CH3CH2NH2',  'CH2CHNH2',   'CH3CHNH',  'CH2CHNH',   'CH3CN',     'CHCNH2',   'CH2CNH',      \
             'CH2CN',    'CHCNH',     'H2NCHO',    'H2NCO',      'AR',         'HE',       'N2'] 
    elif mech_name == 'Glarborg2018' and name_or_zero == 'zero_list':
        list_or_array = np.zeros([107])

    elif mech_name == 'NUIG11_lowT' and name_or_zero == 'name_list':   
        list_or_array = \
            ['AR',             'N2',            'HE',              'H2',             'H',              'O2',             'O',               'H2O',           'OH',           'OHV',            \
             'H2O2',           'HO2',           'HOCO',            'CO',             'CO2',            'CH3O2H',         'CH3O2',           'CH2O2H',        'CH4',          'CH3',            \
             'CH2',            'CH2(S)',        'C',               'CH',             'CHV',            'CH3OH',          'CH3O',            'CH2OH',         'HO2CHO',       'HOCH2O2H',       \
             'HOCH2O2',        'OCH2O2H',       'HOCH2O',          'O2CHO',          'HOCHO',          'OCHO',           'CH2O',            'HCO',           'HCOH',         'C2H5O2',         \
             'C2H6',           'C2H5',          'CHOCHO',          'C2H3OO',         'CHCHO',          'C2H4',           'C2H3',            'C2H2',          'C2H',          'H2CC',           \
             'C2H4O1-2',       'C2H5OH',        'PC2H4OH',         'CH3CHO',         'CH3CO',          'CH2CHO',         'C2H3OH',          'C2H2OH',        'SC2H2OH',      'CH2CO',          \
             'HCCO',           'HCCOH',         'CH2COOH',         'CH3OCH3',        'C3H6O1-2',       'CH3COCHO',       'CH2CHOCHO',       'C3H8',          'IC3H7',        'NC3H7',          \
             'CH3CHCHO',       'CH3CHCO',       'C3H6',            'C3H5-A',         'C3H5-S',         'C3H5-T',         'CC3H6',           'SC3H4OH',       'C3H3O2H',      'C2HCHO',         \
             'C3H4-P',         'C3H4-A',        'C3H3',            'CC3H4',          'C3H2',           'H2CCC(S)',       'CH3OCHCH2',       'C3H5OH',        'SC3H5OH',      'IC3H5OH',        \
             'CH3COCH3',       'CH3COCH2',      'C2H3CHO',         'CH3#CHCOO#',     'CYC2H3OCHO',     'C2H5CHO',        'CH2COHCHO',       'CH3COOH',       'NO',           'HCN',            \
             'NH3',            'NH2',           'NH',              'N',              'NNH',            'HNO',            'NO2',             'N2O',           'HNC',          'CN',             \
             'HNCO',           'HOCN',          'HCNO',            'NCO',            'NCN',            'HNCN',           'HNCNH',           'CH2NH',         'H2CN',         'CH2CN']
    elif mech_name == 'NUIG11_lowT' and name_or_zero == 'zero_list':
        list_or_array = np.zeros([120])

    return list_or_array