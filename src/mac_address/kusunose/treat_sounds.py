import matplotlib.pyplot as plt
import seaborn as sns
from connect_firebase import load_sound

drawim = 1

def fetch_time(id_):
    return id_['time'].rsplit(':', 1)[0]

def estimate_sound(id_1, id_2, id_3):
    id_1 = load_sound(id1)
    id_2 = load_sound(id2)
    id_3 = load_sound(id3)
    
    id_1_time = fetch_time(id_1)
    id_2_time = fetch_time(id_2)
    id_3_time = fetch_time(id_3)
    
    if id_1_time==id_2_time==id_3_time:
        vol_max = id_1['volume'] + id_2['volume'] + id_3['volume']
        vol_1 = id_1['volume'] / vol_max
        vol_2 = id_2['volume'] / vol_max
        vol_3 = id_3['volume'] / vol_max
        
        center_x = (vol_1*id_1['pos'][0] + vol_2*id_2['pos'][0] + vol_3*id_3['pos'][0]) 
        center_y = (vol_1*id_1['pos'][1] + vol_2*id_2['pos'][1] + vol_3*id_3['pos'][1]) 
        
    return (center_x, center_y)

if __name__=='__main__':
    id_1 = load_sound('ID1')
    id_2 = load_sound('ID2')
    id_3 = load_sound('ID3')
    
    x, y = estimate_sound(id_1, id_2, id_3)
    
    if drawim:
        sns.set()
        plt.figure(figsize=(8.0, 8.0))
        plt.plot(*id_1['pos'], marker='.', color='blue', markersize=20)
        plt.annotate('id_1', xy=id_1['pos'], fontsize=20)
        plt.plot(*id_2['pos'], marker='.', color='blue', markersize=20)
        plt.annotate('id_2', xy=id_2['pos'], fontsize=20)
        plt.plot(*id_3['pos'], marker='.', color='blue', markersize=20)
        plt.annotate('id_3', xy=id_3['pos'], fontsize=20)
        plt.plot(center_x, center_y, marker='*', color='red', markersize=40)
        plt.xlim((0, 1))
        plt.ylim((0, 1))
        plt.savefig('sample')
