import sys, os, random, pygame
from solution import *
diag_sudoku_grid='..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
diag_sudoku_grid='5.9.2..1.4...56...8..9.3..5.87..25..654....82..15684971.82.5...7..68...3.4..7.8..'
diagonal_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

values=grid_values(diagonal_grid)

#values=eliminate(values)
#values=only_choice(values)
#display(values)
#twins = [box for box in values.keys() if len(values[box]) == 2]
#print(twins)
#for box in twins:
#    digit = values[box]
#    for peer in peers[box]:
#       if values[peer]==digit:
#            common_peers=set(peers[box]) & set(peers[peer])
#            #print(common_peers)
#            for b in common_peers:
#                for d in digit:
#                    values[b].replace(d,'')

values=solve(diagonal_grid)
display(values)

