#!/usr/local/bin/python3

"""
    Copyright (c) 2021-2022 Nova Intelligent Technology JSC.,
    Author: hai.nt <hai.nt@novaintechs.com>

    All rights reserved.

    --------------------------------------------------------------------------------------

    perform some tests for the noc application

"""

import json
import os
import shutil
from utils import log, tryParseJson, fmtNova


def modMenu():
    try:
        result = {}
        name = "menu"

        path = "/usr/local/opnsense/mvc/app/models/OPNsense/Core/Menu/Menu.xml"
        exists = os.path.exists(path)

        result[name] = {}
        result[name]["path"] = path
        result[name]["exist"] = exists

        if exists:
            fr = open(path, "r")
            lines = fr.readlines()
            fr.close()

            for i, line in enumerate(lines):
                if "License" in line or "Help" in line or "Documentation" in line or "Forum" in line or "Support" in line:
                    lines[i] = ""

            fw = open(path, "w")
            fw.writelines(lines)
            fw.close()

        result["message"] = "modMenu() ok! 💖"

        return result

    except Exception as e:
        return {
            "message": e,
        }


def modInfo():
    try:
        result = {}
        name = "core"

        path = "/usr/local/opnsense/version/core"
        exists = os.path.exists(path)
        mod = {
            "product_name": "NOC",
            "product_nickname": "NovaIntechs",
            "product_email": "info@novaintechs.com",
            "product_website": "https://novaintechs.com/",

            # "Nova Intelligent Technology JSC.,",
            "product_copyright_owner": "NovaIntechs JSC.,",
            "product_copyright_url": "https://novaintechs.com/",
            "product_copyright_years": "2021-2022",
        }

        result[name] = {}
        result[name]["path"] = path
        result[name]["exist"] = exists

        if exists:
            fr = open(path, "r")
            data = json.load(fr)
            for k in mod.keys():
                if k in data:
                    data[k] = mod[k]
                    result[name][k] = mod[k]
            fr.close()

            new_data = json.dumps(data, indent=4)
            fw = open(path, "w")
            fw.write(new_data)
            fw.close()

        result["message"] = "modInfo() ok! 💖"

        return result

    except Exception as e:
        return {
            "message": e,
        }


def modBanner():
    try:
        result = {}
        name = "banner"

        path = "/usr/local/opnsense/service/templates/OPNsense/Auth/motd"
        exists = os.path.exists(path)

        result[name] = {}
        result[name]["path"] = path
        result[name]["exist"] = exists

        if exists:
            fr = open(path, "r")
            lines = fr.readlines()
            fr.close()

            lines.clear()

            fw = open(path, "w")
            fw.write(fmtNova())
            fw.close()

        result["message"] = "modBanner() ok! 💖"

        return result

    except Exception as e:
        return {
            "message": e,
        }


def copyFiles():
    try:
        src_dir = "/usr/local/opnsense/service/templates/OPNsense/Noc/"

        _json = '''
        [
            {
                "name": "default-logo.svg",
                "dest": "/usr/local/opnsense/www/themes/opnsense/build/images/"
            },
            {
                "name": "icon-logo.svg",
                "dest": "/usr/local/opnsense/www/themes/opnsense/build/images/"
            },
            {
                "name": "favicon.png",
                "dest": "/usr/local/opnsense/www/themes/opnsense/build/images/"
            }
        ]
        '''

        _list = json.loads(_json)

        result = {}
        result["pwd"] = os.getcwd()
        result["src_dir"] = src_dir

        for item in _list:
            name = item["name"]

            result[name] = {}

            src = os.path.join(src_dir, name)
            src_exist = os.path.exists(src)

            result[name]["src"] = {}
            result[name]["src"]["path"] = src
            result[name]["src"]["exist"] = src_exist

            dst = os.path.join(item["dest"], name)
            dst_exist = os.path.exists(dst)

            result[name]["dst"] = {}
            result[name]["dst"]["path"] = dst
            result[name]["dst"]["exist"] = dst_exist

            if src_exist and dst_exist:
                result[name]["copy"] = shutil.copyfile(src, dst)

        result["message"] = "copyFiles() ok! 💖"

        return result
    except Exception as e:
        return {
            "message": e,
        }


def main():
    log.debug("[INIT] copyFiles()")
    log.debug(tryParseJson(copyFiles()))
    log.debug("[INIT] modInfo()")
    log.debug(tryParseJson(modInfo()))
    log.debug("[INIT] modMenu()")
    log.debug(tryParseJson(modMenu()))
    log.debug("[INIT] modBanner()")
    log.debug(tryParseJson(modBanner()))


if __name__ == "__main__":
    main()
