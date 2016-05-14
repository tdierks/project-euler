#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator

def euler30():
  total = 0
  # since 9**5 * 6 = 354294, no number greater than that can possibly be a match
  return sum(i for i in xrange(2, 354294) if i == sum(d**5 for d in map(int, list(str(i)))))

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
      parser = argparse.ArgumentParser(description='Euler problem ___.')
      parser.add_argument('--debug', action='store_true')
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    total = euler30()
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
