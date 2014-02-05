#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator
from fractions import Fraction

def e_seq():
  """ yield 2,  1, 2, 1,  1, 4, 1,  1, 6, 1, ... """
  yield 2;
  for n in count(2, 2):
    yield 1
    yield n
    yield 1

def euler65(n):
  """Return the sum of the digits in the numerator of the nth convergent term
     in the continued fraction for e"""
  revFrac = reversed(list(islice(e_seq(), n)))
  f = Fraction(revFrac.next())
  for v in revFrac:
    f = v + 1/f
  debug("Convergent term {} is {}", n, f)
  return sum(int(c) for c in str(f.numerator))

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
      parser = argparse.ArgumentParser(description='Euler problem 64.')
      parser.add_argument('--debug', action='store_true')
      parser.add_argument('--n', default=10, type=long)
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    total = euler65(args.n)
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
