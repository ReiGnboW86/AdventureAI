from swarm import Swarm, Agent
from dotenv import load_dotenv
from ..adventureai import image_agent, sound_agent


load_dotenv()

client = Swarm()


class TextAgent:
    def __init__(
        self,
        player_name,
        player_description,
        starting_location,
        player_choice,
    ):
        if not player_name:
            player_name = "Bob"
        self.player_name = player_name

        if not player_description:
            player_description = "I'm a person with no imagination!"
        self.player_description = player_description

        if not starting_location:
            starting_location = "At home by the computer."

        if not player_choice:
            player_choice = "I am playing an AI-generated fantasy story game."

        self.previous_story = (
            f"This is the story about {player_name}.\n"
            "When prompted to tell us about themselves, "
            f"they wrote: {player_description}\n"
            f"Location: {starting_location}\n"
            f"{player_name}'s next action: {player_choice}"
        )
        self.client = Swarm()
        self.agent = Agent(
            name="The Author",
            model="gpt-4o-mini",
            instructions="""
You are an interactive storyteller for a video game.
Your role is to generate dynamic, atmospheric narratives that adapt to player actions and game conditions. 
You analyze the users input and take into consideration which way they wish to progress the story.
The story should be of length maximum 100 words.

- Create vivid, concise descriptions that capture both atmosphere and action
- Incorporate outcomes of player actions
- Maintain narrative continuity with previous story elements
- Transfer to sound agent for text to speech generation

Before crafting each scene, you'll receive as context variables:
1. previous_story: Previous story events.
2. player_choice: What the player chose to do with the previous story.
3. player_choice_successful: Indicates if the player succeded with their choice.""",
            functions=[self._transfer_to_voice_agent],
        )

    def generate_story(self, dice_result, player_choice):
        response = self._make_api_call(dice_result, player_choice)
        new_story = self._extract_response(response)
        return new_story

    def _make_api_call(self, dice_result, player_choice) -> str:
        response = self.client.run(
            agent=self.author,
            messages=[
                {
                    "role": "user",
                    "content": (
                        "Please progress the story from the following context:"
                        f"Previous story: {self.previous_story}"
                        f"{self.player_name} chose to: {player_choice}"
                        f"Success status of the player action: {dice_result}"
                    ),
                }
            ],
            # What even does this do.
            # Seems our agent can't access this dict
            context_variables={
                "previous_story": self.previous_story,
                "player_choice": player_choice,
                "player_choice_successful": dice_result,
            },
        )

        return response

    def _extract_response(self, response) -> str:
        next_story = response.messages[0]["content"]
        self.previous_story = next_story

        return next_story

    def _transfer_to_voice_agent():
        """Transfers to the text to speech agent"""
        return sound_agent.narrator
