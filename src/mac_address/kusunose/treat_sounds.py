import json
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import seaborn as sns

from connect_firestore import load_sound
from fetch_MAC import count
from gaussian import mk_gaussian


def fetch_time(id_):
    return str(id_['time'][-1]).rsplit(':', 2)[0]

def estimate_sound(id_1, id_2, id_3):
    
    id_1_time = fetch_time(id_1)
    id_2_time = fetch_time(id_2)
    id_3_time = fetch_time(id_3)
    
    bias = 1000
    
    id_1_vol = id_1['volume'][-1] - bias if id_1['volume'][-1]>bias else 0
    id_2_vol = id_2['volume'][-1] - bias if id_2['volume'][-1]>bias else 0
    id_3_vol = id_3['volume'][-1] - bias if id_3['volume'][-1]>bias else 0
    center_x, center_y = None, None
    #if id_1_time==id_2_time==id_3_time:
    vol_max = id_1_vol + id_2_vol + id_3_vol
    vol_1 = id_1_vol / vol_max if id_1_vol!=0 else 0
    vol_2 = id_2_vol / vol_max if id_2_vol!=0 else 0
    vol_3 = id_3_vol / vol_max if id_3_vol!=0 else 0

    
    center_x = (vol_1*id_1['position_x'] + vol_2*id_2['position_x'] + vol_3*id_3['position_x']) 
    center_y = (vol_1*id_1['position_y'] + vol_2*id_2['position_y'] + vol_3*id_3['position_y']) 
    #print((center_x, center_y))
    if center_x==0 and center_y==0:
        return (None, None), vol_max
    return (center_x, center_y), vol_max

if __name__=='__main__':
    member = count()
    
    id_1 = load_sound('id_1')
    id_2 = load_sound('id_2')
    id_3 = load_sound('id_3')
    
    (x, y), vol_max = estimate_sound(id_1, id_2, id_3)
    
    base = np.zeros((100, 100))
    
    if x!=None:
        
        gauss_size = (50, 50)
        y = mk_gaussian(gauss_size, scale=2)
        base[(int(x*100)-(gauss_size[0]//2)):(int(x*100)+(gauss_size[0]//2)), (int(x*100)-(gauss_size[0]//2)):(int(x*100)+(gauss_size[0]//2))] += y
        base /= base.max()
        
    sns.set()
    
    fig = plt.figure(figsize=(8.0, 8.0))
    
    if x!=None:
        plt.imshow(base,interpolation='nearest',cmap='viridis')
        plt.colorbar()
    
    #fig.patch.set_facecolor('white')
    
    plt.plot(id_1['position_x']*100, id_1['position_y']*100, marker='.', color='red', markersize=20)
    plt.annotate('id_1', xy=(id_1['position_x']*100, id_1['position_y']*100), fontsize=20, color='red')
    plt.plot(id_2['position_x']*100, id_2['position_y']*100, marker='.', color='red', markersize=20)
    plt.annotate('id_2', xy=(id_2['position_x']*100, id_2['position_y']*100), fontsize=20, color='red')
    plt.plot(id_3['position_x']*100, id_3['position_y']*100, marker='.', color='red', markersize=20)
    plt.annotate('id_3', xy=(id_3['position_x']*100, id_3['position_y']*100), fontsize=20, color='red')
    plt.xlim((0, 100))
    plt.ylim((0, 100))
    plt.tick_params(labelbottom=False,
                   labelleft=False,
                   labelright=False,
                   labeltop=False)
    plt.tick_params(bottom=False,
                   left=False,
                   right=False,
                   top=False)
    #if x!=None:
    #    plt.plot(x, y, marker='o', color='red', markersize=80, markerfacecolor="None", markeredgecolor='red', markeredgewidth=2)
    plt.savefig('soundmap')
    
    dumper = {}
    dumper['members'] = member
    dumper['sound'] = {}
    dumper['sound']['id_1'] = id_1['volume'][-1]
    dumper['sound']['id_2'] = id_2['volume'][-1]
    dumper['sound']['id_3'] = id_3['volume'][-1]
    with open('room_data.json', 'w') as f:
        json.dump(dumper, f, indent=4)
