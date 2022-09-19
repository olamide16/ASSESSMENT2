num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
if num1 > num2:
    lower = num2
else:
    lower = num1

for i in range(1, lower):
    if num1%i == 0 and num2%i == 0:
        hcf = i
print(hcf)