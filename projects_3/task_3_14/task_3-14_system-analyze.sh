#!/bin/bash

df -h | awk 'NR > 1 {print $1, $5}' 
df -h | awk '{if ($5 > 90)
		 print "WARNING"}'
