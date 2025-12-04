#!/usr/bin/env perl

use strict;
use warnings;

my @input;
while (<>) {
    if (/^([-+]?[0-9]+)/) {
        push @input, $1;
    }
}
printf "read %d numbers\n", scalar @input;

my $total = 0;
my $round = 0;
my %seen;
ROUND: for (;;) {
    $round++;
    for my $num (@input) {
        $total += $num;
        last ROUND if ++$seen{$total} >= 2;
    }
    printf "total is %d after round %d\n", $total, $round;
}
printf "reached %d twice in round %d\n", $total, $round;
