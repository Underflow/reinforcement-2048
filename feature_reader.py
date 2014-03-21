def get_variance(board):
    # FIXME: code me
    return 0

def mergeable_tiles(board, direction):
    # FIXME: code me
    return 0

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

def extract_features(board):
    # Dim(set) = 13
    features = []

    # Vertical/horizontal density extraction
    # Dim = 8
    (xdensity, ydensity) = get_histograms(board)
    for density in xdensity:
        features.append(density)
    for density in ydensity:
        features.append(density)

    # Number of close mergeable tiles for each direction
    # Dim = 4
    for direction in range(0, 4):
        features.append(mergeable_tiles(board, direction))

    # Variance of the board
    # Dim = 1
    features.append(get_variance(board))

    return features


