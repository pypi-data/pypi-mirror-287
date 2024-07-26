# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['IntegrationJenkinsArgs', 'IntegrationJenkins']

@pulumi.input_type
class IntegrationJenkinsArgs:
    def __init__(__self__, *,
                 jenkins_url: pulumi.Input[str],
                 project: pulumi.Input[str],
                 project_name: pulumi.Input[str],
                 enable_ssl_verification: Optional[pulumi.Input[bool]] = None,
                 merge_request_events: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 push_events: Optional[pulumi.Input[bool]] = None,
                 tag_push_events: Optional[pulumi.Input[bool]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IntegrationJenkins resource.
        :param pulumi.Input[str] jenkins_url: Jenkins URL like `http://jenkins.example.com`
        :param pulumi.Input[str] project: ID of the project you want to activate integration on.
        :param pulumi.Input[str] project_name: The URL-friendly project name. Example: `my_project_name`.
        :param pulumi.Input[bool] enable_ssl_verification: Enable SSL verification. Defaults to `true` (enabled).
        :param pulumi.Input[bool] merge_request_events: Enable notifications for merge request events.
        :param pulumi.Input[str] password: Password for authentication with the Jenkins server, if authentication is required by the server.
        :param pulumi.Input[bool] push_events: Enable notifications for push events.
        :param pulumi.Input[bool] tag_push_events: Enable notifications for tag push events.
        :param pulumi.Input[str] username: Username for authentication with the Jenkins server, if authentication is required by the server.
        """
        pulumi.set(__self__, "jenkins_url", jenkins_url)
        pulumi.set(__self__, "project", project)
        pulumi.set(__self__, "project_name", project_name)
        if enable_ssl_verification is not None:
            pulumi.set(__self__, "enable_ssl_verification", enable_ssl_verification)
        if merge_request_events is not None:
            pulumi.set(__self__, "merge_request_events", merge_request_events)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if push_events is not None:
            pulumi.set(__self__, "push_events", push_events)
        if tag_push_events is not None:
            pulumi.set(__self__, "tag_push_events", tag_push_events)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="jenkinsUrl")
    def jenkins_url(self) -> pulumi.Input[str]:
        """
        Jenkins URL like `http://jenkins.example.com`
        """
        return pulumi.get(self, "jenkins_url")

    @jenkins_url.setter
    def jenkins_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "jenkins_url", value)

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

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[str]:
        """
        The URL-friendly project name. Example: `my_project_name`.
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_name", value)

    @property
    @pulumi.getter(name="enableSslVerification")
    def enable_ssl_verification(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable SSL verification. Defaults to `true` (enabled).
        """
        return pulumi.get(self, "enable_ssl_verification")

    @enable_ssl_verification.setter
    def enable_ssl_verification(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_ssl_verification", value)

    @property
    @pulumi.getter(name="mergeRequestEvents")
    def merge_request_events(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable notifications for merge request events.
        """
        return pulumi.get(self, "merge_request_events")

    @merge_request_events.setter
    def merge_request_events(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "merge_request_events", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password for authentication with the Jenkins server, if authentication is required by the server.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="pushEvents")
    def push_events(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable notifications for push events.
        """
        return pulumi.get(self, "push_events")

    @push_events.setter
    def push_events(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "push_events", value)

    @property
    @pulumi.getter(name="tagPushEvents")
    def tag_push_events(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable notifications for tag push events.
        """
        return pulumi.get(self, "tag_push_events")

    @tag_push_events.setter
    def tag_push_events(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "tag_push_events", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        Username for authentication with the Jenkins server, if authentication is required by the server.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


@pulumi.input_type
class _IntegrationJenkinsState:
    def __init__(__self__, *,
                 active: Optional[pulumi.Input[bool]] = None,
                 enable_ssl_verification: Optional[pulumi.Input[bool]] = None,
                 jenkins_url: Optional[pulumi.Input[str]] = None,
                 merge_request_events: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 push_events: Optional[pulumi.Input[bool]] = None,
                 tag_push_events: Optional[pulumi.Input[bool]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IntegrationJenkins resources.
        :param pulumi.Input[bool] active: Whether the integration is active.
        :param pulumi.Input[bool] enable_ssl_verification: Enable SSL verification. Defaults to `true` (enabled).
        :param pulumi.Input[str] jenkins_url: Jenkins URL like `http://jenkins.example.com`
        :param pulumi.Input[bool] merge_request_events: Enable notifications for merge request events.
        :param pulumi.Input[str] password: Password for authentication with the Jenkins server, if authentication is required by the server.
        :param pulumi.Input[str] project: ID of the project you want to activate integration on.
        :param pulumi.Input[str] project_name: The URL-friendly project name. Example: `my_project_name`.
        :param pulumi.Input[bool] push_events: Enable notifications for push events.
        :param pulumi.Input[bool] tag_push_events: Enable notifications for tag push events.
        :param pulumi.Input[str] username: Username for authentication with the Jenkins server, if authentication is required by the server.
        """
        if active is not None:
            pulumi.set(__self__, "active", active)
        if enable_ssl_verification is not None:
            pulumi.set(__self__, "enable_ssl_verification", enable_ssl_verification)
        if jenkins_url is not None:
            pulumi.set(__self__, "jenkins_url", jenkins_url)
        if merge_request_events is not None:
            pulumi.set(__self__, "merge_request_events", merge_request_events)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if project_name is not None:
            pulumi.set(__self__, "project_name", project_name)
        if push_events is not None:
            pulumi.set(__self__, "push_events", push_events)
        if tag_push_events is not None:
            pulumi.set(__self__, "tag_push_events", tag_push_events)
        if username is not None:
            pulumi.set(__self__, "username", username)

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
    @pulumi.getter(name="enableSslVerification")
    def enable_ssl_verification(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable SSL verification. Defaults to `true` (enabled).
        """
        return pulumi.get(self, "enable_ssl_verification")

    @enable_ssl_verification.setter
    def enable_ssl_verification(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_ssl_verification", value)

    @property
    @pulumi.getter(name="jenkinsUrl")
    def jenkins_url(self) -> Optional[pulumi.Input[str]]:
        """
        Jenkins URL like `http://jenkins.example.com`
        """
        return pulumi.get(self, "jenkins_url")

    @jenkins_url.setter
    def jenkins_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "jenkins_url", value)

    @property
    @pulumi.getter(name="mergeRequestEvents")
    def merge_request_events(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable notifications for merge request events.
        """
        return pulumi.get(self, "merge_request_events")

    @merge_request_events.setter
    def merge_request_events(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "merge_request_events", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password for authentication with the Jenkins server, if authentication is required by the server.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

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
    @pulumi.getter(name="projectName")
    def project_name(self) -> Optional[pulumi.Input[str]]:
        """
        The URL-friendly project name. Example: `my_project_name`.
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_name", value)

    @property
    @pulumi.getter(name="pushEvents")
    def push_events(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable notifications for push events.
        """
        return pulumi.get(self, "push_events")

    @push_events.setter
    def push_events(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "push_events", value)

    @property
    @pulumi.getter(name="tagPushEvents")
    def tag_push_events(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable notifications for tag push events.
        """
        return pulumi.get(self, "tag_push_events")

    @tag_push_events.setter
    def tag_push_events(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "tag_push_events", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        Username for authentication with the Jenkins server, if authentication is required by the server.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class IntegrationJenkins(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable_ssl_verification: Optional[pulumi.Input[bool]] = None,
                 jenkins_url: Optional[pulumi.Input[str]] = None,
                 merge_request_events: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 push_events: Optional[pulumi.Input[bool]] = None,
                 tag_push_events: Optional[pulumi.Input[bool]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The `IntegrationJenkins` resource allows to manage the lifecycle of a project integration with Jenkins.

        **Upstream API**: [GitLab REST API docs](https://docs.gitlab.com/ee/api/integrations.html#jenkins)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gitlab as gitlab

        awesome_project = gitlab.Project("awesome_project",
            name="awesome_project",
            description="My awesome project.",
            visibility_level="public")
        jenkins = gitlab.IntegrationJenkins("jenkins",
            project=awesome_project.id,
            jenkins_url="http://jenkins.example.com",
            project_name="my_project_name")
        ```

        ## Import

        ```sh
        $ pulumi import gitlab:index/integrationJenkins:IntegrationJenkins You can import a gitlab_integration_jenkins state using `<resource> <project_id>`:
        ```

        ```sh
        $ pulumi import gitlab:index/integrationJenkins:IntegrationJenkins jenkins 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable_ssl_verification: Enable SSL verification. Defaults to `true` (enabled).
        :param pulumi.Input[str] jenkins_url: Jenkins URL like `http://jenkins.example.com`
        :param pulumi.Input[bool] merge_request_events: Enable notifications for merge request events.
        :param pulumi.Input[str] password: Password for authentication with the Jenkins server, if authentication is required by the server.
        :param pulumi.Input[str] project: ID of the project you want to activate integration on.
        :param pulumi.Input[str] project_name: The URL-friendly project name. Example: `my_project_name`.
        :param pulumi.Input[bool] push_events: Enable notifications for push events.
        :param pulumi.Input[bool] tag_push_events: Enable notifications for tag push events.
        :param pulumi.Input[str] username: Username for authentication with the Jenkins server, if authentication is required by the server.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationJenkinsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The `IntegrationJenkins` resource allows to manage the lifecycle of a project integration with Jenkins.

        **Upstream API**: [GitLab REST API docs](https://docs.gitlab.com/ee/api/integrations.html#jenkins)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gitlab as gitlab

        awesome_project = gitlab.Project("awesome_project",
            name="awesome_project",
            description="My awesome project.",
            visibility_level="public")
        jenkins = gitlab.IntegrationJenkins("jenkins",
            project=awesome_project.id,
            jenkins_url="http://jenkins.example.com",
            project_name="my_project_name")
        ```

        ## Import

        ```sh
        $ pulumi import gitlab:index/integrationJenkins:IntegrationJenkins You can import a gitlab_integration_jenkins state using `<resource> <project_id>`:
        ```

        ```sh
        $ pulumi import gitlab:index/integrationJenkins:IntegrationJenkins jenkins 1
        ```

        :param str resource_name: The name of the resource.
        :param IntegrationJenkinsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationJenkinsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable_ssl_verification: Optional[pulumi.Input[bool]] = None,
                 jenkins_url: Optional[pulumi.Input[str]] = None,
                 merge_request_events: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 push_events: Optional[pulumi.Input[bool]] = None,
                 tag_push_events: Optional[pulumi.Input[bool]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IntegrationJenkinsArgs.__new__(IntegrationJenkinsArgs)

            __props__.__dict__["enable_ssl_verification"] = enable_ssl_verification
            if jenkins_url is None and not opts.urn:
                raise TypeError("Missing required property 'jenkins_url'")
            __props__.__dict__["jenkins_url"] = jenkins_url
            __props__.__dict__["merge_request_events"] = merge_request_events
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            if project_name is None and not opts.urn:
                raise TypeError("Missing required property 'project_name'")
            __props__.__dict__["project_name"] = project_name
            __props__.__dict__["push_events"] = push_events
            __props__.__dict__["tag_push_events"] = tag_push_events
            __props__.__dict__["username"] = username
            __props__.__dict__["active"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(IntegrationJenkins, __self__).__init__(
            'gitlab:index/integrationJenkins:IntegrationJenkins',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            active: Optional[pulumi.Input[bool]] = None,
            enable_ssl_verification: Optional[pulumi.Input[bool]] = None,
            jenkins_url: Optional[pulumi.Input[str]] = None,
            merge_request_events: Optional[pulumi.Input[bool]] = None,
            password: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            project_name: Optional[pulumi.Input[str]] = None,
            push_events: Optional[pulumi.Input[bool]] = None,
            tag_push_events: Optional[pulumi.Input[bool]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'IntegrationJenkins':
        """
        Get an existing IntegrationJenkins resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: Whether the integration is active.
        :param pulumi.Input[bool] enable_ssl_verification: Enable SSL verification. Defaults to `true` (enabled).
        :param pulumi.Input[str] jenkins_url: Jenkins URL like `http://jenkins.example.com`
        :param pulumi.Input[bool] merge_request_events: Enable notifications for merge request events.
        :param pulumi.Input[str] password: Password for authentication with the Jenkins server, if authentication is required by the server.
        :param pulumi.Input[str] project: ID of the project you want to activate integration on.
        :param pulumi.Input[str] project_name: The URL-friendly project name. Example: `my_project_name`.
        :param pulumi.Input[bool] push_events: Enable notifications for push events.
        :param pulumi.Input[bool] tag_push_events: Enable notifications for tag push events.
        :param pulumi.Input[str] username: Username for authentication with the Jenkins server, if authentication is required by the server.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IntegrationJenkinsState.__new__(_IntegrationJenkinsState)

        __props__.__dict__["active"] = active
        __props__.__dict__["enable_ssl_verification"] = enable_ssl_verification
        __props__.__dict__["jenkins_url"] = jenkins_url
        __props__.__dict__["merge_request_events"] = merge_request_events
        __props__.__dict__["password"] = password
        __props__.__dict__["project"] = project
        __props__.__dict__["project_name"] = project_name
        __props__.__dict__["push_events"] = push_events
        __props__.__dict__["tag_push_events"] = tag_push_events
        __props__.__dict__["username"] = username
        return IntegrationJenkins(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Output[bool]:
        """
        Whether the integration is active.
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter(name="enableSslVerification")
    def enable_ssl_verification(self) -> pulumi.Output[bool]:
        """
        Enable SSL verification. Defaults to `true` (enabled).
        """
        return pulumi.get(self, "enable_ssl_verification")

    @property
    @pulumi.getter(name="jenkinsUrl")
    def jenkins_url(self) -> pulumi.Output[str]:
        """
        Jenkins URL like `http://jenkins.example.com`
        """
        return pulumi.get(self, "jenkins_url")

    @property
    @pulumi.getter(name="mergeRequestEvents")
    def merge_request_events(self) -> pulumi.Output[bool]:
        """
        Enable notifications for merge request events.
        """
        return pulumi.get(self, "merge_request_events")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        Password for authentication with the Jenkins server, if authentication is required by the server.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        ID of the project you want to activate integration on.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Output[str]:
        """
        The URL-friendly project name. Example: `my_project_name`.
        """
        return pulumi.get(self, "project_name")

    @property
    @pulumi.getter(name="pushEvents")
    def push_events(self) -> pulumi.Output[bool]:
        """
        Enable notifications for push events.
        """
        return pulumi.get(self, "push_events")

    @property
    @pulumi.getter(name="tagPushEvents")
    def tag_push_events(self) -> pulumi.Output[bool]:
        """
        Enable notifications for tag push events.
        """
        return pulumi.get(self, "tag_push_events")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[Optional[str]]:
        """
        Username for authentication with the Jenkins server, if authentication is required by the server.
        """
        return pulumi.get(self, "username")

