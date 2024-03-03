from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    a, b = Point(11, 300), Point(200, 55)
    maze = Maze(
        100, 100, 4, 6, 40, 40, win
    )
    
    maze.solve()
  
    win.wait_for_close()
    
main()