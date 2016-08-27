#!/usr/bin/perl

use warnings;
use strict;

my $tiles = (shift or 1000000);
my $r = 0;

for (my $u = 2; $u <= $tiles/4; ++$u) {
  my $m = int(sqrt($u));
  for (my $i = 1; $i <= $m; ++$i) {
    if ($u % $i == 0) {
      if ($u/$i - $i >= 1) {
#       print "$i, ", $u/$i, " = $u\n";
        ++$r;
      }
    }
  }
}

print "$r\n";
