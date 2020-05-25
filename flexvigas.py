import math

def flexion(h,b,rec,fc,fy,mu,pu):
    d = (h-rec)*10
    h = h*10
    b = b*10
    d_p = rec*10
    
    if mu <= 0.01:
        return 0, 0, 0
    
    mu = mu*9800000
    pu = pu*9800
    
    xi_lim = 0.003/(0.003+0.004)
    
    b1 = 0.85
    
    if (fc < 30):
        b1 = 0.85
    elif (fc >= 30 and fc <= 55):
        b1 = 0.85-0.008*(fc-30)
    else:
        b1 = 0.65

    nu_lim = b1 * xi_lim * ( 1 - b1 * xi_lim/2)
    meu = mu + pu * (d - h / 2)
    uc = 0.85 * fc * b * d
    
    if (fy == 420):
        aux1 = 0.25
        aux2 = 0.233
    elif (fy == 280):
        aux1 = 0.208; aux2 = 0.345
    else:
        return("error en el acero")
    
    compresion = False; xi = 0; xi2 = xi_lim
    
    while True:
        xi = xi2
        fi = min(max(aux1/xi + aux2,0.65),0.9)
        nu = meu / (fi*uc*d)
        
        if (nu > nu_lim):
            compresion = True
            break
        else:
            xi2 = (1 - math.sqrt(1-2*nu))/b1
            
        if (xi - xi2)<=0.01:
            break
    
    if compresion:
        delta_p = d_p/d
        w_p = (nu-nu_lim)/(1-delta_p)
        v = pu / (fi * uc)
        w = b1 * xi + w_p - v
    else:
        w_p = 0
        v = pu / (fi * uc)
        w = 1 -math.sqrt(1 - 2 * nu) - v
    
    as1 = w * uc / fy
    as2 = w_p * uc / fy
    
    ro = as1 / (b * d)
    rob = (0.003 / 0.005) * (0.85 * b1 * fc / fy)
    
    return round(as1/100,1), round(as2/100,1), round(ro / rob * 100, 1)
    

        
        


    
    
    
