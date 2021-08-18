import copy


class Minimax:
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)

    def minimax(self, matrix, depth, alpha, beta, maximizingPlayer):
        HUMAN_WIN_SCORE = -10000000
        AI_WIN_SCORE = 10000000

        potentialmoves = self.get_potential_moves(matrix)
        if (depth == 0 or self.judge_win(matrix) or
                len(potentialmoves) == 0):
            if(self.judge_win(matrix) and (maximizingPlayer is True)):
                return (None, HUMAN_WIN_SCORE)
            if(self.judge_win(matrix) and (maximizingPlayer is False)):
                return (None, AI_WIN_SCORE)
            return (None, self.evaluate(matrix))

        if (maximizingPlayer):
            value = -float('inf')
            column = None
            for col in potentialmoves:
                matrix_copy = copy.deepcopy(matrix)
                self.make_move(matrix_copy, col, True)
                new_value = self.minimax(matrix_copy, depth - 1,
                                         alpha, beta, False)[1]
                if(new_value > value):
                    value = new_value
                    column = col
                alpha = max(alpha, value)
                if beta < alpha:
                    break
            return (column, value)
        else:
            value = float('inf')
            column = None
            for col in potentialmoves:
                matrix_copy = copy.deepcopy(matrix)
                self.make_move(matrix_copy, col, False)
                new_value = self.minimax(matrix_copy, depth - 1,
                                         alpha, beta, True)[1]
                if(new_value < value):
                    value = new_value
                    column = col

                beta = min(beta, value)
                if beta < alpha:
                    break
            return (column, value)

    def get_potential_moves(self, matrix):
        potentialmoves = []
        COL_LEN = 7

        for i in range(COL_LEN):
            if(matrix[0][i] is False):
                potentialmoves.append(i)

        return potentialmoves

    def make_move(self, matrix, col, maximizingPlayer):
        ROW_LEN = 6

        for i in range(ROW_LEN - 1, -1, -1):
            if(matrix[i][col] == 'R' or matrix[i][col] == 'Y'):
                continue
            else:
                if(maximizingPlayer):
                    matrix[i][col] = 'Y'
                else:
                    matrix[i][col] = 'R'
                break

    def evaluate(self, matrix):
        THREE_EVALUATION = 1000
        TWO_EVALUATION = 10
        CONSECUTIVE_THREE = 3
        CONSECUTIVE_TWO = 2

        color = 'Y'
        opp = 'R'

        how_many_threes = self.check_consecutives(matrix, color,
                                                  CONSECUTIVE_THREE)
        how_many_twos = self.check_consecutives(matrix, color, CONSECUTIVE_TWO)

        opp_how_many_threes = self.check_consecutives(matrix, opp,
                                                      CONSECUTIVE_THREE)
        opp_how_many_twos = self.check_consecutives(matrix, opp,
                                                    CONSECUTIVE_TWO)
        return (how_many_threes * THREE_EVALUATION +
                how_many_twos * TWO_EVALUATION -
                opp_how_many_threes * THREE_EVALUATION -
                opp_how_many_twos * TWO_EVALUATION)

    def check_consecutives(self, matrix, color, consecutives):
        ROW_LEN = 6
        COL_LEN = 7

        count = 0

        for row in range(ROW_LEN):
            for col in range(COL_LEN):
                if (matrix[row][col] == color):
                    tempcount = 1
                    for i in range(row + 1, ROW_LEN):
                        if(matrix[i][col] == color):
                            tempcount += 1
                        else:
                            break
                    if(tempcount >= consecutives):
                        count += 1

                    tempcount = 1
                    for j in range(col + 1, COL_LEN):
                        if(matrix[row][j] == color):
                            tempcount += 1
                        else:
                            break
                    if(tempcount == consecutives):
                        count += 1

                    tempcount = 1
                    col_copy = col + 1
                    for m in range(row + 1, ROW_LEN):
                        if(col_copy > COL_LEN - 1):
                            break
                        elif(matrix[m][col_copy] == color):
                            tempcount += 1
                        else:
                            break
                        col_copy += 1
                    if(tempcount == consecutives):
                        count += 1

                    tempcount = 1
                    col_copy = col + 1
                    for n in range(row - 1, -1, -1):
                        if(col_copy > COL_LEN - 1):
                            break
                        elif(matrix[n][col_copy] == color):
                            tempcount += 1
                        else:
                            break
                        col_copy += 1
                    if(tempcount == consecutives):
                        count += 1
        return count

    def judge_win(self, matrix):
        ROW_LEN = 6
        COL_LEN = 7
        JUDGING_LIMIT = 3

        NEIGHBOR = 2
        NEIGHBOR_NEXT = 3

        for x in range(ROW_LEN - JUDGING_LIMIT):
            for y in range(COL_LEN):
                if (matrix[x][y] == 'R' and
                    matrix[x+1][y] == 'R' and
                    matrix[x+NEIGHBOR][y] == 'R' and
                    matrix[x+NEIGHBOR_NEXT][y] == 'R') or \
                    (matrix[x][y] == 'Y' and
                     matrix[x+1][y] == 'Y' and
                     matrix[x+NEIGHBOR][y] == 'Y' and
                     matrix[x+NEIGHBOR_NEXT][y] == 'Y'):

                    return True

        for x in range(ROW_LEN):
            for y in range(COL_LEN - JUDGING_LIMIT):
                if (matrix[x][y] == 'R' and
                    matrix[x][y+1] == 'R' and
                    matrix[x][y+NEIGHBOR] == 'R' and
                    matrix[x][y+NEIGHBOR_NEXT] == 'R') or \
                    (matrix[x][y] == 'Y' and
                     matrix[x][y+1] == 'Y' and
                     matrix[x][y+NEIGHBOR] == 'Y' and
                     matrix[x][y+NEIGHBOR_NEXT] == 'Y'):

                    return True

        for x in range(ROW_LEN - JUDGING_LIMIT):
            for y in range(JUDGING_LIMIT, COL_LEN):
                if (matrix[x][y] == 'R' and
                    matrix[x+1][y-1] == 'R' and
                    matrix[x+NEIGHBOR][y-NEIGHBOR] == 'R' and
                    matrix[x+NEIGHBOR_NEXT][y-NEIGHBOR_NEXT] == 'R') or \
                    (matrix[x][y] == 'Y' and
                     matrix[x+1][y-1] == 'Y' and
                     matrix[x+NEIGHBOR][y-NEIGHBOR] == 'Y' and
                     matrix[x+NEIGHBOR_NEXT][y-NEIGHBOR_NEXT] == 'Y'):

                    return True
        for x in range(ROW_LEN - JUDGING_LIMIT):
            for y in range(COL_LEN - JUDGING_LIMIT):
                if (matrix[x][y] == 'R' and
                    matrix[x+1][y+1] == 'R' and
                    matrix[x+NEIGHBOR][y+NEIGHBOR] == 'R' and
                    matrix[x+NEIGHBOR_NEXT][y+NEIGHBOR_NEXT] == 'R') or \
                    (matrix[x][y] == 'Y' and
                     matrix[x+1][y+1] == 'Y' and
                     matrix[x+NEIGHBOR][y+NEIGHBOR] == 'Y' and
                     matrix[x+NEIGHBOR_NEXT][y+NEIGHBOR_NEXT] == 'Y'):
                    return True
        return False
