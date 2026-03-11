#!/bin/bash

read name_gene
read level

if ["$#" -ne  2];then 
echo "Недостаточно входящих данных"
echo "Экспрессия гена $name_gene  составляет $level  единиц"
