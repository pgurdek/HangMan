import datetime
import random
import sys
import time

capitols = []
letters_of_capitol = []
filename = 'stats.txt'
capitol_file_name = 'capitols_database.txt'


def read():
    """Import capitols and countrys database"""
    open_countries = open(capitol_file_name, 'r')
    all_countries = open_countries.readlines()
    for line in all_countries:
        clear = "".join(line.split())
        separate = clear.split('|')
        capitols.append(separate)
    open_countries.close()
    return capitols


def captiol():
    """Random Capitol to destroy"""
    capitol = random.choice(read())
    print('Cheats for gods, Randomed word :', capitol)
    return capitol


def captiol_letters():
    """Change randomed capitol to list + underscore"""
    letters_of_capitol = []
    print('Guess what capitol gona be #$@% up }:-) : ')
    for capitol_letter in random_capitol:
        letters_of_capitol.append([capitol_letter.upper(), '_'])
        print("_", end=" ")
    print('\n')
    return letters_of_capitol


def letter():
    """User try to guess with letter"""
    global lives, letters_of_capitol, used_letters

    user_letter = input('\nEnter letter of capitol:').upper()
    used_letters.append(user_letter)

    for index, good_letter in enumerate(letters_of_capitol):
        # print(good_letter[1])
        if user_letter == good_letter[0]:

            letters_of_capitol[index][1] = letters_of_capitol[index][0]
            print(good_letter[0], end=" ")
        else:
            print(good_letter[1], end=" ")

    if not user_letter in random_capitol:
        lives -= 1
        print('')
        print('Ha! MISS motherfucker ! Remaining lives: ', lives)
        hint()
    print('\n Letter which you used: ', used_letters)
    win()
    return lives


def word():
    """User try to guess word"""
    global lives
    word = input('Guess a word !?').upper()
    if random_capitol == word:
        print('You have won!!!')
        art_win()
        statistic()
        again()
    else:
        lives -= 2
        if lives > 0:
            print()
            print('Ha! MISS motherfucker ! Remaining lives: ', lives)
        hint()
    return lives


def hint():
    """Hint for Noob"""
    global lives, capitol_hint
    if lives < 3 and lives > 0:
        print('Oh no! , you almost LOST!!!')
        print('Let me help you')
        print('The capitol of ....', capitol_hint)


def win():
    """Check if we win Letter mode"""
    underscore = True

    for letter_in_capitol in letters_of_capitol:
        if letter_in_capitol[1] == '_':
            underscore = False

    if underscore:
        print('You have won!!')
        art_win()
        statistic()
        again()


def again():
    """Play again ?"""
    play = input('Do you want play once again : ? y/n')
    if play == 'y':
        main()
    else:
        sys.exit()


def statistic():
    """Write to file stats and display stats and the end"""
    global start_time, name
    end_time = time.time()
    your_time = end_time - start_time
    letter_statistics = len(used_letters)
    best_time = round(your_time, 2)
    now = datetime.datetime.now()
    date = now.strftime('%d, %b %Y')
    name = input('What is your name :')
    summary = name, ' | ', best_time, '| ', letter_statistics, '|', random_capitol, '|', date
    file = open(filename, 'a')
    file.writelines(str(summary) + "\n ")
    file.close()
    print('It took you ', best_time, ' seconds')
    print('You have tried : ', letter_statistics)


def boom():
    explosion = open('boom.txt', 'r')
    boom = explosion.readlines()
    for boom_lines in boom:
        print(str(boom_lines))
    print('You are looser')
    explosion.close()


def art_win():
    superman = open('superman.txt', 'r')
    art = superman.readlines()
    for superhuman in art:
        print(str(superhuman))
    print()
    print('You are our savior !!!!!')
    superman.close()


def main():
    """Main"""
    global random_capitol, capitol_hint, lives, start_time, letters_of_capitol, used_letters
    capitol_data = captiol()
    capitol_hint = capitol_data[0]
    random_capitol = capitol_data[1].upper()  # Random Capitol and asign it
    print(random_capitol)
    letters_of_capitol = captiol_letters()
    lives = 5
    start_time = time.time()
    used_letters = []
    while True:
        if lives <= 0:
            boom()
            again()
            break
        word_or_letter = input('Would you like to guess letter(l) or word(w)?')
        if word_or_letter == 'l':
            lives = letter()
        elif word_or_letter == 'w':
            lives = word()
        elif word_or_letter == 'x':
            boom()
            sys.exit()
        else:
            print('What the heck')


if __name__ == '__main__':
    main()
