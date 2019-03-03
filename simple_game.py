import random

#get guess

def get_guess():
    return list(input('enter ur guess (3 digit number)'))

#generate computer code
def generate_code():
        digits = [str(num) for num in range(10)]

        #shuffling the digits
        random.shuffle(digits)
        return digits[:3]
#generate clues

def generate_clues(code,user_guess):
    if user_guess==code:
        return "you have successfully cracked the code"

    clues = []
    for ind,num in enumerate(user_guess):
        if num==code[ind]:
            clues.append("few digits are mathching the exact location")
        elif num in code:
            clues.append("few digits exits in real code")

    if clues== []:
        return ["none of the digit is matching"]
    else:
        return clues

#game run logic
print ("welcome to game code-breaker")

secret_code= generate_code()

clue_report=[]

while clue_report != "you have successfully cracked the code":
    guess = get_guess()

    clue_report = generate_clues(guess,secret_code)
    print(clue_report)
    for clue in clue_report:
        print (clue)
