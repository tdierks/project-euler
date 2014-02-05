#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator

def euler15(n, m):
  """Number of distinct Manhattan paths from one side to the other of an n x m grid
     http://projecteuler.net/problem=15"""
  # You have to walk N + M blocks, of which N have to be horiz and M vertical.
  # The # of paths is the number of ways to arrange the N horiz blocks within
  # the N+M blocks walked: c(N+M, N) = (N+M)!/(N! * M!)
  return math.factorial(n+m)/(math.factorial(n) * math.factorial(m))

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
      parser = argparse.ArgumentParser(description='Euler problem 15.')
      parser.add_argument('--debug', action='store_true')
      parser.add_argument('--n', default=20, type=long)
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    total = euler15(args.n, args.n)
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
