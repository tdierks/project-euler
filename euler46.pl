#/usr/bin/perl

use warnings;
use strict;

sub primes_set($) {
  my $max = shift;
  my @sieve = (0, 1) x (($max + 1) / 2);
  my %is_prime;
  for (my $i = 3; $i <= $max; ++$i) {
    if ($sieve[$i]) {
      $is_prime{$i} = 1;
      for (my $j = 2*$i; $j <= $max; $j += $i) {
        $sieve[$j] = 0;
      }
    }
  }
  return \%is_prime;
}

my $max = 10000;
my $p = primes_set($max);
my @squares = map $_*$_, 0..(int(sqrt($max/2)));

S: for (my $i = 9; $i < $max; $i += 2) {
  next if ${$p}{$i};
  for (my $s = 1; 2*$squares[$s] < $i; ++$s) {
    next S if (${$p}{$i - 2*$squares[$s]});
  }
  die $i;
}
