l1 = [2,4,3]
l2 = [5,6,4]
# Output: [7,0,8]
c = ''
c2 = ''
for a in l1[::-1]:
    c += str(a)

for b in l2[::-1]:
    c2 += str(b)

print(int(c) + int(c2))