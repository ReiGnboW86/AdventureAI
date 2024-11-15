from Swarm import Swarm, Agent
from ..adventureai import (
    author,
    narrator,
    illustrator,
)
from dotenv import load_dotenv


class TriageAgent:
    def __init__(self, name, description, location):
        load_dotenv()
        self.client = Swarm()
        self.agent = Agent(
            name="Dungeon Master",
            model="gpt-4o-mini",
            instructions=(
                "You are a triage agent that connects several "
                "agents working together to write a story for a video game.\n"
                "Your task is to pass information between agents that generate content.\n"
                "Your input will be a string consisting of a story, player choice, player success."
                "You should do things in this order:\n"
                "1. Give the entire input string to the author agent. "
                "Author agent will then generate the next step in the story.\n"
                "2. Take the output from author agent and hand it to the narrator agent. \n"
                "Narrator agent will then generate a sound file."
                "3. Take the output from author agent and hand it to the illustrator agent. \n"
                "Illustrator agent will then generate an image."
                "4. Take the output from author agent and hand it to the navigator agent. \n"
                "Navigator agent will then determine the location of the story."
            ),
            functions=[
                self.transfer_to_author,
                self.transfer_to_illustrator,
                self.transfer_to_narrator,
            ],
        )

        # Player information. Should be moved to database:
        self.player_name = name
        self.player_description = description

        self.previous_story = None
        self.current_story = None
        self.current_location = location
        self.current_image = None
        self.current_audio = None
        self.context_string = None

    def set_context(self, choice, success):
        self.context_string = (
            f"Protagonist name: {self.playername}\n"
            f"Protagonist description: {self.player_description}\n"
            f"Current location: {self.current_location}"
            f"Previous story: {self.previous_story}"
            f"{self.player_description} attempted to: {choice}\n"
            f"{self.player_description} was successful with their action: {success}"
        )

    def next_story(self, choice, success):
        response = self._make_api_call(choice, success)
        new_story = self._extract_response(response)
        return new_story

    def _make_api_call(self, choice, success) -> str:
        response = self.client.run(
            agent=self.author,
            messages=[
                {
                    "role": "user",
                    "content": self.context_string,
                }
            ],
            # Seems our agent can't access context variables
            context_variables={
                "previous_story": self.previous_story,
                "player_choice": choice,
                "player_choice_successful": success,
            },
        )

        return response

    def _extract_response(self, response) -> str:
        """THIS NEEDS TO BE CALIBRATED TO FIT THE NEW RESPONSE WITH MULTIPLE AGENTS"""
        next_story = response.messages[0]["content"]
        self.previous_story = next_story

        return next_story

    def transfer_to_author(self):
        """Transfers to the author agent"""
        return author.agent

    def transfer_to_narrator(self):
        """Transfers to the author agent"""
        return narrator.agent

    def transfer_to_illustrator(self):
        """Transfers to the author agent"""
        return illustrator.agent
