"""
// ========================================================================
// Copyright (c) 2020-2021 Iotium, Inc.
// ------------------------------------------------------------------------
// All rights reserved.
//
// ========================================================================
"""

__author__ = "Rashtrapathy"
__copyright__ = "Copyright (c) 2020 by Iotium, Inc."
__license__ = "All rights reserved."
__email__ = "rashtrapathy.c@iotium.io"

from iotiumlib.requires.commonWrapper import *
from iotiumlib.requires.resourcePayload import *
from iotiumlib.requires.api_endpoints import Cluster
from urllib.parse import unquote

clusterId = str()


class cluster(object):
    def __init__(self, action, payload=None, filters=None, cluster_id=None):

        if payload is None:
            payload = {}

        def get_cluster(uri):
            return cluster.Cluster(self, method='get', uri=uri)

        def getv2_cluster(uri):
            return cluster.Cluster(self, method='getv2', uri=uri, filters=filters)

        def add_cluster(uri):
            return cluster.Cluster(self, method='post', uri=uri)

        def edit_cluster(uri):
            return cluster.Cluster(self, method='put', uri=uri)

        def delete_cluster(uri):
            return cluster.Cluster(self, method='delete', uri=uri)

        def upgrade_cluster(uri):
            return cluster.Cluster(self, method='post', uri=uri)

        _function_mapping = {
            'get': get_cluster,
            'getv2': getv2_cluster,
            'add': add_cluster,
            'edit': edit_cluster,
            'delete': delete_cluster,
            'upgrade': upgrade_cluster
        }

        api = Cluster()
        self.uri = {
            get_cluster: api.v1_cluster_id,
            getv2_cluster: api.v2_cluster,
            add_cluster: api.v1_cluster,
            edit_cluster: api.v1_cluster_id,
            delete_cluster: api.v1_cluster_id,
            upgrade_cluster: api.v1_cluster_upgrade
        }

        self.payload = resourcePaylod.Cluster(payload).__dict__

        self.clusterId = cluster_id

        self.Response = Response()

        _wrapper_fun = _function_mapping[action]
        args = '{}_cluster'.format(action)
        _wrapper_fun(self.uri[eval(args)])

    def Cluster(self, method, uri, filters=None):

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

    @staticmethod
    def add(name, labels=None, nodes=None, container_timezone=None, instance_id=100, election_network_type='WAN'):
        return cluster(action='add', payload=locals())

    @staticmethod
    def edit(cluster_id, name=None, labels=None, nodes=None, container_timezone=None, instance_id=None,
             election_network_type=None, election_network_id=None):
        resp = cluster.get(cluster_id=cluster_id)

        name = resp.Response.output['name'] if name is None else name

        if instance_id is None:
            if 'config' in resp.Response.output and 'instance_id' in resp.Response.output['config']:
                instance_id = resp.Response.output['config']['instance_id']
        else:
            instance_id = instance_id

        if election_network_type is None:
            if 'config' in resp.Response.output and 'election_network_type' in resp.Response.output['config']:
                election_network_type = resp.Response.output['config']['election_network_type']
        else:
            election_network_type = election_network_type

        if election_network_id is None:
            if 'config' in resp.Response.output and 'election_network_id' in resp.Response.output['config']:
                election_network_id = resp.Response.output['config']['election_network_id']
        else:
            election_network_id = election_network_id

        if nodes is None:
            nodes = []
            if 'nodes' in resp.Response.output:
                for n in resp.Response.output['nodes']:
                    node_id = str()
                    priority = int()
                    is_candidate = bool()
                    if 'node' in n:
                        node_id = n['node']['id']

                    if 'config' in n:
                        priority = n['config']['priority']
                        is_candidate = n['config']['is_candidate']
                    nodes.append({"node_id": node_id, "priority": priority, "is_candidate": is_candidate})

        return cluster(action='edit', payload=locals(), cluster_id=cluster_id)

    @staticmethod
    def delete(cluster_id):
        return cluster(action='delete', cluster_id=cluster_id)

    @staticmethod
    def getv2(filters=None):
        return cluster(action='getv2', filters=filters)

    @staticmethod
    def get(cluster_id):
        return cluster(action='get', cluster_id=cluster_id)

    @staticmethod
    def upgrade(cluster_id, policy=None):
        return cluster(action='upgrade', cluster_id=cluster_id, payload=locals())

    class hwmonitoring(object):
        __class__ = "hwmonitoring"

        """
        cluster hardware monitoring
        """

        def __init__(self, action, payload=None, cluster_id=None):

            if payload is None:
                payload = {}

            def enable_hwmonitoring(uri):
                return cluster.hwmonitoring.monitoring(self, method='post', uri=uri)

            def disable_hwmonitoring(uri):
                return cluster.hwmonitoring.monitoring(self, method='delete', uri=uri)

            _function_mapping = {
                'enable': enable_hwmonitoring,
                'disable': disable_hwmonitoring
            }

            self.uri = {
                enable_hwmonitoring: 'api/v1/cluster/{clusterId}/monitoring',
                disable_hwmonitoring: 'api/v1/cluster/{clusterId}/monitoring'
            }

            self.payload = resourcePaylod.HwMonitoring(payload).__dict__
            self.orgId = orch.id
            self.clusterId = cluster_id
            self.Response = Response()

            _wrapper_fun = _function_mapping[action]
            args = '{}_hwmonitoring'.format(action)
            _wrapper_fun(self.uri[eval(args)])

        def __del__(self):
            self.payload = dict()
            self.Response = Response()

        def monitoring(self, method, uri):
            paramRequired = checkforUriParam(uri)
            if paramRequired:
                for param in paramRequired:
                    uri = re.sub(r'{{{}}}'.format(param), eval('self.{}'.format(param)), uri)
            if method == 'post':
                respOp = postApi(formUri(uri), self.payload)
            elif method == 'delete':
                respOp = deleteApi(formUri(uri))
            else:
                return self.Response
            self.Response.output = respOp.json()
            self.Response.code = respOp.status_code
            return self.Response

        @staticmethod
        def enable(cluster_id, scan_interval=5):
            return cluster.hwmonitoring(action='enable', cluster_id=cluster_id, payload=locals())

        @staticmethod
        def disable(cluster_id):
            return cluster.hwmonitoring(action='disable', cluster_id=cluster_id)

    class trafficinsight(object):

        """
        Enable/Disable Trafficinsight on cluster
        """

        def __init__(self, action, payload=None, cluster_id=None):

            if payload is None:
                payload = {}

            def enable_trafficinsight(uri):
                return cluster.trafficinsight.api(self, method='post', uri=uri)

            def disable_trafficinsight(uri):
                return cluster.trafficinsight.api(self, method='delete', uri=uri)

            def get_trafficinsight(uri):
                return cluster.trafficinsight.api(self, method='get', uri=uri)

            _function_mapping = {
                'enable': enable_trafficinsight,
                'disable': disable_trafficinsight,
                'get': get_trafficinsight
            }

            api = Cluster()
            self.uri = {
                enable_trafficinsight: api.v1_cluster_trafficinsight,
                disable_trafficinsight: api.v1_cluster_trafficinsight,
                get_trafficinsight: api.v1_cluster_trafficinsight
            }

            self.payload = resourcePaylod.Trafficinsight(payload).__dict__
            self.orgId = orch.id
            self.clusterId = cluster_id
            self.Response = Response()

            _wrapper_fun = _function_mapping[action]
            args = '{}_trafficinsight'.format(action)
            _wrapper_fun(self.uri[eval(args)])

        def __del__(self):
            self.payload = dict()
            self.Response = Response()

        def api(self, method, uri):
            paramRequired = checkforUriParam(uri)
            if paramRequired:
                for param in paramRequired:
                    uri = re.sub(r'{{{}}}'.format(param), eval('self.{}'.format(param)), uri)
            if method == 'get':
                respOp = getApi(formUri(uri))
            elif method == 'post':
                respOp = postApi(formUri(uri), self.payload)
            elif method == 'delete':
                respOp = deleteApi(formUri(uri))
            else:
                return self.Response
            self.Response.output = respOp.json()
            self.Response.code = respOp.status_code
            return self.Response

        @staticmethod
        def get(cluster_id):
            return cluster.trafficinsight(action='get', cluster_id=cluster_id)

        @staticmethod
        def enable(cluster_id, sampling_frequency="medium", threat_detection_enable=True):
            return cluster.trafficinsight(action='enable', cluster_id=cluster_id, payload=locals())

        @staticmethod
        def disable(cluster_id):
            return cluster.trafficinsight(action='disable', cluster_id=cluster_id)

        @staticmethod
        def isEnabled(cluster_id):
            respObj = cluster.trafficinsight(action='get', cluster_id=cluster_id).Response
            if respObj.code == 200:
                return respObj.output["threat_detection_enable"]
            else:
                return False

    class device_discovery(object):

        """
        Enable/Disable DD on iNode
        """

        def __init__(self, action, filters=None, payload=None, cluster_id=None, report_id=None):

            if payload is None:
                payload = {}

            def enable_device_discovery(uri):
                return cluster.device_discovery.api(self, method='post', uri=uri)

            def disable_device_discovery(uri):
                return cluster.device_discovery.api(self, method='delete', uri=uri)

            def get_device_discovery(uri):
                return cluster.device_discovery.api(self, method='get', uri=uri)

            def report_device_discovery(uri):
                return cluster.device_discovery.api(self, method='getv2', uri=uri, filters=filters)

            def report_id_device_discovery(uri):
                return cluster.device_discovery.api(self, method='get', uri=uri, filters=filters)  # LAT-18757

            def download_device_discovery(uri):
                return cluster.device_discovery.api(self, method='get', uri=uri)

            def scan_device_discovery(uri):
                return cluster.device_discovery.api(self, method='getv2', uri=uri, filters=filters)

            def summary_device_discovery(uri):
                return cluster.device_discovery.api(self, method='get', uri=uri)

            _function_mapping = {
                'enable': enable_device_discovery,
                'disable': disable_device_discovery,
                'get': get_device_discovery,
                'report': report_device_discovery,
                'report_id': report_id_device_discovery,
                'download': download_device_discovery,
                'scan': scan_device_discovery,
                'summary': summary_device_discovery,
            }

            api = Cluster()
            self.uri = {
                enable_device_discovery: api.v2_cluster_id_discovery,
                disable_device_discovery: api.v2_cluster_id_discovery,
                get_device_discovery: api.v2_cluster_id_discovery,
                report_device_discovery: api.v2_cluster_id_discovery_report,
                report_id_device_discovery: api.v2_cluster_id_discovery_report_id,
                download_device_discovery: api.v2_cluster_id_discovery_report_id_download,
                scan_device_discovery: api.v2_cluster_id_discovery_scan,
                summary_device_discovery: api.v2_cluster_id_discovery_scan_summary,
            }

            self.orgId = orch.id
            self.clusterId = cluster_id
            self.reportId = report_id
            self.Response = Response()

            _wrapper_fun = _function_mapping[action]
            args = '{}_device_discovery'.format(action)
            _wrapper_fun(self.uri[eval(args)])

        def __del__(self):
            self.payload = dict()
            self.Response = Response()

        def api(self, method, uri, filters=None):
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
            elif method == 'delete':
                respOp = deleteApi(formUri(uri))
            else:
                return self.Response

            if 'Content-Type' in respOp.headers and 'text/csv' in respOp.headers['Content-Type']:
                if 'Content-Disposition' in respOp.headers:
                    content_disposition = respOp.headers['Content-Disposition']
                    filename_index = content_disposition.find('filename=')
                    if filename_index != -1:
                        filename = unquote(content_disposition[filename_index + 9:])
                    else:
                        filename = 'downloaded_file.csv'
                else:
                    filename = 'downloaded_file.csv'
                with open(filename, 'wb') as file:
                    file.write(respOp.content)
                self.Response.output = f"{filename} downloaded."
                self.Response.code = respOp.status_code
            else:
                self.Response.output = respOp.json()
                self.Response.code = respOp.status_code
            return self.Response

        @staticmethod
        def get(cluster_id):
            return cluster.device_discovery(action='get', cluster_id=cluster_id)

        @staticmethod
        def enable(cluster_id):
            return cluster.device_discovery(action='enable', cluster_id=cluster_id)

        @staticmethod
        def disable(cluster_id):
            return cluster.device_discovery(action='disable', cluster_id=cluster_id)

        @staticmethod
        def report(cluster_id, report_id=None, filters=None):
            if report_id is None:
                return cluster.device_discovery(action='report', cluster_id=cluster_id, filters=filters)
            if report_id is not None:
                return cluster.device_discovery(action='report_id', cluster_id=cluster_id, report_id=report_id,
                                                filters=filters)

        @staticmethod
        def download(cluster_id, report_id):
            return cluster.device_discovery(action='download', cluster_id=cluster_id, report_id=report_id)

        @staticmethod
        def scan(cluster_id, filters=None):
            return cluster.device_discovery(action='scan', cluster_id=cluster_id, filters=filters)

        @staticmethod
        def summary(cluster_id):
            return cluster.device_discovery(action='summary', cluster_id=cluster_id)
