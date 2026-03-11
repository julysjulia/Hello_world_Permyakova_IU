#!/bin/bash

read -p "Вес:" WEIGHT
read -p "Рост:" HEIGHT

result=$((WEIGHT/(HEIGHT**2)))

echo "Ваш ИМТ: $result"

