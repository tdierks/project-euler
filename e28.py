#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import sys
from itertools import *
import math
import operator

# sum of the numbers on the diagonals of an n x n spiral, each cell being numbered
# in an outward spiral from the center, then moving right
# work outward accumulating diagonal items from each new row, starting with 1x1, then 3x3
#  first value in a row will always be the first below the top-left corner, with value (i-2)^2 + 1
#  so diagonal values will be that value + i-2, …+(i-1), …+(i-1), and +(i-1), so
#  (i-2)^2 + (i-1)*[1…4]
# (1x1 is magic:1)
# (3x3 adds 1+2*[1…4] = 3, 5, 7, 9)
# (5x5 adds 9+4*[1…4] = 13, 17, 21, 25)
#
# Non-iterative form:
#  for i odd and > 1:
#    diagonals are 4*(i-2)^2+(i-1)+2*(i-1)+3*(i-1)+4*(i-1)
#    = 4*(i^2-4i+4)+i-1+2i-2+3i-3+4i-4
#    = 4i*2-16i+16+10i-10
#    = 4i*2-6i+6
# Thus:
#  1x1 = 1
#  3x3 = 24
#  5x5 = 76
#  sum = 101

def euler28(n):
  total = 1
  for i in xrange(3, n+1, 2):
    total += 4*i*i - 6*i + 6
  return total

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
      parser = argparse.ArgumentParser(description='Euler problem 28.')
      parser.add_argument('--debug', action='store_true')
      parser.add_argument('--n', default=1001, type=long)
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    total = euler28(args.n)
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
