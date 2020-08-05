import time
import random


def pause_message(text):
    print(text)
    time.sleep(2)


def intro(villan):
    pause_message("There was a small village where everyday is a happy day.")
    pause_message("People helped each other"
                  " and lived in peace and harmony.")
    pause_message(f"A {villan} was sneaking into the village"
                  " at night and started destroying it.")
    pause_message("Nothing but horror and terror"
                  " in the village since then.")
    pause_message("You were one of the courageous"
                  " volunteers who decided to take it down.")
    pause_message(f"You found out that the {villan} was staying"
                  " at one of the houses in the village.")
    pause_message("You have a small dagger in your hand"
                  " and friends with you.")
    pause_message("You are standing in the field where you"
                  " found a house on your right and a cave on your left.")


def cave(items, villan):
    pause_message("You enetered the cave.")
    pause_message("It is very dark and hot inside.")
    if "sword" in items:
        pause_message("You already took the sword of Eden.")
        pause_message("There is nothing to do here.")
    else:
        pause_message("Your eyes caught a glimpse of a"
                      " reflection of a shiny object.")
        pause_message("You eyes were wide open when you realized"
                      " it is the legendary sword of Eden!!")
        pause_message("You replaced the small dagger"
                      " that you have with sword.")
        items.append("sword")
    pause_message("You went back out to the field.")
    pause_message("You are standing in the field where you"
                  " found a house on your right and a cave on your left.")
    field(items, villan)


def house(items, villan):
    pause_message(f"You have entered the {villan}\'s house.")
    pause_message(f"You saw the {villan} sleeping on the ground")
    pause_message("You and your friends think it is a great way"
                  " to attack it while it is asleep.")
    pause_message(f"As you are a few steps from the {villan}")
    pause_message("It woke up and it is running toward your way!")
    fight(items, villan)


def fight(items, villan):
    pause_message("What you want to do next?")
    action2 = input("Enter 1 to attack\nEnter 2 to run away")
    if action2 == "1":
        if "sword" in items:
            pause_message(f"You are running towards the {villan} to"
                          " attack with your sword")
            pause_message("You attacked and watch it fall on ground.")
            pause_message(f"You defeated the {villan}!!")
            pause_message("And now the village has"
                          " restored its peace and harmony")
        else:
            pause_message(f"You are running toward the {villan} "
                          "with your small dagger")
            pause_message("Even with the help your friends")
            pause_message(f"The {villan} managed to defeat you"
                          " and the rest of your friends.")
    elif action2 == "2":
        pause_message(f"You have managed to runaway and the {villan}"
                      " seems like it is not following you.")
        pause_message("You are standing in the field where you"
                      " found a house on your right and a"
                      " cave on your left.")
        field(items, villan)
    else:
        fight(items, villan)


def field(items, villan):
    pause_message("What you want to do next?")
    action1 = input("Enter 1 to go to the house.\nEnter 2 to go to the cave.")
    if action1 == "1":
        house(items, villan)
    elif action1 == "2":
        cave(items, villan)
    else:
        field(items, villan)


def end():
    pause_message("Do you want to play again?")
    ending = input("please enter y/n")
    if "y" in ending:
        play_game()
    elif "n" in ending:
        pause_message("Thanks for playing, see you next time!")
    else:
        end()


def play_game():
    villans = ["vampire", "dragon", "pirate", "beast", "troll"]
    villan = str(random.choice(villans))
    items = []
    intro(villan)
    field(items, villan)
    end()


play_game()
