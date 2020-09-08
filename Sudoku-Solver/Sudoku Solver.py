board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def main_algo(data):
    find = find_empty(data)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(data, i, (row, col)):
            data[row][col] = i

            if main_algo(data):
                return True

            data[row][col] = 0

    return False


def valid(data, num, loc):
    # Check row for duplicates
    for i in range(len(data[0])):
        if data[loc[0]][i] == num and loc[1] != i:
            return False

    # Check column for duplicates
    for i in range(len(data)):
        if data[i][loc[1]] == num and loc[0] != i:
            return False

    # Check 9x9 grid for duplicates
    box_row = loc[0] // 3
    box_col = loc[1] // 3

    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if data[i][j] == num and (i, j) != loc:
                return False

    return True


def data_preview(data):
    for i in range(len(data)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(data[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(data[i][j])
            else:
                print(str(data[i][j]) + " ", end="")


def find_empty(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 0:
                return (i, j)  # row, col

    return None


print(data_preview(board))
main_algo(board)
print("- - - - - - - - - - - - - ")
print("- - - - - - - - - - - - - ")
print(data_preview(board))
