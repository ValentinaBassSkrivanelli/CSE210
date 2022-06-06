
from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):

    def __init__(self):

        super().__init__()
        #create the self mesaage
        self.message = ""

    def get_mesagge(self): 
        #get the message
        return self.message
        #store received message
    def set_message(self, message):
        self.message = message