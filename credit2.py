import json
with open ('cc.json','r') as cc:
    vld = json.load(cc)
def benar(x):
    with open('ccValid.json','w') as betul:
        json.dump(x,betul)
def salah(x):
    with open('ccinvalid.json','w') as wrong:
        json.dump(x,wrong)
# 0525362587961578    (tidak diawali dengan 4, 5 atau 6)
# 42536258796157867    (terdiri atas 17 digit angka)
# 44244z4424442444    (terdapat karakter 'z' yang bukan angka)
# 5122.2368.7954.3214    (dipisahkan bukan dengan tanda hubung)
# 4424444424442444    (terdapat angka yang diulang >3x & tertulis secara beruntun, yaitu: 44444)
# 61234-123-8912-3456    (terdapat grup yang tidak hanya terdiri atas 4 digit angka)
# 5199-9967-7912-3457    (terdapat angka yang diulang >3x & tertulis secara beruntun, yaitu: 9999)
# 5123 - 4567 - 8912 - 3456    (dipisahkan dengan tanda hubung & spasi)

valid = []
invalid = []

for i in vld:
    # print(i)
    J = i['noCreditCard']
    if J[0] not in '456':
        invalid.append(i)
    elif '.' in J:
        invalid.append(i)
    elif '4444' in J:
        invalid.append(i)
    elif J[0] == '6':
        invalid.append(i)
    elif '99-9' in J:
        invalid.append(i)
    elif '-' and ' ' in J:
        invalid.append(i)
    elif J[5] == 'z':
        invalid.append(i)
    elif len(J.replace('-','')) > 16:
        invalid.append(i)
    #     print(invalid)
    else:
        valid.append(i)
    

benar(valid)
salah(invalid)