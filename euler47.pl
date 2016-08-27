#/usr/bin/perl

use warnings;
use strict;

sub nondup_prime_factors($) {
  my $max = shift;
  my @s;
  my %is_prime;
  for (my $i = 2; $i <= $max; ++$i) {
    if (!defined($s[$i])) {
      for (my $j = $i; $j <= $max; $j += $i) {
        $s[$j] = [] unless (defined($s[$j]));
        push @{$s[$j]}, $i;
      }
    }
  }
  return @s;
}

my $max = 1000000;
my @f = nondup_prime_factors($max);
my $g = 4;

my $min = 0;
my $cont = 0;

for (my $i = 2; $i < $max; ++$i) {
  $min = $i if ($cont == 0);
  if (scalar(@{$f[$i]}) == $g) {
    ++$cont;
  } else {
    $cont = 0;
  }
  if ($cont == $g) {
    for (my $j = $min; $j < $min + $g; ++$j) {
      print "$j: ", join(", ", @{$f[$j]}), "\n";
    }
    exit;
  }
}
