monthConversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December"
}
# print(monthConversions.get("Noo", "Not a valid key"))

# i=1
# while i<=10:
#     print(i)
#     i+=1

# a=5
# b=9
# print(a,b)
# a=a+b
# b=a-b
# a=a-b
# print(a,b)
print("")
print("Welcome to the word guessing game")
print("You have 5 chances to guess the word correctly, you lose the game if you are out of chances!")
print("You will also get 5 hints, one of which will appear after every wrong guess")
print("Guess the word in minimum guesses, good luck!")
print("")

theword="microsoft"
guess=""
guesscount = 0
while guess.lower()!=theword and guesscount<5:
    if guesscount == 0:
        print("Hint 1: It is one of the largest companies in the world")
    elif guesscount == 1:
        print("Hint 2 : It is a company which works on Computer technologies")
    elif guesscount == 2:
        print("Hint 3 : This company has developed some of the most popular software products ever (You might be using one right now!)")
    elif guesscount == 3:
        print("Hint 4 : This company is headquartered in Redmond, Washington in the United States")
    else:
        print("Last Hint : The founder of this company was the wealthiest person in the world for a long time")
    guesscount += 1
    guess = input("Enter your guess:")


if guesscount==5 and guess.lower()!=theword:
    print("")
    print("You are out  of guessses :( "
          "Try again")
else:
    if (guesscount>1 and guesscount!=5):
            print("Congratulations, you guessed the word correctly in just",guesscount,"guesses!")
    elif (guesscount == 5):
        print("Congratulations, you guessed the word correctly in", guesscount, "guesses!")
    else:
        print("Congratulations, you guessed the word correctly in just", guesscount, "guess!")