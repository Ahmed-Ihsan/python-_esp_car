from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
import draw_imag
import time

def get_path():
  while 1:
    matrix = [
    [1, 1, 1,1, 1, 1,1, 1, 1,1],
    [1, 1, 1,1, 1, 1,1, 1, 1,1],
    [1, 1, 1,1, 1, 1,1, 1, 1,1],
    [1, 1, 1,1, 1, 1,1, 1, 1,1],
    [1, 1, 1,1, 1, 1,1, 1, 1,1],
    [1, 1, 1,1, 1, 1,1, 1, 1,1],
    [1, 1, 1,1, 1, 1,1, 1, 1,1],
    [1, 1, 1,1, 1, 1,1, 1, 1,1],
    [1, 1, 1,1, 1, 1,1, 1, 1,1]
    ]
    try: 
      pos = draw_imag.creat()
      matrix[pos[0][0]][pos[0][1]] = 0
      grid = Grid(matrix=matrix)
      start = grid.node(pos[1][0],pos[1][1])
      end = grid.node(pos[2][0],pos[2][1])

      finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
      path, runs = finder.find_path(start, end, grid)

      print('operations:', runs, 'path length:', len(path))
      print(grid.grid_str(path=path, start=start, end=end))
      # print(path)
    except:
      continue
    time.sleep(1)
    return path ,pos
  
if __name__ == "__main__":
    get_path()