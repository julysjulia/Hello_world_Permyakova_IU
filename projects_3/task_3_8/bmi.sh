#!/bin/bash

read -p "Вес:" WEIGHT
read -p "Рост:" HEIGHT

result=$($WEIGHT / ($HEIGHT * $HEIGHT))

echo "Ваш ИМТ: $result"
