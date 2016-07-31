#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator

def euler36(n):
  total = 0
  # check odd numbers 1..n; has to be odd because last binary digit can't be 0
  for i in xrange(1, n, 2):
    if str(i) == "".join(reversed(str(i))) and bin(i)[2:] == "".join(reversed(bin(i)[2:])):
      total += i
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
      parser = argparse.ArgumentParser(description='Euler problem 36.')
      parser.add_argument('--debug', action='store_true')
      parser.add_argument('--n', default=1000000, type=long)
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    total = euler36(args.n)
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
