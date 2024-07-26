# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['IntegrationExternalWikiArgs', 'IntegrationExternalWiki']

@pulumi.input_type
class IntegrationExternalWikiArgs:
    def __init__(__self__, *,
                 external_wiki_url: pulumi.Input[str],
                 project: pulumi.Input[str]):
        """
        The set of arguments for constructing a IntegrationExternalWiki resource.
        :param pulumi.Input[str] external_wiki_url: The URL of the external wiki.
        :param pulumi.Input[str] project: ID of the project you want to activate integration on.
        """
        pulumi.set(__self__, "external_wiki_url", external_wiki_url)
        pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="externalWikiUrl")
    def external_wiki_url(self) -> pulumi.Input[str]:
        """
        The URL of the external wiki.
        """
        return pulumi.get(self, "external_wiki_url")

    @external_wiki_url.setter
    def external_wiki_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "external_wiki_url", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        ID of the project you want to activate integration on.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _IntegrationExternalWikiState:
    def __init__(__self__, *,
                 active: Optional[pulumi.Input[bool]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 external_wiki_url: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IntegrationExternalWiki resources.
        :param pulumi.Input[bool] active: Whether the integration is active.
        :param pulumi.Input[str] created_at: The ISO8601 date/time that this integration was activated at in UTC.
        :param pulumi.Input[str] external_wiki_url: The URL of the external wiki.
        :param pulumi.Input[str] project: ID of the project you want to activate integration on.
        :param pulumi.Input[str] slug: The name of the integration in lowercase, shortened to 63 bytes, and with everything except 0-9 and a-z replaced with -. No leading / trailing -. Use in URLs, host names and domain names.
        :param pulumi.Input[str] title: Title of the integration.
        :param pulumi.Input[str] updated_at: The ISO8601 date/time that this integration was last updated at in UTC.
        """
        if active is not None:
            pulumi.set(__self__, "active", active)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if external_wiki_url is not None:
            pulumi.set(__self__, "external_wiki_url", external_wiki_url)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if slug is not None:
            pulumi.set(__self__, "slug", slug)
        if title is not None:
            pulumi.set(__self__, "title", title)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the integration is active.
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The ISO8601 date/time that this integration was activated at in UTC.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="externalWikiUrl")
    def external_wiki_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the external wiki.
        """
        return pulumi.get(self, "external_wiki_url")

    @external_wiki_url.setter
    def external_wiki_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_wiki_url", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the project you want to activate integration on.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def slug(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the integration in lowercase, shortened to 63 bytes, and with everything except 0-9 and a-z replaced with -. No leading / trailing -. Use in URLs, host names and domain names.
        """
        return pulumi.get(self, "slug")

    @slug.setter
    def slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slug", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        Title of the integration.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        The ISO8601 date/time that this integration was last updated at in UTC.
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)


class IntegrationExternalWiki(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 external_wiki_url: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The `IntegrationExternalWiki` resource allows to manage the lifecycle of a project integration with External Wiki Service.

        **Upstream API**: [GitLab REST API docs](https://docs.gitlab.com/ee/api/integrations.html#external-wiki)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gitlab as gitlab

        awesome_project = gitlab.Project("awesome_project",
            name="awesome_project",
            description="My awesome project.",
            visibility_level="public")
        wiki = gitlab.IntegrationExternalWiki("wiki",
            project=awesome_project.id,
            external_wiki_url="https://MyAwesomeExternalWikiURL.com")
        ```

        ## Import

        You can import a gitlab_integration_external_wiki state using the project ID, e.g.

        ```sh
        $ pulumi import gitlab:index/integrationExternalWiki:IntegrationExternalWiki wiki 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] external_wiki_url: The URL of the external wiki.
        :param pulumi.Input[str] project: ID of the project you want to activate integration on.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationExternalWikiArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The `IntegrationExternalWiki` resource allows to manage the lifecycle of a project integration with External Wiki Service.

        **Upstream API**: [GitLab REST API docs](https://docs.gitlab.com/ee/api/integrations.html#external-wiki)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gitlab as gitlab

        awesome_project = gitlab.Project("awesome_project",
            name="awesome_project",
            description="My awesome project.",
            visibility_level="public")
        wiki = gitlab.IntegrationExternalWiki("wiki",
            project=awesome_project.id,
            external_wiki_url="https://MyAwesomeExternalWikiURL.com")
        ```

        ## Import

        You can import a gitlab_integration_external_wiki state using the project ID, e.g.

        ```sh
        $ pulumi import gitlab:index/integrationExternalWiki:IntegrationExternalWiki wiki 1
        ```

        :param str resource_name: The name of the resource.
        :param IntegrationExternalWikiArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationExternalWikiArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 external_wiki_url: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IntegrationExternalWikiArgs.__new__(IntegrationExternalWikiArgs)

            if external_wiki_url is None and not opts.urn:
                raise TypeError("Missing required property 'external_wiki_url'")
            __props__.__dict__["external_wiki_url"] = external_wiki_url
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            __props__.__dict__["active"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["slug"] = None
            __props__.__dict__["title"] = None
            __props__.__dict__["updated_at"] = None
        super(IntegrationExternalWiki, __self__).__init__(
            'gitlab:index/integrationExternalWiki:IntegrationExternalWiki',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            active: Optional[pulumi.Input[bool]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            external_wiki_url: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            slug: Optional[pulumi.Input[str]] = None,
            title: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'IntegrationExternalWiki':
        """
        Get an existing IntegrationExternalWiki resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: Whether the integration is active.
        :param pulumi.Input[str] created_at: The ISO8601 date/time that this integration was activated at in UTC.
        :param pulumi.Input[str] external_wiki_url: The URL of the external wiki.
        :param pulumi.Input[str] project: ID of the project you want to activate integration on.
        :param pulumi.Input[str] slug: The name of the integration in lowercase, shortened to 63 bytes, and with everything except 0-9 and a-z replaced with -. No leading / trailing -. Use in URLs, host names and domain names.
        :param pulumi.Input[str] title: Title of the integration.
        :param pulumi.Input[str] updated_at: The ISO8601 date/time that this integration was last updated at in UTC.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IntegrationExternalWikiState.__new__(_IntegrationExternalWikiState)

        __props__.__dict__["active"] = active
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["external_wiki_url"] = external_wiki_url
        __props__.__dict__["project"] = project
        __props__.__dict__["slug"] = slug
        __props__.__dict__["title"] = title
        __props__.__dict__["updated_at"] = updated_at
        return IntegrationExternalWiki(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Output[bool]:
        """
        Whether the integration is active.
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The ISO8601 date/time that this integration was activated at in UTC.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="externalWikiUrl")
    def external_wiki_url(self) -> pulumi.Output[str]:
        """
        The URL of the external wiki.
        """
        return pulumi.get(self, "external_wiki_url")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        ID of the project you want to activate integration on.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def slug(self) -> pulumi.Output[str]:
        """
        The name of the integration in lowercase, shortened to 63 bytes, and with everything except 0-9 and a-z replaced with -. No leading / trailing -. Use in URLs, host names and domain names.
        """
        return pulumi.get(self, "slug")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        Title of the integration.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The ISO8601 date/time that this integration was last updated at in UTC.
        """
        return pulumi.get(self, "updated_at")

