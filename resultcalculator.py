marks1= int(input("Enter Your Bangla 1st paper number: "))
marks2= int(input("Enter Your Bangla 2nd paper number :"))
marks3= int(input("Enter Your English 1st paper number:"))
marks4= int(input("Enter Your English 2nd paper number: "))
marks5= int(input("Enter Your Math number:"))
marks6= int(input("Enter Your Higher Math number:"))
marks7= int(input("Enter Your Physisc number: "))
marks8= int(input("Enter Your Chemistry  number:"))
marks9= int(input("Enter Your Biology number:"))
marks10= int(input("Enter Your I.C.T number: "))

total_percentage = ((marks1+ marks2+marks3+marks4+marks5+marks6+marks7+marks8+marks9+(marks10)*2)/10)
if(total_percentage==33):
    print("\nYou are passed" , total_percentage)
    

elif(total_percentage>=80):
    print("\nYou got A+" , total_percentage)
    
elif(total_percentage>=70):
    print("\nYou got A Grade", total_percentage)
    
elif(total_percentage>=60):
    print("\nYou got A-", total_percentage)
    
elif(total_percentage>=50):
    print("\nYou got B Grade" , total_percentage)
    
elif(total_percentage>=45):
    print("\nYou got C Grade", total_percentage)
    
elif(total_percentage>=40):
    print("\nYou got D Grade", total_percentage)
    
elif(total_percentage>=34):
    print("\nYou got E Grade", total_percentage)
    
else:
    print("\n\nSorry to say! But you are failed 😓. Try again next year.🙂")