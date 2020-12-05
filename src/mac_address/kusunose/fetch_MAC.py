import re
import subprocess
from connect_firestore import load_register

def catch_mac():
    with open('caughts', 'w') as f:
        cp = subprocess.run(['arp', '-a'], stdout=f)

def load_mac():
    with open('caughts', 'r') as f:
        reads = f.read()

    scan = []
    for i  in reads.strip().split('\n'):
        mac = re.match('(.*)\((.*)\) at (.*) on (.*)', i).groups()[2]
        if ' [ether]' in mac:
            mac.replace(' [ether]', '')
        if len(mac)>17:
            mac = mac[:17]
        scan.append(mac)
        
    return scan

def count():
    data = load_register()
    catch_mac()
    scan = load_mac()
    
    mem = 0
    for i in scan:
        if i in data:
            mem += 1
    return mem
    
    
if __name__=='__main__':
    mem = count()
    print(f'now tatal members: {mem}')