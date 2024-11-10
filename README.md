# AdventureAI
Choose your own adventure AI text game! I was inspired from our little Hackathon project creating a similar game using OpenAI Swarm agents.
This project is planned to be using langchain and a vector database to create a better user experience (maybe I will use agents further down, I don't know yet)

Please follow!

Decided to use Datastax AstraDB (Thanks Tech with Tim @ Youtube) as the Vector database for this project as their free tier is godly (5gb). 

Check them out (Tech with Tim's link for referral): https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbUhaYkFwTWw3ZjRuUlEwSGJsZTRMS2tyNjVRUXxBQ3Jtc0trNXV1R3d6ZC1iVGlZR0N6bnNscWFwcUxRQk55RFpCTjVUNjFXZFFJaW5pSDFGV3JwVk5ocjZWRGhLSUF2eGoyamdac0VGVFJlcUFnSVlLanJMQmhSZHM3bXR2OHl2cnFnbVpJclRqV01DY1hFQXRsQQ&q=https%3A%2F%2Fwww.datastax.com%2Flp%2Fastra-registration%3Futm_medium%3Dyoutube_video%26utm_source%3Ddatastax%26utm_campaign%3Dyt_influencers%26utm_content%3Dvector_search_tim_ruscica&v=nhYcTh6vw9A

UPDATE: We might have to switch from AstraDB to something local to keep our thought of doing this project absolutely free. Altho 5gb is alot, it might not be sufficient in the long run with image generation. I will look for a local open-source solution but we will use AstraDB for now.

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
-

* Felix
- 