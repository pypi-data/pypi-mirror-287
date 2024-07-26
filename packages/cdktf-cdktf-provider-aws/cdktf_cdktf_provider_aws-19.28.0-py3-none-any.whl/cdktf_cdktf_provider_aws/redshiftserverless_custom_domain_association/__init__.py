r'''
# `aws_redshiftserverless_custom_domain_association`

Refer to the Terraform Registry for docs: [`aws_redshiftserverless_custom_domain_association`](https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/redshiftserverless_custom_domain_association).
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class RedshiftserverlessCustomDomainAssociation(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.redshiftserverlessCustomDomainAssociation.RedshiftserverlessCustomDomainAssociation",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/redshiftserverless_custom_domain_association aws_redshiftserverless_custom_domain_association}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        custom_domain_certificate_arn: builtins.str,
        custom_domain_name: builtins.str,
        workgroup_name: builtins.str,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/redshiftserverless_custom_domain_association aws_redshiftserverless_custom_domain_association} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param custom_domain_certificate_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/redshiftserverless_custom_domain_association#custom_domain_certificate_arn RedshiftserverlessCustomDomainAssociation#custom_domain_certificate_arn}.
        :param custom_domain_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/redshiftserverless_custom_domain_association#custom_domain_name RedshiftserverlessCustomDomainAssociation#custom_domain_name}.
        :param workgroup_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/redshiftserverless_custom_domain_association#workgroup_name RedshiftserverlessCustomDomainAssociation#workgroup_name}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7779e87f207c007e54ee7db8809e4cb0d2ba4fd5e78e66b5fab12baafa45123)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = RedshiftserverlessCustomDomainAssociationConfig(
            custom_domain_certificate_arn=custom_domain_certificate_arn,
            custom_domain_name=custom_domain_name,
            workgroup_name=workgroup_name,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a RedshiftserverlessCustomDomainAssociation resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the RedshiftserverlessCustomDomainAssociation to import.
        :param import_from_id: The id of the existing RedshiftserverlessCustomDomainAssociation that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/redshiftserverless_custom_domain_association#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the RedshiftserverlessCustomDomainAssociation to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7225f02e97ed09bcd25a2e59d89878694ec52671a796da380d75f6006ceb3287)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="synthesizeHclAttributes")
    def _synthesize_hcl_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeHclAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="customDomainCertificateExpiryTime")
    def custom_domain_certificate_expiry_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customDomainCertificateExpiryTime"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="customDomainCertificateArnInput")
    def custom_domain_certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customDomainCertificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="customDomainNameInput")
    def custom_domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customDomainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="workgroupNameInput")
    def workgroup_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workgroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customDomainCertificateArn")
    def custom_domain_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customDomainCertificateArn"))

    @custom_domain_certificate_arn.setter
    def custom_domain_certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beaed7ea16a630cc4a088d6aa5d636a0bb634a85dc84c2148744c99d3575d1a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customDomainCertificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="customDomainName")
    def custom_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customDomainName"))

    @custom_domain_name.setter
    def custom_domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b23a5036d490f5aee4aae82c35de1287a9dd287d1fec70363ca92641ec075bd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customDomainName", value)

    @builtins.property
    @jsii.member(jsii_name="workgroupName")
    def workgroup_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workgroupName"))

    @workgroup_name.setter
    def workgroup_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91e23f1ff87b4a19cd5fb2b2c93702d1191cb337a0b18fec3000f0492b8f78fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workgroupName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.redshiftserverlessCustomDomainAssociation.RedshiftserverlessCustomDomainAssociationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "custom_domain_certificate_arn": "customDomainCertificateArn",
        "custom_domain_name": "customDomainName",
        "workgroup_name": "workgroupName",
    },
)
class RedshiftserverlessCustomDomainAssociationConfig(
    _cdktf_9a9027ec.TerraformMetaArguments,
):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        custom_domain_certificate_arn: builtins.str,
        custom_domain_name: builtins.str,
        workgroup_name: builtins.str,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param custom_domain_certificate_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/redshiftserverless_custom_domain_association#custom_domain_certificate_arn RedshiftserverlessCustomDomainAssociation#custom_domain_certificate_arn}.
        :param custom_domain_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/redshiftserverless_custom_domain_association#custom_domain_name RedshiftserverlessCustomDomainAssociation#custom_domain_name}.
        :param workgroup_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/redshiftserverless_custom_domain_association#workgroup_name RedshiftserverlessCustomDomainAssociation#workgroup_name}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e669055d6aa9b8f24b4802488eb05dff7e6c5bf35ed0d00f042e0807b8731c54)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument custom_domain_certificate_arn", value=custom_domain_certificate_arn, expected_type=type_hints["custom_domain_certificate_arn"])
            check_type(argname="argument custom_domain_name", value=custom_domain_name, expected_type=type_hints["custom_domain_name"])
            check_type(argname="argument workgroup_name", value=workgroup_name, expected_type=type_hints["workgroup_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "custom_domain_certificate_arn": custom_domain_certificate_arn,
            "custom_domain_name": custom_domain_name,
            "workgroup_name": workgroup_name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def custom_domain_certificate_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/redshiftserverless_custom_domain_association#custom_domain_certificate_arn RedshiftserverlessCustomDomainAssociation#custom_domain_certificate_arn}.'''
        result = self._values.get("custom_domain_certificate_arn")
        assert result is not None, "Required property 'custom_domain_certificate_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/redshiftserverless_custom_domain_association#custom_domain_name RedshiftserverlessCustomDomainAssociation#custom_domain_name}.'''
        result = self._values.get("custom_domain_name")
        assert result is not None, "Required property 'custom_domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workgroup_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/redshiftserverless_custom_domain_association#workgroup_name RedshiftserverlessCustomDomainAssociation#workgroup_name}.'''
        result = self._values.get("workgroup_name")
        assert result is not None, "Required property 'workgroup_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RedshiftserverlessCustomDomainAssociationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "RedshiftserverlessCustomDomainAssociation",
    "RedshiftserverlessCustomDomainAssociationConfig",
]

publication.publish()

def _typecheckingstub__a7779e87f207c007e54ee7db8809e4cb0d2ba4fd5e78e66b5fab12baafa45123(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    custom_domain_certificate_arn: builtins.str,
    custom_domain_name: builtins.str,
    workgroup_name: builtins.str,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7225f02e97ed09bcd25a2e59d89878694ec52671a796da380d75f6006ceb3287(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beaed7ea16a630cc4a088d6aa5d636a0bb634a85dc84c2148744c99d3575d1a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b23a5036d490f5aee4aae82c35de1287a9dd287d1fec70363ca92641ec075bd8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91e23f1ff87b4a19cd5fb2b2c93702d1191cb337a0b18fec3000f0492b8f78fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e669055d6aa9b8f24b4802488eb05dff7e6c5bf35ed0d00f042e0807b8731c54(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    custom_domain_certificate_arn: builtins.str,
    custom_domain_name: builtins.str,
    workgroup_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
