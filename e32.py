#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator

def euler32():
  """Find all unique products where A * B = C and the digits of A, B, and C cover 1...9
     Return the sum of all such unique products C."""
  
  # All such values have a one-digit A, a 4-digit B, and a 4-digit C or a two-digit A,
  # 3-digit B, and 4-digit C.
  
  products = set()
  checked = 0
  digits = range(1,10)
  for aLen, bLen in ( (1, 4), (2, 3) ):
    for aDigits in permutations(digits, aLen):
      a = reduce(lambda a, b: 10*a + b, aDigits, 0)
      for bDigits in permutations((d for d in digits if d not in aDigits), bLen):
        b = reduce(lambda a, b: 10*a + b, bDigits, 0)
        c = a * b
        cStr = str(c)
        checked += 1
        if len(cStr) + len(aDigits) + len(bDigits) == 9 and '0' not in cStr:
          checkDigits = set(int(d) for d in cStr)
          checkDigits.update(aDigits, bDigits)
          if len(checkDigits) == 9:
            debug("{} x {} = {}", a, b, c)
            products.add(c)
  debug("Checked {} combinations", checked)
  return sum(products)

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
      parser = argparse.ArgumentParser(description='Euler problem 32.')
      parser.add_argument('--debug', action='store_true')
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    total = euler32()
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
