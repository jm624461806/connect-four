class Grid:
    '''
    Implement a Grid class
    '''
    def display(self):
        '''
        Draw the grid in processing syntax
        None -> None
        '''
        STROKEWEIGHT = 3

        strokeWeight(STROKEWEIGHT)
        stroke(0, 0, 1)
        line(0, 100, 700, 100)
        line(0, 200, 700, 200)
        line(0, 300, 700, 300)
        line(0, 400, 700, 400)
        line(0, 500, 700, 500)
        line(0, 600, 700, 600)

        line(100, 100, 100, 700)
        line(200, 100, 200, 700)
        line(300, 100, 300, 700)
        line(400, 100, 400, 700)
        line(500, 100, 500, 700)
        line(600, 100, 600, 700)

        strokeWeight(STROKEWEIGHT)
        stroke(0, 0, 1)
        line(0, 100, 0, 700)

        line(700, 100, 700, 700)

        line(0, 700, 700, 700)
