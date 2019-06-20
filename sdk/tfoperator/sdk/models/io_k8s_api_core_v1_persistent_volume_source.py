# coding: utf-8

"""
    TFOpeartor

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from tfoperator.sdk.models.io_k8s_api_core_v1_aws_elastic_block_store_volume_source import IoK8sApiCoreV1AWSElasticBlockStoreVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_azure_disk_volume_source import IoK8sApiCoreV1AzureDiskVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_azure_file_persistent_volume_source import IoK8sApiCoreV1AzureFilePersistentVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_ceph_fs_persistent_volume_source import IoK8sApiCoreV1CephFSPersistentVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_cinder_persistent_volume_source import IoK8sApiCoreV1CinderPersistentVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_csi_persistent_volume_source import IoK8sApiCoreV1CSIPersistentVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_fc_volume_source import IoK8sApiCoreV1FCVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_flex_persistent_volume_source import IoK8sApiCoreV1FlexPersistentVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_flocker_volume_source import IoK8sApiCoreV1FlockerVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_gce_persistent_disk_volume_source import IoK8sApiCoreV1GCEPersistentDiskVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_glusterfs_volume_source import IoK8sApiCoreV1GlusterfsVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_host_path_volume_source import IoK8sApiCoreV1HostPathVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_iscsi_persistent_volume_source import IoK8sApiCoreV1ISCSIPersistentVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_local_volume_source import IoK8sApiCoreV1LocalVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_nfs_volume_source import IoK8sApiCoreV1NFSVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_photon_persistent_disk_volume_source import IoK8sApiCoreV1PhotonPersistentDiskVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_portworx_volume_source import IoK8sApiCoreV1PortworxVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_quobyte_volume_source import IoK8sApiCoreV1QuobyteVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_rbd_persistent_volume_source import IoK8sApiCoreV1RBDPersistentVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_scale_io_persistent_volume_source import IoK8sApiCoreV1ScaleIOPersistentVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_storage_os_persistent_volume_source import IoK8sApiCoreV1StorageOSPersistentVolumeSource  # noqa: F401,E501
from tfoperator.sdk.models.io_k8s_api_core_v1_vsphere_virtual_disk_volume_source import IoK8sApiCoreV1VsphereVirtualDiskVolumeSource  # noqa: F401,E501


class IoK8sApiCoreV1PersistentVolumeSource(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'aws_elastic_block_store': 'IoK8sApiCoreV1AWSElasticBlockStoreVolumeSource',
        'azure_disk': 'IoK8sApiCoreV1AzureDiskVolumeSource',
        'azure_file': 'IoK8sApiCoreV1AzureFilePersistentVolumeSource',
        'cephfs': 'IoK8sApiCoreV1CephFSPersistentVolumeSource',
        'cinder': 'IoK8sApiCoreV1CinderPersistentVolumeSource',
        'csi': 'IoK8sApiCoreV1CSIPersistentVolumeSource',
        'fc': 'IoK8sApiCoreV1FCVolumeSource',
        'flex_volume': 'IoK8sApiCoreV1FlexPersistentVolumeSource',
        'flocker': 'IoK8sApiCoreV1FlockerVolumeSource',
        'gce_persistent_disk': 'IoK8sApiCoreV1GCEPersistentDiskVolumeSource',
        'glusterfs': 'IoK8sApiCoreV1GlusterfsVolumeSource',
        'host_path': 'IoK8sApiCoreV1HostPathVolumeSource',
        'iscsi': 'IoK8sApiCoreV1ISCSIPersistentVolumeSource',
        'local': 'IoK8sApiCoreV1LocalVolumeSource',
        'nfs': 'IoK8sApiCoreV1NFSVolumeSource',
        'photon_persistent_disk': 'IoK8sApiCoreV1PhotonPersistentDiskVolumeSource',
        'portworx_volume': 'IoK8sApiCoreV1PortworxVolumeSource',
        'quobyte': 'IoK8sApiCoreV1QuobyteVolumeSource',
        'rbd': 'IoK8sApiCoreV1RBDPersistentVolumeSource',
        'scale_io': 'IoK8sApiCoreV1ScaleIOPersistentVolumeSource',
        'storageos': 'IoK8sApiCoreV1StorageOSPersistentVolumeSource',
        'vsphere_volume': 'IoK8sApiCoreV1VsphereVirtualDiskVolumeSource'
    }

    attribute_map = {
        'aws_elastic_block_store': 'awsElasticBlockStore',
        'azure_disk': 'azureDisk',
        'azure_file': 'azureFile',
        'cephfs': 'cephfs',
        'cinder': 'cinder',
        'csi': 'csi',
        'fc': 'fc',
        'flex_volume': 'flexVolume',
        'flocker': 'flocker',
        'gce_persistent_disk': 'gcePersistentDisk',
        'glusterfs': 'glusterfs',
        'host_path': 'hostPath',
        'iscsi': 'iscsi',
        'local': 'local',
        'nfs': 'nfs',
        'photon_persistent_disk': 'photonPersistentDisk',
        'portworx_volume': 'portworxVolume',
        'quobyte': 'quobyte',
        'rbd': 'rbd',
        'scale_io': 'scaleIO',
        'storageos': 'storageos',
        'vsphere_volume': 'vsphereVolume'
    }

    def __init__(self, aws_elastic_block_store=None, azure_disk=None, azure_file=None, cephfs=None, cinder=None, csi=None, fc=None, flex_volume=None, flocker=None, gce_persistent_disk=None, glusterfs=None, host_path=None, iscsi=None, local=None, nfs=None, photon_persistent_disk=None, portworx_volume=None, quobyte=None, rbd=None, scale_io=None, storageos=None, vsphere_volume=None):  # noqa: E501
        """IoK8sApiCoreV1PersistentVolumeSource - a model defined in Swagger"""  # noqa: E501
        self._aws_elastic_block_store = None
        self._azure_disk = None
        self._azure_file = None
        self._cephfs = None
        self._cinder = None
        self._csi = None
        self._fc = None
        self._flex_volume = None
        self._flocker = None
        self._gce_persistent_disk = None
        self._glusterfs = None
        self._host_path = None
        self._iscsi = None
        self._local = None
        self._nfs = None
        self._photon_persistent_disk = None
        self._portworx_volume = None
        self._quobyte = None
        self._rbd = None
        self._scale_io = None
        self._storageos = None
        self._vsphere_volume = None
        self.discriminator = None
        if aws_elastic_block_store is not None:
            self.aws_elastic_block_store = aws_elastic_block_store
        if azure_disk is not None:
            self.azure_disk = azure_disk
        if azure_file is not None:
            self.azure_file = azure_file
        if cephfs is not None:
            self.cephfs = cephfs
        if cinder is not None:
            self.cinder = cinder
        if csi is not None:
            self.csi = csi
        if fc is not None:
            self.fc = fc
        if flex_volume is not None:
            self.flex_volume = flex_volume
        if flocker is not None:
            self.flocker = flocker
        if gce_persistent_disk is not None:
            self.gce_persistent_disk = gce_persistent_disk
        if glusterfs is not None:
            self.glusterfs = glusterfs
        if host_path is not None:
            self.host_path = host_path
        if iscsi is not None:
            self.iscsi = iscsi
        if local is not None:
            self.local = local
        if nfs is not None:
            self.nfs = nfs
        if photon_persistent_disk is not None:
            self.photon_persistent_disk = photon_persistent_disk
        if portworx_volume is not None:
            self.portworx_volume = portworx_volume
        if quobyte is not None:
            self.quobyte = quobyte
        if rbd is not None:
            self.rbd = rbd
        if scale_io is not None:
            self.scale_io = scale_io
        if storageos is not None:
            self.storageos = storageos
        if vsphere_volume is not None:
            self.vsphere_volume = vsphere_volume

    @property
    def aws_elastic_block_store(self):
        """Gets the aws_elastic_block_store of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The aws_elastic_block_store of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1AWSElasticBlockStoreVolumeSource
        """
        return self._aws_elastic_block_store

    @aws_elastic_block_store.setter
    def aws_elastic_block_store(self, aws_elastic_block_store):
        """Sets the aws_elastic_block_store of this IoK8sApiCoreV1PersistentVolumeSource.


        :param aws_elastic_block_store: The aws_elastic_block_store of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1AWSElasticBlockStoreVolumeSource
        """

        self._aws_elastic_block_store = aws_elastic_block_store

    @property
    def azure_disk(self):
        """Gets the azure_disk of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The azure_disk of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1AzureDiskVolumeSource
        """
        return self._azure_disk

    @azure_disk.setter
    def azure_disk(self, azure_disk):
        """Sets the azure_disk of this IoK8sApiCoreV1PersistentVolumeSource.


        :param azure_disk: The azure_disk of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1AzureDiskVolumeSource
        """

        self._azure_disk = azure_disk

    @property
    def azure_file(self):
        """Gets the azure_file of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The azure_file of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1AzureFilePersistentVolumeSource
        """
        return self._azure_file

    @azure_file.setter
    def azure_file(self, azure_file):
        """Sets the azure_file of this IoK8sApiCoreV1PersistentVolumeSource.


        :param azure_file: The azure_file of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1AzureFilePersistentVolumeSource
        """

        self._azure_file = azure_file

    @property
    def cephfs(self):
        """Gets the cephfs of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The cephfs of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1CephFSPersistentVolumeSource
        """
        return self._cephfs

    @cephfs.setter
    def cephfs(self, cephfs):
        """Sets the cephfs of this IoK8sApiCoreV1PersistentVolumeSource.


        :param cephfs: The cephfs of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1CephFSPersistentVolumeSource
        """

        self._cephfs = cephfs

    @property
    def cinder(self):
        """Gets the cinder of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The cinder of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1CinderPersistentVolumeSource
        """
        return self._cinder

    @cinder.setter
    def cinder(self, cinder):
        """Sets the cinder of this IoK8sApiCoreV1PersistentVolumeSource.


        :param cinder: The cinder of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1CinderPersistentVolumeSource
        """

        self._cinder = cinder

    @property
    def csi(self):
        """Gets the csi of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The csi of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1CSIPersistentVolumeSource
        """
        return self._csi

    @csi.setter
    def csi(self, csi):
        """Sets the csi of this IoK8sApiCoreV1PersistentVolumeSource.


        :param csi: The csi of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1CSIPersistentVolumeSource
        """

        self._csi = csi

    @property
    def fc(self):
        """Gets the fc of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The fc of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1FCVolumeSource
        """
        return self._fc

    @fc.setter
    def fc(self, fc):
        """Sets the fc of this IoK8sApiCoreV1PersistentVolumeSource.


        :param fc: The fc of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1FCVolumeSource
        """

        self._fc = fc

    @property
    def flex_volume(self):
        """Gets the flex_volume of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The flex_volume of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1FlexPersistentVolumeSource
        """
        return self._flex_volume

    @flex_volume.setter
    def flex_volume(self, flex_volume):
        """Sets the flex_volume of this IoK8sApiCoreV1PersistentVolumeSource.


        :param flex_volume: The flex_volume of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1FlexPersistentVolumeSource
        """

        self._flex_volume = flex_volume

    @property
    def flocker(self):
        """Gets the flocker of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The flocker of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1FlockerVolumeSource
        """
        return self._flocker

    @flocker.setter
    def flocker(self, flocker):
        """Sets the flocker of this IoK8sApiCoreV1PersistentVolumeSource.


        :param flocker: The flocker of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1FlockerVolumeSource
        """

        self._flocker = flocker

    @property
    def gce_persistent_disk(self):
        """Gets the gce_persistent_disk of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The gce_persistent_disk of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1GCEPersistentDiskVolumeSource
        """
        return self._gce_persistent_disk

    @gce_persistent_disk.setter
    def gce_persistent_disk(self, gce_persistent_disk):
        """Sets the gce_persistent_disk of this IoK8sApiCoreV1PersistentVolumeSource.


        :param gce_persistent_disk: The gce_persistent_disk of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1GCEPersistentDiskVolumeSource
        """

        self._gce_persistent_disk = gce_persistent_disk

    @property
    def glusterfs(self):
        """Gets the glusterfs of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The glusterfs of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1GlusterfsVolumeSource
        """
        return self._glusterfs

    @glusterfs.setter
    def glusterfs(self, glusterfs):
        """Sets the glusterfs of this IoK8sApiCoreV1PersistentVolumeSource.


        :param glusterfs: The glusterfs of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1GlusterfsVolumeSource
        """

        self._glusterfs = glusterfs

    @property
    def host_path(self):
        """Gets the host_path of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The host_path of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1HostPathVolumeSource
        """
        return self._host_path

    @host_path.setter
    def host_path(self, host_path):
        """Sets the host_path of this IoK8sApiCoreV1PersistentVolumeSource.


        :param host_path: The host_path of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1HostPathVolumeSource
        """

        self._host_path = host_path

    @property
    def iscsi(self):
        """Gets the iscsi of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The iscsi of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1ISCSIPersistentVolumeSource
        """
        return self._iscsi

    @iscsi.setter
    def iscsi(self, iscsi):
        """Sets the iscsi of this IoK8sApiCoreV1PersistentVolumeSource.


        :param iscsi: The iscsi of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1ISCSIPersistentVolumeSource
        """

        self._iscsi = iscsi

    @property
    def local(self):
        """Gets the local of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The local of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1LocalVolumeSource
        """
        return self._local

    @local.setter
    def local(self, local):
        """Sets the local of this IoK8sApiCoreV1PersistentVolumeSource.


        :param local: The local of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1LocalVolumeSource
        """

        self._local = local

    @property
    def nfs(self):
        """Gets the nfs of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The nfs of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1NFSVolumeSource
        """
        return self._nfs

    @nfs.setter
    def nfs(self, nfs):
        """Sets the nfs of this IoK8sApiCoreV1PersistentVolumeSource.


        :param nfs: The nfs of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1NFSVolumeSource
        """

        self._nfs = nfs

    @property
    def photon_persistent_disk(self):
        """Gets the photon_persistent_disk of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The photon_persistent_disk of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1PhotonPersistentDiskVolumeSource
        """
        return self._photon_persistent_disk

    @photon_persistent_disk.setter
    def photon_persistent_disk(self, photon_persistent_disk):
        """Sets the photon_persistent_disk of this IoK8sApiCoreV1PersistentVolumeSource.


        :param photon_persistent_disk: The photon_persistent_disk of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1PhotonPersistentDiskVolumeSource
        """

        self._photon_persistent_disk = photon_persistent_disk

    @property
    def portworx_volume(self):
        """Gets the portworx_volume of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The portworx_volume of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1PortworxVolumeSource
        """
        return self._portworx_volume

    @portworx_volume.setter
    def portworx_volume(self, portworx_volume):
        """Sets the portworx_volume of this IoK8sApiCoreV1PersistentVolumeSource.


        :param portworx_volume: The portworx_volume of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1PortworxVolumeSource
        """

        self._portworx_volume = portworx_volume

    @property
    def quobyte(self):
        """Gets the quobyte of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The quobyte of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1QuobyteVolumeSource
        """
        return self._quobyte

    @quobyte.setter
    def quobyte(self, quobyte):
        """Sets the quobyte of this IoK8sApiCoreV1PersistentVolumeSource.


        :param quobyte: The quobyte of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1QuobyteVolumeSource
        """

        self._quobyte = quobyte

    @property
    def rbd(self):
        """Gets the rbd of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The rbd of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1RBDPersistentVolumeSource
        """
        return self._rbd

    @rbd.setter
    def rbd(self, rbd):
        """Sets the rbd of this IoK8sApiCoreV1PersistentVolumeSource.


        :param rbd: The rbd of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1RBDPersistentVolumeSource
        """

        self._rbd = rbd

    @property
    def scale_io(self):
        """Gets the scale_io of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The scale_io of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1ScaleIOPersistentVolumeSource
        """
        return self._scale_io

    @scale_io.setter
    def scale_io(self, scale_io):
        """Sets the scale_io of this IoK8sApiCoreV1PersistentVolumeSource.


        :param scale_io: The scale_io of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1ScaleIOPersistentVolumeSource
        """

        self._scale_io = scale_io

    @property
    def storageos(self):
        """Gets the storageos of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The storageos of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1StorageOSPersistentVolumeSource
        """
        return self._storageos

    @storageos.setter
    def storageos(self, storageos):
        """Sets the storageos of this IoK8sApiCoreV1PersistentVolumeSource.


        :param storageos: The storageos of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1StorageOSPersistentVolumeSource
        """

        self._storageos = storageos

    @property
    def vsphere_volume(self):
        """Gets the vsphere_volume of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501


        :return: The vsphere_volume of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :rtype: IoK8sApiCoreV1VsphereVirtualDiskVolumeSource
        """
        return self._vsphere_volume

    @vsphere_volume.setter
    def vsphere_volume(self, vsphere_volume):
        """Sets the vsphere_volume of this IoK8sApiCoreV1PersistentVolumeSource.


        :param vsphere_volume: The vsphere_volume of this IoK8sApiCoreV1PersistentVolumeSource.  # noqa: E501
        :type: IoK8sApiCoreV1VsphereVirtualDiskVolumeSource
        """

        self._vsphere_volume = vsphere_volume

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IoK8sApiCoreV1PersistentVolumeSource, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IoK8sApiCoreV1PersistentVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
