def km_to_m(d, w):
    if w == 1:
        return (d*1000,'m')
    else:
        return(d/1000,'Km')

def m_to_cm(d, w):
    if w == 1:
        return (d*100,'cm')
    else:
        return(d/100,'m')

def cm_to_mm(d, w):
    if w == 1:
        return (d*10,'mm')
    else:
        return(d/10,'cm')