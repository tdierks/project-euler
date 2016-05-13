#!/usr/local/python

# euler problem 500
# The number of divisors of 120 is 16.
# In fact 120 is the smallest number having 16 divisors.
# 
# Find the smallest number with 2^500500 divisors.
# Give your answer modulo 500500507.

# prime decomposition:
#  n has k factors if the prime factorization of n is:
#   n = a^a1 * b^b1 * c^c1...
#  then:
#   k = (a1 + 1) * (b1 + 1) * (c1 + 1) ...
#   (choose 0..a1 factors of a, 0..b1 factors of b, etc.)

# proposed method:
#  since the number of factors is a power of 2, it implies that each prime
#  must appear some number of times that is one less than a power of two.
#  We want to find the smallest such product, which implies that in evaluating
#  whether to add another prime factor, we want to consider the smallest option:
#  either add another new, unused prime factor (which will double the number of factors)
#  or advance some prior factor by from x to 2x + 1 (which will also double the number of
#  factors).
#
#  thus, we can iterate as follows:
#
#  s is a sorted set of non-prime factors available for multiplication.
#    each is stored as (value, prime, exponent); Starts empty.
#  p is our next unused prime (starts at 2)
#  i is the number of factor doublings we have generated (starts at 0)
#  n is the number which has 2^i factors (starts at 1)
#  2^t is the target number of factors
#
#  while i < t:
#    if there is an entry e in s with value smaller than p:
#      remove e from s
#    else
#      e = (p, p, 1)
#      advance p to next prime
#    n = n * e.value
#    insert (p^(e.exponent + 1), p, e.exponent * 2+1) into s
#    i = i + 1
#
#  For the problem as stated, keep n as n modulo the reduction for efficiency

# 2^1 -> 2^3 = * 2^2
# 2^3 -> 2^7 = * 2^4
# 2^7 -> 2^15 = * 2^8


#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator
import heapq

import primes

def euler500(t, m):
  exponents = {}
  s = []
  pi = primes.primesIterator()
  p = pi.next()
  i = 0
  n = 1
  while i < t:
    if s and s[0][0] < p:
      e = heapq.heappop(s)
    else:
      e = (p, p, 1)
      p = pi.next()
    n = (n * e[0]) % m
    heapq.heappush(s, (e[1]**(e[2] + 1), e[1], e[2] * 2 + 1))
    i += 1
    exponents[e[1]] = e[2]
#    debug("Step {}: n = {}, e.value = {}, p = {}, s = [{}]", i, n, e[0], p, ", ".join(("({}, {}, {})".format(x[0],x[1],x[2]) for x in s)))
#  debug("{} = {}", n, " * ".join("{}^{}".format(j, exponents[j]) for j in sorted(exponents.keys())))
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
      parser = argparse.ArgumentParser(description='Euler problem ___.')
      parser.add_argument('--debug', action='store_true')
      parser.add_argument('--exponent', default=500500, type=long)
      parser.add_argument('--modulo', default=500500507, type=long)
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    total = euler500(args.exponent, args.modulo)
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
