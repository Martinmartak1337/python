from random import randrange
from time import sleep
l = [list] * 64 #defining the map
m = [list]
b = [list] * 8
def defineGameAndOtherCharacterS(row: int, character: str) -> list:
    someThingStrange = randomCall()
    if character == '$':
        global integerValue
        integerValue = someThingStrange
    l[(row*8)-1+someThingStrange] = character
    return l
def randomCall() -> int:
    return randrange(0, 8)
def defineAll() -> list:
    for i in range(6):
        defineGameAndOtherCharacterS(i, '#')
    return  defineGameAndOtherCharacterS(7, '$')
d = defineAll()
def defineBullet() -> int:
    # define it already!
    return -1
def inputField() -> int:
    return 0
def ifStatementForCheckingCharacter(char: str) -> bool:
    if char == '$':
        return True
    return False
def mainGameLoop() -> list:
    c = 0
    for q in range(len(d)-8, len(d)):
        if ifStatementForCheckingCharacter('$'):
            c = q
    for k in range(len(d)-8):
        d[k+8] = d[k]
    for n in range(8):
        d[n] = b[n]
    d[randomCall()] = '#'
    if d[c+inputField()] == '#':
        print("GAME OVER!!!")
        quit(0)
    else:
        d[c+inputField()] = '$'
    return d
def main():
    while True:
        sleep(0.25)
        print(mainGameLoop())
        print('\n')
main()