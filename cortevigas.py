def corte(b,h,rec,fc,fy,vu,nu,phi):
    
    b = b*10
    h = h*10
    rec = rec*10
    
    vu = vu*9800
    nu = nu*9800
    
    d = h - rec
    
    vc = 0
    
    #~ Determinacion de Vc:

    if nu <= 0.01:
        vc = (fc**0.5)/6*b*d
    elif nu >= 0:
        vc = (1+nu/(b*h))*(fc**0.5)/6*b*d
    elif nu < 0:
        vc = (1 + 0.3*nu/(b*h))*(fc**0.5)/6*b*d
        
    #~ Determinacion de Vs
    
    av_s = (vu/phi-vc)/(fy*d)
    
    if av_s*fy > 2/3*(fc**0.5)*b:
        return("cambiar seccion")
    
    vs = av_s*fy*d
    
    #~ limites para el espaciamiento
    
    smax = 0
    
    if vs > ((fc**0.5)/3)*b*d:
        smax = min(d/40,30)
    else:
        smax = min(d/20,60)
        
    #~ armadura minima al corte
    
    av_min = 0
    
    if vu > 0.5*phi*vc:
        av_min = max(0.0625*(fc**0.5)*b/fy/100,0.35*b/fy/100)
        
    av = max(av_s*10,av_min)
    
    return round(av,1), round(smax,1)
    
        
        
