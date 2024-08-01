import random
import unittest
from durakgame import *

class MoveGenerationTest(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        pass

class MoveProcessingTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def test1(self):
        pass

if __name__ == "__main__":
    unittest.main()

class MrLogger(Player):
    def nextMove(self, state: GameState, options: list[Move]) -> int:
        print(f"[{id(self)}]Choosing move for:\n{state}\nand for: {options}\n")
        return 0
    
six = CardValue.Six
seven = CardValue.Seven
eight = CardValue.Eight
nine = CardValue.Nine
ten = CardValue.Ten
jack = CardValue.Jack
queen = CardValue.Queen
king = CardValue.King
ace = CardValue.Ace

heart = Suit.Heart
spade = Suit.Spade
cross = Suit.Cross
diamond = Suit.Diamond

def visualTest():
    deck = intersuitDeck()
    p1 = MrLogger()
    p2 = MrLogger()
    g = Game(deck, p1, p2)

    assert g.trump == Card(nine, heart)

    p1Hand = [
        Card(six, heart), Card(six, spade), 
        Card(seven, heart), Card(seven, spade),
        Card(eight, heart), Card(eight, spade)
    ]
    p2Hand = [
        Card(six, cross), Card(six, diamond), 
        Card(seven, cross), Card(seven, diamond), 
        Card(eight, cross), Card(eight, diamond)
    ]
    assert p1.hand == p1Hand
    assert p2.hand == p2Hand

    assert g.turn == g.move == Switch.First

    print(g.kickoff())
    

def test1():
    deck = standardDeck()
    print(deck)
    # shuffle(deck)
    # p1 = TestPlayer()
    # p2 = TestPlayer()
    # g = Game(deck, p1, p2)
