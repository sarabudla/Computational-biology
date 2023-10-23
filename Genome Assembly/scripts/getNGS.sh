#!/usr/bin/env bash
# getNGS.sh

# Retrieve the Rhodobacter spheroides NGS reads.
fasterq-dump SRR522244 --split-3 -O ../data/
