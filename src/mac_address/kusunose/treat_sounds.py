from connect_firestore import load_sound


def fetch_time(id_):
    return str(id_['time'][-1]).rsplit(':', 2)[0]

def estimate_sound(id_1, id_2, id_3):
    
    id_1_time = fetch_time(id_1)
    id_2_time = fetch_time(id_2)
    id_3_time = fetch_time(id_3)
    
    #bias = 1000
    bias = 0

    id_1_vol = id_1['volume'][-1] - bias if id_1['volume'][-1]>bias else 0
    id_2_vol = id_2['volume'][-1] - bias if id_2['volume'][-1]>bias else 0
    id_3_vol = id_3['volume'][-1] - bias if id_3['volume'][-1]>bias else 0
    center_x, center_y = None, None
    #if id_1_time==id_2_time==id_3_time:

    vol_max = id_1_vol + id_2_vol + id_3_vol
    vol_1 = id_1_vol / vol_max if id_1_vol!=0 else 0
    vol_2 = id_2_vol / vol_max if id_2_vol!=0 else 0
    vol_3 = id_3_vol / vol_max if id_3_vol!=0 else 0


    pos_all = (id_1['position_x'] + id_2['position_x'] + id_3['position_x'], id_1['position_y'] + id_2['position_y'] + id_3['position_y'])
    x1, y1 = (id_1['position_x']-0.5, id_1['position_y']-0.5)
    x2, y2 = (id_2['position_x']-0.5, id_2['position_y']-0.5)
    x3, y3 = (id_3['position_x']-0.5, id_3['position_y']-0.5)

    center_x = (vol_1*x1 + vol_2*x2 + vol_3*x3) 
    center_y = (vol_1*y1 + vol_2*y2 + vol_3*y3) 
    #print((center_x, center_y))
    if center_x==0 and center_y==0:
        return (None, None), vol_max
    return (center_x+0.5, center_y+0.5), vol_max


if __name__=='__main__':
    id_1 = load_sound('id_1')
    id_2 = load_sound('id_2')
    id_3 = load_sound('id_3')
    
    (x, y), vol_max = estimate_sound(id_1, id_2, id_3)
    print((x, y))