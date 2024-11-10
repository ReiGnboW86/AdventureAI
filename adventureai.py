from agents import (
    TextAgent,
    ImageAgent,
    DatabaseAgent,
    CharacterAgent,
    SoundAgent,
    DiceAgent,
    DeathAgent,
    CombatAgent,
    LootAgent,
    NPCAgent,
)

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
