import math
file1 = open('input20.txt', 'r')


class Tile():
    def __init__(self):
        self.rows = []
        self.top = []
        self.left = []
        self.right = []
        self.bottom = []
        self.valid = 0


tiles = {}
for line in file1.readlines():
    line = line.strip()
    if (line[:4] == "Tile"):
        tileNumber = line[5:9]
        tiles[tileNumber] = Tile()
        # print(tileNumber)
    elif (line == ""):
        pass
        # print('empty')
    else:
        tiles[tileNumber].rows.append(list(line))

# flip the rows 
for key in tiles:
    tile = tiles[key]
    tile.top = tile.rows[0]
    tile.bottom = tile.rows[-1]
    cols = list(zip(*tile.rows))
    tile.left = cols[0]
    tile.right = cols[-1]
    tile.sides = [tile.top, tile.bottom, tile.left, tile.right]

    flipped = [row[::-1] for row in tile.rows]
    flippedCols = list(zip(*flipped))

    tile.fMap = flipped
    tile.fTop = flipped[0]
    tile.fBottom = flipped[-1]
    tile.fLeft = flippedCols[0]
    tile.fRight = flippedCols[-1]
    tile.fSides = [tile.fTop, tile.fBottom, tile.fLeft, tile.fRight]

cornerTiles = []
for key in tiles:
    currentTile = tiles[key]
    # print(currentTile.sides)
    for key2 in tiles:
        compareTile = tiles[key2]
        
        if (key != key2):
            for side in currentTile.sides:
                for side1 in compareTile.sides:
                    if (side == side1):
                        currentTile.valid +=1
                
                for side2 in compareTile.fSides:
                    if (side == side2):
                        currentTile.valid +=1
        # if (key != key2):
        #     if (currentTile.top == compareTile.bottom or currentTile.top == flipBottom or currentTile.top == compareTile.top or currentTile.top == flipTop):
        #         currentTile.valid += 1
        #     if (currentTile.bottom == compareTile.top or currentTile.bottom == flipTop or currentTile.bottom == compareTile.bottom or currentTile.bottom == flipBottom):
        #         currentTile.valid += 1
        #     if (currentTile.left == compareTile.right or currentTile.left == flipRight or currentTile.left == compareTile.left or currentTile.left == flipLeft):
        #         currentTile.valid += 1
        #     if (currentTile.right == compareTile.left or currentTile.right == flipLeft or currentTile.right == compareTile.right or currentTile.right == flipRight):
        #         currentTile.valid += 1

    if (currentTile.valid >= 0):
        print(currentTile.valid)
        cornerTiles.append(key)

# for key in tiles:
#     print(tiles[key].valid)
print(cornerTiles)
# print(math.prod(map(int,cornerTiles)))

# print(key)
# print(tile.top)
# print(tile.bottom)
# print(tile.left)
# print(tile.right)
# print('\n')
# print(tiles)
# 19945942578259 answer too low
