# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProjectColumnArgs', 'ProjectColumn']

@pulumi.input_type
class ProjectColumnArgs:
    def __init__(__self__, *,
                 project_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ProjectColumn resource.
        :param pulumi.Input[str] project_id: The ID of an existing project that the column will be created in.
        :param pulumi.Input[str] name: The name of the column.
        """
        pulumi.set(__self__, "project_id", project_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        The ID of an existing project that the column will be created in.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the column.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ProjectColumnState:
    def __init__(__self__, *,
                 column_id: Optional[pulumi.Input[int]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ProjectColumn resources.
        :param pulumi.Input[int] column_id: The ID of the column.
        :param pulumi.Input[str] name: The name of the column.
        :param pulumi.Input[str] project_id: The ID of an existing project that the column will be created in.
        """
        if column_id is not None:
            pulumi.set(__self__, "column_id", column_id)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)

    @property
    @pulumi.getter(name="columnId")
    def column_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the column.
        """
        return pulumi.get(self, "column_id")

    @column_id.setter
    def column_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "column_id", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the column.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of an existing project that the column will be created in.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)


class ProjectColumn(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource allows you to create and manage columns for GitHub projects.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_github as github

        project = github.OrganizationProject("project",
            name="A Organization Project",
            body="This is an organization project.")
        column = github.ProjectColumn("column",
            project_id=project.id,
            name="a column")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the column.
        :param pulumi.Input[str] project_id: The ID of an existing project that the column will be created in.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectColumnArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource allows you to create and manage columns for GitHub projects.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_github as github

        project = github.OrganizationProject("project",
            name="A Organization Project",
            body="This is an organization project.")
        column = github.ProjectColumn("column",
            project_id=project.id,
            name="a column")
        ```

        :param str resource_name: The name of the resource.
        :param ProjectColumnArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectColumnArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectColumnArgs.__new__(ProjectColumnArgs)

            __props__.__dict__["name"] = name
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["column_id"] = None
            __props__.__dict__["etag"] = None
        super(ProjectColumn, __self__).__init__(
            'github:index/projectColumn:ProjectColumn',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            column_id: Optional[pulumi.Input[int]] = None,
            etag: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None) -> 'ProjectColumn':
        """
        Get an existing ProjectColumn resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] column_id: The ID of the column.
        :param pulumi.Input[str] name: The name of the column.
        :param pulumi.Input[str] project_id: The ID of an existing project that the column will be created in.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProjectColumnState.__new__(_ProjectColumnState)

        __props__.__dict__["column_id"] = column_id
        __props__.__dict__["etag"] = etag
        __props__.__dict__["name"] = name
        __props__.__dict__["project_id"] = project_id
        return ProjectColumn(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="columnId")
    def column_id(self) -> pulumi.Output[int]:
        """
        The ID of the column.
        """
        return pulumi.get(self, "column_id")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the column.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The ID of an existing project that the column will be created in.
        """
        return pulumi.get(self, "project_id")

