#!/bin/bash

awk 'BEGIN{FS=","} {print $2}' data.csv
awk 'BEGIN{FS=","} $3 > 20 {print $2}' data.csv
awk 'BEGIN{FS=","} {sum += $3} END {print sum}' data.csv
