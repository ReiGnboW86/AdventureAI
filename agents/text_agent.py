from swarm import Swarm, Agent
import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()

# API_KEY = os.environ.get("OPENAI_API_KEY")

client = Swarm()


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
        print(type(response.messages[0]["content"]))

        return response

    def extract_response(self, response) -> str:
        next_story = response.messages[0]["content"]
        self.previous_story = next_story

        return next_story
