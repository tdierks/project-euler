#!/usr/bin/python

import argparse
import sys
from itertools import *
import math
import operator
import re

ROMAN = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000,
}
for prefix in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
  ROMAN[prefix] = ROMAN[prefix[1]] - ROMAN[prefix[0]]
ROMAN_BY_VALUE = sorted(ROMAN.iteritems(), key=lambda i:i[1], reverse=True)
ROMAN_RE = re.compile("|".join(sorted(ROMAN.iterkeys(), key=lambda s:ROMAN[s], reverse=True)), re.IGNORECASE)

def makeRoman(n):
  s = ""
  while n > 0:
    places = math.floor(math.log10(n))
    topPlace = (n / 10 ** places) * 10 ** places
    for (valueStr, value) in ROMAN_BY_VALUE:
      if value <= topPlace:
        s += valueStr
        n -= value
        break
  return s

def parseRoman(s):
  return sum(ROMAN[c] for c in ROMAN_RE.findall(s))

def euler89(numerals):
  saved = 0
  for s in numerals:
    min = makeRoman(parseRoman(s))
    saved += len(s) - len(min)
  return saved

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
      parser = argparse.ArgumentParser(description='Euler problem 89.')
      parser.add_argument('--debug', action='store_true')
      parser.add_argument('--input', default="e89/roman.txt", type=argparse.FileType('r'))
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    global debug
    if args.debug:
      debug = debug_out
    
    total = euler89(line.strip() for line in args.input if line.strip())
    print total
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
