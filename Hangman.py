import random
word_list = ["echt", "palmy","coax"]
chosen_word = random.choice(word_list)

End_of_game = False

while not End_of_game:
    guess = input("Guess a letter: ").lower()

    display = []
    word_length = len(word_list)
    #for letter in word_list:
    for _ in range(word_length):
        display += "_"
        print(display)

    #for letter in chosen_word:
    for position in range(word_length):
        letter = chosen_word[position]
    if letter == guess:
        #print("Right")
        display[position]= letter
    #else:
    #print("Wrong")    
    if "_" not in display:
        End_of_game = True
        print("You Win.")