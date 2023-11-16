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

def play_game():
    print("Welcome to the future! You are now a time traveller.")
    time.sleep(2)
    print("So you have a special ability to come back to the past.")
    time.sleep(2)
    print("With this ability, you can go back to the past as many time as you want.")
    time.sleep(2)
    print("To get your the girl of your dreams, Alicia.")
    time.sleep(2)
    print("Hope you can succed this time :)")
    time.sleep(2)
    story = {
        "start": {
            "prompt": "Boy: 'Umm.. Where is this'",
             "prompt": "Boy: 'Oh right, this is my room! I need to go to school to meet Alicia.' \n You rush to change your clothes and go to school /n You reached the shool \n Boy: 'Oh there's Alicia!' \n Boy: 'I need to go and see her'",
            "choices": {"1": "Say Hi", "2": "Pretend to know her", "3": "Pretend to get the wrong person", "4": "Pretend to accidently bump into her"}
        },
        "Say Hi": {
            "prompt": "Boy: 'Good morning, Alicia!' \n Alicia: 'Morning... Umm sorry who are you?' \n Boy: 'I'm B from class 5, by the way, are you alone' \n Alicia: 'Of course! I am comeing alone' (in a mean tone) \n Boy: *why so mean TT, but I need to find a topic to talk to her*",
            "choices": {"1": "By the way, you are so pretty", "2": "Hihi, why are you so mean", "3": "Alicia, I wanna tell you something"}
        },
        "By the way, you are so pretty": {
            "prompt": "Boy: 'By the way, you are so pretty' \n Alicia: 'Ew, are you a creep? Sorry I don't like creeper. Bye'",
            "choices": {}
        },
        "Treasure room": {
            "prompt": "The door opens to reveal a room filled with treasure! You win!",
            "choices": {}
        },
        "Continue": {
            "prompt": "You continue your journey. As you walk, you encounter a fork in the path. Will you go left or right?",
            "choices": {"1": "Enchanted forest", "2": "Deserted plain"}
        },
        "Enchanted forest": {
            "prompt": "You enter an enchanted forest. The trees whisper ancient secrets. Do you follow the mysterious sound or stay on the path?",
            "choices": {"1": "Follow sound", "2": "Stay on path"}
        },
        "Follow sound": {
            "prompt": "You follow the mysterious sound and discover a hidden waterfall. A magical creature appears and grants you a special power!",
            "choices": {}
        },
        "Stay on path": {
            "prompt": "You stay on the path and come across a friendly traveler. They offer to join you on your journey.",
            "choices": {}
        },
        "Deserted plain": {
            "prompt": "You enter a deserted plain. The wind carries whispers of ancient tales. In the distance, you see a mysterious figure. Do you approach or continue on the path?",
            "choices": {"1": "Approach figure", "2": "Continue on path"}
        },
        "Approach figure": {
            "prompt": "As you approach the figure, it disappears into thin air. You find a hidden cave entrance. Will you enter the cave or continue on the plain?",
            "choices": {"1": "Enter cave", "2": "Continue on plain"}
        },
        "Enter cave": {
            "prompt": "Inside the cave, you discover ancient artifacts and a map to a hidden city. You decide to follow the map.",
            "choices": {}
        },
        "Continue on plain": {
            "prompt": "You decide to continue on the plain. Suddenly, a sandstorm approaches. You find shelter just in time.",
            "choices": {}
        }
    }

    current_segment = "start"

    while current_segment:
        segment = story[current_segment]
        print(segment["prompt"])
        time.sleep(2)

        choices = segment["choices"]
        if choices:
            user_choice = get_user_choice(choices)
            current_segment = choices[user_choice]
        else:
            print("End of the story.")
            current_segment = None

if __name__ == "__main__":
    play_game()
