#!/usr/bin/env python3

#############################################################################################
# author : nike073i@mail.ru                                                                 #
# github: https://github.com/Nike073i                                                       #
# inpsiredBy: https://github.com/hyprwm/Hyprland/discussions/830#discussioncomment-7767173  #
# description:                                                                              #
#   Скрипт вывода списка открытых окон в Hyprland                                           #
#   Выбор приложения приводит к фокусировке на нем                                          #
#   Интерактив через wofi                                                                   #
#   Параметры wofi можно передать через аргументы комадной строки после имени скрипта.      #
# example: `./show_running_windows.py --location bottom_left -x 4 -y 33`                    #
#############################################################################################

import gi
import sys
import os
import json
import re
import array as arr

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def resolve_icon_path(icon_name, defaultIconName = "application-x-desktop"):
    iconFile = get_icon_file(icon_name)
    if (iconFile):
        return iconFile
    print("У приложения отсутствует иконка. Используется дефолтная")
    return get_icon_file(defaultIconName)

def get_icon_file(icon_name):
    theme = Gtk.IconTheme.get_default()
    icon = theme.lookup_icon(icon_name.lower(), 32, 0)
    return icon.get_filename() if icon else ""

def get_output_string(window):
    title = window['title']
    image = resolve_icon_path(window["class"])
    print(image)
    address = window['address']
    wid = window["workspace"]["id"]
    return f"img:{image}:text:{title} ({address}_{wid})"

wofi_params = ' '.join(sys.argv[1:])
windows = json.loads(os.popen("hyprctl -j clients").read())

output = '\n'.join(
    map(get_output_string,
        filter(
            lambda w: w["workspace"]["id"] != -1,
            windows
    )))

show_command = f"echo \"{output}\" | wofi {wofi_params} -S dmenu"
selected_window = os.popen(show_command).read()

if (selected_window):
    match = re.search(r"\((\w+)\)$", selected_window)
    addr = match.group(1).split("_")[0]
    os.system("hyprctl dispatch focuswindow address:%s"%(addr))

