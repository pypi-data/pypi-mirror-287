r'''
# `aws_workspaces_directory`

Refer to the Terraform Registry for docs: [`aws_workspaces_directory`](https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory).
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


class WorkspacesDirectory(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.workspacesDirectory.WorkspacesDirectory",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory aws_workspaces_directory}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        directory_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        ip_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        self_service_permissions: typing.Optional[typing.Union["WorkspacesDirectorySelfServicePermissions", typing.Dict[builtins.str, typing.Any]]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        workspace_access_properties: typing.Optional[typing.Union["WorkspacesDirectoryWorkspaceAccessProperties", typing.Dict[builtins.str, typing.Any]]] = None,
        workspace_creation_properties: typing.Optional[typing.Union["WorkspacesDirectoryWorkspaceCreationProperties", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory aws_workspaces_directory} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param directory_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#directory_id WorkspacesDirectory#directory_id}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#id WorkspacesDirectory#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_group_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#ip_group_ids WorkspacesDirectory#ip_group_ids}.
        :param self_service_permissions: self_service_permissions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#self_service_permissions WorkspacesDirectory#self_service_permissions}
        :param subnet_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#subnet_ids WorkspacesDirectory#subnet_ids}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#tags WorkspacesDirectory#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#tags_all WorkspacesDirectory#tags_all}.
        :param workspace_access_properties: workspace_access_properties block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#workspace_access_properties WorkspacesDirectory#workspace_access_properties}
        :param workspace_creation_properties: workspace_creation_properties block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#workspace_creation_properties WorkspacesDirectory#workspace_creation_properties}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a02d10c3423b5b41b0acd89ef4b0108250d7c94463808421964cc8e36d63b4e4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = WorkspacesDirectoryConfig(
            directory_id=directory_id,
            id=id,
            ip_group_ids=ip_group_ids,
            self_service_permissions=self_service_permissions,
            subnet_ids=subnet_ids,
            tags=tags,
            tags_all=tags_all,
            workspace_access_properties=workspace_access_properties,
            workspace_creation_properties=workspace_creation_properties,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a WorkspacesDirectory resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the WorkspacesDirectory to import.
        :param import_from_id: The id of the existing WorkspacesDirectory that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the WorkspacesDirectory to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40967eab11501229d9e428eeca878964b004f4ae5d95f0084e7ee43f991a6005)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putSelfServicePermissions")
    def put_self_service_permissions(
        self,
        *,
        change_compute_type: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        increase_volume_size: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        rebuild_workspace: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        restart_workspace: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        switch_running_mode: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param change_compute_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#change_compute_type WorkspacesDirectory#change_compute_type}.
        :param increase_volume_size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#increase_volume_size WorkspacesDirectory#increase_volume_size}.
        :param rebuild_workspace: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#rebuild_workspace WorkspacesDirectory#rebuild_workspace}.
        :param restart_workspace: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#restart_workspace WorkspacesDirectory#restart_workspace}.
        :param switch_running_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#switch_running_mode WorkspacesDirectory#switch_running_mode}.
        '''
        value = WorkspacesDirectorySelfServicePermissions(
            change_compute_type=change_compute_type,
            increase_volume_size=increase_volume_size,
            rebuild_workspace=rebuild_workspace,
            restart_workspace=restart_workspace,
            switch_running_mode=switch_running_mode,
        )

        return typing.cast(None, jsii.invoke(self, "putSelfServicePermissions", [value]))

    @jsii.member(jsii_name="putWorkspaceAccessProperties")
    def put_workspace_access_properties(
        self,
        *,
        device_type_android: typing.Optional[builtins.str] = None,
        device_type_chromeos: typing.Optional[builtins.str] = None,
        device_type_ios: typing.Optional[builtins.str] = None,
        device_type_linux: typing.Optional[builtins.str] = None,
        device_type_osx: typing.Optional[builtins.str] = None,
        device_type_web: typing.Optional[builtins.str] = None,
        device_type_windows: typing.Optional[builtins.str] = None,
        device_type_zeroclient: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param device_type_android: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_android WorkspacesDirectory#device_type_android}.
        :param device_type_chromeos: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_chromeos WorkspacesDirectory#device_type_chromeos}.
        :param device_type_ios: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_ios WorkspacesDirectory#device_type_ios}.
        :param device_type_linux: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_linux WorkspacesDirectory#device_type_linux}.
        :param device_type_osx: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_osx WorkspacesDirectory#device_type_osx}.
        :param device_type_web: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_web WorkspacesDirectory#device_type_web}.
        :param device_type_windows: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_windows WorkspacesDirectory#device_type_windows}.
        :param device_type_zeroclient: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_zeroclient WorkspacesDirectory#device_type_zeroclient}.
        '''
        value = WorkspacesDirectoryWorkspaceAccessProperties(
            device_type_android=device_type_android,
            device_type_chromeos=device_type_chromeos,
            device_type_ios=device_type_ios,
            device_type_linux=device_type_linux,
            device_type_osx=device_type_osx,
            device_type_web=device_type_web,
            device_type_windows=device_type_windows,
            device_type_zeroclient=device_type_zeroclient,
        )

        return typing.cast(None, jsii.invoke(self, "putWorkspaceAccessProperties", [value]))

    @jsii.member(jsii_name="putWorkspaceCreationProperties")
    def put_workspace_creation_properties(
        self,
        *,
        custom_security_group_id: typing.Optional[builtins.str] = None,
        default_ou: typing.Optional[builtins.str] = None,
        enable_internet_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_maintenance_mode: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        user_enabled_as_local_administrator: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param custom_security_group_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#custom_security_group_id WorkspacesDirectory#custom_security_group_id}.
        :param default_ou: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#default_ou WorkspacesDirectory#default_ou}.
        :param enable_internet_access: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#enable_internet_access WorkspacesDirectory#enable_internet_access}.
        :param enable_maintenance_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#enable_maintenance_mode WorkspacesDirectory#enable_maintenance_mode}.
        :param user_enabled_as_local_administrator: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#user_enabled_as_local_administrator WorkspacesDirectory#user_enabled_as_local_administrator}.
        '''
        value = WorkspacesDirectoryWorkspaceCreationProperties(
            custom_security_group_id=custom_security_group_id,
            default_ou=default_ou,
            enable_internet_access=enable_internet_access,
            enable_maintenance_mode=enable_maintenance_mode,
            user_enabled_as_local_administrator=user_enabled_as_local_administrator,
        )

        return typing.cast(None, jsii.invoke(self, "putWorkspaceCreationProperties", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpGroupIds")
    def reset_ip_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpGroupIds", []))

    @jsii.member(jsii_name="resetSelfServicePermissions")
    def reset_self_service_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelfServicePermissions", []))

    @jsii.member(jsii_name="resetSubnetIds")
    def reset_subnet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetIds", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetWorkspaceAccessProperties")
    def reset_workspace_access_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceAccessProperties", []))

    @jsii.member(jsii_name="resetWorkspaceCreationProperties")
    def reset_workspace_creation_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceCreationProperties", []))

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
    @jsii.member(jsii_name="alias")
    def alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alias"))

    @builtins.property
    @jsii.member(jsii_name="customerUserName")
    def customer_user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerUserName"))

    @builtins.property
    @jsii.member(jsii_name="directoryName")
    def directory_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryName"))

    @builtins.property
    @jsii.member(jsii_name="directoryType")
    def directory_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryType"))

    @builtins.property
    @jsii.member(jsii_name="dnsIpAddresses")
    def dns_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="iamRoleId")
    def iam_role_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamRoleId"))

    @builtins.property
    @jsii.member(jsii_name="registrationCode")
    def registration_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registrationCode"))

    @builtins.property
    @jsii.member(jsii_name="selfServicePermissions")
    def self_service_permissions(
        self,
    ) -> "WorkspacesDirectorySelfServicePermissionsOutputReference":
        return typing.cast("WorkspacesDirectorySelfServicePermissionsOutputReference", jsii.get(self, "selfServicePermissions"))

    @builtins.property
    @jsii.member(jsii_name="workspaceAccessProperties")
    def workspace_access_properties(
        self,
    ) -> "WorkspacesDirectoryWorkspaceAccessPropertiesOutputReference":
        return typing.cast("WorkspacesDirectoryWorkspaceAccessPropertiesOutputReference", jsii.get(self, "workspaceAccessProperties"))

    @builtins.property
    @jsii.member(jsii_name="workspaceCreationProperties")
    def workspace_creation_properties(
        self,
    ) -> "WorkspacesDirectoryWorkspaceCreationPropertiesOutputReference":
        return typing.cast("WorkspacesDirectoryWorkspaceCreationPropertiesOutputReference", jsii.get(self, "workspaceCreationProperties"))

    @builtins.property
    @jsii.member(jsii_name="workspaceSecurityGroupId")
    def workspace_security_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceSecurityGroupId"))

    @builtins.property
    @jsii.member(jsii_name="directoryIdInput")
    def directory_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipGroupIdsInput")
    def ip_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="selfServicePermissionsInput")
    def self_service_permissions_input(
        self,
    ) -> typing.Optional["WorkspacesDirectorySelfServicePermissions"]:
        return typing.cast(typing.Optional["WorkspacesDirectorySelfServicePermissions"], jsii.get(self, "selfServicePermissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceAccessPropertiesInput")
    def workspace_access_properties_input(
        self,
    ) -> typing.Optional["WorkspacesDirectoryWorkspaceAccessProperties"]:
        return typing.cast(typing.Optional["WorkspacesDirectoryWorkspaceAccessProperties"], jsii.get(self, "workspaceAccessPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceCreationPropertiesInput")
    def workspace_creation_properties_input(
        self,
    ) -> typing.Optional["WorkspacesDirectoryWorkspaceCreationProperties"]:
        return typing.cast(typing.Optional["WorkspacesDirectoryWorkspaceCreationProperties"], jsii.get(self, "workspaceCreationPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryId")
    def directory_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryId"))

    @directory_id.setter
    def directory_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a7e265d90c60dae6789261f3818f19e65569bfbc6a408c91f4151576b42f3c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3bb0727506c55826122d994f5a4f94a75c1a1bc8162b89bbec70a8d46e627fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipGroupIds")
    def ip_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipGroupIds"))

    @ip_group_ids.setter
    def ip_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ac956f37cf48d3235de6110350f6b4032fd254fef0d1f7e973145e56e112889)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f53f76c3682511ab80d54f7a4fc61eb4ccb138520149f8e51b3ed8be1591be9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fc884854235a55cee5dbc7adc29f65475c7254d062bb8b5e03d8bdc3add69ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f95f65ecbbe2f918672f6f049995581acbeb4313412a900d5064986052d3a4b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.workspacesDirectory.WorkspacesDirectoryConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "directory_id": "directoryId",
        "id": "id",
        "ip_group_ids": "ipGroupIds",
        "self_service_permissions": "selfServicePermissions",
        "subnet_ids": "subnetIds",
        "tags": "tags",
        "tags_all": "tagsAll",
        "workspace_access_properties": "workspaceAccessProperties",
        "workspace_creation_properties": "workspaceCreationProperties",
    },
)
class WorkspacesDirectoryConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        directory_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        ip_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        self_service_permissions: typing.Optional[typing.Union["WorkspacesDirectorySelfServicePermissions", typing.Dict[builtins.str, typing.Any]]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        workspace_access_properties: typing.Optional[typing.Union["WorkspacesDirectoryWorkspaceAccessProperties", typing.Dict[builtins.str, typing.Any]]] = None,
        workspace_creation_properties: typing.Optional[typing.Union["WorkspacesDirectoryWorkspaceCreationProperties", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param directory_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#directory_id WorkspacesDirectory#directory_id}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#id WorkspacesDirectory#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_group_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#ip_group_ids WorkspacesDirectory#ip_group_ids}.
        :param self_service_permissions: self_service_permissions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#self_service_permissions WorkspacesDirectory#self_service_permissions}
        :param subnet_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#subnet_ids WorkspacesDirectory#subnet_ids}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#tags WorkspacesDirectory#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#tags_all WorkspacesDirectory#tags_all}.
        :param workspace_access_properties: workspace_access_properties block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#workspace_access_properties WorkspacesDirectory#workspace_access_properties}
        :param workspace_creation_properties: workspace_creation_properties block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#workspace_creation_properties WorkspacesDirectory#workspace_creation_properties}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(self_service_permissions, dict):
            self_service_permissions = WorkspacesDirectorySelfServicePermissions(**self_service_permissions)
        if isinstance(workspace_access_properties, dict):
            workspace_access_properties = WorkspacesDirectoryWorkspaceAccessProperties(**workspace_access_properties)
        if isinstance(workspace_creation_properties, dict):
            workspace_creation_properties = WorkspacesDirectoryWorkspaceCreationProperties(**workspace_creation_properties)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__600fb0a94c613b912a9e90e7f941c7815b7a746cfa68580a9866dcd6b0b8047a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument directory_id", value=directory_id, expected_type=type_hints["directory_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_group_ids", value=ip_group_ids, expected_type=type_hints["ip_group_ids"])
            check_type(argname="argument self_service_permissions", value=self_service_permissions, expected_type=type_hints["self_service_permissions"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument workspace_access_properties", value=workspace_access_properties, expected_type=type_hints["workspace_access_properties"])
            check_type(argname="argument workspace_creation_properties", value=workspace_creation_properties, expected_type=type_hints["workspace_creation_properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "directory_id": directory_id,
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
        if id is not None:
            self._values["id"] = id
        if ip_group_ids is not None:
            self._values["ip_group_ids"] = ip_group_ids
        if self_service_permissions is not None:
            self._values["self_service_permissions"] = self_service_permissions
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if workspace_access_properties is not None:
            self._values["workspace_access_properties"] = workspace_access_properties
        if workspace_creation_properties is not None:
            self._values["workspace_creation_properties"] = workspace_creation_properties

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
    def directory_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#directory_id WorkspacesDirectory#directory_id}.'''
        result = self._values.get("directory_id")
        assert result is not None, "Required property 'directory_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#id WorkspacesDirectory#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#ip_group_ids WorkspacesDirectory#ip_group_ids}.'''
        result = self._values.get("ip_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def self_service_permissions(
        self,
    ) -> typing.Optional["WorkspacesDirectorySelfServicePermissions"]:
        '''self_service_permissions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#self_service_permissions WorkspacesDirectory#self_service_permissions}
        '''
        result = self._values.get("self_service_permissions")
        return typing.cast(typing.Optional["WorkspacesDirectorySelfServicePermissions"], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#subnet_ids WorkspacesDirectory#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#tags WorkspacesDirectory#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#tags_all WorkspacesDirectory#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def workspace_access_properties(
        self,
    ) -> typing.Optional["WorkspacesDirectoryWorkspaceAccessProperties"]:
        '''workspace_access_properties block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#workspace_access_properties WorkspacesDirectory#workspace_access_properties}
        '''
        result = self._values.get("workspace_access_properties")
        return typing.cast(typing.Optional["WorkspacesDirectoryWorkspaceAccessProperties"], result)

    @builtins.property
    def workspace_creation_properties(
        self,
    ) -> typing.Optional["WorkspacesDirectoryWorkspaceCreationProperties"]:
        '''workspace_creation_properties block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#workspace_creation_properties WorkspacesDirectory#workspace_creation_properties}
        '''
        result = self._values.get("workspace_creation_properties")
        return typing.cast(typing.Optional["WorkspacesDirectoryWorkspaceCreationProperties"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkspacesDirectoryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.workspacesDirectory.WorkspacesDirectorySelfServicePermissions",
    jsii_struct_bases=[],
    name_mapping={
        "change_compute_type": "changeComputeType",
        "increase_volume_size": "increaseVolumeSize",
        "rebuild_workspace": "rebuildWorkspace",
        "restart_workspace": "restartWorkspace",
        "switch_running_mode": "switchRunningMode",
    },
)
class WorkspacesDirectorySelfServicePermissions:
    def __init__(
        self,
        *,
        change_compute_type: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        increase_volume_size: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        rebuild_workspace: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        restart_workspace: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        switch_running_mode: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param change_compute_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#change_compute_type WorkspacesDirectory#change_compute_type}.
        :param increase_volume_size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#increase_volume_size WorkspacesDirectory#increase_volume_size}.
        :param rebuild_workspace: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#rebuild_workspace WorkspacesDirectory#rebuild_workspace}.
        :param restart_workspace: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#restart_workspace WorkspacesDirectory#restart_workspace}.
        :param switch_running_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#switch_running_mode WorkspacesDirectory#switch_running_mode}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9246b87d73abb67ac16dab870c39bd19ee674a6694e0edfcadb5eac365907cab)
            check_type(argname="argument change_compute_type", value=change_compute_type, expected_type=type_hints["change_compute_type"])
            check_type(argname="argument increase_volume_size", value=increase_volume_size, expected_type=type_hints["increase_volume_size"])
            check_type(argname="argument rebuild_workspace", value=rebuild_workspace, expected_type=type_hints["rebuild_workspace"])
            check_type(argname="argument restart_workspace", value=restart_workspace, expected_type=type_hints["restart_workspace"])
            check_type(argname="argument switch_running_mode", value=switch_running_mode, expected_type=type_hints["switch_running_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if change_compute_type is not None:
            self._values["change_compute_type"] = change_compute_type
        if increase_volume_size is not None:
            self._values["increase_volume_size"] = increase_volume_size
        if rebuild_workspace is not None:
            self._values["rebuild_workspace"] = rebuild_workspace
        if restart_workspace is not None:
            self._values["restart_workspace"] = restart_workspace
        if switch_running_mode is not None:
            self._values["switch_running_mode"] = switch_running_mode

    @builtins.property
    def change_compute_type(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#change_compute_type WorkspacesDirectory#change_compute_type}.'''
        result = self._values.get("change_compute_type")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def increase_volume_size(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#increase_volume_size WorkspacesDirectory#increase_volume_size}.'''
        result = self._values.get("increase_volume_size")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def rebuild_workspace(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#rebuild_workspace WorkspacesDirectory#rebuild_workspace}.'''
        result = self._values.get("rebuild_workspace")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def restart_workspace(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#restart_workspace WorkspacesDirectory#restart_workspace}.'''
        result = self._values.get("restart_workspace")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def switch_running_mode(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#switch_running_mode WorkspacesDirectory#switch_running_mode}.'''
        result = self._values.get("switch_running_mode")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkspacesDirectorySelfServicePermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkspacesDirectorySelfServicePermissionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.workspacesDirectory.WorkspacesDirectorySelfServicePermissionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42182ead7060f2e9e13d54b6dfb39784bb41aaf1dc14429792c4d6839bc0f7d7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetChangeComputeType")
    def reset_change_compute_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChangeComputeType", []))

    @jsii.member(jsii_name="resetIncreaseVolumeSize")
    def reset_increase_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncreaseVolumeSize", []))

    @jsii.member(jsii_name="resetRebuildWorkspace")
    def reset_rebuild_workspace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRebuildWorkspace", []))

    @jsii.member(jsii_name="resetRestartWorkspace")
    def reset_restart_workspace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestartWorkspace", []))

    @jsii.member(jsii_name="resetSwitchRunningMode")
    def reset_switch_running_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSwitchRunningMode", []))

    @builtins.property
    @jsii.member(jsii_name="changeComputeTypeInput")
    def change_compute_type_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "changeComputeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="increaseVolumeSizeInput")
    def increase_volume_size_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "increaseVolumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="rebuildWorkspaceInput")
    def rebuild_workspace_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "rebuildWorkspaceInput"))

    @builtins.property
    @jsii.member(jsii_name="restartWorkspaceInput")
    def restart_workspace_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "restartWorkspaceInput"))

    @builtins.property
    @jsii.member(jsii_name="switchRunningModeInput")
    def switch_running_mode_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "switchRunningModeInput"))

    @builtins.property
    @jsii.member(jsii_name="changeComputeType")
    def change_compute_type(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "changeComputeType"))

    @change_compute_type.setter
    def change_compute_type(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb2df3ace164de24fb7e6060735aadd79b717adf4e2ed7348805d7b8dde36086)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "changeComputeType", value)

    @builtins.property
    @jsii.member(jsii_name="increaseVolumeSize")
    def increase_volume_size(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "increaseVolumeSize"))

    @increase_volume_size.setter
    def increase_volume_size(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__694e45369f9cbb1ac4a08c584d0d074818e3b2253c86e6c5013a697cb867fe53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "increaseVolumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="rebuildWorkspace")
    def rebuild_workspace(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "rebuildWorkspace"))

    @rebuild_workspace.setter
    def rebuild_workspace(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f74a5e5677b71b31715956e3981a1a0e3048552489e13649b567b49528e83fca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rebuildWorkspace", value)

    @builtins.property
    @jsii.member(jsii_name="restartWorkspace")
    def restart_workspace(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "restartWorkspace"))

    @restart_workspace.setter
    def restart_workspace(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5381d4a0c6e4f875fbcf19c1a2c4799bfd2280b6f581fbe2da28f64f23951a74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restartWorkspace", value)

    @builtins.property
    @jsii.member(jsii_name="switchRunningMode")
    def switch_running_mode(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "switchRunningMode"))

    @switch_running_mode.setter
    def switch_running_mode(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54260064f7b2b7d242ad93318b5ba171d46951d160db37c8a03a6b6e3211944b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "switchRunningMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WorkspacesDirectorySelfServicePermissions]:
        return typing.cast(typing.Optional[WorkspacesDirectorySelfServicePermissions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WorkspacesDirectorySelfServicePermissions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1497f17bf6f2372fb9348ab3db6ffbfe4fcf770418ad8cdce678e059eb54822b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.workspacesDirectory.WorkspacesDirectoryWorkspaceAccessProperties",
    jsii_struct_bases=[],
    name_mapping={
        "device_type_android": "deviceTypeAndroid",
        "device_type_chromeos": "deviceTypeChromeos",
        "device_type_ios": "deviceTypeIos",
        "device_type_linux": "deviceTypeLinux",
        "device_type_osx": "deviceTypeOsx",
        "device_type_web": "deviceTypeWeb",
        "device_type_windows": "deviceTypeWindows",
        "device_type_zeroclient": "deviceTypeZeroclient",
    },
)
class WorkspacesDirectoryWorkspaceAccessProperties:
    def __init__(
        self,
        *,
        device_type_android: typing.Optional[builtins.str] = None,
        device_type_chromeos: typing.Optional[builtins.str] = None,
        device_type_ios: typing.Optional[builtins.str] = None,
        device_type_linux: typing.Optional[builtins.str] = None,
        device_type_osx: typing.Optional[builtins.str] = None,
        device_type_web: typing.Optional[builtins.str] = None,
        device_type_windows: typing.Optional[builtins.str] = None,
        device_type_zeroclient: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param device_type_android: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_android WorkspacesDirectory#device_type_android}.
        :param device_type_chromeos: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_chromeos WorkspacesDirectory#device_type_chromeos}.
        :param device_type_ios: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_ios WorkspacesDirectory#device_type_ios}.
        :param device_type_linux: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_linux WorkspacesDirectory#device_type_linux}.
        :param device_type_osx: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_osx WorkspacesDirectory#device_type_osx}.
        :param device_type_web: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_web WorkspacesDirectory#device_type_web}.
        :param device_type_windows: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_windows WorkspacesDirectory#device_type_windows}.
        :param device_type_zeroclient: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_zeroclient WorkspacesDirectory#device_type_zeroclient}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbc65258c1106e6b849fc2f4560ccd22b104ecc6315d11c38c77f1ef27ff06dc)
            check_type(argname="argument device_type_android", value=device_type_android, expected_type=type_hints["device_type_android"])
            check_type(argname="argument device_type_chromeos", value=device_type_chromeos, expected_type=type_hints["device_type_chromeos"])
            check_type(argname="argument device_type_ios", value=device_type_ios, expected_type=type_hints["device_type_ios"])
            check_type(argname="argument device_type_linux", value=device_type_linux, expected_type=type_hints["device_type_linux"])
            check_type(argname="argument device_type_osx", value=device_type_osx, expected_type=type_hints["device_type_osx"])
            check_type(argname="argument device_type_web", value=device_type_web, expected_type=type_hints["device_type_web"])
            check_type(argname="argument device_type_windows", value=device_type_windows, expected_type=type_hints["device_type_windows"])
            check_type(argname="argument device_type_zeroclient", value=device_type_zeroclient, expected_type=type_hints["device_type_zeroclient"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if device_type_android is not None:
            self._values["device_type_android"] = device_type_android
        if device_type_chromeos is not None:
            self._values["device_type_chromeos"] = device_type_chromeos
        if device_type_ios is not None:
            self._values["device_type_ios"] = device_type_ios
        if device_type_linux is not None:
            self._values["device_type_linux"] = device_type_linux
        if device_type_osx is not None:
            self._values["device_type_osx"] = device_type_osx
        if device_type_web is not None:
            self._values["device_type_web"] = device_type_web
        if device_type_windows is not None:
            self._values["device_type_windows"] = device_type_windows
        if device_type_zeroclient is not None:
            self._values["device_type_zeroclient"] = device_type_zeroclient

    @builtins.property
    def device_type_android(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_android WorkspacesDirectory#device_type_android}.'''
        result = self._values.get("device_type_android")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device_type_chromeos(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_chromeos WorkspacesDirectory#device_type_chromeos}.'''
        result = self._values.get("device_type_chromeos")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device_type_ios(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_ios WorkspacesDirectory#device_type_ios}.'''
        result = self._values.get("device_type_ios")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device_type_linux(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_linux WorkspacesDirectory#device_type_linux}.'''
        result = self._values.get("device_type_linux")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device_type_osx(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_osx WorkspacesDirectory#device_type_osx}.'''
        result = self._values.get("device_type_osx")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device_type_web(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_web WorkspacesDirectory#device_type_web}.'''
        result = self._values.get("device_type_web")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device_type_windows(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_windows WorkspacesDirectory#device_type_windows}.'''
        result = self._values.get("device_type_windows")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device_type_zeroclient(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#device_type_zeroclient WorkspacesDirectory#device_type_zeroclient}.'''
        result = self._values.get("device_type_zeroclient")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkspacesDirectoryWorkspaceAccessProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkspacesDirectoryWorkspaceAccessPropertiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.workspacesDirectory.WorkspacesDirectoryWorkspaceAccessPropertiesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a2d64b13e0769156ba44c3f2be62c5524ba170af95639e14c31eeb5ce015f95)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDeviceTypeAndroid")
    def reset_device_type_android(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceTypeAndroid", []))

    @jsii.member(jsii_name="resetDeviceTypeChromeos")
    def reset_device_type_chromeos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceTypeChromeos", []))

    @jsii.member(jsii_name="resetDeviceTypeIos")
    def reset_device_type_ios(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceTypeIos", []))

    @jsii.member(jsii_name="resetDeviceTypeLinux")
    def reset_device_type_linux(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceTypeLinux", []))

    @jsii.member(jsii_name="resetDeviceTypeOsx")
    def reset_device_type_osx(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceTypeOsx", []))

    @jsii.member(jsii_name="resetDeviceTypeWeb")
    def reset_device_type_web(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceTypeWeb", []))

    @jsii.member(jsii_name="resetDeviceTypeWindows")
    def reset_device_type_windows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceTypeWindows", []))

    @jsii.member(jsii_name="resetDeviceTypeZeroclient")
    def reset_device_type_zeroclient(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceTypeZeroclient", []))

    @builtins.property
    @jsii.member(jsii_name="deviceTypeAndroidInput")
    def device_type_android_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceTypeAndroidInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceTypeChromeosInput")
    def device_type_chromeos_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceTypeChromeosInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceTypeIosInput")
    def device_type_ios_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceTypeIosInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceTypeLinuxInput")
    def device_type_linux_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceTypeLinuxInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceTypeOsxInput")
    def device_type_osx_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceTypeOsxInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceTypeWebInput")
    def device_type_web_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceTypeWebInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceTypeWindowsInput")
    def device_type_windows_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceTypeWindowsInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceTypeZeroclientInput")
    def device_type_zeroclient_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceTypeZeroclientInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceTypeAndroid")
    def device_type_android(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceTypeAndroid"))

    @device_type_android.setter
    def device_type_android(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__244443cda9ebea0d5913eecc1185012a80ea2ce69659ff7779d22b3cd94084e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceTypeAndroid", value)

    @builtins.property
    @jsii.member(jsii_name="deviceTypeChromeos")
    def device_type_chromeos(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceTypeChromeos"))

    @device_type_chromeos.setter
    def device_type_chromeos(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d64d2c5a8f4ecba59439c3d03a4456e7802ac892f6e9d34b01b6d4040f2dc2f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceTypeChromeos", value)

    @builtins.property
    @jsii.member(jsii_name="deviceTypeIos")
    def device_type_ios(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceTypeIos"))

    @device_type_ios.setter
    def device_type_ios(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31d6850dd281d53f10ff00c224d6275f332f7155c262e50279823290563bae02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceTypeIos", value)

    @builtins.property
    @jsii.member(jsii_name="deviceTypeLinux")
    def device_type_linux(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceTypeLinux"))

    @device_type_linux.setter
    def device_type_linux(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__308045e4320da466b3c6271c41aa3629ca4e34736240cc626e559efda693f7a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceTypeLinux", value)

    @builtins.property
    @jsii.member(jsii_name="deviceTypeOsx")
    def device_type_osx(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceTypeOsx"))

    @device_type_osx.setter
    def device_type_osx(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__584d2f351c0f19248b41526a8ace7bd50c9987fff9282b198cbe76b60d2398b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceTypeOsx", value)

    @builtins.property
    @jsii.member(jsii_name="deviceTypeWeb")
    def device_type_web(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceTypeWeb"))

    @device_type_web.setter
    def device_type_web(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c80a4f63fe9160b5f3fecebf906f1c398cc0580e38314c21c74fbdc407daf57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceTypeWeb", value)

    @builtins.property
    @jsii.member(jsii_name="deviceTypeWindows")
    def device_type_windows(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceTypeWindows"))

    @device_type_windows.setter
    def device_type_windows(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bbeaf25a42ab3408f93d5ba52f4c7c331d52595a0e13cabc438ab2b51ec3551)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceTypeWindows", value)

    @builtins.property
    @jsii.member(jsii_name="deviceTypeZeroclient")
    def device_type_zeroclient(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deviceTypeZeroclient"))

    @device_type_zeroclient.setter
    def device_type_zeroclient(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa0b61824da6a8e0fd1fb6ed4fdabe0738cb75fa89d91755a97a57557a1f049a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceTypeZeroclient", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WorkspacesDirectoryWorkspaceAccessProperties]:
        return typing.cast(typing.Optional[WorkspacesDirectoryWorkspaceAccessProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WorkspacesDirectoryWorkspaceAccessProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e28b7e6f9f8567a4bf60da984cd9fa3f920d8632348a20f3c85bcfc696848c7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.workspacesDirectory.WorkspacesDirectoryWorkspaceCreationProperties",
    jsii_struct_bases=[],
    name_mapping={
        "custom_security_group_id": "customSecurityGroupId",
        "default_ou": "defaultOu",
        "enable_internet_access": "enableInternetAccess",
        "enable_maintenance_mode": "enableMaintenanceMode",
        "user_enabled_as_local_administrator": "userEnabledAsLocalAdministrator",
    },
)
class WorkspacesDirectoryWorkspaceCreationProperties:
    def __init__(
        self,
        *,
        custom_security_group_id: typing.Optional[builtins.str] = None,
        default_ou: typing.Optional[builtins.str] = None,
        enable_internet_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_maintenance_mode: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        user_enabled_as_local_administrator: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param custom_security_group_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#custom_security_group_id WorkspacesDirectory#custom_security_group_id}.
        :param default_ou: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#default_ou WorkspacesDirectory#default_ou}.
        :param enable_internet_access: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#enable_internet_access WorkspacesDirectory#enable_internet_access}.
        :param enable_maintenance_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#enable_maintenance_mode WorkspacesDirectory#enable_maintenance_mode}.
        :param user_enabled_as_local_administrator: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#user_enabled_as_local_administrator WorkspacesDirectory#user_enabled_as_local_administrator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d28d7da7cb05aef0bc87a3ee44c85cbef86d74068fc15026f567a85c347a96a4)
            check_type(argname="argument custom_security_group_id", value=custom_security_group_id, expected_type=type_hints["custom_security_group_id"])
            check_type(argname="argument default_ou", value=default_ou, expected_type=type_hints["default_ou"])
            check_type(argname="argument enable_internet_access", value=enable_internet_access, expected_type=type_hints["enable_internet_access"])
            check_type(argname="argument enable_maintenance_mode", value=enable_maintenance_mode, expected_type=type_hints["enable_maintenance_mode"])
            check_type(argname="argument user_enabled_as_local_administrator", value=user_enabled_as_local_administrator, expected_type=type_hints["user_enabled_as_local_administrator"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if custom_security_group_id is not None:
            self._values["custom_security_group_id"] = custom_security_group_id
        if default_ou is not None:
            self._values["default_ou"] = default_ou
        if enable_internet_access is not None:
            self._values["enable_internet_access"] = enable_internet_access
        if enable_maintenance_mode is not None:
            self._values["enable_maintenance_mode"] = enable_maintenance_mode
        if user_enabled_as_local_administrator is not None:
            self._values["user_enabled_as_local_administrator"] = user_enabled_as_local_administrator

    @builtins.property
    def custom_security_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#custom_security_group_id WorkspacesDirectory#custom_security_group_id}.'''
        result = self._values.get("custom_security_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_ou(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#default_ou WorkspacesDirectory#default_ou}.'''
        result = self._values.get("default_ou")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_internet_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#enable_internet_access WorkspacesDirectory#enable_internet_access}.'''
        result = self._values.get("enable_internet_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_maintenance_mode(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#enable_maintenance_mode WorkspacesDirectory#enable_maintenance_mode}.'''
        result = self._values.get("enable_maintenance_mode")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def user_enabled_as_local_administrator(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.60.0/docs/resources/workspaces_directory#user_enabled_as_local_administrator WorkspacesDirectory#user_enabled_as_local_administrator}.'''
        result = self._values.get("user_enabled_as_local_administrator")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkspacesDirectoryWorkspaceCreationProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkspacesDirectoryWorkspaceCreationPropertiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.workspacesDirectory.WorkspacesDirectoryWorkspaceCreationPropertiesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d103ef46fed4b464ad671d19c8026508b7dfca78709c43a311ddc77c4b0fe22)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCustomSecurityGroupId")
    def reset_custom_security_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomSecurityGroupId", []))

    @jsii.member(jsii_name="resetDefaultOu")
    def reset_default_ou(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultOu", []))

    @jsii.member(jsii_name="resetEnableInternetAccess")
    def reset_enable_internet_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableInternetAccess", []))

    @jsii.member(jsii_name="resetEnableMaintenanceMode")
    def reset_enable_maintenance_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableMaintenanceMode", []))

    @jsii.member(jsii_name="resetUserEnabledAsLocalAdministrator")
    def reset_user_enabled_as_local_administrator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserEnabledAsLocalAdministrator", []))

    @builtins.property
    @jsii.member(jsii_name="customSecurityGroupIdInput")
    def custom_security_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customSecurityGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultOuInput")
    def default_ou_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultOuInput"))

    @builtins.property
    @jsii.member(jsii_name="enableInternetAccessInput")
    def enable_internet_access_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableInternetAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="enableMaintenanceModeInput")
    def enable_maintenance_mode_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableMaintenanceModeInput"))

    @builtins.property
    @jsii.member(jsii_name="userEnabledAsLocalAdministratorInput")
    def user_enabled_as_local_administrator_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "userEnabledAsLocalAdministratorInput"))

    @builtins.property
    @jsii.member(jsii_name="customSecurityGroupId")
    def custom_security_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customSecurityGroupId"))

    @custom_security_group_id.setter
    def custom_security_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14894a72deabf46b1ad02b8dd65a33361002efbadfc6edda098d66c8cf1f4d7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customSecurityGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="defaultOu")
    def default_ou(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultOu"))

    @default_ou.setter
    def default_ou(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97d75ffb8770c333e3a95e56ff00145d4895032db4520208f9bec279ead2d948)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultOu", value)

    @builtins.property
    @jsii.member(jsii_name="enableInternetAccess")
    def enable_internet_access(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableInternetAccess"))

    @enable_internet_access.setter
    def enable_internet_access(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e925798d890c849a74d9182a3c914af9cd8ec65a7b32d5646d7ab776ed9630f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableInternetAccess", value)

    @builtins.property
    @jsii.member(jsii_name="enableMaintenanceMode")
    def enable_maintenance_mode(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableMaintenanceMode"))

    @enable_maintenance_mode.setter
    def enable_maintenance_mode(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__525ab7891d8dad11dc5804ad8615d655470263b977afcc8b524f86cd436ef931)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableMaintenanceMode", value)

    @builtins.property
    @jsii.member(jsii_name="userEnabledAsLocalAdministrator")
    def user_enabled_as_local_administrator(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "userEnabledAsLocalAdministrator"))

    @user_enabled_as_local_administrator.setter
    def user_enabled_as_local_administrator(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d51fa816814e522d58791331ef9cdf3de910cd6a1b587132aa50d189d82ff4fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userEnabledAsLocalAdministrator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WorkspacesDirectoryWorkspaceCreationProperties]:
        return typing.cast(typing.Optional[WorkspacesDirectoryWorkspaceCreationProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WorkspacesDirectoryWorkspaceCreationProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f50b1deb4a5cee7543191f3f589cc1e3346ad1c362623c486a3542a9a27a141)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "WorkspacesDirectory",
    "WorkspacesDirectoryConfig",
    "WorkspacesDirectorySelfServicePermissions",
    "WorkspacesDirectorySelfServicePermissionsOutputReference",
    "WorkspacesDirectoryWorkspaceAccessProperties",
    "WorkspacesDirectoryWorkspaceAccessPropertiesOutputReference",
    "WorkspacesDirectoryWorkspaceCreationProperties",
    "WorkspacesDirectoryWorkspaceCreationPropertiesOutputReference",
]

publication.publish()

def _typecheckingstub__a02d10c3423b5b41b0acd89ef4b0108250d7c94463808421964cc8e36d63b4e4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    directory_id: builtins.str,
    id: typing.Optional[builtins.str] = None,
    ip_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    self_service_permissions: typing.Optional[typing.Union[WorkspacesDirectorySelfServicePermissions, typing.Dict[builtins.str, typing.Any]]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    workspace_access_properties: typing.Optional[typing.Union[WorkspacesDirectoryWorkspaceAccessProperties, typing.Dict[builtins.str, typing.Any]]] = None,
    workspace_creation_properties: typing.Optional[typing.Union[WorkspacesDirectoryWorkspaceCreationProperties, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__40967eab11501229d9e428eeca878964b004f4ae5d95f0084e7ee43f991a6005(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a7e265d90c60dae6789261f3818f19e65569bfbc6a408c91f4151576b42f3c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3bb0727506c55826122d994f5a4f94a75c1a1bc8162b89bbec70a8d46e627fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ac956f37cf48d3235de6110350f6b4032fd254fef0d1f7e973145e56e112889(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f53f76c3682511ab80d54f7a4fc61eb4ccb138520149f8e51b3ed8be1591be9(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fc884854235a55cee5dbc7adc29f65475c7254d062bb8b5e03d8bdc3add69ad(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f95f65ecbbe2f918672f6f049995581acbeb4313412a900d5064986052d3a4b5(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__600fb0a94c613b912a9e90e7f941c7815b7a746cfa68580a9866dcd6b0b8047a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    directory_id: builtins.str,
    id: typing.Optional[builtins.str] = None,
    ip_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    self_service_permissions: typing.Optional[typing.Union[WorkspacesDirectorySelfServicePermissions, typing.Dict[builtins.str, typing.Any]]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    workspace_access_properties: typing.Optional[typing.Union[WorkspacesDirectoryWorkspaceAccessProperties, typing.Dict[builtins.str, typing.Any]]] = None,
    workspace_creation_properties: typing.Optional[typing.Union[WorkspacesDirectoryWorkspaceCreationProperties, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9246b87d73abb67ac16dab870c39bd19ee674a6694e0edfcadb5eac365907cab(
    *,
    change_compute_type: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    increase_volume_size: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    rebuild_workspace: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    restart_workspace: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    switch_running_mode: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42182ead7060f2e9e13d54b6dfb39784bb41aaf1dc14429792c4d6839bc0f7d7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb2df3ace164de24fb7e6060735aadd79b717adf4e2ed7348805d7b8dde36086(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__694e45369f9cbb1ac4a08c584d0d074818e3b2253c86e6c5013a697cb867fe53(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f74a5e5677b71b31715956e3981a1a0e3048552489e13649b567b49528e83fca(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5381d4a0c6e4f875fbcf19c1a2c4799bfd2280b6f581fbe2da28f64f23951a74(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54260064f7b2b7d242ad93318b5ba171d46951d160db37c8a03a6b6e3211944b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1497f17bf6f2372fb9348ab3db6ffbfe4fcf770418ad8cdce678e059eb54822b(
    value: typing.Optional[WorkspacesDirectorySelfServicePermissions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbc65258c1106e6b849fc2f4560ccd22b104ecc6315d11c38c77f1ef27ff06dc(
    *,
    device_type_android: typing.Optional[builtins.str] = None,
    device_type_chromeos: typing.Optional[builtins.str] = None,
    device_type_ios: typing.Optional[builtins.str] = None,
    device_type_linux: typing.Optional[builtins.str] = None,
    device_type_osx: typing.Optional[builtins.str] = None,
    device_type_web: typing.Optional[builtins.str] = None,
    device_type_windows: typing.Optional[builtins.str] = None,
    device_type_zeroclient: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a2d64b13e0769156ba44c3f2be62c5524ba170af95639e14c31eeb5ce015f95(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__244443cda9ebea0d5913eecc1185012a80ea2ce69659ff7779d22b3cd94084e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d64d2c5a8f4ecba59439c3d03a4456e7802ac892f6e9d34b01b6d4040f2dc2f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31d6850dd281d53f10ff00c224d6275f332f7155c262e50279823290563bae02(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__308045e4320da466b3c6271c41aa3629ca4e34736240cc626e559efda693f7a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__584d2f351c0f19248b41526a8ace7bd50c9987fff9282b198cbe76b60d2398b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c80a4f63fe9160b5f3fecebf906f1c398cc0580e38314c21c74fbdc407daf57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bbeaf25a42ab3408f93d5ba52f4c7c331d52595a0e13cabc438ab2b51ec3551(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa0b61824da6a8e0fd1fb6ed4fdabe0738cb75fa89d91755a97a57557a1f049a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e28b7e6f9f8567a4bf60da984cd9fa3f920d8632348a20f3c85bcfc696848c7d(
    value: typing.Optional[WorkspacesDirectoryWorkspaceAccessProperties],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d28d7da7cb05aef0bc87a3ee44c85cbef86d74068fc15026f567a85c347a96a4(
    *,
    custom_security_group_id: typing.Optional[builtins.str] = None,
    default_ou: typing.Optional[builtins.str] = None,
    enable_internet_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_maintenance_mode: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    user_enabled_as_local_administrator: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d103ef46fed4b464ad671d19c8026508b7dfca78709c43a311ddc77c4b0fe22(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14894a72deabf46b1ad02b8dd65a33361002efbadfc6edda098d66c8cf1f4d7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97d75ffb8770c333e3a95e56ff00145d4895032db4520208f9bec279ead2d948(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e925798d890c849a74d9182a3c914af9cd8ec65a7b32d5646d7ab776ed9630f6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__525ab7891d8dad11dc5804ad8615d655470263b977afcc8b524f86cd436ef931(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d51fa816814e522d58791331ef9cdf3de910cd6a1b587132aa50d189d82ff4fe(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f50b1deb4a5cee7543191f3f589cc1e3346ad1c362623c486a3542a9a27a141(
    value: typing.Optional[WorkspacesDirectoryWorkspaceCreationProperties],
) -> None:
    """Type checking stubs"""
    pass
