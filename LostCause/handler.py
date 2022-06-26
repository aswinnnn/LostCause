# Error Handler
# Handles errors which should rarely happen in-game, also my first time custom-error handling.
# 26 June 2022

class Success():
    # Success object for whenever the database works fine. not that important really, but principle.
    pass

class GameError(Exception):
    # Base class for any in-game errors.
    pass

class NotAnOption(GameError):
    # For when the player picks a choice that is not known.
    # This class should be deprecated because of me using rich's inbuilt choice system for options.
    # Im saving this for later when I'll eventually stop using rich and move on to becoming more self-reliant.
    pass

class CharacterAlreadyExists(GameError):
    # For when the player tries to create a character already created. Shitty rule, i know but i dont
    # want the DB to mess up much.
    pass
