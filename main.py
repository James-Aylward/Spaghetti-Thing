# Written by James Aylward #

import wx
from SimulationWindow import *

def main():

    while True:           
        try:
            update_time = int(input("Update time (ms): "))
            row_count = int(input("Row count:"))
            element_count = int(input("Column count:"))
            outline = int(input("Outline (1 or 0):"))
            cell_size = int(input("Cell size: "))

        except ValueError:
            print("\nWrong value types entered\n")
        
        else:
            break

    app = wx.App()
    simulationWindow = SimulationWindow(row_count, element_count, cell_size, update_time, outline) 
    simulationWindow.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()