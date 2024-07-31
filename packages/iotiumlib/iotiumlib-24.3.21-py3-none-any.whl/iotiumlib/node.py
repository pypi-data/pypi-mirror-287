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
from iotiumlib.requires.api_endpoints import Node
from urllib.parse import unquote

nodeId = str()
orgId = str()


class node(object):
    __class__ = "iNode"

    """
    iNode Resource
    """

    def __init__(self, action, filters=None, payload=None, node_id=None):

        if payload is None:
            payload = {}

        def add_inode(uri):
            return node.iNode(self, method='post', uri=uri)

        def edit_inode(uri):
            return node.iNode(self, method='put', uri=uri)

        def delete_inode(uri):
            return node.iNode(self, method='delete', uri=uri)

        def get_inode(uri):
            return node.iNode(self, method='get', uri=uri)

        def getv2_inode(uri):
            return node.iNode(self, method='getv2', uri=uri, filters=filters)

        def get_node_id_inode(uri):
            return node.iNode(self, method='get', uri=uri)

        def reboot_inode(uri):
            return node.iNode(self, method='post', uri=uri)

        def notifications_inode(uri):
            return node.Notifications(self, method='notifications', uri=uri, filters=filters)

        def stats_inode(uri):
            return node.Stats(self, method='stats', uri=uri, filters=filters)

        def statssummary_inode(uri):
            return node.Stats(self, method='stats', uri=uri, filters=filters)

        def upgrade_inode(uri):
            return node.iNode(self, method='post', uri=uri)

        def convert_to_cluster_inode(uri):
            return node.iNode(self, method='post', uri=uri)

        def replace_hsn_inode(uri):
            return node.iNode(self, method='post', uri=uri)

        _function_mapping = {
            'add': add_inode,
            'edit': edit_inode,
            'delete': delete_inode,
            'get': get_inode,
            'reboot': reboot_inode,
            'get_node_id': get_node_id_inode,
            'getv2': getv2_inode,
            'notifications': notifications_inode,
            'stats': stats_inode,
            'statssummary': statssummary_inode,
            'upgrade': upgrade_inode,
            'convert_to_cluster': convert_to_cluster_inode,
            'replace_hsn': replace_hsn_inode
        }

        api = Node()
        self.uri = {
            add_inode: api.v1_node,
            get_inode: api.v2_node,
            getv2_inode: api.v2_node,
            edit_inode: api.v1_node_id,
            delete_inode: api.v1_node_id,
            get_node_id_inode: api.v1_node_id,
            reboot_inode: api.v1_node_id_reboot,
            notifications_inode: api.notifications,
            stats_inode: api.stats,
            statssummary_inode: api.stats_summary,
            upgrade_inode: api.upgrade,
            convert_to_cluster_inode: api.convert_to_cluster,
            replace_hsn_inode: api.v1_node_id_replace_hsn
        }

        self.payload = resourcePaylod.iNode(payload).__dict__

        self.nodeId = node_id
        self.orgId = orch.id

        self.Response = Response()

        _wrapper_fun = _function_mapping[action]
        args = '{}_inode'.format(action)
        _wrapper_fun(self.uri[eval(args)])

    def __del__(self):
        self.payload = dict()
        self.Response = Response()

    def iNode(self, method, uri, filters=None):

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

    def Notifications(self, method, uri, filters=None):
        paramRequired = checkforUriParam(uri)
        if paramRequired:
            for param in paramRequired:
                uri = re.sub(r'{{{}}}'.format(param), eval('self.{}'.format(param)), uri)
        if method == 'notifications':
            self.Response = getApiv2(formUri(uri), filters)
            return self.Response

    def Stats(self, method, uri, filters=None):
        paramRequired = checkforUriParam(uri)
        if paramRequired:
            for param in paramRequired:
                uri = re.sub(r'{{{}}}'.format(param), eval('self.{}'.format(param)), uri)
        if method == 'stats':
            respOp = getApi(formUri(uri))
        elif method == 'statssummary':
            respOp = getApi(formUri(uri))
        else:
            return self.Response
        self.Response.output = respOp.json()
        self.Response.code = respOp.status_code
        return self.Response

    class hwmonitoring(object):

        """
        iNode hardware monitoring
        """

        def __init__(self, action, payload=None, node_id=None):

            if payload is None:
                payload = {}

            def enable_hwmonitoring(uri):
                return node.hwmonitoring.monitoring(self, method='post', uri=uri)

            def disable_hwmonitoring(uri):
                return node.hwmonitoring.monitoring(self, method='delete', uri=uri)

            def get_hwmonitoring(uri):
                return node.hwmonitoring.monitoring(self, method='get', uri=uri)

            _function_mapping = {
                'enable': enable_hwmonitoring,
                'disable': disable_hwmonitoring,
                'get': get_hwmonitoring
            }

            api = Node()
            self.uri = {
                enable_hwmonitoring: api.hw_monitoring,
                disable_hwmonitoring: api.hw_monitoring,
                get_hwmonitoring: api.hw_monitoring
            }

            self.payload = resourcePaylod.HwMonitoring(payload).__dict__
            self.orgId = orch.id
            self.nodeId = node_id
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
        def get(node_id):
            return node.hwmonitoring(action='get', node_id=node_id)

        @staticmethod
        def enable(node_id, scan_interval=5):
            return node.hwmonitoring(action='enable', node_id=node_id, payload=locals())

        @staticmethod
        def disable(node_id):
            return node.hwmonitoring(action='disable', node_id=node_id)

    class trafficinsight(object):

        """
        Enable/Disable Trafficinsight on iNode
        """

        def __init__(self, action, payload=None, node_id=None):

            if payload is None:
                payload = {}

            def enable_trafficinsight(uri):
                return node.trafficinsight.api(self, method='post', uri=uri)

            def disable_trafficinsight(uri):
                return node.trafficinsight.api(self, method='delete', uri=uri)

            def get_trafficinsight(uri):
                return node.trafficinsight.api(self, method='get', uri=uri)

            _function_mapping = {
                'enable': enable_trafficinsight,
                'disable': disable_trafficinsight,
                'get': get_trafficinsight
            }

            api = Node()
            self.uri = {
                enable_trafficinsight: api.trafficinsight,
                disable_trafficinsight: api.trafficinsight,
                get_trafficinsight: api.trafficinsight
            }

            self.payload = resourcePaylod.Trafficinsight(payload).__dict__
            self.orgId = orch.id
            self.nodeId = node_id
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
        def get(node_id):
            return node.trafficinsight(action='get', node_id=node_id)

        @staticmethod
        def enable(node_id, sampling_frequency="medium", threat_detection_enable=True):
            return node.trafficinsight(action='enable', node_id=node_id, payload=locals())

        @staticmethod
        def disable(node_id):
            return node.trafficinsight(action='disable', node_id=node_id)

        @staticmethod
        def isEnabled(node_id):
            respObj = node.trafficinsight(action='get', node_id=node_id).Response
            if respObj.code == 200:
                return respObj.output["threat_detection_enable"]
            else:
                return False

    @staticmethod
    def add(inode_name, profile_id, serial_number=None, org_id=None, standalone_expires=0,
            label=None, data_saving_mode="Fast", ssh_keys=None, container_timezone=None, multinic_mode=None):
        """
        Add iNode
        :param data_saving_mode:
        :param inode_name: iNode Name
        :param serial_number: Serial Number of Edge iNode
        :param profile_id: Profile ID of Edge/Virtual Edge/Virtual
        :param org_id: ORG ID
        :param standalone_expires:
        :param label:
        :return: resp object
        """
        return node(action="add", payload=locals())

    @staticmethod
    def edit(node_id, inode_name=None, label=None, standalone_expires=0,
             data_saving_mode=None, ssh_keys=None, container_timezone=None, multinic_mode=None):
        resp = node.get(node_id=node_id)
        inode_name = resp.Response.output['name'] if inode_name is None else inode_name
        standalone_expires = resp.Response.output[
            'max_headless_time'] if standalone_expires is None else standalone_expires
        data_saving_mode = resp.Response.output['stat_config'][
            'stat_mode'] if data_saving_mode is None else data_saving_mode
        if ssh_keys is None and 'ssh_keys' in resp.Response.output:
            ssh_keys = resp.Response.output['ssh_keys'][0]['id']

        if multinic_mode is None and 'multinic_mode' in resp.Response.output:
            multinic_mode = resp.Response.output['multinic_mode']['enable']

        if label is None:
            labels = []
            for k, v in resp.Response.output['metadata']['labels'].items():
                if not k.startswith('_'):
                    labels.append(":".join([k.strip(), v.strip()]))
            label = str(','.join(labels))
        elif label.title() == "None":
            label = "None"

        return node(action="edit",
                    payload=locals(),
                    node_id=node_id
                    )

    @staticmethod
    def delete(node_id):
        return node(action="delete",
                    node_id=node_id
                    )

    @staticmethod
    def reboot(node_id):
        return node(action="reboot",
                    node_id=node_id
                    )

    @staticmethod
    def get(node_id=None):
        if node_id is not None:
            return node(action='get_node_id', node_id=node_id)
        else:
            return node(action="get")

    @staticmethod
    def getv2(filters=None):
        return node(filters=filters, action='getv2')

    @staticmethod
    def notifications(node_id, type=None, filters=None):

        if filters is None:
            filters = dict()

        if type:
            filters.update({'type': type})

        return node(node_id=node_id, action="notifications", filters=filters)

    @staticmethod
    def stats(node_id):
        return node(node_id=node_id, action="stats")

    @staticmethod
    def statssummary(node_id):
        return node(node_id=node_id, action="statssummary")

    @staticmethod
    def upgrade(node_id, policy=None):
        return node(action='upgrade', node_id=node_id, payload=locals())

    @staticmethod
    def convert_to_cluster(node_id, cluster_name, election_network_type='WAN', instance_id=100,
                           election_network_id=None):
        return node(action='convert_to_cluster', node_id=node_id, payload=locals())

    @staticmethod
    def replace_hsn(node_id, hardware_serial_number=None):
        return node(action='replace_hsn', node_id=node_id, payload=locals())

    class device_discovery(object):

        """
        Enable/Disable DD on iNode
        """

        def __init__(self, action, filters=None, payload=None, node_id=None, report_id=None):

            if payload is None:
                payload = {}

            def enable_device_discovery(uri):
                return node.device_discovery.api(self, method='post', uri=uri)

            def disable_device_discovery(uri):
                return node.device_discovery.api(self, method='delete', uri=uri)

            def get_device_discovery(uri):
                return node.device_discovery.api(self, method='get', uri=uri)

            def report_device_discovery(uri):
                return node.device_discovery.api(self, method='getv2', uri=uri, filters=filters)

            def report_id_device_discovery(uri):
                return node.device_discovery.api(self, method='get', uri=uri, filters=filters)  # LAT-18757

            def download_device_discovery(uri):
                return node.device_discovery.api(self, method='get', uri=uri)

            def scan_device_discovery(uri):
                return node.device_discovery.api(self, method='getv2', uri=uri, filters=filters)

            def summary_device_discovery(uri):
                return node.device_discovery.api(self, method='get', uri=uri)

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

            api = Node()
            self.uri = {
                enable_device_discovery: api.v2_node_id_discovery,
                disable_device_discovery: api.v2_node_id_discovery,
                get_device_discovery: api.v2_node_id_discovery,
                report_device_discovery: api.v2_node_id_discovery_report,
                report_id_device_discovery: api.v2_node_id_discovery_report_id,
                download_device_discovery: api.v2_node_id_discovery_report_id_download,
                scan_device_discovery: api.v2_node_id_discovery_scan,
                summary_device_discovery: api.v2_node_id_discovery_scan_summary,
            }

            self.payload = resourcePaylod.Trafficinsight(payload).__dict__
            self.orgId = orch.id
            self.nodeId = node_id
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
        def get(node_id):
            return node.device_discovery(action='get', node_id=node_id)

        @staticmethod
        def enable(node_id):
            return node.device_discovery(action='enable', node_id=node_id)

        @staticmethod
        def disable(node_id):
            return node.device_discovery(action='disable', node_id=node_id)

        @staticmethod
        def report(node_id, report_id=None, filters=None):
            if report_id is None:
                return node.device_discovery(action='report', node_id=node_id, filters=filters)
            if report_id is not None:
                return node.device_discovery(action='report_id', node_id=node_id, report_id=report_id, filters=filters)

        @staticmethod
        def download(node_id, report_id):
            return node.device_discovery(action='download', node_id=node_id, report_id=report_id)

        @staticmethod
        def scan(node_id, filters=None):
            return node.device_discovery(action='scan', node_id=node_id, filters=filters)

        @staticmethod
        def summary(node_id):
            return node.device_discovery(action='summary', node_id=node_id)

    class node_netplan(object):

        """
        Get/Update iNode Netplan
        """

        def __init__(self, action, filters=None, payload=None, node_id=None):

            if payload is None:
                payload = {}

            def get_node_netplan(uri):
                return node.node_netplan.api(self, method='get', uri=uri)

            def edit_node_netplan(uri):
                return node.node_netplan.api(self, method='put', uri=uri)

            _function_mapping = {
                'get': get_node_netplan,
                'edit': edit_node_netplan
            }

            api = Node()
            self.uri = {
                get_node_netplan: api.v1_node_id_netplan,
                edit_node_netplan: api.v1_node_id_netplan,
            }

            self.payload = resourcePaylod.NodeNetplan(payload).__dict__
            self.orgId = orch.id
            self.nodeId = node_id
            self.Response = Response()

            _wrapper_fun = _function_mapping[action]
            args = '{}_node_netplan'.format(action)
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
            elif method == 'put':
                respOp = putApi(formUri(uri), self.payload)
            else:
                return self.Response

            self.Response.output = respOp.json()
            self.Response.code = respOp.status_code
            return self.Response

        @staticmethod
        def get(node_id):
            return node.node_netplan(action='get', node_id=node_id)

        @staticmethod
        def edit(node_id, TAN=None, WAN=None, FREE=None):
            return node.node_netplan(action='edit', node_id=node_id, payload=locals())
