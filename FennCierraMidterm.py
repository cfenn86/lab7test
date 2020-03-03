study_time= int (input("How many minutes do you have to study? "))      # study minutes from user

def main():
    print("Study Advice")                                                               #title for program
    print("Welcome to your study advice group,enter minutes available get advice")  #instructions
    print("You have", study_time, "minutes to study")
    return(returnAdvice)

if (study_time<=60):
        returnAdvice=("Study main points")                                                  #advice for 0-60 minuetes
        print(returnAdvice)
        
if (study_time<=120):
        returnAdvice=("Plenty of time to read and understand")                              #advice for 61-120 minutes
        print(returnAdvice)
        
if (study_time<=180):
        returnAdvice=("You can cover a lot in this time")                                   #advice for 121-180 minutes
        print(returnAdvice)
        
if (study_time<=240):
        returnAdvice=("Study, study, study")                                                #advice for 181-240 minutes
        print(returnAdvice)
        
if (study_time<=300):
        returnAdvice=("You have all the time in the world")                                 #advice for 241-300 minutes
        print(returnAdvice)
main()                                                                              
    

                    
    
    
    
