import time
def get_user_choice(choices):
    while True:
        print("Choices:")
        for num, choice_text in choices.items():
            print(f"{num}. {choice_text}")

        choice = input("Enter the number of your choice: ")
        if choice.isdigit() and choice in choices:
            return choices[choice]  # Return the actual choice_text, not the number
        else:
            print("Invalid choice. Try again.")

def restart():
    print("You lost! Please try again...")

def segment_1(name):
    print("Welcome to the future! You are now a time traveler.")
    time.sleep(1)
    print("So you have a special ability to come back to the past.")
    time.sleep(1)
    print("With this ability, you can go back to the past as many times as you want.")
    time.sleep(1)
    print("To get the girl of your dreams, Alicia.")
    time.sleep(1)
    print(f"Hope you can succeed this time, {name} :)")
    time.sleep(3)
    print(f"{name}: 'Umm.. Where is this'")
    time.sleep(1)
    print(f"{name}: 'Oh right, this is my room! I need to go to school to meet Alicia.'")
    time.sleep(1)
    print("You rush to change your clothes and go to school")
    time.sleep(3)
    print("You reached the school")
    time.sleep(1)
    print(f"{name}: 'Oh, there's Alicia!'")
    time.sleep(1)
    print(f"{name}: 'I need to go and talk to her'")
    return get_user_choice({"1": "Say Hi", "2": "Pretend to know her", "3": "Pretend to get the wrong person", "4": "Pretend to accidentally bump into her"})

def segment_11(name):
    print(f"{name}: 'Good morning, Alicia!'")
    time.sleep(1)
    print("Alicia: 'Morning... Umm sorry, who are you?'")
    time.sleep(1)
    print(f"{name}: 'I'm {name} from class 5, by the way, are you alone'")
    time.sleep(1)
    print("Alicia: 'What do you mean??? Why are you asking?!' (in a mean tone)")
    time.sleep(1)
    print(f"{name}: *why so mean TT, but I need to continue talking to her*")
    time.sleep(1)
    return get_user_choice({"1": "By the way, you are so pretty", "2": "Hihi, why are you so mean", "3": "Alicia, I wanna tell you something"})


def segment_111():
    print("Boy: 'By the way, you are so pretty'")
    time.sleep(1)
    print("Alicia: 'Ew, are you a creep? Sorry I don't like creeps. Bye'")
    time.sleep(1)
    print("Do you want to restart the game")
    return get_user_choice({"1": "Restart"})


def play_game():
    name = get_player_name()
    current_segment = segment_1(name)
    print(current_segment)
    while current_segment:
      
        if current_segment == "Say Hi":
            current_segment = segment_11(name)
        elif current_segment == "By the way, you are so pretty":
            current_segment = segment_111()
        elif current_segment == "Restart":
            restart()
            current_segment = segment_1()
        # Add more conditions for other segments if needed

def get_player_name():
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")
    return name

if __name__ == "__main__":
    play_game()
