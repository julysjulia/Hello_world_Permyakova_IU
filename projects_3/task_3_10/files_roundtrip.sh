#!/bin/bash

for ((i=1; i<=10;i++)) do
	touch test${i}.txt
done
count=10
while [$count -ge 1]; do
	rm  'test{$i}.txt'
done
