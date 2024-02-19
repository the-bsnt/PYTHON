# Guessing Game :There is valid number and you have to guess that number in 3 try


def game():  # defining game as function
    vaild_number = 7
    print("Guess the number from 1 to 9 to win. You have only three chances")

    for i in range(0, 3):
        n = int(input("Guess : "))
        if n == vaild_number:
            print(" You Won ! ")
            exit(0)
    print("Sorry, You Loose!")
    ask = input("Do you want to try again. y-yes / n-no ")
    if ask == "y":
        game()
    else:
        exit(0)


game()

# NOTE : You dont need to define main function in python
# def main():    #defining main function
#     print("Guess the number from 1 to 9 to win. You have only three chances")
#     game()


# main() #calling main function
