y = 0
cipher = []
final = []
plain = []
new = []
key = 3
parameter = "99991580011"
transposition = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#Encrypting with Caeser cipher
for a in parameter:
    y = (int(a) + key) % 10
    cipher.append(y)
print(cipher[0])
cipher.append(3)
cipher.append(3)
cipher.append(3)
cipher.append(3)
cipher.append(3)

print(cipher)
j = 0

for p in range(0,4):
    for q in range(0,4):
        #j = j+1
        transposition[p][q] = cipher[j]
        j = j+1

j = 0
for m in range(0,4):
    for n in range(0,4):
        #j = j+1
        final.append(transposition[n][m])
       


print(final)       
final = ''.join(str(e) for e in final)

print("Cipher:" + final)

for a in final:
    new.append(a)
j = 0
for m in range(0,4):
    for n in range(0,4):
        #j = j+1
        transposition[m][n] = new[j]
        j = j+1
print(transposition)
cipher = []
for m in range(0,4):
    for n in range(0,4):
        #j = j+1
        cipher.append(transposition[n][m])
cipher = cipher[0:11]
print(cipher)


for a in cipher:
    print(a)
    diff = int(a) - key
    if (diff < 0):
        diff = abs(diff)
        diff = 10 - diff
        plain.append(diff)
    else:
        plain.append(diff)
        
plain = ''.join(str(e) for e in plain)
print(plain)
qr_value = str(plain)

















        
