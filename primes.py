#!/usr/bin/python

import math

PRIMES = [
  2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
  83, 89, 97
]
PRIMES_SET = set(PRIMES)
PRIMES_TO = 100

def generatePrimesTo(n):
  global PRIMES_TO
  # Only try values equal to 1 or 5 mod 6
  start = (PRIMES_TO + 1) - (PRIMES_TO + 1) % 6
  for v_start in xrange(start, n + 1, 6):
    for v in (v_start + 1, v_start + 5):
      if v > PRIMES_TO and v <= n:
        isPrime = True
        maxDivisor = int(math.sqrt(v))
        for testDivisor in (p for p in PRIMES if p <= maxDivisor):
          if v % testDivisor == 0:
            isPrime = False
            break
        if isPrime:
          PRIMES.append(v)
          PRIMES_SET.add(v)
  PRIMES_TO = n

def primesBelow(n):
  if n > PRIMES_TO:
    generatePrimesTo(n)
  return (p for p in PRIMES if p <= n)

def isPrime(n):
  if n > PRIMES_TO:
    generatePrimesTo(n)
  return n in PRIMES_SET
