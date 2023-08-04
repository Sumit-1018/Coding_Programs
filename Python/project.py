import random

project=int(input("Which Project do you want to check?(1-25)\n="))
if(project==1):
    #project 1
    score=0
    user_input="Play"
    user_input=user_input.lower()
    while(user_input=="play"):
        comp_choice=random.randint(1,6)
        user=int(input("Enter your choice from 1 to 6 :="))
        if(user==comp_choice):
            print("Congrats! Correcr Guess!!")
            score+=10
        else:
            print("Sorry :( /n Wrong Guess!! ")
        user_input=str(input("Do you want to play again(Play/Exit):="))
    print("Your Score is :-",score," Come Back Soon :))")
elif(project==2):
    #project2
    print("!!Welcome to Rock Paper Scissors Game!!")
    user_input="play"
    user_input=user_input.lower()
    while(user_input=="play"):
        score_comp=0
        score_user=0
        user_move=str(input("Rock,Paper or Scissors?\n="))
        user_move=user_move.lower()
        move={1:"rock",2:"paper",3:"scissors"}
        comp_choice=random.randint(1,3)
        comp_choice=move[comp_choice]
        if(user_move==comp_choice):
            print("Tie")
        elif(user_move=="rock" and comp_choice=="paper"):
            print("You Loose :(\n PAPER covers ROCK")
            score_comp+=1
        elif(user_move=="rock" and comp_choice=="scissors"):
            print("You Win :)\n ROCK Smashes SCISSORS")
            score_user+=1
        elif(user_move=="paper" and comp_choice=="rock"):
            print("You Win!!\n PAPER covers ROCK")
            score_user+=1
        elif(user_move=="paper" and comp_choice=="scissors"):
            print("You Loose :( SCISSORS cuts PAPER")
            score_comp+=1
        elif(user_move=="scissors" and comp_choice=="paper"):
            print("You Win :)\n SCISSORS cuts PAPER")
            score_user+=1
        elif(user_move=="scissors" and comp_choice=="rock"):
            print("You Losse :(\n ROCK smashes SCISSORS")
            score_comp+=1
        user_input=str(input("Do you want to play?(Play/Exit)\n="))
    print("Game Aborted!\n Your Score:-{}\n Computer Score:-{}".format(score_user,score_comp))
elif(project==3):
    user_input="Play"
    user_input=user_input.lower()
    while(user_input=="play"):
        list_email=[]
        more="Yes"
        more=more.lower()
        while(more=="yes"):
            new_email=str(input("Enter the e-mail id:-"))
            more=str(input("Do you want to attend more e-mail id's? (Yes/NO)\n="))
            list_email.append(new_email)
        length_list_email=len(list_email)
        for i in range(0,length_list_email):
            temp=list_email[i].split("@")
            print("Username:- {} and domain:- {}".format(temp[0],temp[1].upper()))
        user_input=str(input("Do you want to play?(Play/Exit)\n="))

        
        