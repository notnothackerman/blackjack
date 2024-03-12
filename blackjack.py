Python 3.9.1 (v3.9.1:1e5d33e9b9, Dec  7 2020, 12:10:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # # ############### Blackjack Project #####################

# # #Difficulty Normal 😎: Use all Hints below to complete the project.
# # #Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# # #Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# # #Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# # ############### Our Blackjack House Rules #####################

# # ## The deck is unlimited in size. 
# # ## There are no jokers. 
# # ## The Jack/Queen/King all count as 10.
# # ## The the Ace can count as 11 or 1.
# # ## Use the following list as the deck of cards:
# # ## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# # ## The cards in the list have equal probability of being drawn.
# # ## Cards are not removed from the deck as they are drawn.
# # ## The computer is the dealer.
# # # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import random

# # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# cards = [2, 3, 4, 5, 6, 7, 8, 9]

# # # your_cards = random.sample(cards, 2)	
# # # dealers_cards = random.sample(cards, 2)	
# your_cards = [11,11]
# dealers_cards = [5,5]



# print(your_cards)
# print(dealers_cards)

# current_score = sum(your_cards)
# dealers_score = sum(dealers_cards)

# you_lose = False


# def play_blackjack():
#   # your_cards = [11,11]
#   # dealers_cards = [5,5]
#   you_lose = False
  
#   global current_score
#   if 11 in your_cards and current_score > 21:
#     your_cards[your_cards.index(11)] = 1
#     current_score = sum(your_cards)
#     print("Ace downgraded to 1!")
    
#   print(f"Your Cards: {your_cards}, current score: {current_score}")
#   print(f"Dealer's first card: {dealers_cards[0]}")

#   hit_or_pass = input("Type 'hit' to get another card, type 'n' to pass: ")
#   if hit_or_pass == "hit":
#     hit()
#   else:
#     pass_()
#   current_score = sum(your_cards)
#   dealers_score = sum(dealers_cards)
#   while you_lose == False:
#     if current_score > 21:
#       print(f"Your Cards: {your_cards}, current score: {current_score}")
#       print("Bust, you lose!")
#       play_again()
#     if current_score == 21:
#       if dealers_score == 21:
#         print("you lose")
#         play_again()
#     if dealers_score == current_score:
#       print("Draw!")
#       play_again()
#     elif 22 > dealers_score > current_score:
#       print("Dealer Wins!")
#       play_again()
#     else:
#       print("You Win!")
#       play_again()
      
# def play_again():
#     retry = input("would you like to play again? 'y' or 'n'?: ")
#     if retry == "y":
#         you_lose == True
#         play_blackjack()



# def hit():
#   your_cards.append(random.choice(cards))
#   hit_current_score = sum(your_cards)  
#   print(f"Your Cards: {your_cards}, current score: {hit_current_score}")
#   print(f"Dealer's first card: {dealers_cards[0]}")
#   hit_or_pass = input("Type 'hit' to get another card, type 'n' to pass: ")
#   if hit_or_pass == "hit":
#     hit()
#   else:
#     pass_()
#   return



# def pass_():
#   global current_score
#   global dealers_score
#   while dealers_score < current_score:
#     dealers_cards.append(random.choice(cards))
#     dealers_score = sum(dealers_cards)
#   print(f"Your Final Hand: {your_cards}, Your Final Score: {current_score}")
#   print(f"Dealer's final hand: {dealers_cards}, Dealer's Final Score: {dealers_score}")
  



# greeting = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
# if greeting == "y":
#   play_blackjack()

#################################################
# ############### Blackjack Project #####################

# #Difficulty Normal 😎: Use all Hints below to complete the project.
# #Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# #Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# #Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# ############### Our Blackjack House Rules #####################

# ## The deck is unlimited in size. 
# ## There are no jokers. 
# ## The Jack/Queen/King all count as 10.
# ## The the Ace can count as 11 or 1.
# ## Use the following list as the deck of cards:
# ## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# ## The cards in the list have equal probability of being drawn.
# ## Cards are not removed from the deck as they are drawn.
# ## The computer is the dealer.
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random
from clear import clear
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = [2, 3, 4, 5, 6, 7, 8, 9]
your_cards = []
dealers_cards = []
def calculate_my_score():
  return sum(your_cards)


def calculate_dealers_score():
  return sum(dealers_cards)


def hit():
  your_cards.append(random.choice(cards))
 
  return

def pass_():
  dealers_score = calculate_dealers_score()
  current_score = calculate_my_score()
  while dealers_score < current_score:
    dealers_cards.append(random.choice(cards))
    dealers_score = calculate_dealers_score()
 
    return

def play_again():
  retry = input("would you like to play again? 'y' or 'n'?: ")
  if retry == "y":
      global you_lose
      you_lose = True
      your_cards.clear()
      dealers_cards.clear()
      clear()
      game()

def game():
    your_cards = random.sample(cards, 2)	
    dealers_cards = random.sample(cards, 2)
    dealers_score = calculate_dealers_score()
    current_score = calculate_my_score()
    
    print(your_cards)
    print(dealers_cards)
    
    
    you_lose = False
    while you_lose == False:
          current_score = calculate_my_score()
          dealers_score = calculate_dealers_score()
          if 11 in your_cards and current_score > 21:
            your_cards[your_cards.index(11)] = 1
            current_score = sum(your_cards)
            print("Ace downgraded to 1!")
          if current_score == 21:
            print("You have Black Jack! You Win!")
            play_again()
          if dealers_score == 21:
            print("Dealer has Black Jack! You Lose!")
            play_again()
          while current_score < 22:
              print(f"Your Cards: {your_cards}, current score: {current_score}")
              print(f"Dealer's first card: {dealers_cards[0]}")
              hit_or_pass = input("Type 'hit' to get another card, type 'n' to pass: ")
              while hit_or_pass == "hit":
                hit()
                current_score = calculate_my_score()
                dealers_score = calculate_dealers_score()
                print(f"Your Cards: {your_cards}, current score: {current_score}")
                print(f"Dealer's first card: {dealers_cards[0]}")
                if current_score > 21:
                    break
                hit_or_pass = input("Type 'hit' to get another card, type 'n' to pass: ")
              dealers_score = calculate_dealers_score()  
              pass_()
              dealers_score = calculate_dealers_score() 
              print(f"Your Final Hand: {your_cards}, Your Final Score: {current_score}")
              print(f"Dealer's final hand: {dealers_cards}, Dealer's Final Score: {dealers_score}")
              if current_score > 21:
                print("Bust, you lose!")
                play_again()
              if current_score == 21:
                if dealers_score == 21:
                  print("you lose")
                  play_again()
              if dealers_score == current_score:
                print("Draw!")
                play_again()
              elif 22 > dealers_score > current_score:
                print("Dealer Wins!")
                play_again()
              else:
                print("You Win!")
                play_again()
  
    

greeting = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
if greeting == "y": 
  game()







SyntaxError: multiple statements found while compiling a single statement
>>> 