#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator

# to start us off
primes = [2, 3, 5, 7, 11, 13, 17, 19]
primeSet = set(primes)

def seedPrimes(upTo):
  for i in xrange(primes[-1]+2, upTo, 2):
    isPrime = True
    limit = int(math.sqrt(i))
    for j in primes:
      if j > limit:
        break
      if i % j == 0:
        isPrime = False
        break
    if isPrime:
      primes.append(i)
      primeSet.add(i)

def isPrime(n):
  if n in primeSet:
    return True
  for i in primes:
    if n % i == 0:
      return False
  primeSet.add(i)
  return True

def rotations(n):
  s = str(n)
  for i in range(len(s)):
    yield int(s[i:] + s[:i])

def euler35(n):
  """A 'circular' prime is any number where all rotations of the digits are prime.
     Return all circular primes below n."""
  seedPrimes(int(math.sqrt(n)))
  circCount = 0
  for i in xrange(2, n):
    isCircPrime = True
    for ir in rotations(i):
      if not isPrime(ir):
        isCircPrime = False
        break
    if isCircPrime:
      circCount += 1
  return circCount

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
      parser = argparse.ArgumentParser(description='Euler problem 35.')
      parser.add_argument('--debug', action='store_true')
      parser.add_argument('--n', default=100, type=long)
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    total = euler35(args.n)
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
