import random    #we have used this to generate random words 
from words import words  #with the help of this we can generate one random word that we have to guess in the game 
import string

def get_valid_word(words):    # there are some places where there is '' and  - is present in the word so we have select words without them so first we will rectify this 
  word = random.choice(words) # this will choose one random word from words file 
  while '_' in word or ' ' in word:   # we use this while loop because when we choose word randomly and some of them contain _ or ' ' in it
    word = random.choice(words)   # but we don't want those words so what we do is we choose word before and if that contain any one of them it will again choose the random word.
  return word.upper()

def hangman():

  word = get_valid_word(words)  # here using get valid word function we are storing the value in word data type for playing the game
  word_letter = set(words)  #Set is a datatype in Python that contains unordered but unique values. The values in sets can only be non-mutable, i.e, numbers, strings and tuples.  #letters in the word  

  alphabet = set(string.ascii_uppercase) # here we are importing string file whhich is already define din the python and we will use this to get all the letter or alphabets in uppercase to guess

  used_letter = set() # we will store the letter in it which is already entered/guessed by the user

  lives = 12

  #getting user input
  while len(word_letter) > 0 and lives > 0:

    #letter used 
    # ' '.join(['a','b','cd']) ---> 'a b cd'
    print('you have', lives ,' lives left , You have already used this letter:', ' '.join(used_letter)) # here we will show the how much lives left for the user to guess right word and the letter we have already used it will show the letters

    # what is the correct word i.e W _ O _ R D

    word_list = [letter if letter in used_letter else '_' for letter in word] # here we will create one list where we check weather the letter entered present in the used letter if it is present then we will show letter otherwise we will show _ or dash you can say
    print('Current Word: ', ' '.join(word_list))

    user_letter = input("Guess a letter : ").upper()  # we will get user input that is one letter guessed by the user


    if user_letter in alphabet - used_letter:  #in this step we are checking weather the letter guessed by the user is present in alphabet or a valid and we haven't used this then we will add user letter in used letter

      used_letter.add(user_letter)   # here we are adding the user letter in the used letter set method

      if user_letter in  word_letter:  #then we check if the letter guessed by the user are present in the word letter

        word_letter.remove(user_letter) # then we will remove the user letter from the word letter 
      else:
        lives = lives -1 # take away one life if you guess wrong
        print("This letter is not present in word   ")

    elif user_letter in used_letter: #if user guessed the letter that is already used then it will print this  otherwise it will show invalid character

      print("You have already gussed this charchter, Please choose different charachter")

    else:

      print("Invalid character")
    
# gets here when the len of word becomes == 0 and lives == 0

  if lives == 0:  #this will work when the lives become zero it will show the and and you died message 
    print('sorry, you died !!', 'the word is', word, '!!')
  else:  # this means your life is not zero and you have guessed the word correctly
    print('yeaah !! you have guessed the word', word , '!!')

hangman()
