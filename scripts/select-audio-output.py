#!/usr/bin/env python3

#########################################################################################
# author : nike073i@mail.ru                                                             #
# github: https://github.com/Nike073i                                                   #
# description:                                                                          #
#   Скрипт выбора аудио выхода.                                                         #
#   Управление сервером PulseAudio через pactl.                                         #
#   Интерактив через wofi                                                               #
#   Параметры wofi можно передать через аргументы комадной строки после имени скрипта.  #
# example: `./select_audio_output.py --location bottom_right -x -31 -y -33`             #
#########################################################################################

import os
import re
import json
import sys

def get_output_string(dev):
    return f"{dev['index']}. {dev['name'] if dev['description'] == '(null)' else dev['description']}"

def get_devices():
    status_command = "pactl -f json list sinks"
    command_out = os.popen(status_command).read()
    return json.loads(command_out)

wofi_params = ' '.join(sys.argv[1:])
devices = get_devices()
output = '\n'.join(map(get_output_string, devices))
show_command = f"echo \"{output}\" | wofi {wofi_params} -S dmenu"

selected_dev = os.popen(show_command).read()

if (selected_dev):
    match = re.search(r"(\d+)\.", selected_dev)
    dev_id = match.group(1)
    os.system(f"pactl set-default-sink {dev_id}")
