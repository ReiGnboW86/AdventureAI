"""
I dont think this needs to be an agent. Here is why:
We could have this part of the game be a way of keeping track of the Adventurer.
    Health, Buff/Debuffs, Stats, Inventory

This could easily be stored within a dictionary in the database:
(I will be using Wise old man and his setup as an example for this entire directory)
See more in how this ties together with the other agents.


"Wise old man": {
    "stats": {
        "health": 70,
        "strength": 5,
        "dexterity": 6,
        "intelligence": 10,
        "charisma": 7,
        "stamina": 2,
    },
    "inventory": [
        Bag of candy,
        Invisibility potion,
        Bottle of chlorophorm,
        Handkerchief,
    ],
    "currently_wearing": {
        "head": Spectacles,
        "chest": Wolf t-shirt,
        "legs": Manchester pantaloons,
        "feet": Hospital slippers,
    },
    "buffs": [
        Aura of the white van,
        Shackles of the old and tired,
    ],
}
"""


class CharacterAgent:
    pass
