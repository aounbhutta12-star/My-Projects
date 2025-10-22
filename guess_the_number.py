import random




guess=random.randint(1,100)

attempt=0


while True:
    
    n=int(input("Guess the number between 1 and 100: "))
   
    attempt +=1
    
    if(n>guess):
        print("Too High! Guess a lower number ")
  
    elif(n<guess):
        print("Too Low")
        
    elif(n==guess):
        print(f"Yes you guessed the  number ({guess}) in ({attempt}) attempt")
        break

