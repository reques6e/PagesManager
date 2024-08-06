#!/bin/bash

# Директория с файлами SCSS
scss_dir="web/ui/static/scss"
# Директория для сохранения файлов CSS
css_dir="web/ui/static/css"

# Перебираем все файлы SCSS в директории
for scss_file in "$scss_dir"/*.scss; do
    # Получаем имя файла без пути и расширения
    filename=$(basename "$scss_file" .scss)
    # Компилируем SCSS в CSS
    sassc "$scss_file" "$css_dir/$filename.css"

    # Проверяем статус последней команды
    if [ $? -ne 0 ]; then
        echo "Ошибка компиляции SCSS: $scss_file"
        exit 1
    fi
done

echo "Все файлы SCSS успешно скомпилированы"
exit 0
