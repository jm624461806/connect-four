class Circle:
    '''
    Implement a Circle class
    '''
    def __init__(self, xpos=0, ypos=0, color='R'):
        '''
        Initialize a Circle class
        (Number), (Number), (String) -> None
        '''
        self.color = color
        self.x = xpos
        self.y = ypos

    def drop_me(self):
        '''
        Animate the dropping process.
        None -> None
        '''
        VEL_FAC = 20

        self.y += VEL_FAC
        self.draw_me()

    def draw_me_initial(self):
        '''
        Draw out the circle above the grid when click
        None -> None
        '''
        DROP_AREA_Y_LIMIT = 100
        FIRST_COL_LIMIT = 100
        SECOND_COL_LIMIT = 200
        THIRD_COL_LIMIT = 300
        FOURTH_COL_LIMIT = 400
        FIFTH_COL_LIMIT = 500
        SIXTH_COL_LIMIT = 600
        SEVENTH_COL_LIMIT = 700

        CIRCLE_Y = 50
        FIRST_CIRCLE_X = 50
        SECOND_CIRCLE_X = 150
        THIRD_CIRCLE_X = 250
        FOURTH_CIRCLE_X = 350
        FIFTH_CIRCLE_X = 450
        SIXTH_CIRCLE_X = 550
        SEVENTH_CIRCLE_X = 650

        if(self.y < DROP_AREA_Y_LIMIT):
            if(self.x < FIRST_COL_LIMIT and self.x >= 0):
                self.x = FIRST_CIRCLE_X
                self.y = CIRCLE_Y

            if(self.x >= FIRST_COL_LIMIT and self.x < SECOND_COL_LIMIT):
                self.x = SECOND_CIRCLE_X
                self.y = CIRCLE_Y

            if(self.x >= SECOND_COL_LIMIT and self.x < THIRD_COL_LIMIT):
                self.x = THIRD_CIRCLE_X
                self.y = CIRCLE_Y

            if(self.x >= THIRD_COL_LIMIT and self.x < FOURTH_COL_LIMIT):
                self.x = FOURTH_CIRCLE_X
                self.y = CIRCLE_Y

            if(self.x >= FOURTH_COL_LIMIT and self.x < FIFTH_COL_LIMIT):
                self.x = FIFTH_CIRCLE_X
                self.y = CIRCLE_Y

            if(self.x >= FIFTH_COL_LIMIT and self.x < SIXTH_COL_LIMIT):
                self.x = SIXTH_CIRCLE_X
                self.y = CIRCLE_Y

            if(self.x >= SIXTH_COL_LIMIT and self.x < SEVENTH_COL_LIMIT):
                self.x = SEVENTH_CIRCLE_X
                self.y = CIRCLE_Y

            self.draw_me()

    def draw_me(self):
        '''
        Draw the circle processing syntax
        None -> None
        '''
        WIDTH = 100
        HEIGHT = 100

        noStroke()
        if(self.color == 'R'):
            fill(1, 0, 0)
        elif(self.color == 'Y'):
            fill(1, 1, 0)
        ellipse(self.x, self.y, WIDTH, HEIGHT)
