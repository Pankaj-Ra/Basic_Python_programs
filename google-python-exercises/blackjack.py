#!/usr/local/bin/python -tt

import sys
import os
import random

from copy import deepcopy

class Blackjack():

    def __init__(self,coins):
        self.player_coins = coins
        self.player = 'challenger'
        self.player_cards = 0
        self.dealer_cards = 0
        self.cards = []
        self.hands = []

    def new_deck(self,):
        self.player = 'challenger'
        self.player_cards = 0
        self.dealer_cards = 0
        cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        hands = [4]*13
        self.cards = deepcopy(cards)
        self.hands = deepcopy(hands)

    def players_input(self, player):
        while True:
            try:
                coins = int(input('Player please place your bet:\n'))
            except TypeError:
                print('Please enter only realnumbers\n')
                continue
            else:
                if coins > self.player_coins:
                    print(f'You are low on funds !!! Bet below: {self.player_coins}')
                    continue
                self.player_coins -= coins
                break

    def shuffle_cards(self):
        while True:
            num = random.randint(0,12)
            if self.hands[num] == 0:
                continue
            else:
                self.hands[num] -= 1
                switcher={
                    1:11,
                    11:10,
                    12:10,
                    13:10
                }
                print(f'card : {self.cards[num]}')
                return switcher.get(self.cards[num], self.cards[num])

    def first_deal(self):
        print(f'Dealer\'s cards:\n')
        card1 = self.shuffle_cards()
        card2 = self.shuffle_cards()
        if card1 == card2 == 11:
            card2 = 1
        self.dealer_cards = card1 + card2
        print(f'Dealer\'s Cards show: {self.dealer_cards}\n')
        print(f'Players\'s cards:\n')
        card1 = self.shuffle_cards()
        card2 = self.shuffle_cards()
        if card1 == card2 == 11:
            card2 = 1
        self.player_cards = card1 + card2
        print(f'Player\'s Cards show: {self.player_cards}\n')

    def deal_cards(self, player):
        if not self.dealer_cards:
            self.first_deal()
            return
        card = self.shuffle_cards()
        if player == 'challenger':
            print(f'Players\'s card:\n')
            if card == 11 and self.player_cards > 10:
                card = 1
            self.player_cards += card
            print(f'Player\'s Cards show: {self.player_cards}\n')
        else:
            print(f'Dealer\'s card:\n')
            if card == 11 and self.dealer_cards > 10:
                card = 1
            self.dealer_cards += card
            print(f'Dealer\'s Cards show: {self.dealer_cards}\n')

    def bust(self, player):
        if player == 'challenger' and self.player_cards > 21:
            print('Player Busted!!! and Dealer Won the Game !!!\n')
            return True
        elif player == 'dealer' and self.dealer_cards > 21:
            print('Dealer Busted!!! and Player Won the Game !!!\n')
            return True
        return False

    def winnner(self, player):
        if player == 'challenger' and self.player_cards == 21:
            print('BlackJack:\nPlayer Won the Game !!!\n')
            return True
        elif player == 'dealer' and self.dealer_cards == 21:
            print('BlackJack:\nDealer Won the Game !!!\n')
            return True
        return False


    def bet(self, player, amount):
        pass

    def replay(self):
        play = input('Try Your Luck Again ? Enter "yes" or "no"\n')
        if play == 'yes':
            self.new_deck()
            return True
        return False


def main():
    coins = int(input('Player enter the no of chips you want to buy:\n'))
    bjack = Blackjack(coins)
    bjack.new_deck()
    bjack.players_input(bjack.player)
    while True:
        bjack.deal_cards(bjack.player)
        if bjack.winnner(bjack.player) or bjack.bust(bjack.player):
            if bjack.replay():
                continue
            break
        while True:
            next_deal = input(f'{bjack.player} Choose your next move:\n Enter "hit" for deal or "stand" for hold\n')
            if next_deal == 'hit':
                break
            elif next_deal == 'stand':
                if bjack.player == 'challenger':
                     bjack.player = 'dealer'
                else:
                    bjack.player = 'challenger'
                continue
            else:
                print('Please enter a valid input!:\n')



if __name__ == '__main__':
    main()
