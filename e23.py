#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator
from e21 import divisor_sum

def euler23(through):
  abundance = set()
  for i in xrange(2, through):
    if divisor_sum(i) > i:
      abundance.add(i)
  abundant_sorted = sorted(abundance)
  total = 0
  for i in xrange(1, through):
    canWrite = False
    for j in takewhile(lambda n: n < i, abundant_sorted):
      if i - j in abundance:
        canWrite = True
        break
    if not canWrite:
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
      parser = argparse.ArgumentParser(description='Euler problem ___.')
      parser.add_argument('--debug', action='store_true')
      parser.add_argument('--n', default=28123, type=long)
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    total = euler23(args.n)
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
