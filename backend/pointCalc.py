class PointCalculator(object):
#A class to calculate the points a player deserves for their selected cards for a round
#This is done before comparison with other players as most cards don't care about what other players have
#Cards that care about other players are check in endOfRound.py

    def __init__(self, selectedCards):
        self._cards = selectedCards
        self._makiIcons = 0
        self._sashimiAmount = 0
        self._puddingAmount = 0
        self._tempuraAmount = 0
        self._wasabiPlaced = False
        self._dumplingAmount = 0
        self._points = 0
        self._dumplingScores = [0, 1, 3, 6, 10, 15]
        self.checkCards()
        self.calculatePoints()

    def checkCards(self):
        for i in range(8):
            card = self._cards.draw()

            print(card)

            if card.getCardType() == "Sashimi":
                self._sashimiAmount += 1

            elif card.getCardType() == "Pudding":
                self._puddingAmount += 1

            elif card.getCardType() == "Tempura":
                self._tempuraAmount += 1

            elif card.getCardType() == "Wasabi":
                self._wasabiPlaced = True

            elif card.getCardType() == "Dumpling":
                self._dumplingAmount += 1

            elif card.getCardType() == "Maki Roll 1":
                self._makiIcons += 1

            elif card.getCardType() == "Maki Roll 2":
                self._makiIcons += 2

            elif card.getCardType() == "Maki Roll 3":
                self._makiIcons += 3

            elif card.getCardType() == "Nigiri 1":

                if self._wasabiPlaced:
                    self._points += 3
                    self._wasabiPlaced = False
                else:
                    self._points += 1

            elif card.getCardType() == "Nigiri 2":

                if self._wasabiPlaced:
                    self._points += 6
                    self._wasabiPlaced = False
                else:
                    self._points += 2

            elif card.getCardType() == "Nigiri 3":

                if self._wasabiPlaced:
                    self._points += 9
                    self._wasabiPlaced = False
                else:
                    self._points += 3

    def calculatePoints(self):

        self._points += ((self._sashimiAmount//3)*10)

        self._points += ((self._tempuraAmount//2)*5)

        if self._dumplingAmount > 5:
            self._points += 15
        else:
            self._points += self._dumplingScores[self._dumplingAmount]

    def returnScores(self):

        return [self._points, self._makiIcons, self._puddingAmount]


def main():
    from PremadeSelectedCards import *
    from SelectedCards import *
    cards = PremadeSelectedCards()
    scores = PointCalculator(cards)
    print(scores.returnScores())
