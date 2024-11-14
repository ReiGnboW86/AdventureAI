from swarm import Swarm, Agent
import openai
import os
import json

# API_KEY = os.environ.get("OPENAI_API_KEY")

client = Swarm()


class TextAgent:
    def __init__(self):
        # if not API_KEY:
        #     raise ValueError("API KEY NOT SET MTHRFKR")
        self.narrator = Agent(
            name="The Narrator",
            instructions="""
You are a fantasy storyteller for a video game.
Create engaging narratives based on provided context such as:
context(contains the previous story and what the player would like to do next),
dice results(wether or not a player was successful with doing something),
the action level(higher number means its action-packed, lower number means its calm and peaceful).
Keep descriptions vivid but concise with a maximum of 200 words.
Generate the next segment as JSON in this format:
{{
    "new_story": Detailed situation description. Datatype string.,
    "new_location": "The location of 'text' (Does not need to change if it fits the narrative). Datatype string.,
    "action_change": The change in action_level (example: +1, -3). Datatype integer.
}}""",
            functions=[],
        )

        self.previous_story: str = "You woke up in the barn."
        self.location = "New York City"
        self.action_level: int = 7

    def generate_story(self, dice_result, player_choice):
        response = client.run(
            agent=self.narrator,
            messages=[
                {
                    "role": "user",
                    "content": f"Player chose: {player_choice}. Successful roll: {dice_result}",
                }
            ],
            context_variables={
                "previous_story": self.previous_story,
                "current_location": self.location,
                "current_action_level": self.action_level,
            },
        )
        print(type(response.messages[0]["content"]))

        new_story = response.messages[0]["content"]
        # self.location = story_data["new_location"]
        # self.action_level = self.action_level + story_data["action_change"]

        return new_story


#     def get_story(self, dice_result):
#         # DEPRECATED?
#         prompt = f"""
# - Previous Story: {self.previous_story}
# - Current Location: {self.location}
# - Current Action Level: {self.action_level}

# Generate the next segment in this format:
# {{
#     "new_story": Detailed situation description. Datatype string.,
#     "new_location": "The location of 'text' (Does not need to change if it fits the narrative). Datatype string.,
#     "action_change": The change in action_level (example: +1, -3). Datatype integer.
# }}
# """

#         response = client.chat.completions.create(
#             model="gpt-4",
#             messages=[
#                 {
#                     "role": "system",
#                     "content": """
# You are a fantasy storyteller for a video game.
# Create engaging narratives based on provided context such as:
# context(contains the previous story and what the player would like to do next),
# dice results(wether or not a player was successful with doing something),
# the action level(higher number means its action-packed, lower number means its calm and peaceful).
# Keep descriptions vivid but concise with a maximum of 200 words.
# """,
#                 },
#                 {"role": "user", "content": prompt},
#             ],
#             temperature=0.7,
#         )

#         story_content = response.choices[0].message.content

#         try:
#             story_data = json.loads(story_content)
#         except json.JSONDecodeError:
#             story_data = {
#                 "new_story": self.previous_story,
#                 "new_location": self.location,
#                 "action_change": 0,
#             }

#             return story_data
