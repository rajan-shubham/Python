
for Numb in range (1, 101):

cnt = 0

for a in range(2, (Numb//2 + 1)):

if(Numb % a == 0):

cnt = cnt + 1

break

if (cnt == 0 and Numb != 1):

print(" %d" %Numb, end = ' ')
