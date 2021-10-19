num = int(input("Enter positive number : "))
counter = 0
comma = ""
top = []

sum = 0

for i in range(1, (num+1)):

    if(num % i == 0):

        counter = counter + 1

print(comma, i, end='')

comma = ","

if(counter < 4):

    top.append(i)

sum += i

print("\nTotal number of factor are : ", counter)

print("Top 3 : ", top)

avg = float(sum)/3

print("Average is : ", avg)