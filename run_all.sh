#!/usr/bin/env bash
set -e

echo "========================================="
echo " Billboard + Spotify workflow"
echo " Using Snakemake"
echo "========================================="

# (Optional) activate conda or virtualenv here if you have one, e.g.:
# source ~/miniconda3/etc/profile.d/conda.sh
# conda activate billboard-env

# Run the Snakemake workflow
snakemake --cores 1
