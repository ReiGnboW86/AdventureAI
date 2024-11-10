from agents.text_agent import TextAgent
from agents.image_agent import ImageAgent
from agents.database_agent import DatabaseAgent
from agents.character_agent import CharacterAgent
from agents.sound_agent import SoundAgent
from agents.dice_agent import DiceAgent
from agents.death_agent import DeathAgent
from agents.combat_agent import CombatAgent
from agents.loot_agent import LootAgent
from agents.npc_agent import NPCAgent

"""Use all the agents in this file, start the gameflow by getting the user to customize their character (what feats is yet undecided)."""


def play_game():
    text_agent = TextAgent()
    image_agent = ImageAgent()
    database_agent = DatabaseAgent()
    character_agent = CharacterAgent()
    sound_agent = SoundAgent()
    dice_agent = DiceAgent()
    death_agent = DeathAgent()
    combat_agent = CombatAgent()
    loot_agent = LootAgent()
    npc_agent = NPCAgent()


if __name__ == "__main__":
    play_game()
