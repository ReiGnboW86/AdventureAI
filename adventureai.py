from agents import TextAgent
from agents import ImageAgent
from agents import SoundAgent
from database import Database


def play_game():
    db = Database(dbname="adventure_db", user="user", password="password")

    text_agent = TextAgent()
    image_agent = ImageAgent()
    sound_agent = SoundAgent()


if __name__ == "__main__":
    play_game()
