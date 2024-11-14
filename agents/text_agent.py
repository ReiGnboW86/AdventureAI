from swarm import Swarm, Agent
import openai
import os
import json


class TextAgent:
    def __init__(self):
        self.client = Swarm()
        self.narrator = Agent(
            name="The Narrator",
            instructions="""
You are a fantasy storyteller for a video game.
Create engaging narratives based on provided context such as:
context(contains the previous story and what the player would like to do next),
dice results(wether or not a player was successful with doing something),
the action level(higher number means its action-packed, lower number means its calm and peaceful).
Keep descriptions vivid but concise with a maximum of 200 words.
Format your response in three different messages and follow this example:

"new_story": "Detailed situation description",
"new_location": "The location of 'new_story' (Does not need to change if it fits the narrative).",
"action_change": -2
""",
            functions=[],
        )

        self.previous_story: str = ""
        self.location = ""
        self.action_level: int = 0

    def generate_story(self, dice_result, player_choice):
        response = self.client.run(
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

        try:
            story_data = json.loads(response)
        except json.JSONDecodeError:
            story_data = {
                "new_story": self.previous_story,
                "new_location": self.location,
                "action_change": 0,
            }

        new_story = response.messages[0]["content"]
        self.location = response.messages[1]["content"]
        self.action_level = (
            self.action_level + response.messages[2]["content"]
        )

        return new_story

    def get_story(self, dice_result):
        # DEPRECATED?
        prompt = f"""
- Previous Story: {self.previous_story}
- Current Location: {self.location}
- Current Action Level: {self.action_level}

Generate the next segment in this format:
{{
    "new_story": Detailed situation description. Datatype string.,
    "new_location": "The location of 'text' (Does not need to change if it fits the narrative). Datatype string.,
    "action_change": The change in action_level (example: +1, -3). Datatype integer.
}}
"""

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": """
You are a fantasy storyteller for a video game.
Create engaging narratives based on provided context such as:
context(contains the previous story and what the player would like to do next),
dice results(wether or not a player was successful with doing something),
the action level(higher number means its action-packed, lower number means its calm and peaceful).
Keep descriptions vivid but concise with a maximum of 200 words.
""",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )

        story_content = response.choices[0].message.content

        try:
            story_data = json.loads(story_content)
        except json.JSONDecodeError:
            story_data = {
                "new_story": self.previous_story,
                "new_location": self.location,
                "action_change": 0,
            }

            return story_data
