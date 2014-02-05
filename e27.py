#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator

import primes

def euler27():
  """Find the coefficients for f(n) = n^2 + an + b for -1000 < a < 1000 and -1000 < b < 1000
     that produces primes for n = 0 through n = m for the largest m."""
  # for n = 0, f(n) = b, so b must be an odd prime.
  # for n = 1, f(n) = 1 + a + b, so a must be odd and no smaller than -(b-2)
  #  (possible exceptions for f(n) = 2 are not possible with n > 1)
  
  best_n = -1
  
  for b in primes.primesBelow(1000):
    for a in xrange(-(b-2), 1000, 2):
      for n in count():
        if not primes.isPrime(n * n + a * n + b):
          break
      if best_n < n-1:
        best_n = n-1
        best_a = a
        best_b = b
        debug("{} primes produced by a = {}, b = {}", n, a, b)
  
  return best_a * best_b

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
      parser = argparse.ArgumentParser(description='Euler problem 27.')
      parser.add_argument('--debug', action='store_true')
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    total = euler27()
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
