import random
computer= random.choice([-1,0,1,2])

your_str= input("Enter your choose: ").lower()
you_Dict={ "s":1 ,"w":-1 ,"g":0, "m":2, }
reverse_Dict={ 1:"Sanke", -1:"Water", 0:"Gun", 2:"Mongoose", }

if your_str not in you_Dict:
     print("Something went wrong!")
else:
     you=you_Dict[your_str]
     print(f"You choose: {reverse_Dict[you]} \n Computer choose: {reverse_Dict[computer]}")


     if(computer==you):
          print("Its tie!")
     
     else:
          if(computer==-1 and you==0):
               print("You lose!")
          elif(computer==-1 and you==1):
               print("You win!")
          elif(computer==-1 and you==2):
               print("You win!")
          elif(computer == 0 and you == -1):
               print("You win!")
          elif(computer==0 and you==1):
               print("You lose!")
          elif(computer==0 and you==2):
               print("You lose!")
        
          elif(computer==1 and you==-1):
               print("You lose!")
          elif(computer==1 and you==0):
               print("You lose!")
          elif(computer==1 and you==2):
               print("You win!")  
          elif(computer == 2 and you == -1):
               print("You lose!")
          elif(computer==2 and you==0):
               print("You win!")
          elif(computer==2 and you==1):
               print("You lose!")
          else:
               print("Something went wrong")
          



        