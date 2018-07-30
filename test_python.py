def generate_matrix(num):
    init_matrix(num)

    ori = True
    row_col_flag = True
    row_len = col_len = num
    i = 1
    for row in range(num):
        for col in range(num):
            if row > row_len or col > col_len:
                continue
            if row_col_flag:
                if ori:
                    matrix[row][col] = i
                else:
                    matrix[row][col_len - col] = i
            else:
                if ori:
                    matrix[col][row] = i
                else:
                    matrix[col][row_len - row] = i
            i += 1
        else:
            if row_col_flag:
                col_len -= 1
            else:
                row_len -= 1
            row_col_flag = not row_col_flag


def init_matrix(num):
    for i in num:
        for j in num:
            matrix[i][j] = 0


if __name__ == "__main__":
    import sys

    matrix = []
    generate_matrix(6)
    print matrix
    # generate_matrix(sys.stdin.readline())
    # sys.stdout(matrix)
