# Extract the variance of the board
def get_variance(board):
    # FIXME: code me
    return 0

# Extracts the number of close mergeable tiles for each direction
def mergeable_tiles(board, direction):
    # FIXME: code me
    return 0

# Extracts vertical and horizontal histograms of the board
def get_histograms(board):
    xhisto = [0, 0, 0, 0]
    yhisto = [0, 0, 0, 0]

    for x in range(0, 4):
        yhval = 0
        for y in range(0, 4):
            if board[x][y]:
                xhisto[y] += board[x][y]
                yhval += board[x][y]
        yhisto[x] += yhval

    return (xhisto, yhisto)

