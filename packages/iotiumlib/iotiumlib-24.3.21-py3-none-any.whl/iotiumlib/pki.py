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

from iotiumlib.requires.commonWrapper import *
from iotiumlib.requires.resourcePayload import *
from iotiumlib.requires.api_endpoints import Pki


class pki(object):
    def __init__(self, action, filters=None, payload=None, org_id=None, pki_id=None):

        if payload is None:
            payload = {}
        self.payload = dict()
        self.resp = Response()

        def get_pki(uri):
            return pki.Pki(self, method='get', uri=uri)

        def getv2_pki(uri):
            return pki.Pki(self, method='getv2', uri=uri, filters=filters)
        
        def delete_pki(uri):
            return pki.Pki(self, method='delete', uri=uri)
        

        _function_mapping = {
            'get': get_pki,
            'getv2': getv2_pki,
            'delete':delete_pki
        }

        api = Pki()
        self.uri = {
            get_pki: api.v1_pki,
            getv2_pki: api.v2_pki,
            delete_pki: api.v1_pki_id
        }

        self.payload = resourcePaylod.Organisation(payload).__dict__

        self.orgId = orch.id
        self.pkiCertId = pki_id

        self.Response = Response()

        _wrapper_fun = _function_mapping[action]
        args = '{}_pki'.format(action)
        _wrapper_fun(self.uri[eval(args)])

    def Pki(self, method, uri, filters=None):
        respOp = dict()
        paramRequired = checkforUriParam(uri)
        if paramRequired:
            for param in paramRequired:
                uri = re.sub(r'{{{}}}'.format(param), eval('self.{}'.format(param)), uri)

        if method == 'get':
            respOp = getApi(formUri(uri))
        elif method == 'getv2':
            self.Response = getApiv2(formUri(uri), filters)
            return self.Response
        elif method == 'post':
            respOp = postApi(formUri(uri), self.payload)
        elif method == 'put':
            respOp = putApi(formUri(uri), self.payload)
        elif method == 'delete':
            respOp = deleteApi(formUri(uri))
        else:
            return self.Response
        self.Response.output = respOp.json()
        self.Response.code = respOp.status_code
        return self.Response


def get():
    return pki(action='get')

def getv2(filters=None):
    return pki(filters=filters, action='getv2')

def delete(pki_id):
    return pki(pki_id=pki_id, action='delete')
