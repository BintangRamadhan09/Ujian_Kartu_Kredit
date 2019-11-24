import json

with open('cc.json','r') as CC:
    out = json.load(CC)
def inValid(x):
    with open('ccInvalid.json', 'w') as inV:
        json.dump(x, inV)

I =[]
V=[]
for i in out:
    j = i['noCreditCard']
    if j[0] not in '456':
        zI.append(i)
    elif j.isdigit() == False:
        zI.append(i)
    elif j[5] == ' ':
        zI.append(i)
    elif j[5]=='-':
        zV.append(i)
    elif j[0:len()]
    elif len(j) > 16:
        I.append(i)
    else:
        V.append(i)

with open('ccValid.json', 'a') as ccV:
    json.dump(V, ccV)

with open('ccInvalid.json', 'a') as inV:
    json.dump(I, inV)

for i in out:
    j = i['noCreditCard']
    if j[0:len(j):4).isdigit] == False:
        print(i)
