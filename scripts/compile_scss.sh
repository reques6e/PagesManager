#!/bin/bash

# Выполнение команды sassc
sassc web/ui/static/scss/login.scss web/ui/static/css/login.css

if [ $? -eq 0 ]; then
    echo "SCSS успешно скомпилирован"
    exit 0
else
    echo "Ошибка компиляции SCSS"
    exit 1
fi
