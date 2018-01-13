# Python program

def passwordCracker(password, attempt):
   #if all(x in attempt for x in password):
      #print(x)
    for i in password:
        if i in attempt:
            print(attempt.find(i))


if __name__== "__main__":
   t = int(input("Enter no of cases").strip())
   for a0 in range(t): 
            no_of_password = int(input("No of password").strip())
            password = input("Enter valid password").strip().split(' ')
            attempt = input("check password").strip()
            #print(attempt)
            result = passwordCracker(password, attempt)
            print(result)

