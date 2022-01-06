import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_1 = Card("Hearts", 2)
        self.card_2 = Card("Diamonds", 5)
        self.card_ace = Card("Clubs", 1)
        self.card_game = CardGame()

    def test_check_for_ace(self):
        expected = True
        actual = self.card_game.check_for_ace(self.card_ace)
        self.assertEqual(expected, actual)

    def test_highest_card(self):
        expected = self.card_2
        actual = self.card_game.highest_card(self.card_1, self.card_2)
        self.assertEqual(expected, actual)

    def test_cards_total(self):
        all_cards = [self.card_ace, self.card_1, self.card_2]
        expected = "You have a total of 8"
        actual = self.card_game.cards_total(all_cards)
        self.assertEqual(expected, actual)