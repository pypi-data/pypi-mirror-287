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

import toml

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
    class SecretFunctions
    """

    config = None

    def read_config(self, config_file: str) -> "SecretFunctions":
        """
        Summary:
        read the config file

        Parameters:
        ----------
        config_file : str
            the config file to read

        Returns:
        -------
        dict
            the config file as a dictionary
        """
        self.config = toml.load(config_file)

        return self

    def get_secret_key(self, key: str, section: str = None) -> Any:
        """
        Summary:
        get the secret key from the settings.ini file

        Parameters:
        ----------
        key : str
            the key to get the secret for
        section : str
            the section in the config file

        Returns:
        -------
        str
            the secret key
        """
        if section is not None:
            if section in self.config:
                return self.config[section][key]
            else:
                return None
        else:
            return self.config.get(key)
