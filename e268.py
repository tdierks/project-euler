#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator

smallPrimes = [
  2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
  83, 89, 97
];

def euler268(cap, primeMax, count):
  primes = [i for i in smallPrimes if i < primeMax]
  total = 0
  
  for p in combinations(primes, count):
    factor = reduce(operator.mul, p, 1)
    possible = (cap-1) / factor
    debug("primes = {}, factor = {}, possible = {}", p, factor, possible)
    exclude = 1.0
    for sp in primes:
      if sp not in p and sp < p[-1]:
        debug(" excluding {}", sp)
        exclude *= (1.0 - 1.0/sp)
    
    debug(" total exclusion: {}", exclude)
    debug(" adding: {}", int(math.ceil(possible * exclude)))
    total += int(math.ceil(possible * exclude))

  return total

def preciseEuler268(cap, primeMax, count):
  primes = [i for i in smallPrimes if i < primeMax]
  included = set()
  
  for p in combinations(primes, count):
    factor = reduce(operator.mul, p, 1)
    for v in xrange(factor, cap, factor):
      included.add(v)
  
  return len(included)

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
      parser = argparse.ArgumentParser(description='Euler problem 267.')
      parser.add_argument('--cap', default=1000, type=long)
      parser.add_argument('--primeCap', default=100, type=int)
      parser.add_argument('--count', default=4, type=int)
      parser.add_argument('--debug', action='store_true')
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    if args.primeCap > 100:
      raise InputError(args.primeCap, "primeCap can't be over 100, sorry")
  

    total = euler268(args.cap, args.primeCap, args.count)
    print total

    totalP = preciseEuler268(args.cap, args.primeCap, args.count)
    print totalP

    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
