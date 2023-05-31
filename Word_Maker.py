from random import choice
from time import sleep

def W_Maker(letters, count, len_words, flag):
    li_w = []
    n = 0
    while len_words != len(li_w):
        n+=1
        word = ""
        for num in range(count):
            word += choice(letters)
        if flag == False:
            for let in letters:
                if word.count(let) > 1:
                    word = ""
                    break
        if word not in li_w and word != "":
            li_w.append(word)
        if n == 1500:
            n = 0
            sleep(0.5)
    return li_w

while True:
    lets = input("<<<<<<<<<<<<<----------------------------------- Letters ----------------------------------->>>>>>>>>>>>>\
        \nThis tool builds words and helps you solve tables.\
        \nEnter a few letters and split them with space: ").strip()
    if lets.lower() == "exit" or lets.lower() == "e" or lets.lower() == "quit" or lets.lower() == "q":
        break
    lets = lets.split()
    err = False
    for let in lets:
        if len(let) > 1:
            print(f"<<< Error: Input is incorrect. (Reason for error: {let}) | Split one by one with a space. >>>")
            err = True
            break
        elif lets.count(let) > 1:
            print(f"<<< Error: Input is incorrect. (Reason for error: {let} | Count of '{let}' in input is {lets.count(let)}, but it must be 1.) >>>")
            err = True
            break
    if err == True:
        continue

    Count = input("<----------------------------------- Word length ----------------------------------->\
        \nSpecify the word length: ").strip()
    try:
        Count = int(Count)
    except:
        Count = len(lets)
    Flag = input("<----------------------------------- Repetition ----------------------------------->\
        \nDo you want a letter to be repeated in one word? y/n: ")
    if Flag.lower() == "y" or Flag.lower() == "yes":
        Flag = True
    else:
        Flag = False
    if Flag == False and Count > len(lets):
        print("<<< Error: cannot make any words. >>>")
        continue
    len_lets = len(lets)
    len_words = 1
    division = 1
    if Flag == False:
        for num in range(1, len_lets+1):
            len_words *= num
        for num in range(1, (len_lets - Count)+1):
            division *= num
        len_words = int(round(len_words / division))
    else:
        len_words = len_lets ** Count
    print("<-------------------------/^\/^\/^\| RESULT |/^\/^\/^\------------------------->\
        \nThe number of words:", len_words)
    All_words = W_Maker(lets, Count, len_words, Flag)
    
    i = 1
    for word in All_words:
        print(f"{i}: {word}")
        i += 1
    
# Author: M == PAIREN
# Contact Me: https://t.me/V_d_P_h_K
