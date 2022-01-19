
# GAME OVER
def yes_drink():
    print("Justin hands you a bottle with a mysterious drink.")
    input()
    print("The drink is a bright blue and it looks like it sparkles in the sun.")
    input()
    print("You drink it and it tastes sweet and bubbly.")
    input()
    print("A couple seconds later you black out.")
    input()
    print("You wake up inside an unfamiliar room. Justin the knight is by your side.")
    input()
    print("'Oh! You're awake!' Justin says. 'You fell ill by the river.'")
    input()
    print("You feel confused and your vision is blurry.")
    input()
    print("You see your father, the King by your side as well.")
    input()
    print("'Princess! You are much too weak to keep going out like this! I have made the formal decision to keep you locked up in here until you are to marry.' says the King.")
    input()
    print("You get up quickly by the news and ask the King where you are.")
    input()
    print("'Don't worry about where we are. Justin the knight will stay by your side and I will have maids and cooks come in to take care of you.' says the King.")
    input()
    print("You are angry. You don't want to be locked up. You want to be free and live your life and take daily walks by the river with Justin.")
    input()
    print("'I'm sorry, Princess! You will stay here and be safe from the outside world.' says the King.")
    input()
    print("You live the rest of your life with Justin the knight by your side and a couple of maids and cooks. You never get married to any Prince because your father, the King, forgot about you.")
    input()
    game_over("YOU DIED OF OLD AGE AND A BORING LIFE. BUT AT LEAST YOU HAD JUSTIN THE KNIGHT BY YOUR SIDE.")

# Go on an adventure or not
def no_drink():
    print("You and Justin the knight continue to walk along the river until going back inside the castle.")
    input()
    print("You head back to the castle and your father, the King stops you and Justin in the hallway.")
    input()
    print("'Justin, you are to go on an adventure.' says the King. 'I need you to bring me back some of the finest teas from other countries.'")
    input()
    print("'I am no adventurer. I am a knight in shining armour. Why are you asking me?' says Justin.")
    input()
    print("The King tells Justin that it is because the other adventurers are busy fighting dragons and he wants the tea as soon as possible.")
    input()
    print("Justin reluctantly agrees to go on the adventure but asks, 'Who will take care of the Princess?'.")
    input()
    print("The King looks at you and looks at Justin the knight. He then says, 'Take her with you! It will be important for her to know about other countries if she are to be Queen one day'.")


    adventure_option = input("Do you go on an adventure or stay? You say 'go on an adventure' or 'stay' > ")


    if "go on an adventure" in adventure_option:
        print("You go on the best adventure of your life!")
        input()
        print("You and Justin gather the finest teas in the world.")
        input()
        print("When you come back to the castle. You tell the King that you quit being a princess and you wish to adventure around the world with Justin.")
        input()
        print("Justin supports you and the King reluctantly agrees.")
        input()
        game_over("YOU LIVE OUT YOUR DAYS AS AN ADVENTURER WITH YOUR BEST FRIEND JUSTIN! WHAT AN AMAZING LIFE YOU LIVED!")

    else:
        print("A couple seconds later you black out.")
        input()
        print("You wake up inside an unfamiliar room. Justin the knight is by your side.")
        input()
        print("'Oh! You're awake!' Justin says. 'You fell ill.'")
        input()
        print("You feel confused and your vision is blurry.")
        input()
        print("You see your father, the King by your side as well.")
        input()
        print("'Princess! You are much too weak to go on an adventure! I have made the formal decision to keep you locked up in here until you are to marry.' says the King.")
        input()
        print("You get up quickly by the news and ask the King where you are.")
        input()
        print("'Don't worry about where we are. I will have maids and cooks come in to take care of you.' says the King.")
        input()
        print("You are angry. You don't want to be locked up. You want to be free and live your life and go on an adventure with Justin.")
        input()
        print("'I'm sorry, Princess! You will stay here and be safe from the outside world.' says the King.")
        input()
        print("You live the rest of your life by yourself and a couple of maids and cooks. You never get married to any Prince because your father, the King, forgot about you.")
        input()
        print("Justin came by once after his adventure was over and introduced you to another adventurer, a beautiful woman. He tells you that he is in love with the woman adventurer and he will live out his days with her. He quit his knight duties at the castle and became a full fledged adventurer and you never hear from him again.")
        input()
        game_over("YOU DIED OF OLD AGE AND A BROKEN HEART. WHAT A SAD LIFE YOU LIVED.")

# Function to ask play again or not
def play_again():
  print("\nDo you want to play again? (y or n)")
  
  # convert the player's input to lower_case
  answer = input(">").lower()

  if "y" in answer:
    # if player typed "yes" or "y" start the game from the beginning
    start_game()
  else:
    # if user types anything besides "yes" or "y", exit() the program
    print("Good-bye!")
    exit()


# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # ask player to play again or not by activating play_again() function
  play_again()

# Function to start the game
def start_game():
    print("You are a princess of the kingdom of Momotuna.")
    input()
    print("You start your day by taking a stroll along the river beside the castle.")
    input()
    print("You bring along your most trusted knight in shining armour, Justin.")
    input()
    print("The sun is shining bright and beautiful like always.")   
        
    thirsty_option = input("Justin asks you a question. 'Princess', he says. 'Are you thirsty? I brought you a drink if you are feeling parched'. You answer him with a 'yes' or a 'no' > ")

    # Thirsty Option
    if thirsty_option == "yes":
        yes_drink()
    elif thirsty_option == "no":
        no_drink()
    else:
        print("You stare at Justin the Knight blankly and speak gibberish. Justin looks at you with confusion. Nothing else happens.")
        play_again()
    
# Ask player their name
def main():
    player_name = input('What is your name? > ')
    print(f"Hello {player_name}")
    
if __name__ == '__main__':
    main()

start_game()