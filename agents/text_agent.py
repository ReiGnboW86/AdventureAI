from swarm import Swarm, Agent
import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()


class TextAgent:
    def __init__(self):
        self.client = Swarm()
        self.narrator = Agent(
            name="The Narrator",
            model="gpt-4o-mini",
            instructions="""
You are an interactive fantasy storyteller for a video game. 
Your role is to generate dynamic, atmospheric narratives that adapt to player actions and game conditions. 
The story should be of length maximum 100 words.

- Create vivid, concise descriptions that capture both atmosphere and action
- Adapt the tone and pacing based on the provided action level
- Incorporate outcomes of player actions
- Maintain narrative continuity with previous story elements

Before crafting each scene, you'll receive as context variables:
1. previous_story: Previous story events.
2. player_choice: What the player chose to do with the previous story.
3. player_choice_successful: Indicates if the player succeded with their choice.""",
        )

        self.previous_story: str = "You are sleeping in a barn."

    def generate_story(self, dice_result, player_choice):
        response = self.make_api_call(dice_result, player_choice)
        new_story = self.extract_response(response)
        return new_story

    def make_api_call(self, dice_result, player_choice) -> str:
        response = self.client.run(
            agent=self.narrator,
            messages=[
                {
                    "role": "user",
                    "content": (
                        "Please progress the story from the following context:"
                        f"Previous story: {self.previous_story}"
                        f"The player chose to: {player_choice}"
                        f"Success status of the player action: {dice_result}"
                    ),
                }
            ],
            context_variables={
                "previous_story": self.previous_story,
                "player_choice": player_choice,
                "player_choice_successful": dice_result,
            },
        )

        return response

    def extract_response(self, response) -> str:
        next_story = response.messages[0]["content"]
        self.previous_story = next_story

        return next_story


# for dict in reponse.messages:
#     if dict["sender"] == "The interpreter":
#         content = dict["content"]
# messages=[
#     {
#         'content': None,
#         'refusal': None,
#         'role': 'assistant',
#         'audio': None,
#         'function_call': None,
#         'tool_calls': [
#             {
#                 'id': 'call_jTCd604A8BYQMLJiw4L1KNZ4',
#                 'function': {
#                     'arguments': '{}',
#                     'name': 'transfer_to_interpter'
#                 },
#                 'type': 'function'
#             }
#         ],
#         'sender': 'The Narrator'
#     },
#     {
#         'role': 'tool',
#         'tool_call_id': 'call_jTCd604A8BYQMLJiw4L1KNZ4',
#         'tool_name': 'transfer_to_interpter',
#         'content': '{"assistant": "The interpreter"}'
#     },
#     {
#         'content': 'You wake up in the dim light of the barn, dust motes dancing in the air as you slowly adjust to your surroundings. As you sit up, the scent of hay and the distant sounds of the city seep into your senses, reminding you that you are not far from the bustling streets of New York City. The sun is rising, casting a warm glow through the hayloft window, and you feel a strange energy coursing through your veins. You realize that the choices ahead of you could lead to unexpected adventures; New York City awaits just outside the barn doors. You stretch and prepare to step into the vibrant chaos of the metropolis, where new challenges and discoveries lie in wait.;New York City;7',
#         'refusal': None,
#         'role': 'assistant',
#         'audio': None,
#         'function_call': None,
#         'tool_calls': None,
#         'sender': 'The interpreter'
#     }
# ]

# agent=Agent(
#     name='The interpreter',
#     model='gpt-4o-mini',
#     instructions='''
# You are an interpreter of AI generated storytelling.
# Your role is to take a string as input and convert them into a uniform output.
# Find each segment in the string and separate them accordingly.
# Your output must always be formatted like this:
# The story;The location;The action level difference

# The story will always be a longer text.
# The location does not nessecarily need to be a real place.
# The action level must always be able to be typecast into an integer to use in mathematical operations.
# Do use semicolons as separators.
# Do not define what something is in their respective column (Location: New York # DO NOT DO THIS).
# ''',
#     functions=[],
#     tool_choice=None,
#     parallel_tool_calls=True
# )

# context_variables={
#     'previous_story': 'You are sleeping in a barn.',
#     'player_choice': 'I try to wake up',
#     'player_choice_successful': True,
#     'current_location': 'New York City',
#     'current_action_level': 7
# }
