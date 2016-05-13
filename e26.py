#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator

# calculate the number 1/m where m < n which has the longest repeating part of its fraction
# technique: long division. Track remainder as dividing by n, populating a dict with
# remainder -> decimal position; return [current] - [reposed] when we hit a loop.
# ex. 1/6 -> 1: 10/6 = 1r4, rem[4] = 1; 2: 40/6 = 6r4 rem[4] is populated, loop = 2-1 = 1
#  1/7 -> 1: 10/7 = 1r3, rem[3] = 1; 2: 30/7 = 4r2, rem[2] = 2; 3: 20/7 = 2r6, rem[6] = 3;
#    4: 60/7 = 8r4, rem[4] = 4; 5: 40/7 = 5r5, rem[5] = 5; 6: 50/7 = 7r1, rem[1] = 6;
#    7: 10/7 = 1r3, rem[3] is populated w/1, loop = 7-1 = 6

def repeat_size(i):
  rems = {}
  num = 1
  pos = 0
  while True:
    rem = num * 10 % i
    if rem == 0:
      return 0 # terminating fraction
    if rem in rems:
      return pos - rems[rem]
    rems[rem] = pos
    num = rem
    pos += 1

def euler26(n):
  longest_len = 0
  longest_val = None
  for i in range(2, n):
    rep_size = repeat_size(i)
    if rep_size > longest_len:
      longest_len = rep_size
      longest_val = i
      debug("{}: {}", longest_val, longest_len)
  return longest_val    

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
      parser.add_argument('--n', default=1000, type=long)
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    total = euler26(args.n)
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
