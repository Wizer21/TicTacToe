listOfRows = []
aRow = {}
bRow = {}
cRow = {}

listOfRows = [aRow, bRow, cRow]

def newGame():

    aRow.clear()
    bRow.clear()
    cRow.clear()

    aRow[0] = 0
    aRow[1] = 0
    aRow[2] = 0

    bRow[0] = 0
    bRow[1] = 0
    bRow[2] = 0

    cRow[0] = 0
    cRow[1] = 0
    cRow[2] = 0

# 0 = Case Vide
# 1 = Case Joueur
# 3 = Case Ia

def iniAlgo(position): #Initialisation
    position = int(position)
    # Ajouter la nouvelle case à la liste des valeurs
    if position <= 2:
        aRow[position]  = 1
    elif position <= 5:
        position -= 3
        bRow[position]  = 1
    else:
        position -= 6
        cRow[position]  = 1

    winPlays = []
    counterPlays  = []
    goodPlays = []

    # Regarde les 3 lignes
    player = 1
    ia = 2
    empty = []

    for i in range(len(listOfRows)):
        pointPlayer = 0
        pointsIA = 0
        empty.clear()
        for idPos in range(len(listOfRows[i])):
            if listOfRows[i][idPos] == player:
                pointPlayer += 1
            if listOfRows[i][idPos] == ia:
                pointsIA += 1
            if listOfRows[i][idPos] == 0:
                empty.append(idPos)
        if pointPlayer == 3:
            return 1
        if pointsIA == 2 and len(empty) == 1:
            winPlays.append(str(i) + str(empty[0]))
        if pointPlayer == 2 and len(empty) == 1:
            counterPlays.append(str(i) + str(empty[0]))
        if len(empty) == 2 and pointPlayer == 1:
            goodPlays.append(str(i) + str(empty[0]))
            goodPlays.append(str(i) + str(empty[1]))

    # Regarde les 3 colones
    columns = {}
    for idRow in range(len(listOfRows)):
        pointPlayer = 0
        pointsIA = 0
        empty.clear()

        columns.clear()
        for i in range(3):
            columns[i] = listOfRows[i][idRow]

        for idPos in range(len(columns)):
            if columns[idPos] == player:
                pointPlayer += 1
            if columns[idPos] == ia:
                pointsIA += 1
            if columns[idPos] == 0:
                empty.append(idPos)
        if pointPlayer == 3:
            return 1
        if pointsIA == 2 and len(empty) == 1:
            winPlays.append(str(idRow) + str(empty[0]))
        if pointPlayer == 2 and len(empty) == 1:
            counterPlays.append(str(idRow) + str(empty[0]))
        if len(empty) == 2 and pointPlayer == 1:
            goodPlays.append(str(idRow) + str(empty[0]))
            goodPlays.append(str(idRow) + str(empty[1]))

    # verifier Diagonale 1
    diag = []
    for y in range(len(listOfRows)):
        value = listOfRows[y][y]
        diag.append(value)

    pointPlayer = 0
    pointsIA = 0
    empty.clear()

    for idPos in range(len(diag)):
        if diag[idPos] == player:
            pointPlayer += 1
        if diag[idPos] == ia:
            pointsIA += 1
        if diag[idPos] == 0:
            empty.append(str(idPos) + str(idPos))
    if pointPlayer == 3:
        return 1
    if pointsIA == 2 and len(empty) == 1:
        winPlays.append(empty[0])
    if pointPlayer == 2 and len(empty) == 1:
        counterPlays.append(empty[0])
    if len(empty) == 2 and pointPlayer == 1:
        goodPlays.append(empty[0])
        goodPlays.append(empty[1])

    # verifier Diagonale 2
    diag.clear()

    diag.append(listOfRows[2][0])
    diag.append(listOfRows[1][1])
    diag.append(listOfRows[0][2])

    pointPlayer = 0
    pointsIA = 0
    empty.clear()

    for idPos in range(len(diag)):
        if diag[idPos] == player:
            pointPlayer += 1
        if diag[idPos] == ia:
            pointsIA += 1
        if diag[idPos] == 0:
            empty.append(str(idPos) + str(idPos))
    if pointPlayer == 3:
        return 1
    if pointsIA == 2 and len(empty) == 1:
        winPlays.append(empty[0])
    if pointPlayer == 2 and len(empty) == 1:
        counterPlays.append(empty[0])
    if len(empty) == 2 and pointPlayer == 1:
        goodPlays.append(empty[0])
        goodPlays.append(empty[1])

    # 0 = continue
    # 1 = win

    if len(winPlays) > 0:
        return str(1) + winPlays[0]
    if len(counterPlays) > 0:
        return str(0) + counterPlays[0]
    if len(goodPlays) > 0:
        return str(0) + goodPlays[0]

    for i in range(len(listOfRows)):
        for j in listOfRows[i]:
            if listOfRows[i][j] == 0:
                return str(0) + str(i) + str(j)

