import random

class BlackjackGame:
    def __init__(self):
        self.deck = self.create_deck()
        self.shuffle_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
        return deck * 4  # Using 4 standard decks

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_card(self, hand):
        card = self.deck.pop()
        hand.append(card)

    def calculate_hand_value(self, hand):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        total_value = sum(values[card['rank']] for card in hand)
        num_aces = sum(1 for card in hand if card['rank'] == 'A')

        while total_value > 21 and num_aces:
            total_value -= 10
            num_aces -= 1

        return total_value

    def hit(self, hand):
        self.deal_card(hand)

    def print_hands(self, hide_dealer_card=False):
        print("\nYour hand:")
        for card in self.player_hand:
            print(f"{card['rank']} of {card['suit']}")
        print(f"Total value: {self.calculate_hand_value(self.player_hand)}")

        print("\nDealer's hand:")
        if hide_dealer_card:
            print("Hidden Card")
            print(f"{self.dealer_hand[1]['rank']} of {self.dealer_hand[1]['suit']}")
        else:
            for card in self.dealer_hand:
                print(f"{card['rank']} of {card['suit']}")
            print(f"Total value: {self.calculate_hand_value(self.dealer_hand)}")

    def play_round(self):
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]

        # Player's turn
        while True:
            self.print_hands(hide_dealer_card=True)
            move = input("Do you want to (H)it or (S)tand? ").upper()

            if move == 'H':
                self.hit(self.player_hand)
                if self.calculate_hand_value(self.player_hand) > 21:
                    print("Bust! You lose.")
                    return
            elif move == 'S':
                break

        # Dealer's turn
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.hit(self.dealer_hand)

        # Determine the winner
        self.print_hands()
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        if dealer_value > 21 or (player_value <= 21 and player_value > dealer_value):
            print("You win!")
        elif player_value == dealer_value:
            print("It's a tie!")
        else:
            print("Dealer wins.")

# Main game loop
def main():
    game = BlackjackGame()

    while True:
        game.play_round()
        play_again = input("Do you want to play again? (Y/N) ").upper()
        if play_again != 'Y':
            break

if __name__ == "__main__":
    main()
