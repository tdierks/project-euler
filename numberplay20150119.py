#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator
from primes import primesBelow
from collections import *

def numberplay20150119(limit):
  ps = set(primesBelow(limit))
  sqs = list(takewhile(lambda x2: x2 <= limit, imap(lambda x: x*x, count(1))))
  decomp = defaultdict(set)
  for sq in sqs:
    for p in ps:
      if sq - p in ps:
        decomp[sq].add(p)
  
  def findLoop(bags, used):
    p = bags[-1]
    for sq in sqs:
      p2 = sq - p
      if p2 in ps and (p2 not in used or p2 == bags[0]):
        if p2 == bags[0]:
          if len(bags) > 4:
            return bags
        else:
          bags.append(p2)
          used.add(p2)
          r = findLoop(bags, used)
          if r:
            return r
          else:
            bags.pop()
            used.remove(p2)
    return False
  
  for p in ps:
    bags = [p]
    used = set(bags)
    return findLoop(bags, used)

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
      parser = argparse.ArgumentParser(description='http://wordplay.blogs.nytimes.com/2015/01/19/recaman/')
      parser.add_argument('--debug', action='store_true')
      parser.add_argument('--n', default=100, type=long)
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    bags = numberplay20150119(args.n)
    print "{} bags with {} marbles".format(len(bags), sum(bags))
    print "bags: {}".format(",".join([str(v) for v in bags]))
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
