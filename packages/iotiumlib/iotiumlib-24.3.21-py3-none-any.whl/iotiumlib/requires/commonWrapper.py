"""
// ========================================================================
// Copyright (c) 2018-2019 Iotium, Inc.
// ------------------------------------------------------------------------
// All rights reserved.
//
// ========================================================================
"""

__author__ = "Rashtrapathy"
__copyright__ = "Copyright (c) 2018-2019 by Iotium, Inc."
__license__ = "All rights reserved."
__email__ = "rashtrapathy.c@iotium.io"

import json

import requests
import urllib3

from iotiumlib.requires.commonVariables import *
from iotiumlib.requires.utils import formattedOutput

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Response:
    def __init__(self):
        self.code = int()
        self.output = list()
        self.formattedOutput = list()
        self.message = str()

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, item):
        return self[item]

    def __str__(self):
        return str(self.output)


class Session(object):
    def __init__(self):
        self.host = commonVariables().__orchip__
        self.token = commonVariables().__token__
        self.apikey = commonVariables().__apikey__
        self.username = commonVariables().__username__
        self.header = headers(token=self.token, apikey=self.apikey, username=self.username)
        if commonVariables().headers:
            self.header.update(commonVariables().headers)


def headers(token, apikey, username):
    if not username:
        return_headers = {'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'X_AUTH_TOKEN {}'.format(token),
            'X-API-KEY': apikey
            }
    else:
        return_headers = {'Content-Type': 'application/json',
         'Accept': 'application/json',
         'Authorization': 'X_AUTH_TOKEN {}'.format(token),
         'X-API-KEY': apikey, 'X_USERNAME': username
         }
    return return_headers

def applyFilters(filters):
    import re

    if not filters:
        filters = {'org_id': orch.id}
    else:
        default_filters = dict()
        for k, v in filters.items():
            default_filters.update({k: v})
        filters = default_filters

    return filters


def formUri(uri):
    # return "https://{}/{}".format(Session().host, uri)
    return f"{Session().host}/{uri}" if Session().host.startswith("http://") else f"https://{Session().host}/api/{uri}"


def postApi(uri, payload):
    return requests.post(uri, data=json.dumps(payload), verify=False, headers=Session().header)


def putApi(uri, payload):
    return requests.put(uri, data=json.dumps(payload), verify=False, headers=Session().header)


def getApiv2(uri, filters=None):
    import inspect

    v2resp = Response()

    try:
        resp = requests.get(format(uri), params=applyFilters(filters), verify=False, headers=Session().header)

        resp.raise_for_status()

        final_result = []
        results = []

        if resp.status_code == 200 and resp.headers['Content-Type'] in ["text/plain;charset=utf-8", "application/json"]:
            v2resp.code = resp.status_code
            if int(resp.json()['total_count']) > 25 and 'page' not in applyFilters(filters).keys():
                a, b = divmod(resp.json()['total_count'], 100)
                page_list = [100] * a
                page_list.append(b)
                for page in range(len(page_list)):
                    prms = applyFilters(filters)
                    prms.update({'page': page, 'size': 100})
                    resp = requests.get(uri, params=prms, verify=False, headers=Session().header)
                    if resp.status_code == 200:
                        results.append(resp.json()['results'])
                for result in results:
                    for r in result:
                        final_result.append(r)

                v2resp.output = final_result
                v2resp.formattedOutput = formattedOutput(v2resp.output, inspect.stack()[1][3])
                return v2resp
            else:
                for result in resp.json()['results']:
                    final_result.append(result)
                v2resp.output = final_result
                v2resp.formattedOutput = formattedOutput(v2resp.output, inspect.stack()[1][3])
                return v2resp
        elif resp.status_code == 200 and resp.headers['Content-Type'] == "application/x-yaml":
            v2resp.code = resp.status_code
            v2resp.output = resp.content
            return v2resp
        elif resp.status_code == 200 and resp.headers['Content-Type'] == "application/octet-stream":
            v2resp.code = resp.status_code
            v2resp.output = resp.content
            return v2resp
        else:
            v2resp.code = resp.status_code
            v2resp.output = []
            v2resp.formattedOutput = []
            v2resp.message = resp.json()["message"]
            return v2resp
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError,
            requests.exceptions.Timeout, requests.exceptions.RequestException) as errh:
        print("HTTPRequestException: {}".format(errh))
        v2resp.code = 0
        v2resp.output = []
        v2resp.formattedOutput = []
        v2resp.message = str(errh)
        return v2resp
    except Exception as err:
        print("Exception: {}".format(err))
        v2resp.code = 0
        v2resp.output = []
        v2resp.formattedOutput = []
        v2resp.message = str(err)
        return v2resp


def getApi(uri, filters=None):
    if filters is None:
        return requests.get(uri, verify=False, headers=Session().header)
    else:
        return requests.get(uri, verify=False, headers=Session().header, params=applyFilters(filters))


def deleteApi(uri):
    return requests.delete(uri, verify=False, headers=Session().header)
