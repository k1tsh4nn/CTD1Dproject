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

def segment_1():
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

def segment_11():
    print("You: 'Good morning, Alicia!'")
    time.sleep(1)
    print("Alicia: 'Morning... Umm sorry, who are you?'")
    time.sleep(1)
    print("You: 'I'm from Bryan class 5, by the way, are you alone'")
    time.sleep(1)
    print("Alicia: 'What do you mean??? Why are you asking?!' (in a mean tone)")
    time.sleep(1)
    print("Boy: *why so mean TT, but I need to continue talking to her*")
    time.sleep(1)
    return get_user_choice({"1": "By the way, you are so pretty", "2": "Hihi, why are you so mean", "3": "Alicia, I wanna tell you something"})

def segment_111():
    print("Boy: 'By the way, you are so pretty'")
    time.sleep(1)
    print("Alicia: 'Ew, are you a creep? Sorry I don't like creeper. Bye'")
    time.sleep(1)
    print("Do you want to restart the game")
    return get_user_choice({"1": "Restart"})

def mysterious_door():
    print("Narrator: You stand in front of a mysterious door with intricate carvings. Do you try to open the door or go back to the room?")
    return get_user_choice({"1": "Treasure room", "2": "Start"})

def treasure_room():
    print("Narrator: The door opens to reveal a room filled with treasure! You win!")

def continue_journey():
    print("Narrator: You continue your journey. As you walk, you encounter a fork in the path. Will you go left or right?")
    return get_user_choice({"1": "Enchanted forest", "2": "Deserted plain"})

def enchanted_forest():
    print("Narrator: You enter an enchanted forest. The trees whisper ancient secrets. Do you follow the mysterious sound or stay on the path?")
    return get_user_choice({"1": "Follow sound", "2": "Stay on path"})

def follow_sound():
    print("Narrator: You follow the mysterious sound and discover a hidden waterfall.")
    time.sleep(1)
    print("Magical Creature: 'Welcome, traveler! What brings you to this enchanted place?'")
    return get_user_choice({"1": "Ask about the creature", "2": "Express gratitude"})

def ask_about_creature():
    print("You: 'What kind of creature are you?'")
    time.sleep(1)
    print("Magical Creature: 'I am a guardian spirit of this forest. I grant you a special power for respecting our home.'")

def express_gratitude():
    print("You: 'Thank you for welcoming me. I'm on a journey to find...'")
    time.sleep(1)
    print("Magical Creature: 'Ah, the journey of life! May it be filled with wonders.'")

def stay_on_path():
    print("Narrator: You stay on the path and come across a friendly traveler. They offer to join you on your journey.")

def deserted_plain():
    print("Narrator: You enter a deserted plain. The wind carries whispers of ancient tales. In the distance, you see a mysterious figure.")
    time.sleep(1)
    print("Narrator: Do you approach the figure or continue on the path?")
    return get_user_choice({"1": "Approach figure", "2": "Continue on path"})

def approach_figure():
    print("Narrator: As you approach the figure, it disappears into thin air.")
    time.sleep(1)
    print("Narrator: You find a hidden cave entrance. Will you enter the cave or continue on the plain?")
    return get_user_choice({"1": "Enter cave", "2": "Continue on plain"})

def enter_cave():
    print("Narrator: Inside the cave, you discover ancient artifacts and a map to a hidden city.")
    time.sleep(1)
    print("Narrator: You decide to follow the map.")

def continue_on_plain():
    print("Narrator: You decide to continue on the plain. Suddenly, a sandstorm approaches.")
    time.sleep(1)
    print("Narrator: You find shelter just in time.")

def play_game():
    current_segment = segment_1()

    while current_segment:
        if current_segment == "Say Hi":
            current_segment = segment_11()
        elif current_segment == "By the way, you are so pretty":
            current_segment = segment_111()
        elif current_segment == "Restart":
            restart()
            current_segment = segment_1()
        elif current_segment == "Continue":
            current_segment = continue_journey()
        elif current_segment == "Enchanted forest":
            current_segment = enchanted_forest()
        elif current_segment == "Follow sound":
            current_segment = follow_sound()
        elif current_segment == "Ask about the creature":
            ask_about_creature()
            current_segment = None
        elif current_segment == "Express gratitude":
            express_gratitude()
            current_segment = None
        elif current_segment == "Stay on path":
            stay_on_path()
            current_segment = None
        elif current_segment == "Deserted plain":
            current_segment = deserted_plain()
        elif current_segment == "Approach figure":
            current_segment = approach_figure()
        elif current_segment == "Enter cave":
            enter_cave()
            current_segment = None
        elif current_segment == "Continue on plain":
            continue_on_plain()
            current_segment = None


if __name__ == "__main__":
    play_game()
