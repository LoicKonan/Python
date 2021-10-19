try:
    num = int(input("Enter positive number : "))

    while not(input() == 'e'):

        counter = 0

        comma = ""

        top = []

        sum = 0

        for i in range(1, (num+1)):

            if(num % i == 0):
                a = b = c = 0
                a = b   
                b = c   
                c = i
                
                counter = counter + 1
                print(comma, i, end ='')
                comma = ","

            if(counter < 4):

                top.append(i)
                sum += i

        print("\nTotal number of factor are : ", counter)

        print('Top 3 :', a, '', b, '', c )

        avg = float(a+b+c)/3

        print("Average is : ", avg)
        
except ValueError:
    print("You a character so bye Felicia lol !!!")