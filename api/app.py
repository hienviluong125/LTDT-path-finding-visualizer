from flask import Flask, jsonify, request
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.finder.bi_a_star import BiAStarFinder
from pathfinding.finder.best_first import BestFirst
from pathfinding.finder.breadth_first import BreadthFirstFinder
from pathfinding.finder.dijkstra import DijkstraFinder
from pathfinding.finder.ida_star import IDAStarFinder

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def index():
  matrix = request.json['matrix']
  start_pos = request.json['start']
  end_pos = request.json['end']
  finder_name = request.json['finder']
  is_diagonal = request.json['isDiagonal']

  grid = Grid(matrix=matrix)

  start = grid.node(start_pos[0], start_pos[1])
  end = grid.node(end_pos[0], end_pos[1])

  diagonal_movement = DiagonalMovement.always if is_diagonal else DiagonalMovement.never

  finder = None

  if finder_name == 'a_star':
    print("FINDER => ")
    print('a_star')
    finder = AStarFinder(diagonal_movement=diagonal_movement)
  elif finder_name == 'breadth_first':
    print("FINDER => ")
    print('breadth_first')
    finder = BreadthFirstFinder(diagonal_movement=diagonal_movement)
  elif finder_name == 'bi_a_star':
    print("FINDER => ")
    print('bi_a_star')
    finder = BiAStarFinder(diagonal_movement=diagonal_movement)
  elif finder_name == 'best_first':
    print("FINDER => ")
    print('best_first')
    finder = BestFirst(diagonal_movement=diagonal_movement)
  elif finder_name == 'dijkstra':
    print("FINDER => ")
    print('dijkstra')
    finder = DijkstraFinder(diagonal_movement=diagonal_movement)
  elif finder_name == 'ida_star':
    print("FINDER => ")
    print('ida_star')
    finder = IDAStarFinder(diagonal_movement=diagonal_movement)

  path, runs = finder.find_path(start, end, grid)
  return jsonify({"path": path, "steps": len(path), "finder_name": finder_name})
