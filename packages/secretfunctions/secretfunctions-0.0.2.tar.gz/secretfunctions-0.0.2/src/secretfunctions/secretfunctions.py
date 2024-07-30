"""
# =============================================================================
#
#  Licensed Materials, Property of Ralph Vogl, Munich
#
#  Project : stocksdatabase
#
#  Copyright (c) by Ralph Vogl
#
#  All rights reserved.
#
#  Description:
#
#  a simple module to keep secrets private
#
# =============================================================================
"""

# -------------------------------------------------------------
# IMPORTS
# -------------------------------------------------------------
from typing import Any
import os
import load_dotenv

# -------------------------------------------------------------
#  FUNCTION DEFINITIONS
# -------------------------------------------------------------

# -------------------------------------------------------------
# DEFINITIONS REGISTRY
# -------------------------------------------------------------

# -------------------------------------------------------------
# DEFINITIONS
# -------------------------------------------------------------

# -------------------------------------------------------------
# VARIABLE DEFINTIONS
# -------------------------------------------------------------


# -------------------------------------------------------------
# CLASS DEFINTIONS
# -------------------------------------------------------------


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass in this example.
    """

    # Dictionary stores single instance of the class for
    # each subclass of the SingletonMeta metaclass
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # Single instance of the class already been created?
        if cls not in cls._instances:
            # Create the instance by calling the call
            # method of the parent's (super () .. call ())
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SecretFunctions(metaclass=SingletonMeta):
    """
    class SecretFunctions loads .env file in home directory and makes all values available
    via get_secret_key method
    """

    config = None

    def __init__(self):
        """
        Constructor of SecretFunctions class, reads the .env file in home directory
        as the standard config file and makes all values available
        """
        env_filename = f"{os.path.expanduser('~')}{os.path.sep}.env"
        load_dotenv.load_dotenv(env_filename)

    def get_secret_key(self, key: str, default: Any = None) -> Any:
        """
        Summary:
        get the secret key from the settings.ini file

        Parameters:
        ----------
        key : str
            the key to get the secret for
        section : str
            the section in the config file
        default : Any
            the default value to return if the key is not found

        Returns:
        -------
        Any
            the secret key or the default value
        """
        val = os.getenv(key)
        if not val:
            return default
        return val
