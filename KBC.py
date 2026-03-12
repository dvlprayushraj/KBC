a = str(input("Enter your name: "))
print("Welcome to KBC . " + a)

print()

print("Here are the rules of the game: ")

print()
print("1. You will be asked 5 questions.")
print("2. Each question will have 4 options, only one of which is correct.")
print("3. You can use 3 lifelines: 50-50, Audience Poll")

print()
print("TOUR BANK ACCOUNT HAS 0rs TO START WITH. ")
print("FOR EACH CORRECT ANSWER YOU WILL GET 1000rs. ")

print()
print("Let's start the game! ")

print("Question 1: What is the capital of France?")
print("A. Berlin")
print("B. Madrid")
print("C. Paris")
print("D. Rome")

answer1 = input("Enter your answer (A/B/C/D): ")
if answer1.upper() == "C":
    print("Correct! You have won 1000rs.")
else:
    print("Wrong answer. The correct answer is C. Paris.")

print()
print()


print("Question 2: Who is the CEO of Tesla?")
print("A. Jeff Bezos")
print("B. Elon Musk")
print("C. Bill Gates")
print("D. Mark Zuckerberg")

answer2 = input("Enter your answer (A/B/C/D): ")
if answer2.upper() == "B":
    print("Correct! You have won 1000rs.")
else:
    print("Wrong answer. The correct answer is B. Elon Musk.")


print()


amount = 2000
print("Your current bank account balance is: " + str(amount) + "rs.")



print()


print("Question 3: What is the largest planet in our solar system?")
print("A. Earth")
print("B. Jupiter")
print("C. Saturn")
print("D. Mars")

answer3 = input("Enter your answer (A/B/C/D): ")
if answer3.upper() == "B":
    print("Correct! You have won 1000rs.")
else:
    print("Wrong answer. The correct answer is B. Jupiter.")


amount += 1000
print("Your current bank account balance is: " + str(amount) + "rs.")

print()
print("Question 4: Who wrote the play 'Romeo and Juliet'?")
print("A. William Shakespeare")
print("B. Charles Dickens")
print("C. Jane Austen")
print("D. Mark Twain")

answer4 = input("Enter your answer (A/B/C/D): ")
if answer4.upper() == "A":
    print("Correct! You have won 1000rs.")
else:
    print("Wrong answer. The correct answer is A. William Shakespeare.")

amount += 1000
print("Your current bank account balance is: " + str(amount) + "rs.")


if amount >= 4000:
    print()
    print("Congratulations!" + a + " You have won the game with a total of " + str(amount) + "rs.")
else:    print()
print("Game over. You have won a total of " + str(amount) + "rs. Better luck next time!")






