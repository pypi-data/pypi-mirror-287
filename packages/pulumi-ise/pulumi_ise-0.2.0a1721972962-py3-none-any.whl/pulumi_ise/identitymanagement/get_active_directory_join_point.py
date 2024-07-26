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

__all__ = [
    'GetActiveDirectoryJoinPointResult',
    'AwaitableGetActiveDirectoryJoinPointResult',
    'get_active_directory_join_point',
    'get_active_directory_join_point_output',
]

@pulumi.output_type
class GetActiveDirectoryJoinPointResult:
    """
    A collection of values returned by getActiveDirectoryJoinPoint.
    """
    def __init__(__self__, ad_scopes_names=None, aging_time=None, attributes=None, auth_protection_type=None, country=None, department=None, description=None, domain=None, email=None, enable_callback_for_dialin_client=None, enable_dialin_permission_check=None, enable_domain_allowed_list=None, enable_failed_auth_protection=None, enable_machine_access=None, enable_machine_auth=None, enable_pass_change=None, enable_rewrites=None, failed_auth_threshold=None, first_name=None, groups=None, id=None, identity_not_in_ad_behaviour=None, job_title=None, last_name=None, locality=None, name=None, organizational_unit=None, plaintext_auth=None, rewrite_rules=None, schema=None, state_or_province=None, street_address=None, telephone=None, unreachable_domains_behaviour=None):
        if ad_scopes_names and not isinstance(ad_scopes_names, str):
            raise TypeError("Expected argument 'ad_scopes_names' to be a str")
        pulumi.set(__self__, "ad_scopes_names", ad_scopes_names)
        if aging_time and not isinstance(aging_time, int):
            raise TypeError("Expected argument 'aging_time' to be a int")
        pulumi.set(__self__, "aging_time", aging_time)
        if attributes and not isinstance(attributes, list):
            raise TypeError("Expected argument 'attributes' to be a list")
        pulumi.set(__self__, "attributes", attributes)
        if auth_protection_type and not isinstance(auth_protection_type, str):
            raise TypeError("Expected argument 'auth_protection_type' to be a str")
        pulumi.set(__self__, "auth_protection_type", auth_protection_type)
        if country and not isinstance(country, str):
            raise TypeError("Expected argument 'country' to be a str")
        pulumi.set(__self__, "country", country)
        if department and not isinstance(department, str):
            raise TypeError("Expected argument 'department' to be a str")
        pulumi.set(__self__, "department", department)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if enable_callback_for_dialin_client and not isinstance(enable_callback_for_dialin_client, bool):
            raise TypeError("Expected argument 'enable_callback_for_dialin_client' to be a bool")
        pulumi.set(__self__, "enable_callback_for_dialin_client", enable_callback_for_dialin_client)
        if enable_dialin_permission_check and not isinstance(enable_dialin_permission_check, bool):
            raise TypeError("Expected argument 'enable_dialin_permission_check' to be a bool")
        pulumi.set(__self__, "enable_dialin_permission_check", enable_dialin_permission_check)
        if enable_domain_allowed_list and not isinstance(enable_domain_allowed_list, bool):
            raise TypeError("Expected argument 'enable_domain_allowed_list' to be a bool")
        pulumi.set(__self__, "enable_domain_allowed_list", enable_domain_allowed_list)
        if enable_failed_auth_protection and not isinstance(enable_failed_auth_protection, bool):
            raise TypeError("Expected argument 'enable_failed_auth_protection' to be a bool")
        pulumi.set(__self__, "enable_failed_auth_protection", enable_failed_auth_protection)
        if enable_machine_access and not isinstance(enable_machine_access, bool):
            raise TypeError("Expected argument 'enable_machine_access' to be a bool")
        pulumi.set(__self__, "enable_machine_access", enable_machine_access)
        if enable_machine_auth and not isinstance(enable_machine_auth, bool):
            raise TypeError("Expected argument 'enable_machine_auth' to be a bool")
        pulumi.set(__self__, "enable_machine_auth", enable_machine_auth)
        if enable_pass_change and not isinstance(enable_pass_change, bool):
            raise TypeError("Expected argument 'enable_pass_change' to be a bool")
        pulumi.set(__self__, "enable_pass_change", enable_pass_change)
        if enable_rewrites and not isinstance(enable_rewrites, bool):
            raise TypeError("Expected argument 'enable_rewrites' to be a bool")
        pulumi.set(__self__, "enable_rewrites", enable_rewrites)
        if failed_auth_threshold and not isinstance(failed_auth_threshold, int):
            raise TypeError("Expected argument 'failed_auth_threshold' to be a int")
        pulumi.set(__self__, "failed_auth_threshold", failed_auth_threshold)
        if first_name and not isinstance(first_name, str):
            raise TypeError("Expected argument 'first_name' to be a str")
        pulumi.set(__self__, "first_name", first_name)
        if groups and not isinstance(groups, list):
            raise TypeError("Expected argument 'groups' to be a list")
        pulumi.set(__self__, "groups", groups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity_not_in_ad_behaviour and not isinstance(identity_not_in_ad_behaviour, str):
            raise TypeError("Expected argument 'identity_not_in_ad_behaviour' to be a str")
        pulumi.set(__self__, "identity_not_in_ad_behaviour", identity_not_in_ad_behaviour)
        if job_title and not isinstance(job_title, str):
            raise TypeError("Expected argument 'job_title' to be a str")
        pulumi.set(__self__, "job_title", job_title)
        if last_name and not isinstance(last_name, str):
            raise TypeError("Expected argument 'last_name' to be a str")
        pulumi.set(__self__, "last_name", last_name)
        if locality and not isinstance(locality, str):
            raise TypeError("Expected argument 'locality' to be a str")
        pulumi.set(__self__, "locality", locality)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if organizational_unit and not isinstance(organizational_unit, str):
            raise TypeError("Expected argument 'organizational_unit' to be a str")
        pulumi.set(__self__, "organizational_unit", organizational_unit)
        if plaintext_auth and not isinstance(plaintext_auth, bool):
            raise TypeError("Expected argument 'plaintext_auth' to be a bool")
        pulumi.set(__self__, "plaintext_auth", plaintext_auth)
        if rewrite_rules and not isinstance(rewrite_rules, list):
            raise TypeError("Expected argument 'rewrite_rules' to be a list")
        pulumi.set(__self__, "rewrite_rules", rewrite_rules)
        if schema and not isinstance(schema, str):
            raise TypeError("Expected argument 'schema' to be a str")
        pulumi.set(__self__, "schema", schema)
        if state_or_province and not isinstance(state_or_province, str):
            raise TypeError("Expected argument 'state_or_province' to be a str")
        pulumi.set(__self__, "state_or_province", state_or_province)
        if street_address and not isinstance(street_address, str):
            raise TypeError("Expected argument 'street_address' to be a str")
        pulumi.set(__self__, "street_address", street_address)
        if telephone and not isinstance(telephone, str):
            raise TypeError("Expected argument 'telephone' to be a str")
        pulumi.set(__self__, "telephone", telephone)
        if unreachable_domains_behaviour and not isinstance(unreachable_domains_behaviour, str):
            raise TypeError("Expected argument 'unreachable_domains_behaviour' to be a str")
        pulumi.set(__self__, "unreachable_domains_behaviour", unreachable_domains_behaviour)

    @property
    @pulumi.getter(name="adScopesNames")
    def ad_scopes_names(self) -> str:
        """
        String that contains the names of the scopes that the active directory belongs to. Names are separated by comma.
        """
        return pulumi.get(self, "ad_scopes_names")

    @property
    @pulumi.getter(name="agingTime")
    def aging_time(self) -> int:
        """
        Aging Time
        """
        return pulumi.get(self, "aging_time")

    @property
    @pulumi.getter
    def attributes(self) -> Sequence['outputs.GetActiveDirectoryJoinPointAttributeResult']:
        """
        List of AD attributes
        """
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="authProtectionType")
    def auth_protection_type(self) -> str:
        """
        Enable prevent AD account lockout for WIRELESS/WIRED/BOTH
        """
        return pulumi.get(self, "auth_protection_type")

    @property
    @pulumi.getter
    def country(self) -> str:
        """
        User info attribute
        """
        return pulumi.get(self, "country")

    @property
    @pulumi.getter
    def department(self) -> str:
        """
        User info attribute
        """
        return pulumi.get(self, "department")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Join point description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def domain(self) -> str:
        """
        AD domain associated with the join point
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        User info attribute
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="enableCallbackForDialinClient")
    def enable_callback_for_dialin_client(self) -> bool:
        """
        Enable Callback For Dial In Client
        """
        return pulumi.get(self, "enable_callback_for_dialin_client")

    @property
    @pulumi.getter(name="enableDialinPermissionCheck")
    def enable_dialin_permission_check(self) -> bool:
        """
        Enable Dial In Permission Check
        """
        return pulumi.get(self, "enable_dialin_permission_check")

    @property
    @pulumi.getter(name="enableDomainAllowedList")
    def enable_domain_allowed_list(self) -> bool:
        return pulumi.get(self, "enable_domain_allowed_list")

    @property
    @pulumi.getter(name="enableFailedAuthProtection")
    def enable_failed_auth_protection(self) -> bool:
        """
        Enable prevent AD account lockout due to too many bad password attempts
        """
        return pulumi.get(self, "enable_failed_auth_protection")

    @property
    @pulumi.getter(name="enableMachineAccess")
    def enable_machine_access(self) -> bool:
        """
        Enable Machine Access
        """
        return pulumi.get(self, "enable_machine_access")

    @property
    @pulumi.getter(name="enableMachineAuth")
    def enable_machine_auth(self) -> bool:
        """
        Enable Machine Authentication
        """
        return pulumi.get(self, "enable_machine_auth")

    @property
    @pulumi.getter(name="enablePassChange")
    def enable_pass_change(self) -> bool:
        """
        Enable Password Change
        """
        return pulumi.get(self, "enable_pass_change")

    @property
    @pulumi.getter(name="enableRewrites")
    def enable_rewrites(self) -> bool:
        """
        Enable Rewrites
        """
        return pulumi.get(self, "enable_rewrites")

    @property
    @pulumi.getter(name="failedAuthThreshold")
    def failed_auth_threshold(self) -> int:
        """
        Number of bad password attempts
        """
        return pulumi.get(self, "failed_auth_threshold")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> str:
        """
        User info attribute
        """
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter
    def groups(self) -> Sequence['outputs.GetActiveDirectoryJoinPointGroupResult']:
        """
        List of AD Groups
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the object
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="identityNotInAdBehaviour")
    def identity_not_in_ad_behaviour(self) -> str:
        """
        Identity Not In AD Behaviour
        """
        return pulumi.get(self, "identity_not_in_ad_behaviour")

    @property
    @pulumi.getter(name="jobTitle")
    def job_title(self) -> str:
        """
        User info attribute
        """
        return pulumi.get(self, "job_title")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> str:
        """
        User info attribute
        """
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter
    def locality(self) -> str:
        """
        User info attribute
        """
        return pulumi.get(self, "locality")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the active directory join point
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationalUnit")
    def organizational_unit(self) -> str:
        """
        User info attribute
        """
        return pulumi.get(self, "organizational_unit")

    @property
    @pulumi.getter(name="plaintextAuth")
    def plaintext_auth(self) -> bool:
        """
        Plain Text Authentication
        """
        return pulumi.get(self, "plaintext_auth")

    @property
    @pulumi.getter(name="rewriteRules")
    def rewrite_rules(self) -> Sequence['outputs.GetActiveDirectoryJoinPointRewriteRuleResult']:
        """
        List of Rewrite rules
        """
        return pulumi.get(self, "rewrite_rules")

    @property
    @pulumi.getter
    def schema(self) -> str:
        """
        Schema
        """
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter(name="stateOrProvince")
    def state_or_province(self) -> str:
        """
        User info attribute
        """
        return pulumi.get(self, "state_or_province")

    @property
    @pulumi.getter(name="streetAddress")
    def street_address(self) -> str:
        """
        User info attribute
        """
        return pulumi.get(self, "street_address")

    @property
    @pulumi.getter
    def telephone(self) -> str:
        """
        User info attribute
        """
        return pulumi.get(self, "telephone")

    @property
    @pulumi.getter(name="unreachableDomainsBehaviour")
    def unreachable_domains_behaviour(self) -> str:
        """
        Unreachable Domains Behaviour
        """
        return pulumi.get(self, "unreachable_domains_behaviour")


class AwaitableGetActiveDirectoryJoinPointResult(GetActiveDirectoryJoinPointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetActiveDirectoryJoinPointResult(
            ad_scopes_names=self.ad_scopes_names,
            aging_time=self.aging_time,
            attributes=self.attributes,
            auth_protection_type=self.auth_protection_type,
            country=self.country,
            department=self.department,
            description=self.description,
            domain=self.domain,
            email=self.email,
            enable_callback_for_dialin_client=self.enable_callback_for_dialin_client,
            enable_dialin_permission_check=self.enable_dialin_permission_check,
            enable_domain_allowed_list=self.enable_domain_allowed_list,
            enable_failed_auth_protection=self.enable_failed_auth_protection,
            enable_machine_access=self.enable_machine_access,
            enable_machine_auth=self.enable_machine_auth,
            enable_pass_change=self.enable_pass_change,
            enable_rewrites=self.enable_rewrites,
            failed_auth_threshold=self.failed_auth_threshold,
            first_name=self.first_name,
            groups=self.groups,
            id=self.id,
            identity_not_in_ad_behaviour=self.identity_not_in_ad_behaviour,
            job_title=self.job_title,
            last_name=self.last_name,
            locality=self.locality,
            name=self.name,
            organizational_unit=self.organizational_unit,
            plaintext_auth=self.plaintext_auth,
            rewrite_rules=self.rewrite_rules,
            schema=self.schema,
            state_or_province=self.state_or_province,
            street_address=self.street_address,
            telephone=self.telephone,
            unreachable_domains_behaviour=self.unreachable_domains_behaviour)


def get_active_directory_join_point(id: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetActiveDirectoryJoinPointResult:
    """
    This data source can read the Active Directory Join Point.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ise as ise

    example = ise.identitymanagement.get_active_directory_join_point(id="76d24097-41c4-4558-a4d0-a8c07ac08470")
    ```


    :param str id: The id of the object
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ise:identitymanagement/getActiveDirectoryJoinPoint:getActiveDirectoryJoinPoint', __args__, opts=opts, typ=GetActiveDirectoryJoinPointResult).value

    return AwaitableGetActiveDirectoryJoinPointResult(
        ad_scopes_names=pulumi.get(__ret__, 'ad_scopes_names'),
        aging_time=pulumi.get(__ret__, 'aging_time'),
        attributes=pulumi.get(__ret__, 'attributes'),
        auth_protection_type=pulumi.get(__ret__, 'auth_protection_type'),
        country=pulumi.get(__ret__, 'country'),
        department=pulumi.get(__ret__, 'department'),
        description=pulumi.get(__ret__, 'description'),
        domain=pulumi.get(__ret__, 'domain'),
        email=pulumi.get(__ret__, 'email'),
        enable_callback_for_dialin_client=pulumi.get(__ret__, 'enable_callback_for_dialin_client'),
        enable_dialin_permission_check=pulumi.get(__ret__, 'enable_dialin_permission_check'),
        enable_domain_allowed_list=pulumi.get(__ret__, 'enable_domain_allowed_list'),
        enable_failed_auth_protection=pulumi.get(__ret__, 'enable_failed_auth_protection'),
        enable_machine_access=pulumi.get(__ret__, 'enable_machine_access'),
        enable_machine_auth=pulumi.get(__ret__, 'enable_machine_auth'),
        enable_pass_change=pulumi.get(__ret__, 'enable_pass_change'),
        enable_rewrites=pulumi.get(__ret__, 'enable_rewrites'),
        failed_auth_threshold=pulumi.get(__ret__, 'failed_auth_threshold'),
        first_name=pulumi.get(__ret__, 'first_name'),
        groups=pulumi.get(__ret__, 'groups'),
        id=pulumi.get(__ret__, 'id'),
        identity_not_in_ad_behaviour=pulumi.get(__ret__, 'identity_not_in_ad_behaviour'),
        job_title=pulumi.get(__ret__, 'job_title'),
        last_name=pulumi.get(__ret__, 'last_name'),
        locality=pulumi.get(__ret__, 'locality'),
        name=pulumi.get(__ret__, 'name'),
        organizational_unit=pulumi.get(__ret__, 'organizational_unit'),
        plaintext_auth=pulumi.get(__ret__, 'plaintext_auth'),
        rewrite_rules=pulumi.get(__ret__, 'rewrite_rules'),
        schema=pulumi.get(__ret__, 'schema'),
        state_or_province=pulumi.get(__ret__, 'state_or_province'),
        street_address=pulumi.get(__ret__, 'street_address'),
        telephone=pulumi.get(__ret__, 'telephone'),
        unreachable_domains_behaviour=pulumi.get(__ret__, 'unreachable_domains_behaviour'))


@_utilities.lift_output_func(get_active_directory_join_point)
def get_active_directory_join_point_output(id: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetActiveDirectoryJoinPointResult]:
    """
    This data source can read the Active Directory Join Point.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ise as ise

    example = ise.identitymanagement.get_active_directory_join_point(id="76d24097-41c4-4558-a4d0-a8c07ac08470")
    ```


    :param str id: The id of the object
    """
    ...
