from random import choice


class Hand:
    def __init__(self):
        self.cards = []
        self.deck = []
        self.card_count = len(self.cards)
        self.hand_sum = 0
        self.cards_string = str(self.cards).replace("[", "").replace("]", "")


    def generate_deck(self):
        # generate 1-15 cards four times
        # change values 11 - 14 to 10 (10 - 14 are jacks, queens, kings)
        # change value 15 to aces (15 to 11)
        for i in range(0, 4):
            for j in range(1, 15):
                if 10 < j < 14:
                    self.deck.append(10)
                elif j == 14:
                    self.deck.append(11)
                else:
                    self.deck.append(j)

    def calculate_hand_sum(self):
        running = 0
        for card in self.cards:
            running += card
        self.hand_sum = running

    def deal_card(self, first=False):

        # add new card to hand
        self.cards.append(choice(self.deck))

        # loop through cards and replace aces with 1's if necessary
        for i in range(len(self.cards)):
            self.calculate_hand_sum()
            if self.hand_sum > 21:
                if self.cards[i] == 11:
                    self.cards[i] = 1
                    if not first:
                        print("Changing ace...")

        # update string of cards
        self.cards_string = str(self.cards).replace("[", "").replace("]", "")


    def start_hand(self, hand, first=False):

        # regen deck

        self.deck = []
        self.generate_deck()

        # reset cards
        self.cards = []

        # deal two cards
        self.deal_card(first)
        self.deal_card(first)

        # print the hand
        self.print_hand(hand, first)

    def print_hand(self, hand, first=False):
        match hand:
            case "Your":
                print(f"{hand} Hand: \n{self.cards_string}, Sum: {self.hand_sum}\n")
            case "House":
                if first:
                    print(f"{hand}'s Hand: \t(Stands on 17) \n{self.cards[0]}, x, Sum: {self.hand_sum - self.cards[1]}")
                else:
                    print(f"{hand}'s Hand: {self.cards_string}, Sum: {self.hand_sum}")


