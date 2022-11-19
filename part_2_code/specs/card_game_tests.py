import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_ace= Card("Spades", 1)
        self.card_5 = Card("Hearts", 5)
        self.card_10 = Card("Diamonds", 10)
        self.card_game = CardGame()
    
    def test_check_for_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card_ace))

    def test_check_for_ace(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card_5))

    def test_highest_card(self):
        card = self.card_game.highest_card(self.card_5, self.card_10)
        self.assertEqual(self.card_10, card)

    def test_cards_total(self):
        cards_list = [self.card_5, self.card_10, self.card_ace]
        cards = self.card_game.cards_total(cards_list)
        self.assertEqual("You have a total of 16", cards)