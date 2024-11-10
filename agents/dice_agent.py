"""
Takes input from:
    Combat Agent
    Story Agent
    Loot Agent

Gives output to:
    Combat Agent
    Story Agent
    Loot Agent


Makes a dice roll based on when the player is trying to do a more than trivial task.
For normal tasks as walking and brushing teeth, it doesnt make a roll.
For attacking dragons and doing taxes, it should.

Might implement an agent to calculate the difficulty
of each task (DifficultyAgent?) or its handled here.

Stores rolls in DatabaseAgent.
Works together with TextAgent and ImageAgent in how the story should proceed
based on the outcome.

This agent should determine how difficult a task is.
Decide what number is needed to pass and then use random.choice(20)
The only AI-related thing here is to determine the threshhold of a successful roll.
I dont think we need to store rolls unless you are talking about inspiration where a player can re-roll if they fail.

In DnD you can get inspired by your own or others actions based on who you are and your beliefs.
One inspire = one extra dice-roll
This seems like alot to implement. Or it could be determined by another agent based on the character description the player sets at character creation.
"""


class DiceAgent:
    pass
