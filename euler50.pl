#/usr/bin/perl

use warnings;
use strict;

sub primes($) {
  my $max = shift;
  my @sieve = (0, 1) x (($max + 1) / 2);
  my @p = (2);
  for (my $i = 3; $i <= $max; ++$i) {
    if ($sieve[$i]) {
      push @p, $i;
      for (my $j = 2*$i; $j <= $max; $j += $i) {
        $sieve[$j] = 0;
      }
    }
  }
  return @p;
}

my $max = 1000000;
my @p = primes($max);
my %ph = map(($_, 1), @p);
my @max = (0);

for (my $i = 0; $i < scalar(@p); ++$i) {
  my $t = 0;
  for (my $j = $i; $j < scalar(@p); ++$j) {
    $t += $p[$j];
    last if ($t > $max);
    if ($ph{$t}) {
      if ($max[0] < ($j - $i + 1)) {
        $max[0] = $j - $i + 1;
        $max[1] = $t;
        $max[2] = $i;
      }
    }
  }
}

print $max[1], " = ", join(" + ", @p[$max[2]..($max[2]+$max[0]-1)]), " ($max[0])\n";
