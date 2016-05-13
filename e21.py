#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator

def divisor_sum(i):
  # prepopulate 1 so we don't generate i
  divisors = set([1])
  for factor in xrange(2, int(math.sqrt(i)+1)):
    if i % factor == 0:
      divisors.add(factor)
      divisors.add(i/factor)
  return sum(divisors)

def get_dsi(i, ds):
  if i not in ds:
    ds[i] = divisor_sum(i)
  return ds[i]

def euler21(largest):
  divisor_sums = {}
  total = 0
  for i in xrange(2, largest+1):
    dsi = get_dsi(i, divisor_sums)
    ic = get_dsi(dsi, divisor_sums)
    if i == ic and i != dsi:
      debug("{} {}", i, dsi)
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
      parser.add_argument('--max', default=10000, type=long)
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    total = euler21(args.max)
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
