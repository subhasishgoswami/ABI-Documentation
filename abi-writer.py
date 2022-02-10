import json
import sys
# Opening JSON file
f = open(sys.argv[1])
d= open('documentation.md', 'a')
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
for i in data['abi']:
    d.write('\n# '+ i['name']+ '\n\n')
    if 'type' in i:
        d.write('`Type: '+ i['type'] + '` ')
    if 'stateMutability' in i:
        d.write('`Type Of Function: '+ i['stateMutability'] + '`')
    d.write('\n\n## '+ 'Inputs' + '\n\n')
    for j in i['inputs']:
        d.write('* '+ j['name'] + ' `(Type Of Input: ' + j['type'] + ')`\n')
    


# Closing file
d.close()
f.close()