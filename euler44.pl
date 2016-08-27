#!/usr/bin/perl

use warnings;
use strict;

my @p;
my %ph;

my $max = 10000;

for (my $i = 1; $i < $max; ++$i) {
  $p[$i] = $i * (3 * $i - 1)/2;
  $ph{$p[$i]} = $i;
}

my $leastdiff = 9999999;

for (my $i = 1; $i < $max; ++$i) {
  for (my $j = 1; $j < $i; ++$j) {
    my $sp = $p[$i] + $p[$j];
    if ($ph{$sp}) {
      my $dp = $p[$i] - $p[$j];
      if ($ph{$dp}) {
        print "P_$i = $p[$i], P_$j = $p[$j], sum = $sp (P_$ph{$sp}), diff = $dp (P_$ph{$dp})\n";
        $leastdiff = $dp if ($dp < $leastdiff);
      }
    }
  }
}

print "$leastdiff\n";
