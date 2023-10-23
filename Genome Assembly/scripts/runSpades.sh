#!/usr/bin/env bash
# runSpades.sh

mkdir -p "../results/rhodo/"

function Spades {
    spades.py \
    -1 ../data/trimmed/Rhodo.R1.paired.fastq \
    -2 ../data/trimmed/Rhodo.R2.paired.fastq \
    -o rhodo
}

Spades # runs the function Spades
