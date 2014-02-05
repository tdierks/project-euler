#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator

def euler81(matrix):
  """Given an input matrix (array of MxN integers), find the path from top-left to
     bottom-right with a minimal sum. Return that sum"""
  # dict from (x,y) to (cost, (cell_list))
  paths = {}
  paths[(-1,0)] = paths[(0, -1)] = ( 0, [] )
  
  for y in range(len(matrix)):
    for x in range(len(matrix[y])):
      try:
        left = paths[(x-1, y)]
      except KeyError:
        left = (99999999, [])
      try:
        above = paths[(x, y-1)]
      except KeyError:
        above = (99999999, [])
      cheaper = min(left, above, key = lambda x: x[0])
      paths[(x,y)] = (cheaper[0] + matrix[x][y], cheaper[1][:] + [(x,y)])
  debug("{}", paths[(len(matrix[0])-1, len(matrix)-1)][1])
  return paths[(len(matrix[0])-1, len(matrix)-1)][0]

def debug_out(s, *args, **kwargs):
  print s.format(*args, **kwargs)

def debug_noop(s, *args, **kwargs):
  pass

debug = debug_noop

class Usage(Exception):
  def __init__(self, msg):
    self.msg = msg

def main(argv=None):
  if argv is None:
    argv = sys.argv
  try:
    try:
      parser = argparse.ArgumentParser(description='Euler problem 81.')
      parser.add_argument('--debug', action='store_true')
      parser.add_argument('--matrix', default='e81/matrix.txt', type=argparse.FileType('r'))
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    matrix = []
    for line in args.matrix:
      line = line.strip()
      matrix.append([int(v) for v in line.split(",")])
    
    total = euler81(matrix)
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
