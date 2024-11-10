"""
Takes input from:
    Text Agent
    Loot Agent
    Database (if we want to make an image of the character)
    NPC Agent

Gives output to:
    Text Agent (or just the user directly)
    Death Agent


Creates an image using Stable Diffusion 1.5 through an API (which I will make)
based on the :
    TextAgent,
    CombatAgent,
    CharacterAgent,
    NPCAgent,
    LootAgent,
    DeathAgent,
    DiceAgent.

This will be used alot and the images will be saved using DatabaseAgent.

Images should be generated when:
    Text Agent progresses the story.
    Combat initiates.
    A new item is introduced (old items can have their images stored in the database)
    A new NPC is introduced (old npcs can have their images stored in the database.)

Images should NOT be generated when:
    A dice is rolled: This can be stored beforehand since there are only 20 different outcomes.
    For each step in combat: Seems unessecary. We could just have one image when initiated and one when combat is over.

"""


class ImageAgent:
    pass
