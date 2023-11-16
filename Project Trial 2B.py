import time

def get_user_choice(choices):
    while True:
        print("Choices:")
        for num, choice_text in choices.items():
            print(f"{num}. {choice_text}")

        choice = input("Enter the number of your choice: ")
        if choice.isdigit() and choice in choices:
            return choice
        else:
            print("Invalid choice. Try again.")

def segment_1(name):
    print("Welcome to the future! You are now a time traveler.")
    time.sleep(1)
    print("So you have a special ability to come back to the past.")
    time.sleep(1)
    print("With this ability, you can go back to the past as many times as you want.")
    time.sleep(1)
    print("To get the girl of your dreams, Alicia.")
    time.sleep(1)
    print("Hope you can succeed this time :)")
    time.sleep(3)
    print("You: 'Umm.. Where is this'")
    time.sleep(1)
    print("You: 'Oh right, this is my room! I need to go to school to meet Alicia.'")
    time.sleep(1)
    print("You rush to change your clothes and go to school")
    time.sleep(3)
    print("You reached the school")
    time.sleep(1)
    print("You: 'Oh, there's Alicia!'")
    time.sleep(1)
    print("You: 'I need to go and talk to her'")
    return get_user_choice({"1": "Say Hi", "2": "Pretend to know her", "3": "Pretend to get the wrong person", "4": "Pretend to accidentally bump into her"})

def segment_11(name):
    print("You: 'Good morning, Alicia!'")
    time.sleep(1)
    print("Alicia: 'Morning... Umm sorry, who are you?'")
    time.sleep(1)
    print(f"You: 'I'm {name} from class 5, by the way, are you alone'")
    time.sleep(1)
    print("Alicia: 'What do you mean??? Why are you asking?!' (in a mean tone)")
    time.sleep(1)
    print("Boy: *why so mean TT, but I need to continue talking to her*")
    time.sleep(1)
    return get_user_choice({"1": "By the way, you are so pretty", "2": "Hihi, why are you so mean", "3": "Alicia, I wanna tell you something"})

def segment_111():
    print("Narrator: You stand in front of a mysterious door with intricate carvings. Do you try to open the door or go back to the room?")
    return get_user_choice({"1": "Treasure room", "2": "Start"})

def play_game():
    name = get_player_name()
    current_segment = segment_1(name)

    while current_segment:
        if current_segment == "Say Hi":
            current_segment = segment_11(name)
        elif current_segment == "By the way, you are so pretty":
            current_segment = segment_111()
        elif current_segment == "By the way, you are so pretty":
            current_segment = segment_111()

def get_player_name():
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")
    return name

if __name__ == "__main__":
    play_game()
