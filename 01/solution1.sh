#!/bin/bash
echo "run this in terminal"
cat <<EOF
< input.txt perl -ne 'BEGIN{$prev = 3500};chomp;print $prev." ";if($prev < $_){print "is less"}else{print "is more"}print " than $_\n";$prev=$_' | grep less | wc -l
EOF
