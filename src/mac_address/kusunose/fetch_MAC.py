import re

with open('caughts', 'r') as f:
    reads = f.read()

with open('macs', 'w') as f
for i  in reads.strip().split('\n'):
    print(re.match('(.*)\((.*)\) at (.*) on (.*)', i).groups()[2])
    