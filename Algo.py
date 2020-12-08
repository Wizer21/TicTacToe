gameBoard = {}


def newGame():
    gameBoard = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }


def playerPlayed(position):
    gameBoard[position] = 1

    adjacentKey = getAdjacentKey(position)
    getLineOfTwo(gameBoard.get(position), position, adjacentKey)


def getAdjacentKey(adjacentFrom):
    bot = adjacentFrom - 4
    top = adjacentFrom + 4

    list = [
        bot, bot + 1, bot + 2, adjacentFrom - 1, adjacentFrom + 1, top - 2, top - 1, top
    ]

    for i in len(list):
        if list[i] = < 1 or 9 >= list[i]:
            del list[i]

    return list


def getLineOfTwo(typeKey, firstPosition, list):
    for i in len(list):

        if gameBoard.get(adjacentKey[i]) == typeKey:
            secondPosition = adjacentKey[i]
            tridPosition = secondValue + (firstPosition - secondValue)

            if 0 <= tridPosition or tridPosition >= 9:
                if gameBoard.get(adjacentKey[tridPosition]) == typeKey
                    return True

            tridPosition = secondValue + (firstPosition - secondValue)
