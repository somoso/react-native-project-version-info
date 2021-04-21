#!/usr/bin/env python3
import sys
import os


def parse_gradle_file(rn_dir, version_type):
    buildfile = os.path.join(rn_dir, 'android', 'app', 'build.gradle')
    with open(buildfile, 'r') as b:
        content = b.readlines()

    version_name = None
    version_code = None
    for line in content:
        tokenize = line.strip().split(" ")
        if tokenize[0] == "versionName":
            version_name = tokenize[1].strip('"')
        elif tokenize[0] == "versionCode":
            version_code = tokenize[1]

    if version_type == "name":
        print(version_name)
    if version_type == "code":
        print(version_code)


if __name__ == '__main__':
    version_type = sys.argv[1]
    rn_dir = sys.argv[2]
    if rn_dir is None:
        rn_dir = os.path.curdir
    if not os.path.exists(rn_dir):
        print("Not a valid directory")
        sys.exit()
    parse_gradle_file(rn_dir, version_type)
