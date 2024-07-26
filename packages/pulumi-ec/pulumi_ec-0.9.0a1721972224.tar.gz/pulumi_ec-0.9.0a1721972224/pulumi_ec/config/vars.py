# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('ec')


class _ExportableConfig(types.ModuleType):
    @property
    def apikey(self) -> Optional[str]:
        """
        API Key to use for API authentication. The only valid authentication mechanism for the Elasticsearch Service.
        """
        return __config__.get('apikey')

    @property
    def endpoint(self) -> Optional[str]:
        return __config__.get('endpoint')

    @property
    def insecure(self) -> Optional[bool]:
        """
        Allow the provider to skip TLS validation on its outgoing HTTP calls.
        """
        return __config__.get_bool('insecure')

    @property
    def password(self) -> Optional[str]:
        """
        Password to use for API authentication. Available only when targeting ECE Installations or Elasticsearch Service
        Private.
        """
        return __config__.get('password')

    @property
    def timeout(self) -> Optional[str]:
        """
        Timeout used for individual HTTP calls. Defaults to "1m".
        """
        return __config__.get('timeout')

    @property
    def username(self) -> Optional[str]:
        """
        Username to use for API authentication. Available only when targeting ECE Installations or Elasticsearch Service
        Private.
        """
        return __config__.get('username')

    @property
    def verbose(self) -> Optional[bool]:
        """
        When set, a "request.log" file will be written with all outgoing HTTP requests. Defaults to "false".
        """
        return __config__.get_bool('verbose')

    @property
    def verbose_credentials(self) -> Optional[bool]:
        """
        When set with verbose, the contents of the Authorization header will not be redacted. Defaults to "false".
        """
        return __config__.get_bool('verboseCredentials')

    @property
    def verbose_file(self) -> Optional[str]:
        """
        Timeout used for individual HTTP calls. Defaults to "1m".
        """
        return __config__.get('verboseFile')

