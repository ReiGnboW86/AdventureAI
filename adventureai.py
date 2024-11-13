"""
AdventureAI - An AI-Powered Choose Your Own Adventure Game

Main Game Architecture and Flow Controller

Core Components:
    - Text Generation (Mistral LLM)
    - Image Generation (Stable Diffusion 1.5)
    - Sound Generation (Bark/AudioCraft)
    - Database Management (PostgreSQL)
    - Game Logic Systems

Game Flow:
    1. Character Creation
        - Player inputs character description
        - System generates character stats and initial inventory
        - Creates character portrait
        - Establishes character in database

    2. Story Progression
        - TextAgent generates scene description
        - ImageAgent creates comic panel
        - SoundAgent generates ambient sounds
        - Player receives multi-modal scene presentation
        - Player inputs desired action
        - System processes action through relevant agents

    3. Action Resolution
        - DiceRoller determines success/failure
        - TextAgent interprets results
        - CombatAgent handles battles
        - NPCAgent manages interactions
        - LootAgent handles item acquisition
        - Database maintains state

    4. Death Handling
        - CombatAgent processes character death
        - Generates death scene and description
        - Handles game over state
        - Manages character deletion

Technical Implementation:
    - Asynchronous agent communication
    - State management through PostgreSQL
    - Media asset caching
    - Error handling and recovery
    - Save state management
    - Resource optimization

Components:
    Agents:
        TextAgent:
            - Central story coordinator
            - Interprets player input
            - Generates narrative content

        ImageAgent:
            - Creates scene visualizations
            - Maintains visual consistency
            - Handles comic panel layout

        SoundAgent:
            - Generates audio effects
            - Creates character voices
            - Manages ambient sound

        NPCAgent:
            - Handles character interactions
            - Manages AI behaviors
            - Controls monster actions

        LootAgent:
            - Generates items and rewards
            - Manages drop tables
            - Controls item distribution

        CombatAgent:
            - Manages battle system
            - Handles death scenarios
            - Controls combat flow

    Utilities:
        Database:
            - Maintains game state
            - Handles data persistence
            - Manages relationships

        DiceRoller:
            - Handles probability
            - Manages random events
            - Controls action outcomes

Usage:
    Run this file directly to start the game:
    `python adventureai.py`
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
