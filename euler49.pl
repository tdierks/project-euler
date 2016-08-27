#/usr/bin/perl

use warnings;
use strict;

sub primes_vector($) {
  my $max = shift;
  my @sieve = (0, 1) x (($max + 1) / 2);
  $sieve[1] = 0;
  $sieve[2] = 1;
  for (my $i = 3; $i <= $max; ++$i) {
    if ($sieve[$i]) {
      for (my $j = 2*$i; $j <= $max; $j += $i) {
        $sieve[$j] = 0;
      }
    }
  }
  return @sieve;
}

sub sorted_digits($) {
  my @d = split //, shift;
  return join '', sort @d;
}

my @s = primes_vector(9999);
my @sd;

for (my $f = 1001; $f < 9999; ++$f) {
  $sd[$f] = sorted_digits($f) if ($s[$f]);
}

for (my $f = 1001; $f < 9997; ++$f) {
  if ($s[$f]) {
    my $fd = sorted_digits($f);
    for (my $i = 2; $i < (9999-$f) / 2; $i += 2) {
      my $ff = $f + $i;
      next unless ($s[$ff] and $sd[$f] eq $sd[$ff]);
      my $fff = $ff + $i;
      next unless ($s[$fff] and $sd[$f] eq $sd[$fff]);
      print "$f $ff $fff\n";
    }
  }
}
