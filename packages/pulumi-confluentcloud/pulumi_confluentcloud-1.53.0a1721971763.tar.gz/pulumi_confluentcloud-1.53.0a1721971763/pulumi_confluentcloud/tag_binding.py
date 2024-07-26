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
from ._inputs import *

__all__ = ['TagBindingArgs', 'TagBinding']

@pulumi.input_type
class TagBindingArgs:
    def __init__(__self__, *,
                 entity_name: pulumi.Input[str],
                 entity_type: pulumi.Input[str],
                 tag_name: pulumi.Input[str],
                 credentials: Optional[pulumi.Input['TagBindingCredentialsArgs']] = None,
                 rest_endpoint: Optional[pulumi.Input[str]] = None,
                 schema_registry_cluster: Optional[pulumi.Input['TagBindingSchemaRegistryClusterArgs']] = None):
        """
        The set of arguments for constructing a TagBinding resource.
        :param pulumi.Input[str] entity_name: The qualified name of the entity., for example, `${data.confluent_schema_registry_cluster.main.id}:.:${confluent_schema.purchase.schema_identifier}`, `${data.confluent_schema_registry_cluster.main.id}:${confluent_kafka_cluster.basic.id}:${confluent_kafka_topic.purchase.topic_name}`.
        :param pulumi.Input[str] entity_type: The entity type.
        :param pulumi.Input[str] tag_name: The name of the tag to be applied, for example, `PII`. The name must not be empty and consist of a letter followed by a sequence of letter, number, space, or _ characters.
        :param pulumi.Input['TagBindingCredentialsArgs'] credentials: The Cluster API Credentials.
        :param pulumi.Input[str] rest_endpoint: The REST endpoint of the Schema Registry cluster, for example, `https://psrc-00000.us-central1.gcp.confluent.cloud:443`).
        """
        pulumi.set(__self__, "entity_name", entity_name)
        pulumi.set(__self__, "entity_type", entity_type)
        pulumi.set(__self__, "tag_name", tag_name)
        if credentials is not None:
            pulumi.set(__self__, "credentials", credentials)
        if rest_endpoint is not None:
            pulumi.set(__self__, "rest_endpoint", rest_endpoint)
        if schema_registry_cluster is not None:
            pulumi.set(__self__, "schema_registry_cluster", schema_registry_cluster)

    @property
    @pulumi.getter(name="entityName")
    def entity_name(self) -> pulumi.Input[str]:
        """
        The qualified name of the entity., for example, `${data.confluent_schema_registry_cluster.main.id}:.:${confluent_schema.purchase.schema_identifier}`, `${data.confluent_schema_registry_cluster.main.id}:${confluent_kafka_cluster.basic.id}:${confluent_kafka_topic.purchase.topic_name}`.
        """
        return pulumi.get(self, "entity_name")

    @entity_name.setter
    def entity_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "entity_name", value)

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Input[str]:
        """
        The entity type.
        """
        return pulumi.get(self, "entity_type")

    @entity_type.setter
    def entity_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "entity_type", value)

    @property
    @pulumi.getter(name="tagName")
    def tag_name(self) -> pulumi.Input[str]:
        """
        The name of the tag to be applied, for example, `PII`. The name must not be empty and consist of a letter followed by a sequence of letter, number, space, or _ characters.
        """
        return pulumi.get(self, "tag_name")

    @tag_name.setter
    def tag_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "tag_name", value)

    @property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input['TagBindingCredentialsArgs']]:
        """
        The Cluster API Credentials.
        """
        return pulumi.get(self, "credentials")

    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input['TagBindingCredentialsArgs']]):
        pulumi.set(self, "credentials", value)

    @property
    @pulumi.getter(name="restEndpoint")
    def rest_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        The REST endpoint of the Schema Registry cluster, for example, `https://psrc-00000.us-central1.gcp.confluent.cloud:443`).
        """
        return pulumi.get(self, "rest_endpoint")

    @rest_endpoint.setter
    def rest_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rest_endpoint", value)

    @property
    @pulumi.getter(name="schemaRegistryCluster")
    def schema_registry_cluster(self) -> Optional[pulumi.Input['TagBindingSchemaRegistryClusterArgs']]:
        return pulumi.get(self, "schema_registry_cluster")

    @schema_registry_cluster.setter
    def schema_registry_cluster(self, value: Optional[pulumi.Input['TagBindingSchemaRegistryClusterArgs']]):
        pulumi.set(self, "schema_registry_cluster", value)


@pulumi.input_type
class _TagBindingState:
    def __init__(__self__, *,
                 credentials: Optional[pulumi.Input['TagBindingCredentialsArgs']] = None,
                 entity_name: Optional[pulumi.Input[str]] = None,
                 entity_type: Optional[pulumi.Input[str]] = None,
                 rest_endpoint: Optional[pulumi.Input[str]] = None,
                 schema_registry_cluster: Optional[pulumi.Input['TagBindingSchemaRegistryClusterArgs']] = None,
                 tag_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TagBinding resources.
        :param pulumi.Input['TagBindingCredentialsArgs'] credentials: The Cluster API Credentials.
        :param pulumi.Input[str] entity_name: The qualified name of the entity., for example, `${data.confluent_schema_registry_cluster.main.id}:.:${confluent_schema.purchase.schema_identifier}`, `${data.confluent_schema_registry_cluster.main.id}:${confluent_kafka_cluster.basic.id}:${confluent_kafka_topic.purchase.topic_name}`.
        :param pulumi.Input[str] entity_type: The entity type.
        :param pulumi.Input[str] rest_endpoint: The REST endpoint of the Schema Registry cluster, for example, `https://psrc-00000.us-central1.gcp.confluent.cloud:443`).
        :param pulumi.Input[str] tag_name: The name of the tag to be applied, for example, `PII`. The name must not be empty and consist of a letter followed by a sequence of letter, number, space, or _ characters.
        """
        if credentials is not None:
            pulumi.set(__self__, "credentials", credentials)
        if entity_name is not None:
            pulumi.set(__self__, "entity_name", entity_name)
        if entity_type is not None:
            pulumi.set(__self__, "entity_type", entity_type)
        if rest_endpoint is not None:
            pulumi.set(__self__, "rest_endpoint", rest_endpoint)
        if schema_registry_cluster is not None:
            pulumi.set(__self__, "schema_registry_cluster", schema_registry_cluster)
        if tag_name is not None:
            pulumi.set(__self__, "tag_name", tag_name)

    @property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input['TagBindingCredentialsArgs']]:
        """
        The Cluster API Credentials.
        """
        return pulumi.get(self, "credentials")

    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input['TagBindingCredentialsArgs']]):
        pulumi.set(self, "credentials", value)

    @property
    @pulumi.getter(name="entityName")
    def entity_name(self) -> Optional[pulumi.Input[str]]:
        """
        The qualified name of the entity., for example, `${data.confluent_schema_registry_cluster.main.id}:.:${confluent_schema.purchase.schema_identifier}`, `${data.confluent_schema_registry_cluster.main.id}:${confluent_kafka_cluster.basic.id}:${confluent_kafka_topic.purchase.topic_name}`.
        """
        return pulumi.get(self, "entity_name")

    @entity_name.setter
    def entity_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "entity_name", value)

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> Optional[pulumi.Input[str]]:
        """
        The entity type.
        """
        return pulumi.get(self, "entity_type")

    @entity_type.setter
    def entity_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "entity_type", value)

    @property
    @pulumi.getter(name="restEndpoint")
    def rest_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        The REST endpoint of the Schema Registry cluster, for example, `https://psrc-00000.us-central1.gcp.confluent.cloud:443`).
        """
        return pulumi.get(self, "rest_endpoint")

    @rest_endpoint.setter
    def rest_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rest_endpoint", value)

    @property
    @pulumi.getter(name="schemaRegistryCluster")
    def schema_registry_cluster(self) -> Optional[pulumi.Input['TagBindingSchemaRegistryClusterArgs']]:
        return pulumi.get(self, "schema_registry_cluster")

    @schema_registry_cluster.setter
    def schema_registry_cluster(self, value: Optional[pulumi.Input['TagBindingSchemaRegistryClusterArgs']]):
        pulumi.set(self, "schema_registry_cluster", value)

    @property
    @pulumi.getter(name="tagName")
    def tag_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the tag to be applied, for example, `PII`. The name must not be empty and consist of a letter followed by a sequence of letter, number, space, or _ characters.
        """
        return pulumi.get(self, "tag_name")

    @tag_name.setter
    def tag_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tag_name", value)


class TagBinding(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credentials: Optional[pulumi.Input[pulumi.InputType['TagBindingCredentialsArgs']]] = None,
                 entity_name: Optional[pulumi.Input[str]] = None,
                 entity_type: Optional[pulumi.Input[str]] = None,
                 rest_endpoint: Optional[pulumi.Input[str]] = None,
                 schema_registry_cluster: Optional[pulumi.Input[pulumi.InputType['TagBindingSchemaRegistryClusterArgs']]] = None,
                 tag_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Import

        You can import a Tag Binding by using the Schema Registry cluster ID, Tag name, entity name and entity type in the format `<Schema Registry Cluster Id>/<Tag Name>/<Entity Name>/<Entity Type>`, for example:

        $ export IMPORT_SCHEMA_REGISTRY_API_KEY="<schema_registry_api_key>"

        $ export IMPORT_SCHEMA_REGISTRY_API_SECRET="<schema_registry_api_secret>"

        $ export IMPORT_SCHEMA_REGISTRY_REST_ENDPOINT="<schema_registry_rest_endpoint>"

        ```sh
        $ pulumi import confluentcloud:index/tagBinding:TagBinding main lsrc-8wrx70/PII/lsrc-8wrx70:.:100001/sr_schema
        ```

        !> **Warning:** Do not forget to delete terminal command history afterwards for security purposes.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['TagBindingCredentialsArgs']] credentials: The Cluster API Credentials.
        :param pulumi.Input[str] entity_name: The qualified name of the entity., for example, `${data.confluent_schema_registry_cluster.main.id}:.:${confluent_schema.purchase.schema_identifier}`, `${data.confluent_schema_registry_cluster.main.id}:${confluent_kafka_cluster.basic.id}:${confluent_kafka_topic.purchase.topic_name}`.
        :param pulumi.Input[str] entity_type: The entity type.
        :param pulumi.Input[str] rest_endpoint: The REST endpoint of the Schema Registry cluster, for example, `https://psrc-00000.us-central1.gcp.confluent.cloud:443`).
        :param pulumi.Input[str] tag_name: The name of the tag to be applied, for example, `PII`. The name must not be empty and consist of a letter followed by a sequence of letter, number, space, or _ characters.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TagBindingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        You can import a Tag Binding by using the Schema Registry cluster ID, Tag name, entity name and entity type in the format `<Schema Registry Cluster Id>/<Tag Name>/<Entity Name>/<Entity Type>`, for example:

        $ export IMPORT_SCHEMA_REGISTRY_API_KEY="<schema_registry_api_key>"

        $ export IMPORT_SCHEMA_REGISTRY_API_SECRET="<schema_registry_api_secret>"

        $ export IMPORT_SCHEMA_REGISTRY_REST_ENDPOINT="<schema_registry_rest_endpoint>"

        ```sh
        $ pulumi import confluentcloud:index/tagBinding:TagBinding main lsrc-8wrx70/PII/lsrc-8wrx70:.:100001/sr_schema
        ```

        !> **Warning:** Do not forget to delete terminal command history afterwards for security purposes.

        :param str resource_name: The name of the resource.
        :param TagBindingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TagBindingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credentials: Optional[pulumi.Input[pulumi.InputType['TagBindingCredentialsArgs']]] = None,
                 entity_name: Optional[pulumi.Input[str]] = None,
                 entity_type: Optional[pulumi.Input[str]] = None,
                 rest_endpoint: Optional[pulumi.Input[str]] = None,
                 schema_registry_cluster: Optional[pulumi.Input[pulumi.InputType['TagBindingSchemaRegistryClusterArgs']]] = None,
                 tag_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TagBindingArgs.__new__(TagBindingArgs)

            __props__.__dict__["credentials"] = None if credentials is None else pulumi.Output.secret(credentials)
            if entity_name is None and not opts.urn:
                raise TypeError("Missing required property 'entity_name'")
            __props__.__dict__["entity_name"] = entity_name
            if entity_type is None and not opts.urn:
                raise TypeError("Missing required property 'entity_type'")
            __props__.__dict__["entity_type"] = entity_type
            __props__.__dict__["rest_endpoint"] = rest_endpoint
            __props__.__dict__["schema_registry_cluster"] = schema_registry_cluster
            if tag_name is None and not opts.urn:
                raise TypeError("Missing required property 'tag_name'")
            __props__.__dict__["tag_name"] = tag_name
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["credentials"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(TagBinding, __self__).__init__(
            'confluentcloud:index/tagBinding:TagBinding',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            credentials: Optional[pulumi.Input[pulumi.InputType['TagBindingCredentialsArgs']]] = None,
            entity_name: Optional[pulumi.Input[str]] = None,
            entity_type: Optional[pulumi.Input[str]] = None,
            rest_endpoint: Optional[pulumi.Input[str]] = None,
            schema_registry_cluster: Optional[pulumi.Input[pulumi.InputType['TagBindingSchemaRegistryClusterArgs']]] = None,
            tag_name: Optional[pulumi.Input[str]] = None) -> 'TagBinding':
        """
        Get an existing TagBinding resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['TagBindingCredentialsArgs']] credentials: The Cluster API Credentials.
        :param pulumi.Input[str] entity_name: The qualified name of the entity., for example, `${data.confluent_schema_registry_cluster.main.id}:.:${confluent_schema.purchase.schema_identifier}`, `${data.confluent_schema_registry_cluster.main.id}:${confluent_kafka_cluster.basic.id}:${confluent_kafka_topic.purchase.topic_name}`.
        :param pulumi.Input[str] entity_type: The entity type.
        :param pulumi.Input[str] rest_endpoint: The REST endpoint of the Schema Registry cluster, for example, `https://psrc-00000.us-central1.gcp.confluent.cloud:443`).
        :param pulumi.Input[str] tag_name: The name of the tag to be applied, for example, `PII`. The name must not be empty and consist of a letter followed by a sequence of letter, number, space, or _ characters.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TagBindingState.__new__(_TagBindingState)

        __props__.__dict__["credentials"] = credentials
        __props__.__dict__["entity_name"] = entity_name
        __props__.__dict__["entity_type"] = entity_type
        __props__.__dict__["rest_endpoint"] = rest_endpoint
        __props__.__dict__["schema_registry_cluster"] = schema_registry_cluster
        __props__.__dict__["tag_name"] = tag_name
        return TagBinding(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional['outputs.TagBindingCredentials']]:
        """
        The Cluster API Credentials.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter(name="entityName")
    def entity_name(self) -> pulumi.Output[str]:
        """
        The qualified name of the entity., for example, `${data.confluent_schema_registry_cluster.main.id}:.:${confluent_schema.purchase.schema_identifier}`, `${data.confluent_schema_registry_cluster.main.id}:${confluent_kafka_cluster.basic.id}:${confluent_kafka_topic.purchase.topic_name}`.
        """
        return pulumi.get(self, "entity_name")

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Output[str]:
        """
        The entity type.
        """
        return pulumi.get(self, "entity_type")

    @property
    @pulumi.getter(name="restEndpoint")
    def rest_endpoint(self) -> pulumi.Output[Optional[str]]:
        """
        The REST endpoint of the Schema Registry cluster, for example, `https://psrc-00000.us-central1.gcp.confluent.cloud:443`).
        """
        return pulumi.get(self, "rest_endpoint")

    @property
    @pulumi.getter(name="schemaRegistryCluster")
    def schema_registry_cluster(self) -> pulumi.Output[Optional['outputs.TagBindingSchemaRegistryCluster']]:
        return pulumi.get(self, "schema_registry_cluster")

    @property
    @pulumi.getter(name="tagName")
    def tag_name(self) -> pulumi.Output[str]:
        """
        The name of the tag to be applied, for example, `PII`. The name must not be empty and consist of a letter followed by a sequence of letter, number, space, or _ characters.
        """
        return pulumi.get(self, "tag_name")

