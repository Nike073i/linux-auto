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

if [ -f "$TARGET_PATH" ]; then
    yad --question \
           --text="Файл уже существует. Вы хотите перезаписать его?" \
           --title="Подтверждение" \
           --button="Перезаписать:0" \
           --button="Открыть текущий:1";

    case $? in
        0)
            cp "$FILE_PATH" "$TARGET_PATH"
            ;;
        252)
            exit 1
            ;;
    esac
fi

onlyoffice-desktopeditors "$TARGET_PATH" &
