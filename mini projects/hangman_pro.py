import random

file_path = r"mini projects\words.txt"
with open(file_path, 'r') as file:
    lines = file.readlines()[1:]

word_list = []
for line in lines:
    word_list.extend(line.strip().split(","))


#dictionary key:()
hangman_art = {0:("  ",
                  "  ",
                  "  "),
               1:(" o ",
                  "  ",
                  "  "),
               2:(" o ",
                  " | ",
                  "  "),
               3:(" o ",
                  "/| ",
                  "  "),
               4:(" o ",
                  "/|\\",
                  "  "),
               5:(" o ",
                  "/|\\",
                  "/  "),
               6:(" o ",
                  "/|\\",
                  "/ \\")}



def display_man(wrong_guesses):
    print("**********************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(word_list)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letter = set()
    is_running = True


    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Guess the word: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("invalid.")
            continue

        if guess in guessed_letter:
            print(f"{guess} is already guessed.")
            continue


        guessed_letter.add(guess)



        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1



        if wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Lose!")
            is_running = False


        if not "_" in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Congratulations. You win!")
            is_running = False




if __name__=='__main__':
    main()