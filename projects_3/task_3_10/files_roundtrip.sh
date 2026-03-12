#!/bin/bash

for ((i=1; i<=10;i++)) do
        touch test${i}.txt
done

for j in {10..1}; do
        while [ -e "test$j.txt" ]; do
                rm "test$j.txt"
        done
done
