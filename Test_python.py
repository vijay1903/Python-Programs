numbers = [1,10,6]
sum = 0
for num in numbers:
    for i in range(1,num+1):
        if num%i==0 and i%2!=0: 
            sum = sum + i
print(sum)
