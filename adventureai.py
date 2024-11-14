from agents.text_agent import TextAgent
from agents.image_agent import ImageAgent
from agents.sound_agent import SoundAgent

"""Use all the agents in this file, start the gameflow by getting the user to customize their character (what feats is yet undecided)."""


def play_game():
    text_agent = TextAgent()
    image_agent = ImageAgent()
    sound_agent = SoundAgent()


if __name__ == "__main__":
    play_game()
