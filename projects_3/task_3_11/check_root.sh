#!/bin/bash

check_root() {
	if  ["$EUID" -ne 0]; then
		echo 'Ошибка'
		exit 1
	fi
}
