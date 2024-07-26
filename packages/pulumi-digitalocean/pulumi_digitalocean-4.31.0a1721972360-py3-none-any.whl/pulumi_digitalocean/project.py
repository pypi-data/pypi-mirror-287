# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProjectArgs', 'Project']

@pulumi.input_type
class ProjectArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 purpose: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Project resource.
        :param pulumi.Input[str] description: the description of the project
        :param pulumi.Input[str] environment: the environment of the project's resources. The possible values are: `Development`, `Staging`, `Production`)
        :param pulumi.Input[bool] is_default: a boolean indicating whether or not the project is the default project. (Default: "false")
        :param pulumi.Input[str] name: The name of the Project
        :param pulumi.Input[str] purpose: the purpose of the project, (Default: "Web Application")
        :param pulumi.Input[Sequence[pulumi.Input[str]]] resources: a list of uniform resource names (URNs) for the resources associated with the project
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if environment is not None:
            pulumi.set(__self__, "environment", environment)
        if is_default is not None:
            pulumi.set(__self__, "is_default", is_default)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if purpose is not None:
            pulumi.set(__self__, "purpose", purpose)
        if resources is not None:
            pulumi.set(__self__, "resources", resources)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        the description of the project
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[str]]:
        """
        the environment of the project's resources. The possible values are: `Development`, `Staging`, `Production`)
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[pulumi.Input[bool]]:
        """
        a boolean indicating whether or not the project is the default project. (Default: "false")
        """
        return pulumi.get(self, "is_default")

    @is_default.setter
    def is_default(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_default", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Project
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def purpose(self) -> Optional[pulumi.Input[str]]:
        """
        the purpose of the project, (Default: "Web Application")
        """
        return pulumi.get(self, "purpose")

    @purpose.setter
    def purpose(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "purpose", value)

    @property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        a list of uniform resource names (URNs) for the resources associated with the project
        """
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "resources", value)


@pulumi.input_type
class _ProjectState:
    def __init__(__self__, *,
                 created_at: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner_id: Optional[pulumi.Input[int]] = None,
                 owner_uuid: Optional[pulumi.Input[str]] = None,
                 purpose: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Project resources.
        :param pulumi.Input[str] created_at: the date and time when the project was created, (ISO8601)
        :param pulumi.Input[str] description: the description of the project
        :param pulumi.Input[str] environment: the environment of the project's resources. The possible values are: `Development`, `Staging`, `Production`)
        :param pulumi.Input[bool] is_default: a boolean indicating whether or not the project is the default project. (Default: "false")
        :param pulumi.Input[str] name: The name of the Project
        :param pulumi.Input[int] owner_id: the id of the project owner.
        :param pulumi.Input[str] owner_uuid: the unique universal identifier of the project owner.
        :param pulumi.Input[str] purpose: the purpose of the project, (Default: "Web Application")
        :param pulumi.Input[Sequence[pulumi.Input[str]]] resources: a list of uniform resource names (URNs) for the resources associated with the project
        :param pulumi.Input[str] updated_at: the date and time when the project was last updated, (ISO8601)
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if environment is not None:
            pulumi.set(__self__, "environment", environment)
        if is_default is not None:
            pulumi.set(__self__, "is_default", is_default)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if owner_id is not None:
            pulumi.set(__self__, "owner_id", owner_id)
        if owner_uuid is not None:
            pulumi.set(__self__, "owner_uuid", owner_uuid)
        if purpose is not None:
            pulumi.set(__self__, "purpose", purpose)
        if resources is not None:
            pulumi.set(__self__, "resources", resources)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        the date and time when the project was created, (ISO8601)
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        the description of the project
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[str]]:
        """
        the environment of the project's resources. The possible values are: `Development`, `Staging`, `Production`)
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[pulumi.Input[bool]]:
        """
        a boolean indicating whether or not the project is the default project. (Default: "false")
        """
        return pulumi.get(self, "is_default")

    @is_default.setter
    def is_default(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_default", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Project
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[int]]:
        """
        the id of the project owner.
        """
        return pulumi.get(self, "owner_id")

    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "owner_id", value)

    @property
    @pulumi.getter(name="ownerUuid")
    def owner_uuid(self) -> Optional[pulumi.Input[str]]:
        """
        the unique universal identifier of the project owner.
        """
        return pulumi.get(self, "owner_uuid")

    @owner_uuid.setter
    def owner_uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner_uuid", value)

    @property
    @pulumi.getter
    def purpose(self) -> Optional[pulumi.Input[str]]:
        """
        the purpose of the project, (Default: "Web Application")
        """
        return pulumi.get(self, "purpose")

    @purpose.setter
    def purpose(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "purpose", value)

    @property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        a list of uniform resource names (URNs) for the resources associated with the project
        """
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "resources", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        the date and time when the project was last updated, (ISO8601)
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)


class Project(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 purpose: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a DigitalOcean Project resource.

        Projects allow you to organize your resources into groups that fit the way you work.
        You can group resources (like Droplets, Spaces, Load Balancers, domains, and Floating IPs)
        in ways that align with the applications you host on DigitalOcean.

        The following resource types can be associated with a project:

        * App Platform Apps
        * Database Clusters
        * Domains
        * Droplets
        * Floating IPs
        * Kubernetes Clusters
        * Load Balancers
        * Spaces Buckets
        * Volumes

        **Note:** A provider managed project cannot be set as a default project.

        ## Example Usage

        The following example demonstrates the creation of an empty project:

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        playground = digitalocean.Project("playground",
            name="playground",
            description="A project to represent development resources.",
            purpose="Web Application",
            environment="Development")
        ```

        The following example demonstrates the creation of a project with a Droplet resource:

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        foobar = digitalocean.Droplet("foobar",
            name="example",
            size=digitalocean.DropletSlug.DROPLET_S1_VCPU1_GB,
            image="ubuntu-22-04-x64",
            region=digitalocean.Region.NYC3)
        playground = digitalocean.Project("playground",
            name="playground",
            description="A project to represent development resources.",
            purpose="Web Application",
            environment="Development",
            resources=[foobar.droplet_urn])
        ```

        ## Import

        Projects can be imported using the `id` returned from DigitalOcean, e.g.

        ```sh
        $ pulumi import digitalocean:index/project:Project myproject 245bcfd0-7f31-4ce6-a2bc-475a116cca97
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: the description of the project
        :param pulumi.Input[str] environment: the environment of the project's resources. The possible values are: `Development`, `Staging`, `Production`)
        :param pulumi.Input[bool] is_default: a boolean indicating whether or not the project is the default project. (Default: "false")
        :param pulumi.Input[str] name: The name of the Project
        :param pulumi.Input[str] purpose: the purpose of the project, (Default: "Web Application")
        :param pulumi.Input[Sequence[pulumi.Input[str]]] resources: a list of uniform resource names (URNs) for the resources associated with the project
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProjectArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a DigitalOcean Project resource.

        Projects allow you to organize your resources into groups that fit the way you work.
        You can group resources (like Droplets, Spaces, Load Balancers, domains, and Floating IPs)
        in ways that align with the applications you host on DigitalOcean.

        The following resource types can be associated with a project:

        * App Platform Apps
        * Database Clusters
        * Domains
        * Droplets
        * Floating IPs
        * Kubernetes Clusters
        * Load Balancers
        * Spaces Buckets
        * Volumes

        **Note:** A provider managed project cannot be set as a default project.

        ## Example Usage

        The following example demonstrates the creation of an empty project:

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        playground = digitalocean.Project("playground",
            name="playground",
            description="A project to represent development resources.",
            purpose="Web Application",
            environment="Development")
        ```

        The following example demonstrates the creation of a project with a Droplet resource:

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        foobar = digitalocean.Droplet("foobar",
            name="example",
            size=digitalocean.DropletSlug.DROPLET_S1_VCPU1_GB,
            image="ubuntu-22-04-x64",
            region=digitalocean.Region.NYC3)
        playground = digitalocean.Project("playground",
            name="playground",
            description="A project to represent development resources.",
            purpose="Web Application",
            environment="Development",
            resources=[foobar.droplet_urn])
        ```

        ## Import

        Projects can be imported using the `id` returned from DigitalOcean, e.g.

        ```sh
        $ pulumi import digitalocean:index/project:Project myproject 245bcfd0-7f31-4ce6-a2bc-475a116cca97
        ```

        :param str resource_name: The name of the resource.
        :param ProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 purpose: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectArgs.__new__(ProjectArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["environment"] = environment
            __props__.__dict__["is_default"] = is_default
            __props__.__dict__["name"] = name
            __props__.__dict__["purpose"] = purpose
            __props__.__dict__["resources"] = resources
            __props__.__dict__["created_at"] = None
            __props__.__dict__["owner_id"] = None
            __props__.__dict__["owner_uuid"] = None
            __props__.__dict__["updated_at"] = None
        super(Project, __self__).__init__(
            'digitalocean:index/project:Project',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            environment: Optional[pulumi.Input[str]] = None,
            is_default: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            owner_id: Optional[pulumi.Input[int]] = None,
            owner_uuid: Optional[pulumi.Input[str]] = None,
            purpose: Optional[pulumi.Input[str]] = None,
            resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'Project':
        """
        Get an existing Project resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: the date and time when the project was created, (ISO8601)
        :param pulumi.Input[str] description: the description of the project
        :param pulumi.Input[str] environment: the environment of the project's resources. The possible values are: `Development`, `Staging`, `Production`)
        :param pulumi.Input[bool] is_default: a boolean indicating whether or not the project is the default project. (Default: "false")
        :param pulumi.Input[str] name: The name of the Project
        :param pulumi.Input[int] owner_id: the id of the project owner.
        :param pulumi.Input[str] owner_uuid: the unique universal identifier of the project owner.
        :param pulumi.Input[str] purpose: the purpose of the project, (Default: "Web Application")
        :param pulumi.Input[Sequence[pulumi.Input[str]]] resources: a list of uniform resource names (URNs) for the resources associated with the project
        :param pulumi.Input[str] updated_at: the date and time when the project was last updated, (ISO8601)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProjectState.__new__(_ProjectState)

        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["description"] = description
        __props__.__dict__["environment"] = environment
        __props__.__dict__["is_default"] = is_default
        __props__.__dict__["name"] = name
        __props__.__dict__["owner_id"] = owner_id
        __props__.__dict__["owner_uuid"] = owner_uuid
        __props__.__dict__["purpose"] = purpose
        __props__.__dict__["resources"] = resources
        __props__.__dict__["updated_at"] = updated_at
        return Project(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        the date and time when the project was created, (ISO8601)
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        the description of the project
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Output[Optional[str]]:
        """
        the environment of the project's resources. The possible values are: `Development`, `Staging`, `Production`)
        """
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> pulumi.Output[Optional[bool]]:
        """
        a boolean indicating whether or not the project is the default project. (Default: "false")
        """
        return pulumi.get(self, "is_default")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Project
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[int]:
        """
        the id of the project owner.
        """
        return pulumi.get(self, "owner_id")

    @property
    @pulumi.getter(name="ownerUuid")
    def owner_uuid(self) -> pulumi.Output[str]:
        """
        the unique universal identifier of the project owner.
        """
        return pulumi.get(self, "owner_uuid")

    @property
    @pulumi.getter
    def purpose(self) -> pulumi.Output[Optional[str]]:
        """
        the purpose of the project, (Default: "Web Application")
        """
        return pulumi.get(self, "purpose")

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Sequence[str]]:
        """
        a list of uniform resource names (URNs) for the resources associated with the project
        """
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        the date and time when the project was last updated, (ISO8601)
        """
        return pulumi.get(self, "updated_at")

