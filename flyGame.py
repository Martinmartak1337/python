from random import randrange
from time import sleep
from os import name
from newFlyGame import abba
l = [list] * 64 #defining the map
m = [list]
b = [list] * 8
def defineGameAndOtherCharacterS(row: int, character: str) -> list:
    someThingStrange = randomCall()
    if character == '$':
        global integerValue
        integerValue = someThingStrange
    l[(row*8)-1+someThingStrange] = character # break here.
    return l
def randomCall() -> int:
    return randrange(0, 8)
def defineAll() -> list:
    for i in range(7):
        defineGameAndOtherCharacterS(i, '#')
    return  defineGameAndOtherCharacterS(7, '$')
d = defineAll()
def inputField() -> int:
    return int(input())
def ifStatementForCheckingCharacter(char: str) -> bool:
    if char == '$':
        return True
    return False
def mainGameLoop(score: int) -> list:
    c = 0
    for q in range(len(d)-8, len(d)):
        if ifStatementForCheckingCharacter('$'):
            c = q
    for k in range(len(d)-8):
        d[k+8] = d[k]
    for n in range(8):
        d[n] = b[n]
    d[randomCall()] = '#'
    if d[c+inputField()-8] == '#':
        abba(score)
        print("GAME OVER!!!")
        quit(0)
    else:
        d[c+inputField()-8] = '$'
    return d
def hasWrittenScore() -> bool:
    return True
def main():
    game = 0
    while True:
        f = mainGameLoop(game)          # [0, 0, 0, 0, 0, 0, 0, #]
        game+=1
        sleep(0.05)
        print(f)
        print('\n')
main()

