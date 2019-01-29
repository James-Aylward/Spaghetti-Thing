# Written by James Aylward #

import wx 
import Windows
import random

class SimulationWindow(Windows.SimulationWindow): 
    
    # Constructor
    def __init__(self, row_count, element_count, cell_size, update_time, outline): 
        Windows.SimulationWindow.__init__(self, None)

        # Cellular Automaton Setttings      
        self.row_count = row_count
        self.element_count = element_count
        self.cell_size = cell_size
        self.update_time = update_time


        # Rendering settings
        self.alive_colour = wx.Colour(255, 215, 160)
        self.dead_colour = wx.Colour(255, 0, 0)
        self.outline = outline


        # Setup board and window
        self.board = [[random.randint(0, 1) for element in range(self.element_count)] for row in range(self.row_count)]
        self.SetSize(self.element_count * self.cell_size + 50, self.row_count * self.cell_size + 50)
        self.BackgroundColour = self.dead_colour

        self.on_tick()


    # This function will be called on each tick
    def on_tick(self):
        self.update()
        self.Refresh()
        wx.CallLater(self.update_time, self.on_tick)


    # Renders the board data to the window
    def render(self, event):  
        dc = wx.PaintDC(self)
        
        if not self.outline:
            dc.SetPen(wx.TRANSPARENT_PEN)
        
        brush = wx.Brush(self.alive_colour)
        dc.SetBrush(brush)

        for row_pos in range(len(self.board)):
            for element_pos in range(len(self.board[0])):
                
                # Alive
                if self.board[row_pos][element_pos]:
                    dc.DrawRectangle(self.cell_size * element_pos, self.cell_size * row_pos, self.cell_size, self.cell_size)
    

    # Update the board data
    def update(self):
        for row_pos in range(len(self.board)):
            for element_pos in range(len(self.board[0])):
                
                alive_count = self.get_alive_neighbour_count(row_pos, element_pos)
                alive = self.board[row_pos][element_pos]
                
                # Underpopulation
                if alive_count < 2 and alive:
                    self.board[row_pos][element_pos] = 0

                # Overpopulation
                elif alive_count > 3 and alive:
                    self.board[row_pos][element_pos] = 0

                # Reproduction
                elif alive_count == 3 and not alive:
                    self.board[row_pos][element_pos] = 1


    # Gets number of alive neighbours (kinda obvious)
    def get_alive_neighbour_count(self, row_pos, element_pos):
        count = 0

        for row_off in range(-1, 2):
            for elem_off in range(-1, 2):

                new_row = row_pos + row_off
                new_elem = element_pos + elem_off

                # As to not count itself
                if (row_off == 0 and elem_off == 0) or (new_row < 0 or new_elem < 0):
                    pass
                
                # Ready to count neighbours
                else:
                    try:
                        if self.board[new_row][new_elem] == 1:
                            count += 1
                    except IndexError:
                        pass
        return count
