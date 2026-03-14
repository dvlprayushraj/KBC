import random





#code end

def user_input(user_input):

    user_input = str(input("Enter a letter to guess: "))
    if(user_input == random_letter):
        print("Congratulations! You guessed the correct letter.")

    else:
        print("Sorry, that's not correct. Try again!")


user_input = input("Enter a letter to guess: ")
print("You entered:", user_input)



def generate_random_alphabet(alphabet):
    random_letter = random.choice(alphabet)

    return random_letter

alphabet = 'abcdefghijklmnopqrstuvwxyz'

random_letter = generate_random_alphabet(alphabet)
print("Random letter:", random_letter)
