#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator

def euler38():
  biggerest = 0
  for digits in permutations(range(1, 9)):
    dStr = '9' + str(reduce(lambda a, b: 10*a + b, digits))
    for initialLen in range(1,5):
      initialVal = int(dStr[:initialLen])
      remStr = dStr[initialLen:]
      for i in count(2):
        nextVal = initialVal * i
        if remStr.startswith(str(nextVal)):
          remStr = remStr[len(str(nextVal)):]
          if not remStr:
            debug(" : {}", dStr)
            if int(dStr) > biggerest:
              biggerest = int(dStr)
            break
        else:
          break
  return biggerest

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
      parser = argparse.ArgumentParser(description='Euler problem 38.')
      parser.add_argument('--debug', action='store_true')
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    total = euler38()
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
