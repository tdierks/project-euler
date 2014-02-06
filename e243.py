#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator
from fractions import Fraction
import primes

def euler243(limit):
  """Find the smallest d such that the number of irreducible fractions v/d for
     v = 1..d-1, divided by d-1 is less than n; e.g. d=12 has 4 irreducible,
     so would result in 4/11."""
  # Since an irreducible fraction is one where the greatest common divisor of
  # numerator and denominator is 1, this is the same as Euler's phi function
  # (or the totient), phi(d)/(d-1). So, find the smallest d such that phi(d)/(d-1)
  # is less than limit.
  # phi(n) = n * (1 - 1/p) for each unique prime factor of p.
  # So this is smallest when there are many unique prime factors and they are as
  # small as possible. However, it's not as simple as multiplying small primes
  # together, thanks to the (d-1) divisor: phi(6)/6 = phi(12)/12 = 1/3, but
  # phi(6)/5 = 2/5 > phi(12)/11 = 4/11, so for n = 4/10, 12 is the right answer,
  # not the value 30 that we'd get by calculating the product of distinct small primes
  # alone.
  
  # So what we want to do is: presuming that the right value is A * B, where A
  # is the product of a sequence of the primes 2...p, and B is a fairly small
  # multiple of small prime factors, which is less than the next prime beyond p.
  
  some_primes = list(primes.primesBelow(100))
  some_factors = [c for c in xrange(1,100)]
  
  for i in range(2, len(some_primes) - 1):
    primes_so_far = some_primes[:i]
#    debug("{} {}", i, primes_so_far)
    for c in some_factors:
      if c < some_primes[i]:
        n = reduce(operator.mul, primes_so_far, 1) * c
        phi = n * reduce(operator.mul, (1.0 - 1.0/p for p in primes_so_far))
        f = phi/float(n-1)
        debug("{} = {} * {}: {}", n, n/c, c, f)
        if f < limit:
          return n

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
      parser = argparse.ArgumentParser(description='Euler problem 243.')
      parser.add_argument('--debug', action='store_true')
      parser.add_argument('--n', default='15499/94744', type=Fraction)
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    total = euler243(float(args.n))
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
