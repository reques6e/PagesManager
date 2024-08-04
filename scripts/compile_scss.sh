#!/bin/bash

# Выполнение команды sassc
sassc web/ui/static/scss/styles.scss web/ui/static/css/styles.css

# Проверка кода завершения предыдущей команды
if [ $? -eq 0 ]; then
    # Команда выполнена успешно
    echo "SCSS успешно скомпилирован"
    exit 0
else
    # Команда завершилась с ошибкой
    echo "Ошибка компиляции SCSS"
    exit 1
fi
