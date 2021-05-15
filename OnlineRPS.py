# !!!! Write your information of MySqL Db to ConnectToDB  !!!!

#  choose one of them Rock-Paper-Scissors
#  save your choose or answer saved game
#  see the results
#  fun 

def ConnectToDB():
    import mysql.connector
    conn = mysql.connector.connect(db='db',   # Your DB name
                                   user='user', #Your username
                                   passwd='passw+', # Your password
                                   host='host') # Your host-ip
    c = conn.cursor()
    return c,conn


def YourChoice(player,choice):
    c,conn=ConnectToDB()
    SqL="INSERT INTO Game (Players , Choices) VALUES (%s,%s)"
    send=['{}'.format(player),'{}'.format(choice)]

    c.execute(SqL,send)
    conn.commit()
    conn.close()

def Choice():
    choice=(input("What you want to choose ?  'R' for Rock, 'P' for Paper, 'S' for Scissors'  :  ")).lower()
    if choice== 's':
        choice= 'Scissors'
        return choice
    elif  choice == 'r':
        choice = 'Rock'
        return choice
    elif choice== 'p':
        choice= 'Paper'
        return choice
    else:
        print("\nWrong Choose !! Try Again")
        return Choice()


def FindExhi():
    c,conn=ConnectToDB()
    SqlPlayers = "SELECT * FROM `Game` ORDER BY `Game`.`Players`"
    c.execute(SqlPlayers)
    Players = []
    Choices = []
    for x in c:
        Players.append(x[0])
        Choices.append(x[1])

    return Players,Choices

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'Rock' and opponent == 'Scissors') or (player == 'Scissors' and opponent == 'Paper') \
        or (player == 'Paper' and opponent == 'Rock'):
        return True


def Won(player):
    print("You Won")
    c,conn=ConnectToDB()
    SqL="INSERT INTO  Winners (Player , Wins ) VALUES(%s,%s)"
    Send=['{}'.format(player),1]
    c.execute(SqL,Send)
    conn.commit()
    conn.close()


def Lost(Name):
    print("You Lost")
    c,conn=ConnectToDB()
    SqL="INSERT INTO  Winners (Player , Wins ) VALUES(%s,%s)"
    Send=['{}'.format(Name),1]
    c.execute(SqL,Send)
    conn.commit()
    conn.close()
    
    
def Tie(Name):
    print("Its Tie")
    c,conn=ConnectToDB()
    SqL="INSERT INTO  Winners (Player , Wins ) VALUES(%s,%s)"
    Send=['{}'.format(Name),1]
    c.execute(SqL,Send)
    conn.commit()
    conn.close()

    
def DeletePerson(Name):
    c,conn=ConnectToDB()
    DeletePerson = "DELETE  FROM `Game` WHERE `Players`= '{}'".format(Name)
    c.execute(DeletePerson)
    conn.commit()
    conn.close()
    
       



def play():
    print("    Hİ WELCOME TO ROCK-PAPER-SCİSSORS GAME ")

    while True:
    
        GameWay=int(input("\n   PRESS -1- İF YOU WANT TO CREATE A GAME:  \n  "
                          "\n   PRESS -2- İF YOU WANT TO ANSWER CREATED GAME:   "
                          "\n   PRESS -3- İF YOU WANT TO SEE WİNNERS TABLE:   "))
        if GameWay ==1 or GameWay ==2 or GameWay==3:
            break
        print("YOU MADE WRONG CHOİCE")
        continue
    
    print("  ///   ///  ///     ")
    print("  ///   Game loading  ///     ")
    print("  ///   ///  ///     ")
    player = input("   What's your name ? :   ")


    if GameWay==1:
        choice = Choice()
        YourChoice(player, choice)
        print( "Your choice has been saved ")



    if GameWay==2:
        Players, Choices = FindExhi()
        i = 1
        for Name in Players:
            print(" {} created a game, if you want to match with {} press {}".format(Name, Name, i))
            i += 1
        X=int(input())
        Person=Players[X-1]
        opponent=Choices[X-1]
        choice=Choice()

        if opponent==choice:
            return Tie(Person),DeletePerson(Person)
        elif is_win(choice,opponent):
            return Won(player),DeletePerson(Person)
        
        else:
            return Lost(Person),DeletePerson(Person)
        
    if GameWay==3:
        
        c,conn=ConnectToDB()
        SqL="SELECT * FROM `Winners` ORDER BY `Winners`.`Player`"
        c.execute(SqL)
        for x in c:
            print(x)
    
        

c,conn=ConnectToDB()
SqL="CREATE TABLE IF NOT EXISTS  Winners (Player VARCHAR(20), Wins int(20))"

c.execute(SqL)
conn.commit()
conn.close()

while True:   
    play()
