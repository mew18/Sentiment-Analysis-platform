from os import system

def driver():
    system('cls')
    print("Welcome to RJ's sentiment analysis" )

    c=int(input('Please choose one of the following options : \n 1) Sentiment analysis of a twitter post   \n 2) Sentiment analysis of your own sentence  \n 3) Exit  ' ) )

    if(c==1):
        system('cls')
        import sa1
        system('cls')
        rep=input('Do you wish to try again : ')
        if(rep=='y' or rep=='Y'):
            driver()

    elif(c==2):
        system('cls')
        import sa2
        system('cls')
        rep=input('Do you wish to try again : ')
        if(rep=='y' or rep=='Y'):
            driver()       
        
    else:
        input('Press ENTER to exit')

driver()