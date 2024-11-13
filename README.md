# AdventureAI
Choose your own adventure AI text game! I was inspired from our little Hackathon project creating a similar game using OpenAI Swarm agents.
This project is planned to be using langchain and a vector database to create a better user experience.

Please star and follow!

We just uncovered our next project for our class which is to learn PostgreSQL. Therefor, I have decided we are going to use that as our database to store the data together with pg_embeddings.

Decided on an LLM model to use for generation, due to its unhinged restrictions and filter, we're going to use Mistral's 7b Dolphin model Q4 K-M
https://huggingface.co/TheBloke/dolphin-2.0-mistral-7B-GGUF

How this implementation is going to look is unclear at the moment, but we will figure it out as we go.

# The Story so far

Invited Felix to colab on this project since we made the Hackathon project together and he is an awesome dev with good ideas. I wrote some placeholder code and docstrings to outline how the program is thought to function and decided on a few packages that we will use. For now I have imported the GPT4All free LLM but I plan on using a Mistral model without censorship (since this is important to us). A choose your own adventure game should only be limited by your mind (and laws). This makes this game 18+ when it is realeased eventually. 

# Thoughts

* Decide on an LLM to use for local generation

* Decide how we want to ship the final product. Interactive webpage? Standalone app? Mobile app? API for integration for larger scale? The possibilitys are endless.

* Choose an agent framework that suits our needs and skills (OpenAI Swarm or Langchain Agents)

* Think of more packages or agents we might need to make the experience better

* Decide on what we want to use for rendering everything together eventually (original plan is to make the game kind of like a comic book rendering (Tkinter?))

# TODO

* Get TextAgent to implement basic storytelling functionality in using a local LLM

* Get DatabaseAgent to connect to the database and save information in the correct format

* Get ImageAgent to render images in 512x512 focusing on accuracy and speed of rendering

* Get DiceAgent to figure out when to make a DiceRoll and when to pass a task as a trivial task

* Get CharacterAgent implemented with the DatabaseAgent and the ImageAgent and call it as the first thing the player gets to do in adventureai.py

* Get DeathAgent to figure out when you are dead or when CombatAgent tells you that life is over OR when you make a daredevil move and fail miserably (jumping comes to mind)

* Get SoundAgent to play appropriate/inappropriate sounds based on the context of the story and actions of the player

* Get LootAgent to randomize loot from encounters (low chance of useful, high chance of fun) with NPCS/Monsters and store this together with the players inventory with CharacterAgent.

* Get NPCAgent to dynamically identify bigger story characters as NPCs and store their data together with their loot while also showing an image of them based on their description.

* Get CombatAgent to dynamically identify a situation or action that requires a check if the player or monster succeeds and how much damage someone takes depending on the context (fork to knee, small problem. Claymore to retina, huge problem.)

# CONTINUOUS WORK

* Writing the adventureai.py file logic based on what is implemented gradually.

* Testing the game, documenting bugs and errors.

* Writinging a correct documentation in a separate file.

# IMPLEMENTED

Here we update the README.md in the main branch to show what we are currently working on implementing.

* Bjorn

Wrote extensive plan and updated file structure. We need a meeting soon to discuss these changes before we start implementing.

* Felix
- 

# Huge Update Breakdown

We decided we don't need all the previously specified agents, so this is the updated structure along with some packages we might use

agents/: Contains all AI-driven components of the game.

text_agent.py: Handles story generation using Mistral LLM.
image_agent.py: Generates comic-style images using Stable Diffusion.
sound_agent.py: Manages audio and voice generation with Bark/AudioCraft.
npc_agent.py: Controls NPC behavior and dialogue.
loot_agent.py: Handles item generation and distribution.
combat_agent.py: Manages the battle system and death mechanics.
utils/: Contains utility classes and functions.

database.py: Interface for PostgreSQL using SQLAlchemy.
dice_roller.py: Utility for probability and random event handling.
models/: Contains data models for the game state and entities.

game_models.py: Defines ORM models for the database.
tests/: Contains unit tests for each component that needs testing.

adventureai.py: The main game loop script.