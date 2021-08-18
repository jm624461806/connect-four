from grid import Grid
from circle import Circle
from minimax import Minimax
import math


class GameController:
    '''
    Implement a GameController class.
    '''
    VISITED = {
            50: 650,
            150: 650,
            250: 650,
            350: 650,
            450: 650,
            550: 650,
            650: 650
        }
    BOARDWIDTH = 7
    BOARDHEIGHT = 6

    def __init__(self, space):
        '''
        Initialize the GameController class.
        Dictionary -> None
        '''
        self.SPACE = space
        self.boardwidth = self.BOARDWIDTH
        self.boardheight = self.BOARDHEIGHT
        self.millis = 0
        self.mouse_pressed = False
        self.mouse_released = False
        self.computer_turn = False
        self.game_result = False
        self.get_the_choice = False
        self.computer_announce = False
        self.file_trigger = False
        self.player_announce = True
        self.player_win_boolean = True
        self.grid = Grid()
        self.circle_to_drop = Circle()
        self.circles = []
        self.occupied = [
            [False] * self.boardwidth for _ in range(self.boardheight)
        ]
        self.visited = self.VISITED
        self.scores = {}

    def above_the_grid(self):
        '''
        Control the drawing of the to-be-dropped disk when mouse is pressed.
        None -> None
        '''
        if(self.mouse_pressed):
            x = mouseX
            y = mouseY
            okay_to_draw = self.if_mouse_pressed(x, y)
            if(okay_to_draw):
                self.circle_to_drop.draw_me_initial()

    def update(self):
        '''
        Main function that controls the flow of the game.
        None -> None
        '''
        TEXTSIZE = 50
        SPOTS = 42
        GAMEPAUSE = 800

        HALF_SPACE_FAC = 2

        DROPPING_WINDOW_Y = 60
        YOUR_TURN_X = 110
        AI_TURN_X = 200
        YOU_WIN_X = 80
        AI_WIN_X = 160

        for circle in self.circles:
            circle.draw_me()

        self.grid.display()

        if(self.file_trigger):
            if(self.player_win_boolean):
                self.read_the_score()
                self.record_the_score()
                self.file_trigger = False
                self.player_win_boolean = False

        if(self.player_announce):
            fill(0)
            textSize(TEXTSIZE)
            text("Your turn",
                 self.SPACE['w']/HALF_SPACE_FAC - YOUR_TURN_X,
                 DROPPING_WINDOW_Y)

        if(self.mouse_released):
            if(self.ok_to_drop(self.circle_to_drop.x)):
                self.circle_to_drop.drop_me()

            if(self.circle_to_drop.y >= self.visited[self.circle_to_drop.x]):
                self.after_the_drop()
                self.mouse_released = False
                self.computer_turn = True
                self.get_the_choice = True
                self.computer_announce = True
                self.player_announce = False
                self.millis = millis()

        if(self.judge_win() and self.circle_to_drop.color == 'R'):
            fill(0)
            textSize(TEXTSIZE)
            text("You win!",
                 self.SPACE['w']/HALF_SPACE_FAC - YOU_WIN_X,
                 self.SPACE['h']/HALF_SPACE_FAC)
            self.computer_turn = False
            self.get_the_choice = False
            self.game_result = True
            self.computer_announce = False
            self.file_trigger = True
            self.millis = millis()

        elif(len(self.circles) == SPOTS):
            self.after_full_board()
            self.computer_turn = False
            self.get_the_choice = False
            self.computer_announce = False

        if(self.computer_announce):
            fill(0)
            textSize(TEXTSIZE)
            text("Computer's turn",
                 self.SPACE['w']/HALF_SPACE_FAC - AI_TURN_X,
                 DROPPING_WINDOW_Y)

        if(millis() > self.millis + GAMEPAUSE):
            self.computer_announce = False

            if(self.get_the_choice):
                col = self.get_computer_moves()
                self.computer_make_move(col)
                self.get_the_choice = False

            if(self.computer_turn):
                if(self.ok_to_drop(self.circle_to_drop.x)):
                    self.circle_to_drop.drop_me()

                if(self.circle_to_drop.y >=
                        self.visited[self.circle_to_drop.x]):
                    self.after_the_drop()
                    self.computer_turn = False
                    self.player_announce = True

            if(self.judge_win() and self.circle_to_drop.color == 'Y'):
                fill(0)
                textSize(TEXTSIZE)
                text("Computer win!",
                     self.SPACE['w']/HALF_SPACE_FAC - AI_WIN_X,
                     self.SPACE['h']/HALF_SPACE_FAC)
                self.game_result = True
                self.player_announce = False

            if(len(self.circles) == SPOTS):
                self.after_full_board()
                self.player_announce = False

    def handle_mouse_press(self, xposition, yposition):
        '''
        Handle the circle behavior once the mouse is pressed.
        Number, Number -> None
        '''
        self.player_announce = False

        WINDOW_Y_LIMIT = 100
        FIRST_COL_LIMIT = 100
        SECOND_COL_LIMIT = 200
        THIRD_COL_LIMIT = 300
        FOURTH_COL_LIMIT = 400
        FIFTH_COL_LIMIT = 500
        SIXTH_COL_LIMIT = 600
        SEVENTH_COL_LIMIT = 700

        FIRST_CIRCLE_X = 50
        SECOND_CIRCLE_X = 150
        THIRD_CIRCLE_X = 250
        FOURTH_CIRCLE_X = 350
        FIFTH_CIRCLE_X = 450
        SIXTH_CIRCLE_X = 550
        SEVENTH_CIRCLE_X = 650

        if(yposition >= WINDOW_Y_LIMIT or yposition < 0):
            return
        if(self.mouse_released):
            return
        if(self.computer_turn):
            self.mouse_pressed = False
            return
        if(self.game_result):
            self.mouse_pressed = False
            return
        if(yposition >= 0 and yposition <= WINDOW_Y_LIMIT):
            if(xposition >= 0 and xposition < FIRST_COL_LIMIT):
                if(self.ok_to_drop(FIRST_CIRCLE_X)):
                    self.mouse_pressed = True

            if(xposition >= FIRST_COL_LIMIT and xposition < SECOND_COL_LIMIT):
                if(self.ok_to_drop(SECOND_CIRCLE_X)):
                    self.mouse_pressed = True

            if(xposition >= SECOND_COL_LIMIT and xposition < THIRD_COL_LIMIT):
                if(self.ok_to_drop(THIRD_CIRCLE_X)):
                    self.mouse_pressed = True

            if(xposition >= THIRD_COL_LIMIT and xposition < FOURTH_COL_LIMIT):
                if(self.ok_to_drop(FOURTH_CIRCLE_X)):
                    self.mouse_pressed = True

            if(xposition >= FOURTH_COL_LIMIT and xposition < FIFTH_COL_LIMIT):
                if(self.ok_to_drop(FIFTH_CIRCLE_X)):
                    self.mouse_pressed = True

            if(xposition >= FIFTH_COL_LIMIT and xposition < SIXTH_COL_LIMIT):
                if(self.ok_to_drop(SIXTH_CIRCLE_X)):
                    self.mouse_pressed = True

            if(xposition >= SIXTH_COL_LIMIT and xposition < SEVENTH_COL_LIMIT):
                if(self.ok_to_drop(SEVENTH_CIRCLE_X)):
                    self.mouse_pressed = True

    def if_mouse_pressed(self, xposition, yposition):
        '''
        Record the circle behavior if the mouse if pressed and move around.
        Return the boolean value of wether the dropping is legal.
        Number, Number -> Boolean
        '''
        WINDOW_Y_LIMIT = 100
        FIRST_COL_LIMIT = 100
        SECOND_COL_LIMIT = 200
        THIRD_COL_LIMIT = 300
        FOURTH_COL_LIMIT = 400
        FIFTH_COL_LIMIT = 500
        SIXTH_COL_LIMIT = 600
        SEVENTH_COL_LIMIT = 700

        FIRST_CIRCLE_X = 50
        SECOND_CIRCLE_X = 150
        THIRD_CIRCLE_X = 250
        FOURTH_CIRCLE_X = 350
        FIFTH_CIRCLE_X = 450
        SIXTH_CIRCLE_X = 550
        SEVENTH_CIRCLE_X = 650

        if(yposition >= 0 and yposition <= WINDOW_Y_LIMIT):
            if(xposition >= 0 and xposition < FIRST_COL_LIMIT):
                if(self.ok_to_drop(FIRST_CIRCLE_X)):
                    self.circle_to_drop = Circle(xposition, yposition, 'R')
                    return True
            elif(xposition >= FIRST_COL_LIMIT and
                 xposition < SECOND_COL_LIMIT):
                if(self.ok_to_drop(SECOND_CIRCLE_X)):
                    self.circle_to_drop = Circle(xposition, yposition, 'R')
                    return True
            elif(xposition >= SECOND_COL_LIMIT and
                 xposition < THIRD_COL_LIMIT):
                if(self.ok_to_drop(THIRD_CIRCLE_X)):
                    self.circle_to_drop = Circle(xposition, yposition, 'R')
                    return True
            elif(xposition >= THIRD_COL_LIMIT and
                 xposition < FOURTH_COL_LIMIT):
                if(self.ok_to_drop(FOURTH_CIRCLE_X)):
                    self.circle_to_drop = Circle(xposition, yposition, 'R')
                    return True
            elif(xposition >= FOURTH_COL_LIMIT and
                 xposition < FIFTH_COL_LIMIT):
                if(self.ok_to_drop(FIFTH_CIRCLE_X)):
                    self.circle_to_drop = Circle(xposition, yposition, 'R')
                    return True
            elif(xposition >= FIFTH_COL_LIMIT and xposition < SIXTH_COL_LIMIT):
                if(self.ok_to_drop(SIXTH_CIRCLE_X)):
                    self.circle_to_drop = Circle(xposition, yposition, 'R')
                    return True
            elif(xposition >= SIXTH_COL_LIMIT and
                 xposition < SEVENTH_COL_LIMIT):
                if(self.ok_to_drop(SEVENTH_CIRCLE_X)):
                    self.circle_to_drop = Circle(xposition, yposition, 'R')
                    return True
        else:
            return False

    def handle_mouse_release(self):
        '''
        Handle the behavior when the mouse is released.
        None -> None
        '''
        if(self.mouse_released):
            return
        if(not self.mouse_pressed):
            self.mouse_released = False
        else:
            self.mouse_released = True
            self.mouse_pressed = False

    def ok_to_drop(self, x):
        '''
        Judge if the column is okay to drop.
        Integer -> Boolean
        '''
        COLUMN_FULL_LIMIT = 50

        if(self.visited[x] > COLUMN_FULL_LIMIT):
            return True
        else:
            return False

    def after_the_drop(self):
        '''
        Record the just-dropped circle information.
        None -> None
        '''
        DISTANCE_BEWTEEN_BALLS = 100

        self.calculate_occupied()
        self.visited[self.circle_to_drop.x] -= DISTANCE_BEWTEEN_BALLS
        self.circles.append(self.circle_to_drop)

    def calculate_occupied(self):
        '''
        Record the disk position in the 6*7 board.
        None -> None
        '''
        POSITION_CAL_FAC_ONE = 50
        POSITION_CAL_FAC_TWO = 100

        row = int((self.circle_to_drop.y - POSITION_CAL_FAC_ONE) /
                  POSITION_CAL_FAC_TWO - 1)
        col = int((self.circle_to_drop.x - POSITION_CAL_FAC_ONE) /
                  POSITION_CAL_FAC_TWO)
        if(self.circle_to_drop.color == 'R'):
            self.occupied[row][col] = 'R'
        elif(self.circle_to_drop.color == 'Y'):
            self.occupied[row][col] = 'Y'

    def judge_win(self):
        '''
        Judge if any player wins the game.
        None -> Boolean
        '''
        ROW_LEN = 6
        COL_LEN = 7
        EDGE_FAC = 3

        NEIGHBOR = 2
        NEIGHBOR_NEXT = 3

        for x in range(self.boardheight - EDGE_FAC):
            for y in range(self.boardwidth):
                if (self.occupied[x][y] == 'R' and
                    self.occupied[x+1][y] == 'R' and
                    self.occupied[x+NEIGHBOR][y] == 'R' and
                    self.occupied[x+NEIGHBOR_NEXT][y] == 'R') or\
                    (self.occupied[x][y] == 'Y' and
                     self.occupied[x+1][y] == 'Y' and
                     self.occupied[x+NEIGHBOR][y] == 'Y' and
                     self.occupied[x+NEIGHBOR_NEXT][y] == 'Y'):

                    return True

        for x in range(self.boardheight):
            for y in range(self.boardwidth - EDGE_FAC):
                if (self.occupied[x][y] == 'R' and
                    self.occupied[x][y+1] == 'R' and
                    self.occupied[x][y+NEIGHBOR] == 'R' and
                    self.occupied[x][y+NEIGHBOR_NEXT] == 'R') or\
                    (self.occupied[x][y] == 'Y' and
                     self.occupied[x][y+1] == 'Y' and
                     self.occupied[x][y+NEIGHBOR] == 'Y' and
                     self.occupied[x][y+NEIGHBOR_NEXT] == 'Y'):

                    return True

        for x in range(self.boardheight - EDGE_FAC):
            for y in range(3, self.boardwidth):
                if (self.occupied[x][y] == 'R' and
                    self.occupied[x+1][y-1] == 'R' and
                    self.occupied[x+NEIGHBOR][y-NEIGHBOR] == 'R' and
                    self.occupied[x+NEIGHBOR_NEXT][y-NEIGHBOR_NEXT] == 'R') or\
                    (self.occupied[x][y] == 'Y' and
                     self.occupied[x+1][y-1] == 'Y' and
                     self.occupied[x+NEIGHBOR][y-NEIGHBOR] == 'Y' and
                     self.occupied[x+NEIGHBOR_NEXT][y-NEIGHBOR_NEXT] == 'Y'):

                    return True
        for x in range(self.boardheight - EDGE_FAC):
            for y in range(self.boardwidth - EDGE_FAC):
                if (self.occupied[x][y] == 'R' and
                    self.occupied[x+1][y+1] == 'R' and
                    self.occupied[x+NEIGHBOR][y+NEIGHBOR] == 'R' and
                    self.occupied[x+NEIGHBOR_NEXT][y+NEIGHBOR_NEXT] == 'R') or\
                    (self.occupied[x][y] == 'Y' and
                     self.occupied[x+1][y+1] == 'Y' and
                     self.occupied[x+NEIGHBOR][y+NEIGHBOR] == 'Y' and
                     self.occupied[x+NEIGHBOR_NEXT][y+NEIGHBOR_NEXT] == 'Y'):

                    return True
        return False

    def get_computer_moves(self):
        '''
        AI calculated the move and return the col the disk should
        be dropped.
        None -> Integer
        '''
        DEPTH = 5

        mima = Minimax(self.occupied)
        return mima.minimax(mima.matrix, DEPTH, -float('inf'),
                            float('inf'), True)[0]

    def computer_make_move(self, col):
        '''
        Computer drop the disk.
        Integer -> None
        '''
        POSITION_CAL_FAC_ONE = 50
        POSITION_CAL_FAC_TWO = 100
        CIRCLE_POSITION_Y = 50

        xposition = col * POSITION_CAL_FAC_TWO + POSITION_CAL_FAC_ONE
        yposition = CIRCLE_POSITION_Y
        self.circle_to_drop = Circle(xposition, yposition, 'Y')
        self.circle_to_drop.draw_me_initial()

    def after_full_board(self):
        '''
        Game is a tie notification!
        None -> None
        '''
        TEXTSIZE = 50
        HALF_SPACE_FAC = 2
        TIE_X = 150

        fill(0)
        textSize(50)
        text("Game is a TIE!",
             self.SPACE['w']/HALF_SPACE_FAC - TIE_X,
             self.SPACE['h']/HALF_SPACE_FAC)

    def read_the_score(self):
        '''
        Read the name and score, then sort them.
        None -> None
        '''
        f = open("scores.txt", 'r')
        for line in f:
            score_list = line.rstrip().split()
            score = score_list[-1]
            score_list.pop(-1)
            name = ' '.join(score_list)
            self.scores[name] = int(score)
        f.close()

    def record_the_score(self):
        '''
        Record the name and corresponding score.
        None -> None
        '''
        name = self.input('Please enter your name')
        while(name is None or name == ''):
            name = self.input('Please enter your name')
        if name in self.scores.keys():
            self.scores[name] += 1
        else:
            self.scores[name] = 1
        the_names = self.top_n_counts()

        f = open("scores.txt", "w")
        for score in the_names:
            s = score[0] + ' ' + str(score[1]) + '\n'
            f.write(s)
        f.close()

    def input(self, message=''):
        '''
        Let python input workable in processing.
        '''
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def top_n_counts(self):
        '''
        Sort the self.scores in a descending
        order.
        None -> List
        '''
        return sorted(
            self.scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
