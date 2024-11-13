"""
AdventureAI - An AI-Powered Choose Your Own Adventure Game

Main Game Architecture and Flow Controller

Core Components:
    Text Generation:
        - Uses Mistral 7B Dolphin model
        - Local inference via llama.cpp
        - Uncensored content generation
        - Dynamic story adaptation

    Image Generation:
        - Stable Diffusion 1.5
        - Comic panel style
        - Character portraits
        - Scene visualization

    Sound Generation:
        - Bark/AudioCraft integration
        - Voice synthesis
        - Sound effects
        - Ambient audio

    Database:
        - PostgreSQL with pg_embeddings
        - SQLAlchemy ORM
        - State persistence
        - Media caching

Game Flow:
    1. Character Creation:
        - Description input
        - Stats generation
        - Portrait creation
        - Database initialization

    2. Story Progression:
        - Scene generation
        - Visual rendering
        - Audio production
        - Player interaction
        - State updates

    3. Action Resolution:
        - Probability calculation
        - Outcome determination
        - Multi-modal feedback
        - State persistence

    4. Death Handling:
        - Death scene creation
        - State cleanup
        - Game over processing
        - Save management

Technical Features:
    - Asynchronous processing
    - Resource optimization
    - Error recovery
    - State management
    - Media caching
    - Performance monitoring

Usage:
    Run directly to start game:
    `python adventureai.py`

Requirements:
    - Python 3.8+
    - PostgreSQL 12+
    - GPU recommended
    - 16GB+ RAM
    - See requirements.txt
"""

from agents import (
    TextAgent,
    ImageAgent,
    SoundAgent,
    NPCAgent,
    LootAgent,
    CombatAgent,
)
from database.database import Database
from utils.dice import DiceRoller


def play_game():
    """
    Main game loop that initializes and coordinates all components.

    Flow:
    1. Initialize database and utilities
    2. Start agent services
    3. Begin character creation
    4. Start main game loop
    5. Process player input
    6. Generate appropriate responses
    7. Update game state
    8. Handle game over conditions
    """
    # Initialize database and utilities
    database = Database()
    dice_roller = DiceRoller()

    # Initialize agents
    text_agent = TextAgent()
    image_agent = ImageAgent()
    sound_agent = SoundAgent()
    npc_agent = NPCAgent()
    loot_agent = LootAgent()
    combat_agent = CombatAgent()


if __name__ == "__main__":
    play_game()
