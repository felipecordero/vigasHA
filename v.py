#~ Hormigones

##import base64
##import importlib
##c = 'dmVyaWZDYW5lcGE='

fc = {"H20" : 16.0, "H25":20.0, "H30":25.0, "H35":30.0, "H40":35.0}

fy = {"A6342H":420, "A4428H":280}

E  = {"H20" : 18800.0, "H25" : 21019.0  , "H30":23500.0 , "H35":25730.0 , "H40":27806.0 }

#~ Variables para calculo

res = { "Apoyado-Apoyado":{     "Mi":0.0  ,"Mc":1.0/8.0   ,"Md": 0.0     ,\
                                "Vi":0.5  ,  "Vc":0.0     ,"Vd":0.5   ,\
                                "Di":0.0      ,"Dc":5.0/384.0 ,"Dd":0.0    ,\
                            } ,\
        "Apoyado-Empotrado":{   "Mi":0.0      ,"Mc":9.0/128.0 ,"Md":1.0/8.0   ,\
                                "Vi":3.0/8.0    ,"Vc":0.0     ,"Vd":5.0/8.0   ,\
                                "Di":0.0      ,"Dc":1.0/185.0 ,"Dd":0.0    ,\
                                } ,\
        "Empotrado-Empotrado":{ "Mi":1.0/12.0   ,"Mc":1.0/24.0  ,"Md":1.0/12.0  ,\
                                "Vi":1.0/2.0    ,"Vc":0.0    ,"Vd":1.0/2.0   ,\
                                "Di":0.0     ,"Dc":1.0/384.0 ,"Dd":0.0     ,\
                                } ,\
        "Voladizo (x 1.3 incluido)":{ "Mi":1.3 * 1.0/2.0   ,"Mc":0.0  ,"Md":0.0  ,\
                                "Vi":1.3 * 1.0    ,"Vc":0.0     ,"Vd":0.0   ,\
                                "Di":0.0      ,"Dc":0.0 ,"Dd":  1.0/8.0     ,\
                                } ,\
        }

##importlib.import_module(base64.b64decode(c).decode())






