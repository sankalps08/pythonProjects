import random 
#this import file we are using to choose something randaomly from the deck

class Card:  #this is  the card class in this we will define suit of the card and rank of the card and print the way we want to see card in hand 
  # this is a constructor function or method in which we have defined the suit of the cared and the rank using self
    def __init__(self, suit, rank) :
      self.suit = suit
      self.rank = rank 
      
      
    def __str__(self) -> str: #this is a string function or method in which we will right the statement we want to see when we choose card from the deck
      return f"{self.rank['rank']} of {self.suit}"
     # we have used f string to combine and putting value of suit and rank in the statement


#this is the Deck class in this we will d efine the deck and put that deck in a empty list and the choose 2 cards randomoly from the deck after shuffling the deck using shuffle fucntion    
class Deck:
  def __init__(self): 
      # we will create constructor function and put everything about suit card rank in this function
      self.cards = [] # empty card list
      suits = ['spades' , 'club', 'dimond' , 'hearts']  # all four suits use in cards and in the next step we will define ranks using dictonary
      # A can be 11 or 1 but here we will assign A = 11 and all high cards will be 10 only
      ranks = [ 
              {"rank": "A", "value": 11},
              {"rank": "2", "value": 2},
              {"rank": "3", "value": 3},
              {"rank": "4", "value": 4},
              {"rank": "5", "value": 5},
              {"rank": "6", "value": 6},
              {"rank": "7", "value": 7},
              {"rank": "8", "value": 8},
              {"rank": "9", "value": 9},
              {"rank": "10", "value": 10},
              {"rank": "J", "value": 10},
              {"rank": "Q", "value": 10},
              {"rank": "K", "value": 10},
              ]
              # in the we will use for loop and append every possible suit and rank value in self.cards and make it a list of deck
      for suit in suits:
        for rank in ranks:
          self.cards.append(Card(suit, rank))
  # now we will create one function that will shuffle the deck randomly using random function and this will shuffule only when the len of the deck will be greater than 1.
  def shuffle(self):
      if len(self.cards) > 1:
        random.shuffle(self.cards)
  # next we gonna use the deal method or function in deck class after creating deck and shuffuling the deck we have to deal cards to the player and the dealer
  def deal(self,n):
        cards_dealt = []  #we will create one empty list cards_dealt
        for i in range(n): # now we will use for loop and pick n numbers of cards from the deck if only if the lenghth of cards greater than zero
          if len(self.cards) > 0:
            card  = self.cards.pop() # we will use pop() function to take out card from the shuffled deck that is self.cards, it will pop-out cards according the value of n, whatever we put in deal () function will pop-out.
            cards_dealt.append(card)
        return cards_dealt # then we will return the pop-out value which we have stored in cards_dealt empty list

# this is the hand class we will use this class to store hands for dealer and player, ex. in black jack we deal 2 cards to each player.
class Hand:
  # this constructor method will have one value dealer which we will set as false as default 
  def __init__(self, dealer = False):
    self.cards = [] #we will create one empty list of self.cards and assign value as zero for because we have to calculate
    self.value = 0
    self.dealer = dealer # we are assigning dealer using self parameter of constructor, now we will create one method to add card in the cards and we will pass card_list as a parameter and then use extend method to put those or extend the self.card lsit by passing card_list

  def add_card(self, card_list):
    self.cards.extend(card_list)

  # here we will calculate the value for cards that is present in hand because we should know the value before hit or stand because if our value cross 21 we loose 
  def calculate_value(self):
    self.value = 0 # we will use this from hand class contructor
    has_ace = False # we will put this as false in the start , as you know in this game ace can have 2 values 11 or 1 we have assigned 11 in the start now we will use if to solve that problem , we will clear here that when we want to use 11 and we want to use 1.
    # this for loop will calculate the card values it will go in self.cards 1 by one and add the values according to the rank of the card.
    for card in self.cards:
      card_value = int(card.rank["value"])
      self.value += card_value
      # here we will check weather the cards having ace or not by using if 
      if card.rank["value"] == 'A':
        has_ace = True
  # we come out of the loop and check if has_ace and self.value that is value of cards is greater than 21 or not if it will be greater it will subtract 10 from ace value and ace will become 1 and if it is not exceeding 21 value will remain 11 only.
    if has_ace and self.value > 21:
      self.value -= 10
    
  # the will get the value after calculating value from the calculate value function
  def  get_value(self):
    self.calculate_value()
    return self.value  # we will return total values here after calculating

  #this fucntion will call only when the value of get value fucntion equals to 21
  def is_blackjack(self):
    return self.get_value() == 21
  # now we will use display method to display hand on output screen
  # In display we will see the hand of the player and the dealer but dealer hand will show only one value because we cannot show dealer both values so we will print hidden for one value and print the other one.
  # it will print dealer's hand if self.dealer is true else it will print player both hands and value 
  def display(self, show_all_dealer_card = False):
    print(f''' {"dealer's" if self.dealer else "your'"}hand :''')
    #her ewe will use for loop and use enumerate function it will provide  the index of the value. like 0 -- 1,1 --2, first one is index and second one is value we pass 2 values index and card and enumerate through cards
    for index, card in enumerate(self.cards):
      #we will check if index is zero,self.dealer that mean it is dealer hand,and show all dealer card as false and is balckjack is false it will print hidden only else both dealer and player cards will print with value 
      if index == 0 and self.dealer and not show_all_dealer_card and not self.is_blackjack():
        print('hidden')
      else:
         print(card)
    # it will print the total value of player cards if its player hand not dealer's
    if not self.dealer:
      print("value" , self.get_value())
      print()

# this is the main function in which we will design the game that we will see on the screen while playing the game we will define one method in this class as play and in that we will define two variables game number and games user want to play and assign as zero in the start 
class Game:
  def play(self):
    game_num = 0
    games_to_play  = 0
    # we will only continue only if the user put number that means if user will put alphabet it will get error but here we have use try and except to print out something if it catch error in out case it is in except block it will come out of loop when game of play become equal to zero
    while games_to_play <= 0:
      try:
        games_to_play = int(input("How many games do you want to play : "))
      except:
        print("You need to enter number")
    # here we have used while loop , when game of number is less then the  game user want to play we will continue this loop and increase game num value by 1.
    while game_num < games_to_play:
      game_num+= 1
      deck = Deck() #  here we are calling deck class and in the next line we are shuffling the deck using shuffle method
      deck.shuffle()

      player_hand = Hand() # here we are calling the hand class for player and in the next line we are calling the hand class for dealer and it will happen when dealer  become equal to true and we have mentioned here that dealer is true
      dealer_hand = Hand(dealer=True)

      # here we will use for loop for and it will loop 2 times or whatever the value yyou pass in range and each iteration giving card to player hand and dealer handthat is dealt from the deck.  
      for i in range(2):
        player_hand.add_card(deck.deal(1))
        dealer_hand.add_card(deck.deal(1))

      print() # printing empty line 
      print("*" * 30)  # this line will print * 30 times in a row something like ********** this
      print(f"Game {game_num} of {games_to_play} " ) # we will print game number of game to play here and in the next line we will do the same step we did in the above step
      print("*" * 30)
      player_hand.display() # we will use display method and print player and dealer hand 
      dealer_hand.display()

      if self.check_winner(player_hand , dealer_hand): # we will check for winner after printing player and dealer cards.if it will not found any mention scenerio in check_winner function it will continue.
          continue
      choice = '' # we will create one variable called choice and pass empty string
      # we will use while loop and check it player hand value is less than 21  or not then we will check weather the choice is not in s or stand then we will ask to hit or stand 
      while player_hand.get_value() < 21 and choice not in ['s','stand']:
          choice = input("Please choose 'Hit' or 'Stand': ").lower()
          print()
          # we again use while loop and check weathe the choices are in stand or hit if its not ask again and lower() is used to covert everything in lower case 
          while choice not in ['s','stand', 'h' , 'Hit']:
            choice = input("Please choose 'Hit' or 'Stand' or (H/S): ").lower()
            print()
          # if the user choose hit or h player hand deal 1 card from the deck and display the new card  
          if choice in ['h', 'Hit']:
            player_hand.add_card(deck.deal(1))
            player_hand.display()
      # now I will check winner function if we found our winner or not and if conditions not matched continue
      if self.check_winner(player_hand , dealer_hand):
          continue

      
      # player hand value will be stored in player hand value
      player_hand_value = player_hand.get_value()
      dealer_hand_value = dealer_hand.get_value()

      # now we will check if the dealer hand value is less than 17 or not if it is then will add one card in dealer hand  and save that value in dealer hand value variable
      while dealer_hand_value < 17 :
          dealer_hand.add_card(deck.deal(1))
          dealer_hand_value = dealer_hand.get_value()

      dealer_hand.display(show_all_dealer_card=True) #we will display dealr hand and then we again check if we get the winner or not by placing check winner function and passing player hand value and dealer hand value .

      if self.check_winner(player_hand , dealer_hand):
          continue
      #we will print the final result in the and pring check winner message 
      print("Final results")
      print("Your hand: ", player_hand_value)
      print("dealer hand: ", dealer_hand_value)

      self.check_winner(player_hand, dealer_hand, True)

    print("\nThanks for playing!")

  # here we will create one method called check winner to check winner status so we will pass player hand dealer hand as parameter and game over parameter and put that as false in the start.
  # then  we will check if the game over is false that is not game over we will use if and elif case to check all conditions, what we will print if player hand value exceed 21 , what if dealer hand value exceed what if both will get 21 what is player get 21 and dealer loose and vice-versa.
  def check_winner(self, player_hand , dealer_hand, game_over = False):
    if not game_over:
        if player_hand.get_value() > 21:
          print("You busted. Dealer wins! 😭")
          return True
        elif dealer_hand.get_value() > 21:
          print("Dealer busted. You win! 😀")
          return True
        elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
          print("Both players have blackjack! Tie! 😑")
          return True
        elif player_hand.is_blackjack():
          print("You have blackjack. You win! 😀")
          return True
        elif dealer_hand.is_blackjack():
          print("Dealer has blackjack. Dealer wins! 😭")
          return True
    else: # this means if game over become true we will print these cases.
        if player_hand.get_value() > dealer_hand.get_value():
          print("You win! 😀")
        elif player_hand.get_value() == dealer_hand.get_value():
          print("Tie! 😑")
        else:
          print("Dealer wins. 😭")
          return True
    return False

g = Game()
g.play()
