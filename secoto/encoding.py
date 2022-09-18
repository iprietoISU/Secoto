#This "encryption" system was something I made overnight in high school
#It injects artifical crypto-secure entropy into its outputs.
import random
import numpy as np
import secrets

class tumultCypherInstance():

    _ALPHLABET = [1]

    def __init__(self, seed):
        self.seed = seed
        self.encMatrix = []
    
    def _generateMatrix(self):
        symbols = list(range(16))*16
        random.seed(self.seed)
        random.shuffle(symbols)
        self.encMatrix = (np.array(symbols).reshape((16,16))).copy()

    def _chooseRandCoords(self, value):
        possibleCoords = np.array(np.where(self.encMatrix == value))
        randIndex = secrets.randbelow(0,16)
        return (possibleCoords[0][randIndex], possibleCoords[1][randIndex])

    def encode(self, val):
        print("") #TODO

    def decode(self, val):
        print("") #TODO