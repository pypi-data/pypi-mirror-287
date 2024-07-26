# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['UploadedCertificateArgs', 'UploadedCertificate']

@pulumi.input_type
class UploadedCertificateArgs:
    def __init__(__self__, *,
                 certificate: pulumi.Input[str],
                 private_key: pulumi.Input[str],
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UploadedCertificate resource.
        :param pulumi.Input[str] certificate: PEM encoded TLS certificate.
        :param pulumi.Input[str] private_key: PEM encoded private key belonging to the certificate.
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) the
               certificate should be created with.
        :param pulumi.Input[str] name: Name of the Certificate.
        """
        pulumi.set(__self__, "certificate", certificate)
        pulumi.set(__self__, "private_key", private_key)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Input[str]:
        """
        PEM encoded TLS certificate.
        """
        return pulumi.get(self, "certificate")

    @certificate.setter
    def certificate(self, value: pulumi.Input[str]):
        pulumi.set(self, "certificate", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Input[str]:
        """
        PEM encoded private key belonging to the certificate.
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        User-defined labels (key-value pairs) the
        certificate should be created with.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Certificate.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _UploadedCertificateState:
    def __init__(__self__, *,
                 certificate: Optional[pulumi.Input[str]] = None,
                 created: Optional[pulumi.Input[str]] = None,
                 domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 fingerprint: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 not_valid_after: Optional[pulumi.Input[str]] = None,
                 not_valid_before: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UploadedCertificate resources.
        :param pulumi.Input[str] certificate: PEM encoded TLS certificate.
        :param pulumi.Input[str] created: (string) Point in time when the Certificate was created at Hetzner Cloud (in ISO-8601 format).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domain_names: (list) Domains and subdomains covered by the certificate.
        :param pulumi.Input[str] fingerprint: (string) Fingerprint of the certificate.
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) the
               certificate should be created with.
        :param pulumi.Input[str] name: Name of the Certificate.
        :param pulumi.Input[str] not_valid_after: (string) Point in time when the Certificate stops being valid (in ISO-8601 format).
        :param pulumi.Input[str] not_valid_before: (string) Point in time when the Certificate becomes valid (in ISO-8601 format).
        :param pulumi.Input[str] private_key: PEM encoded private key belonging to the certificate.
        """
        if certificate is not None:
            pulumi.set(__self__, "certificate", certificate)
        if created is not None:
            pulumi.set(__self__, "created", created)
        if domain_names is not None:
            pulumi.set(__self__, "domain_names", domain_names)
        if fingerprint is not None:
            pulumi.set(__self__, "fingerprint", fingerprint)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if not_valid_after is not None:
            pulumi.set(__self__, "not_valid_after", not_valid_after)
        if not_valid_before is not None:
            pulumi.set(__self__, "not_valid_before", not_valid_before)
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[str]]:
        """
        PEM encoded TLS certificate.
        """
        return pulumi.get(self, "certificate")

    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate", value)

    @property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[str]]:
        """
        (string) Point in time when the Certificate was created at Hetzner Cloud (in ISO-8601 format).
        """
        return pulumi.get(self, "created")

    @created.setter
    def created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created", value)

    @property
    @pulumi.getter(name="domainNames")
    def domain_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        (list) Domains and subdomains covered by the certificate.
        """
        return pulumi.get(self, "domain_names")

    @domain_names.setter
    def domain_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "domain_names", value)

    @property
    @pulumi.getter
    def fingerprint(self) -> Optional[pulumi.Input[str]]:
        """
        (string) Fingerprint of the certificate.
        """
        return pulumi.get(self, "fingerprint")

    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fingerprint", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        User-defined labels (key-value pairs) the
        certificate should be created with.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Certificate.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="notValidAfter")
    def not_valid_after(self) -> Optional[pulumi.Input[str]]:
        """
        (string) Point in time when the Certificate stops being valid (in ISO-8601 format).
        """
        return pulumi.get(self, "not_valid_after")

    @not_valid_after.setter
    def not_valid_after(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "not_valid_after", value)

    @property
    @pulumi.getter(name="notValidBefore")
    def not_valid_before(self) -> Optional[pulumi.Input[str]]:
        """
        (string) Point in time when the Certificate becomes valid (in ISO-8601 format).
        """
        return pulumi.get(self, "not_valid_before")

    @not_valid_before.setter
    def not_valid_before(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "not_valid_before", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[str]]:
        """
        PEM encoded private key belonging to the certificate.
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class UploadedCertificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Upload a TLS certificate to Hetzner Cloud.

        ## Import

        Uploaded certificates can be imported using their `id`:

        hcl

        ```sh
        $ pulumi import hcloud:index/uploadedCertificate:UploadedCertificate sample_certificate id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate: PEM encoded TLS certificate.
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) the
               certificate should be created with.
        :param pulumi.Input[str] name: Name of the Certificate.
        :param pulumi.Input[str] private_key: PEM encoded private key belonging to the certificate.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UploadedCertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Upload a TLS certificate to Hetzner Cloud.

        ## Import

        Uploaded certificates can be imported using their `id`:

        hcl

        ```sh
        $ pulumi import hcloud:index/uploadedCertificate:UploadedCertificate sample_certificate id
        ```

        :param str resource_name: The name of the resource.
        :param UploadedCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UploadedCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UploadedCertificateArgs.__new__(UploadedCertificateArgs)

            if certificate is None and not opts.urn:
                raise TypeError("Missing required property 'certificate'")
            __props__.__dict__["certificate"] = certificate
            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            if private_key is None and not opts.urn:
                raise TypeError("Missing required property 'private_key'")
            __props__.__dict__["private_key"] = None if private_key is None else pulumi.Output.secret(private_key)
            __props__.__dict__["created"] = None
            __props__.__dict__["domain_names"] = None
            __props__.__dict__["fingerprint"] = None
            __props__.__dict__["not_valid_after"] = None
            __props__.__dict__["not_valid_before"] = None
            __props__.__dict__["type"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["privateKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(UploadedCertificate, __self__).__init__(
            'hcloud:index/uploadedCertificate:UploadedCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            certificate: Optional[pulumi.Input[str]] = None,
            created: Optional[pulumi.Input[str]] = None,
            domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            fingerprint: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            not_valid_after: Optional[pulumi.Input[str]] = None,
            not_valid_before: Optional[pulumi.Input[str]] = None,
            private_key: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'UploadedCertificate':
        """
        Get an existing UploadedCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate: PEM encoded TLS certificate.
        :param pulumi.Input[str] created: (string) Point in time when the Certificate was created at Hetzner Cloud (in ISO-8601 format).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domain_names: (list) Domains and subdomains covered by the certificate.
        :param pulumi.Input[str] fingerprint: (string) Fingerprint of the certificate.
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) the
               certificate should be created with.
        :param pulumi.Input[str] name: Name of the Certificate.
        :param pulumi.Input[str] not_valid_after: (string) Point in time when the Certificate stops being valid (in ISO-8601 format).
        :param pulumi.Input[str] not_valid_before: (string) Point in time when the Certificate becomes valid (in ISO-8601 format).
        :param pulumi.Input[str] private_key: PEM encoded private key belonging to the certificate.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UploadedCertificateState.__new__(_UploadedCertificateState)

        __props__.__dict__["certificate"] = certificate
        __props__.__dict__["created"] = created
        __props__.__dict__["domain_names"] = domain_names
        __props__.__dict__["fingerprint"] = fingerprint
        __props__.__dict__["labels"] = labels
        __props__.__dict__["name"] = name
        __props__.__dict__["not_valid_after"] = not_valid_after
        __props__.__dict__["not_valid_before"] = not_valid_before
        __props__.__dict__["private_key"] = private_key
        __props__.__dict__["type"] = type
        return UploadedCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Output[str]:
        """
        PEM encoded TLS certificate.
        """
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        """
        (string) Point in time when the Certificate was created at Hetzner Cloud (in ISO-8601 format).
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="domainNames")
    def domain_names(self) -> pulumi.Output[Sequence[str]]:
        """
        (list) Domains and subdomains covered by the certificate.
        """
        return pulumi.get(self, "domain_names")

    @property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        """
        (string) Fingerprint of the certificate.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        User-defined labels (key-value pairs) the
        certificate should be created with.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the Certificate.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notValidAfter")
    def not_valid_after(self) -> pulumi.Output[str]:
        """
        (string) Point in time when the Certificate stops being valid (in ISO-8601 format).
        """
        return pulumi.get(self, "not_valid_after")

    @property
    @pulumi.getter(name="notValidBefore")
    def not_valid_before(self) -> pulumi.Output[str]:
        """
        (string) Point in time when the Certificate becomes valid (in ISO-8601 format).
        """
        return pulumi.get(self, "not_valid_before")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[str]:
        """
        PEM encoded private key belonging to the certificate.
        """
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "type")

