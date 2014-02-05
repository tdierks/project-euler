#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator

month_lengths = {
  False: [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
}
# leap years
month_lengths[True] = month_lengths[False][:]
month_lengths[True][1] += 1

def isLeap(year):
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def euler19():
  year = 1901
  start_day = 0 # day of week of 1/1/start_year, 0 = Monday
  end_year = 2000
  
  mondays = 0
  while year <= end_year:
    for days in month_lengths[isLeap(year)]:
      if start_day == 0:
        mondays += 1
      start_day = (start_day + days) % 7
    year += 1
  
  return mondays
  
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
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    total = euler19()
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
