#!/usr/bin/python3
"""
Module for adds all arguments to a Python list,
and then save them to a file"""
import json
import os.path
import sys
save_json_file = __import__('7-save_to_json_file').save_to_json_file
load_jason_file = __import__('8-load_from_json_file').load_from_json_file

file = "add_item.json"
json_list = []
if os.path.exists(file):
    json_list = load_jason_file(file)

for elem in range(1, len(sys.argv)):
    json_list.append(sys.argv[elem])

save_json_file(json_list, file)
