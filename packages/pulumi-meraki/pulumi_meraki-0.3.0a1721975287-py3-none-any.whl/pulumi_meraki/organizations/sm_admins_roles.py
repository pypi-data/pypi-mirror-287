# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SmAdminsRolesArgs', 'SmAdminsRoles']

@pulumi.input_type
class SmAdminsRolesArgs:
    def __init__(__self__, *,
                 organization_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 role_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a SmAdminsRoles resource.
        :param pulumi.Input[str] organization_id: organizationId path parameter. Organization ID
        :param pulumi.Input[str] name: The name of the limited access role
        :param pulumi.Input[str] role_id: The Id of the limited access role
        :param pulumi.Input[str] scope: The scope of the limited access role
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags of the limited access role
        """
        pulumi.set(__self__, "organization_id", organization_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if role_id is not None:
            pulumi.set(__self__, "role_id", role_id)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Input[str]:
        """
        organizationId path parameter. Organization ID
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the limited access role
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Id of the limited access role
        """
        return pulumi.get(self, "role_id")

    @role_id.setter
    def role_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_id", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        The scope of the limited access role
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The tags of the limited access role
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _SmAdminsRolesState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 role_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering SmAdminsRoles resources.
        :param pulumi.Input[str] name: The name of the limited access role
        :param pulumi.Input[str] organization_id: organizationId path parameter. Organization ID
        :param pulumi.Input[str] role_id: The Id of the limited access role
        :param pulumi.Input[str] scope: The scope of the limited access role
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags of the limited access role
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if role_id is not None:
            pulumi.set(__self__, "role_id", role_id)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the limited access role
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[str]]:
        """
        organizationId path parameter. Organization ID
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Id of the limited access role
        """
        return pulumi.get(self, "role_id")

    @role_id.setter
    def role_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_id", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        The scope of the limited access role
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The tags of the limited access role
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class SmAdminsRoles(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 role_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_meraki as meraki

        example = meraki.organizations.SmAdminsRoles("example",
            name="sample name",
            organization_id="string",
            scope="all_tags",
            tags=["tag"])
        pulumi.export("merakiOrganizationsSmAdminsRolesExample", example)
        ```

        ## Import

        ```sh
        $ pulumi import meraki:organizations/smAdminsRoles:SmAdminsRoles example "organization_id,role_id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the limited access role
        :param pulumi.Input[str] organization_id: organizationId path parameter. Organization ID
        :param pulumi.Input[str] role_id: The Id of the limited access role
        :param pulumi.Input[str] scope: The scope of the limited access role
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags of the limited access role
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SmAdminsRolesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_meraki as meraki

        example = meraki.organizations.SmAdminsRoles("example",
            name="sample name",
            organization_id="string",
            scope="all_tags",
            tags=["tag"])
        pulumi.export("merakiOrganizationsSmAdminsRolesExample", example)
        ```

        ## Import

        ```sh
        $ pulumi import meraki:organizations/smAdminsRoles:SmAdminsRoles example "organization_id,role_id"
        ```

        :param str resource_name: The name of the resource.
        :param SmAdminsRolesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SmAdminsRolesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 role_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SmAdminsRolesArgs.__new__(SmAdminsRolesArgs)

            __props__.__dict__["name"] = name
            if organization_id is None and not opts.urn:
                raise TypeError("Missing required property 'organization_id'")
            __props__.__dict__["organization_id"] = organization_id
            __props__.__dict__["role_id"] = role_id
            __props__.__dict__["scope"] = scope
            __props__.__dict__["tags"] = tags
        super(SmAdminsRoles, __self__).__init__(
            'meraki:organizations/smAdminsRoles:SmAdminsRoles',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            role_id: Optional[pulumi.Input[str]] = None,
            scope: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'SmAdminsRoles':
        """
        Get an existing SmAdminsRoles resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the limited access role
        :param pulumi.Input[str] organization_id: organizationId path parameter. Organization ID
        :param pulumi.Input[str] role_id: The Id of the limited access role
        :param pulumi.Input[str] scope: The scope of the limited access role
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags of the limited access role
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SmAdminsRolesState.__new__(_SmAdminsRolesState)

        __props__.__dict__["name"] = name
        __props__.__dict__["organization_id"] = organization_id
        __props__.__dict__["role_id"] = role_id
        __props__.__dict__["scope"] = scope
        __props__.__dict__["tags"] = tags
        return SmAdminsRoles(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the limited access role
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        organizationId path parameter. Organization ID
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> pulumi.Output[str]:
        """
        The Id of the limited access role
        """
        return pulumi.get(self, "role_id")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[str]:
        """
        The scope of the limited access role
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[str]]:
        """
        The tags of the limited access role
        """
        return pulumi.get(self, "tags")

