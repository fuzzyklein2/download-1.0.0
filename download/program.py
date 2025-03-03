from .startup import *

class Program():
    """ Abstract class that processes command line arguments as files. """

    def __init__(self, *args, **kwargs):
        """ Initialize the application.

            :settings: `dict` containing configuration variables, environment
                       variables, and command line arguments.
        """
        log.info(f"Initializing {self.__class__.__name__} class...")
        