num = int(input("Enter Any Number: "))
while(num>=0):
    if(num%2==0):
        print("The number is Even")
    elif(num%2!=0):
        print("The number is Odd")
    else:
        print("The number is neither Even nor Odd")
    num = int(input("Enter Any Number: "))