#!/usr/bin/python

import argparse
import sys
import math
from decimal import Decimal

def binomial(i, j):
  """ith entry in binomial expansion of j"""
  return math.factorial(j)/(math.factorial(i)*math.factorial(j-i))

def minHeads(f, flips, goal):
  """Return the minimum # of heads that must be gotten in flips to reach a
     particular goal while gambling fraction f of your capital on each flip"""
  for i in xrange(flips+1):
    try:
      v = Decimal(1 + 2*f)**i * Decimal(1 - f)**(flips-i)
      if v >= goal:
        return i
    except:
      print "Died on f={}, i={}".format(f,i)
      raise
  return None

def searchForF(flips, goal, min=0.0, max=1.0):
  """Find the f that minimizes minHeads between min & max"""
  best = flips+1
  bestF = min
  bestCount = 0
  
  tests = 50
  step = (max-min)/(tests-1)
  
  for n in range(tests):
    testF = min + n * step
    heads = minHeads(testF, flips, goal)
#     print "{}: {}".format(testF, heads)
    if heads == None:
      continue
    if heads == best:
      bestCount += 1
    elif heads < best:
      best = heads
      bestF = testF
      bestCount = 1
  
  if bestCount > 1:
    return (bestF, best)
  else:
    return searchForF(flips, goal, bestF-step, bestF+step)

def euler267(flips, goal):
  """Calculate the chance, f, to maximize the chance of turning $1 into
     $goal after a certain number of flips of a fair coin where you bet
     1/f of your capital on each flip with a 2:1 return if it comes up heads.
     http://projecteuler.net/problem=267"""
  
  # In the binomial expansion of 1000 flips, the ith entry is the chance
  # of getting i tails and (1000-i) heads (or vice-versa). (Where chance
  # is the number of occurrences out of 2^1000 possible outcomes.)
  # Your overall winnings are: (1+f)^heads * (1-f)^tails
  # So, for example, if you flipped 3 heads and 2 tails in 5 flips
  # with f = 1/4, you would win (3/2)^3 * (3/4)^2 = 243/128 of your initial
  # stake. Note that this is order-independent.
  #
  # Thus, for any particular f, the chance you'll win $goal starting with $1 is:
  # find the smallest number of heads, H, for which the above is greater than $goal,
  # and sum the binomial expansion for heads = 0..H.
  # 
  # Maximize f by recursively searching in (0,1)
  (f, heads) = searchForF(flips, goal)
    
  # sum up binomial expansion
  goodOutcomes = sum(binomial(i, flips) for i in xrange(heads, flips+1))
  
  # print value
  print "chances is maximized with f = {}, needing {} heads\nChance is {}/{}\nor {:.12f}".format(
    f, heads, goodOutcomes, 2**flips, float(goodOutcomes)/2**flips)

class Usage(Exception):
  def __init__(self, msg):
    self.msg = msg

def main(argv=None):
  if argv is None:
    argv = sys.argv
  try:
    try:
      parser = argparse.ArgumentParser(description='Euler problem 267.')
      parser.add_argument('--flips', default=1000, type=int)
      parser.add_argument('--goal', default=1e9, type=float)
      args = parser.parse_args()
    except ArgumentError, msg:
      raise Usage(msg)
    
    euler267(args.flips, args.goal)
    
    
  except Usage, err:
    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"
    return 2

if __name__ == "__main__":
    sys.exit(main())
