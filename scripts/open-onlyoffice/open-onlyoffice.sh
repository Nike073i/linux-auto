#!/bin/bash

TARGET_DIR="$HOME/tmp/onlyoffice"

mkdir -p "$TARGET_DIR"

FILE_PATH="$1"

if [ -z "$FILE_PATH" ]; then
    FILE_PATH=$(yad --file --title="Выберите файл для открытия в OnlyOffice")
    
    if [ -z "$FILE_PATH" ]; then
        echo "Файл не выбран"
        exit 1
    fi
fi

if [ ! -f "$FILE_PATH" ]; then
    yad --error --text="Файл не существует: $FILE_PATH"
    exit 1
fi

FILENAME=$(basename "$FILE_PATH")
TARGET_PATH="$TARGET_DIR/$FILENAME"

cp "$FILE_PATH" "$TARGET_PATH"

onlyoffice-desktopeditors "$TARGET_PATH" &
