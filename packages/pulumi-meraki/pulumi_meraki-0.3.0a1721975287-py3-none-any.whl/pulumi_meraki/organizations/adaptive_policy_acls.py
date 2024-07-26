# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['AdaptivePolicyAclsArgs', 'AdaptivePolicyAcls']

@pulumi.input_type
class AdaptivePolicyAclsArgs:
    def __init__(__self__, *,
                 organization_id: pulumi.Input[str],
                 acl_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ip_version: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['AdaptivePolicyAclsRuleArgs']]]] = None):
        """
        The set of arguments for constructing a AdaptivePolicyAcls resource.
        :param pulumi.Input[str] organization_id: organizationId path parameter. Organization ID
        :param pulumi.Input[str] acl_id: ID of the adaptive policy ACL
        :param pulumi.Input[str] description: Description of the adaptive policy ACL
        :param pulumi.Input[str] ip_version: IP version of adpative policy ACL
        :param pulumi.Input[str] name: Name of the adaptive policy ACL
        :param pulumi.Input[Sequence[pulumi.Input['AdaptivePolicyAclsRuleArgs']]] rules: An ordered array of the adaptive policy ACL rules
        """
        pulumi.set(__self__, "organization_id", organization_id)
        if acl_id is not None:
            pulumi.set(__self__, "acl_id", acl_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if ip_version is not None:
            pulumi.set(__self__, "ip_version", ip_version)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)

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
    @pulumi.getter(name="aclId")
    def acl_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the adaptive policy ACL
        """
        return pulumi.get(self, "acl_id")

    @acl_id.setter
    def acl_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acl_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the adaptive policy ACL
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> Optional[pulumi.Input[str]]:
        """
        IP version of adpative policy ACL
        """
        return pulumi.get(self, "ip_version")

    @ip_version.setter
    def ip_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_version", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the adaptive policy ACL
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AdaptivePolicyAclsRuleArgs']]]]:
        """
        An ordered array of the adaptive policy ACL rules
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AdaptivePolicyAclsRuleArgs']]]]):
        pulumi.set(self, "rules", value)


@pulumi.input_type
class _AdaptivePolicyAclsState:
    def __init__(__self__, *,
                 acl_id: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ip_version: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['AdaptivePolicyAclsRuleArgs']]]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AdaptivePolicyAcls resources.
        :param pulumi.Input[str] acl_id: ID of the adaptive policy ACL
        :param pulumi.Input[str] created_at: When the adaptive policy ACL was created
        :param pulumi.Input[str] description: Description of the adaptive policy ACL
        :param pulumi.Input[str] ip_version: IP version of adpative policy ACL
        :param pulumi.Input[str] name: Name of the adaptive policy ACL
        :param pulumi.Input[str] organization_id: organizationId path parameter. Organization ID
        :param pulumi.Input[Sequence[pulumi.Input['AdaptivePolicyAclsRuleArgs']]] rules: An ordered array of the adaptive policy ACL rules
        :param pulumi.Input[str] updated_at: When the adaptive policy ACL was last updated
        """
        if acl_id is not None:
            pulumi.set(__self__, "acl_id", acl_id)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if ip_version is not None:
            pulumi.set(__self__, "ip_version", ip_version)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="aclId")
    def acl_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the adaptive policy ACL
        """
        return pulumi.get(self, "acl_id")

    @acl_id.setter
    def acl_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acl_id", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        When the adaptive policy ACL was created
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the adaptive policy ACL
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> Optional[pulumi.Input[str]]:
        """
        IP version of adpative policy ACL
        """
        return pulumi.get(self, "ip_version")

    @ip_version.setter
    def ip_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_version", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the adaptive policy ACL
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
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AdaptivePolicyAclsRuleArgs']]]]:
        """
        An ordered array of the adaptive policy ACL rules
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AdaptivePolicyAclsRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        When the adaptive policy ACL was last updated
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)


class AdaptivePolicyAcls(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ip_version: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AdaptivePolicyAclsRuleArgs']]]]] = None,
                 __props__=None):
        """
        ## Example Usage

        ## Import

        ```sh
        $ pulumi import meraki:organizations/adaptivePolicyAcls:AdaptivePolicyAcls example "acl_id,organization_id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl_id: ID of the adaptive policy ACL
        :param pulumi.Input[str] description: Description of the adaptive policy ACL
        :param pulumi.Input[str] ip_version: IP version of adpative policy ACL
        :param pulumi.Input[str] name: Name of the adaptive policy ACL
        :param pulumi.Input[str] organization_id: organizationId path parameter. Organization ID
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AdaptivePolicyAclsRuleArgs']]]] rules: An ordered array of the adaptive policy ACL rules
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AdaptivePolicyAclsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ## Import

        ```sh
        $ pulumi import meraki:organizations/adaptivePolicyAcls:AdaptivePolicyAcls example "acl_id,organization_id"
        ```

        :param str resource_name: The name of the resource.
        :param AdaptivePolicyAclsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AdaptivePolicyAclsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ip_version: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AdaptivePolicyAclsRuleArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AdaptivePolicyAclsArgs.__new__(AdaptivePolicyAclsArgs)

            __props__.__dict__["acl_id"] = acl_id
            __props__.__dict__["description"] = description
            __props__.__dict__["ip_version"] = ip_version
            __props__.__dict__["name"] = name
            if organization_id is None and not opts.urn:
                raise TypeError("Missing required property 'organization_id'")
            __props__.__dict__["organization_id"] = organization_id
            __props__.__dict__["rules"] = rules
            __props__.__dict__["created_at"] = None
            __props__.__dict__["updated_at"] = None
        super(AdaptivePolicyAcls, __self__).__init__(
            'meraki:organizations/adaptivePolicyAcls:AdaptivePolicyAcls',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            acl_id: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            ip_version: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AdaptivePolicyAclsRuleArgs']]]]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'AdaptivePolicyAcls':
        """
        Get an existing AdaptivePolicyAcls resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl_id: ID of the adaptive policy ACL
        :param pulumi.Input[str] created_at: When the adaptive policy ACL was created
        :param pulumi.Input[str] description: Description of the adaptive policy ACL
        :param pulumi.Input[str] ip_version: IP version of adpative policy ACL
        :param pulumi.Input[str] name: Name of the adaptive policy ACL
        :param pulumi.Input[str] organization_id: organizationId path parameter. Organization ID
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AdaptivePolicyAclsRuleArgs']]]] rules: An ordered array of the adaptive policy ACL rules
        :param pulumi.Input[str] updated_at: When the adaptive policy ACL was last updated
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AdaptivePolicyAclsState.__new__(_AdaptivePolicyAclsState)

        __props__.__dict__["acl_id"] = acl_id
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["description"] = description
        __props__.__dict__["ip_version"] = ip_version
        __props__.__dict__["name"] = name
        __props__.__dict__["organization_id"] = organization_id
        __props__.__dict__["rules"] = rules
        __props__.__dict__["updated_at"] = updated_at
        return AdaptivePolicyAcls(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aclId")
    def acl_id(self) -> pulumi.Output[str]:
        """
        ID of the adaptive policy ACL
        """
        return pulumi.get(self, "acl_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        When the adaptive policy ACL was created
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Description of the adaptive policy ACL
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> pulumi.Output[str]:
        """
        IP version of adpative policy ACL
        """
        return pulumi.get(self, "ip_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the adaptive policy ACL
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
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.AdaptivePolicyAclsRule']]:
        """
        An ordered array of the adaptive policy ACL rules
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        When the adaptive policy ACL was last updated
        """
        return pulumi.get(self, "updated_at")

