#!/usr/bin/env python3
import sys
import os
import json


def parse_plist_file(rn_dir, version_type):
    with open(os.path.join(rn_dir, 'app.json'), 'r') as file:
        data = file.read()
        app_json = json.loads(data)
        project_name = app_json['name']
    build_file = os.path.join(rn_dir, 'ios', f"{project_name}.xcodeproj", 'project.pbxproj')

    with open(build_file, 'r') as b:
        content = b.readlines()

    version_name = None
    version_code = None
    for line in content:
        tokenize = line.strip().split(" = ")
        if tokenize[0] == "MARKETING_VERSION":
            version_name = tokenize[1].strip(';')
        elif tokenize[0] == "CURRENT_PROJECT_VERSION":
            version_code = tokenize[1].strip(';')

    if version_type == "name":
        print(version_name)
    if version_type == "code":
        print(version_code)


if __name__ == '__main__':
    version_type_arg = sys.argv[1]
    rn_dir_arg = sys.argv[2]
    if rn_dir_arg is None:
        rn_dir_arg = os.path.curdir
    if not os.path.exists(rn_dir_arg):
        print("Not a valid directory")
        sys.exit()
    parse_plist_file(rn_dir_arg, version_type_arg)
