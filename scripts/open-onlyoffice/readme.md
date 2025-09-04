# OnlyOffice Opener

Утилита для открытия файлов в OnlyOffice в обход ограничения snap-контейнеризации. 

Копирует выбранный файл в папку $HOME/tmp/onlyoffice 

## Зависимости
- `yad` - графическая менюшка выбора файлов. 

```sh
sudo apt install yad
```

## Установка
1. Скрипт разместить в удобном месте Например - `~/scripts/open-onlyoffice.sh` или в `/usr/local/bin/open-onlyoffice.sh`
2. Сделать скрипт исполняемым. `chmox +x open-onlyoffice.sh`
3. Скопировать `.desktop`-файл в `~/.local/share/applications/`
4. Изменить в `.desktop`-файле свойство `Exec` на путь к скрипту. Например: `Exec=/home/skuld/scripts/open-onlyoffice.sh %F`
