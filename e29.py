#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator

def euler29(n):
  values = set()
  for a in xrange(2, n+1):
    for b in xrange(2, n+1):
      values.add(a**b)
  return len(values)

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
      parser = argparse.ArgumentParser(description='Euler problem 29.')
      parser.add_argument('--debug', action='store_true')
      parser.add_argument('--n', default=100, type=long)
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    total = euler29(args.n)
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
