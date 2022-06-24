#!/usr/local/bin/python3

"""
    Copyright (c) 2021-2022 Nova Intelligent Technology JSC.,
    Author: hai.nt <hai.nt@novaintechs.com>
    
    All rights reserved.

    --------------------------------------------------------------------------------------

    opnsense api helper
    
"""

import requests
import argparse
import urllib3
from utils import readConfig, log, tryParseJson

urllib3.disable_warnings()


def getApiConf():
    try:
        conf = readConfig("/usr/local/etc/nocconfig/api.conf", "api")

        api_key = conf.get("key")
        api_secret = conf.get("secret")
        api_endpoint = conf.get("endpoint")

        return (api_key, api_secret, api_endpoint)
    except Exception:
        return ("", "", "")


def get(api):
    (api_key, api_secret, api_endpoint) = getApiConf()

    url = f"{api_endpoint}/{api}"

    res = requests.get(url,
                       verify=False,
                       auth=(api_key, api_secret))

    if res.status_code == 200:
        log.debug("[API] Receive status OK")
    else:
        log.warn("[API] Connection / Authentication issue, response received:")

    log.debug(f"[API] Response: {tryParseJson(res.text)}")

    res.close()
    return res


def post(api, data, contentType):
    (api_key, api_secret, api_endpoint) = getApiConf()

    url = f"{api_endpoint}/{api}"
    headers = {"content-type": contentType}

    res = requests.post(url,
                        verify=False,
                        data=data,
                        headers=headers,
                        auth=(api_key, api_secret))

    if res.status_code == 200:
        log.debug("[API] Receive status OK")
    else:
        log.debug("[API] Connection / Authentication issue, response received:")

    log.debug(f"[API] Response: {tryParseJson(res.text)}")

    res.close()
    return res


def main():

    parser = argparse.ArgumentParser(description="OPNsense API client helper")

    parser.add_argument("-m", "--method",
                        type=str,
                        default="GET",
                        help="method `GET`/`POST`, default is `GET`")
    parser.add_argument("-a", "--api",
                        type=str,
                        required=True,
                        help="API url. for example: `nocconfig/ezmesh/get`")
    parser.add_argument("-d", "--data",
                        type=str,
                        help="data")
    parser.add_argument("-t", "--contentType",
                        type=str,
                        default="application/json",
                        help="header content-type: application/json, application/x-www-form-urlencoded, text/plain, text/html")

    args = parser.parse_args()

    method = args.method.upper()
    api = args.api
    data = args.data
    contentType = args.contentType

    if method == "GET":
        get(api)
    elif method == "POST":
        post(api, data, contentType)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
