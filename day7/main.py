import random

words=["giorno", "mista",'diablo','porpo','abakkio',]

word=list(random.choice(words))

q_word=list(len(word)*'_')

life=5

while life!=0:
    print(f"YOUR LIFE: {life}")
    print(q_word)
    guess=input("Guess the letter: ")
    if guess in word:
        num=0
        for letter in word:            
            if letter==guess:
                q_word[num]=guess
            num+=1
        print(f"yes, {guess} is in the word")
        if "_" not in q_word:
            print("you won")
            break
    else:
        life-=1
        print(f"no, {guess} is not in the word. -1 life")
        if life==0:
            print("no life left. you lost")


    