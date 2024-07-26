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

__config__ = pulumi.Config('rabbitmq')


class _ExportableConfig(types.ModuleType):
    @property
    def cacert_file(self) -> Optional[str]:
        return __config__.get('cacertFile') or _utilities.get_env('RABBITMQ_CACERT')

    @property
    def clientcert_file(self) -> Optional[str]:
        return __config__.get('clientcertFile')

    @property
    def clientkey_file(self) -> Optional[str]:
        return __config__.get('clientkeyFile')

    @property
    def endpoint(self) -> Optional[str]:
        return __config__.get('endpoint')

    @property
    def insecure(self) -> Optional[bool]:
        return __config__.get_bool('insecure') or _utilities.get_env_bool('RABBITMQ_INSECURE')

    @property
    def password(self) -> Optional[str]:
        return __config__.get('password')

    @property
    def proxy(self) -> Optional[str]:
        return __config__.get('proxy')

    @property
    def username(self) -> Optional[str]:
        return __config__.get('username')

