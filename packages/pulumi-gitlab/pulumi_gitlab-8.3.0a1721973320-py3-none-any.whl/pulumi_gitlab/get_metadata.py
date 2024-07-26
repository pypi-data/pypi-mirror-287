# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetMetadataResult',
    'AwaitableGetMetadataResult',
    'get_metadata',
    'get_metadata_output',
]

@pulumi.output_type
class GetMetadataResult:
    """
    A collection of values returned by getMetadata.
    """
    def __init__(__self__, enterprise=None, id=None, kas=None, revision=None, version=None):
        if enterprise and not isinstance(enterprise, bool):
            raise TypeError("Expected argument 'enterprise' to be a bool")
        pulumi.set(__self__, "enterprise", enterprise)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kas and not isinstance(kas, dict):
            raise TypeError("Expected argument 'kas' to be a dict")
        pulumi.set(__self__, "kas", kas)
        if revision and not isinstance(revision, str):
            raise TypeError("Expected argument 'revision' to be a str")
        pulumi.set(__self__, "revision", revision)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def enterprise(self) -> bool:
        """
        If the GitLab instance is an enterprise instance or not. Supported for GitLab 15.6 onwards.
        """
        return pulumi.get(self, "enterprise")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the data source. It will always be `1`
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kas(self) -> 'outputs.GetMetadataKasResult':
        """
        Metadata about the GitLab agent server for Kubernetes (KAS).
        """
        return pulumi.get(self, "kas")

    @property
    @pulumi.getter
    def revision(self) -> str:
        """
        Revision of the GitLab instance.
        """
        return pulumi.get(self, "revision")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Version of the GitLab instance.
        """
        return pulumi.get(self, "version")


class AwaitableGetMetadataResult(GetMetadataResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMetadataResult(
            enterprise=self.enterprise,
            id=self.id,
            kas=self.kas,
            revision=self.revision,
            version=self.version)


def get_metadata(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMetadataResult:
    """
    The `get_metadata` data source retrieves the metadata of the GitLab instance.

    **Upstream API**: [GitLab REST API docs](https://docs.gitlab.com/ee/api/metadata.html)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gitlab as gitlab

    this = gitlab.get_metadata()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gitlab:index/getMetadata:getMetadata', __args__, opts=opts, typ=GetMetadataResult).value

    return AwaitableGetMetadataResult(
        enterprise=pulumi.get(__ret__, 'enterprise'),
        id=pulumi.get(__ret__, 'id'),
        kas=pulumi.get(__ret__, 'kas'),
        revision=pulumi.get(__ret__, 'revision'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_metadata)
def get_metadata_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMetadataResult]:
    """
    The `get_metadata` data source retrieves the metadata of the GitLab instance.

    **Upstream API**: [GitLab REST API docs](https://docs.gitlab.com/ee/api/metadata.html)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_gitlab as gitlab

    this = gitlab.get_metadata()
    ```
    """
    ...
