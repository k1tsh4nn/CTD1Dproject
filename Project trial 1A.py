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
    print("Welcome to the Choose Your Adventure Game!")
    time.sleep(1)

    story = {
        "start": {
            "prompt": "You wake up in a mysterious room. There are two paths ahead. Do you go left or right?",
            "choices": {"1": "Dark tunnel", "2": "Mysterious door"}
        },
        "Dark tunnel": {
            "prompt": "You venture down a dark tunnel. It gets colder and narrower. Suddenly, you see a light at the end.",
            "choices": {"1": "Continue"}
        },
        "Mysterious door": {
            "prompt": "You stand in front of a mysterious door with intricate carvings. Do you try to open the door or go back to the room?",
            "choices": {"1": "Treasure room", "2": "Start"}
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
        time.sleep(1)

        choices = segment["choices"]
        if choices:
            user_choice = get_user_choice(choices)
            current_segment = choices[user_choice]
        else:
            print("End of the story.")
            current_segment = None

if __name__ == "__main__":
    play_game()
