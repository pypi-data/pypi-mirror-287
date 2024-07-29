#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Generic, Callable, Any, final

from ..config.serialize import SerializeConfig
from ..exceptions import SerializeException
from ..generic import T
from ..utils.strings import StringUtils
from ..utils.objects import ObjectsUtils


class _SerializeField(Generic[T]):

    def __init__(self, value: T, *, name=None, autoname: bool = False, camel: bool = False,
                 hooks: list[Callable[[T], bool]] = None):
        ObjectsUtils.check_type(name, str, type(None))
        ObjectsUtils.check_type(autoname, bool)
        ObjectsUtils.check_type(camel, bool)
        self.__name: str = name
        self.__autoname: bool = autoname
        self.__camel: bool = camel
        self.__hooks: list[Callable[[T], bool]] = hooks or []
        self.__hook_handler(value)

    @final
    def __hook_handler(self, value):
        for hook in self.__hooks:
            if not hook(value):
                raise SerializeException(f"{self.__class__.__name__}: {value} hook result fail.")
        self.__value = value

    @final
    @property
    def value(self) -> T:
        """
        object's origin value.
        field = SerializeField("ABC")
        print(field.value)  # "ABC"

        field = SerializeField(123)
        print(field.value)  # 123
        :return:
        """
        return self.__value

    @final
    @value.setter
    def value(self, value: T):
        """
        modify field value.
        will run hooks callback function, if return False will raise exception.
        """
        self.__hook_handler(value)

    @final
    @property
    def name(self) -> str:
        """
        The name of the serialized key
        class User(Serializable):
            def __init__(self):
                self.__name = SerializeField("Tony", name="userName")
        User().serializer()  # {"userName": "Tony"}
        :return:
        """
        return self.__name

    @final
    @property
    def autoname(self) -> bool:
        """
        If you do not specify a name, try to automatically generate a name.
        class User(Serializable):
            def __init__(self):
                self.__name = SerializeField("Tony", autoname=True)
        User().serializer()  # {"name": "Tony"}
        :return:
        """
        return self.__autoname

    @final
    @property
    def camel(self) -> bool:
        """
        Convert python's serpentine naming to camel naming.
        only autoname is True has valid.
        class User(Serializable):
            def __init__(self):
                self.__user_name = SerializeField("Tony", autoname=True, camel=True)
        User().serializer()  # {"userName": "Tony"}

        class User(Serializable):
            def __init__(self):
                self.__user_name = SerializeField("Tony", autoname=True)
        User().serializer()  # {"user_name": "Tony"}
        :return:
        """
        return self.__camel


def __parser_iter(values, camel):
    l = []
    l_append = l.append
    for value in values:
        l_append(__parser(value, camel))
    return l


def __parser_dict(values, camel):
    d = {}
    for key, value in values.items():
        if camel:
            k = StringUtils.convert_to_camel(key).origin()
        else:
            k = key
        d[k] = __parser(value, camel)
    return d


def __parser(value, camel):
    if issubclass(type(value), (list, tuple, set)):
        return __parser_iter(value, camel)
    elif issubclass(type(value), dict):
        return __parser_dict(value, camel)
    elif isinstance(value, _Serializable):
        return value.serializer()
    return value


def _serializer(value, camel):
    return __parser(value, camel)


class _Serializable(Generic[T]):

    def __new__(cls, *args, **kwargs):
        instance = object.__new__(cls)
        prefix = f"_{cls.__name__}__"
        instance.__prefix = prefix
        return instance

    @property
    def autoname(self) -> bool:
        return False

    @property
    def camel(self) -> bool:
        return False

    @final
    def __serializer(self) -> dict[str, T]:
        d = {}
        index = 0
        for key, value in self.__dict__.items():
            if isinstance(value, _SerializeField):
                index += 1
                camel = value.camel or self.camel or SerializeConfig.camel
                name = value.name
                if not name:
                    name = f"unknownKey{index}"
                    if value.autoname or self.autoname or SerializeConfig.autoname:
                        if key.startswith(self.__prefix):
                            name = key.replace(self.__prefix, "")
                        elif key[0] == "_" and key[1] != "_":
                            name = key[1:]
                        if camel:
                            name = StringUtils.convert_to_camel(name).origin()
                if (name and (len(name) == 1 and len("_"))) or StringUtils.is_black(name):
                    continue
                d[name] = _serializer(value.value, camel)
        return d

    @final
    def serializer(self) -> dict[str, T] or Any:
        """
        For serialization operations, custom serialization methods are used first,
        and defaults are used if not implemented
        :return:
        """
        try:
            return self.custom_serializer()
        except NotImplementedError:
            return self.__serializer()

    def custom_serializer(self):
        """
        A custom serialization interface is provided to the user, and if the interface is implemented,
        the serialization results of the interface are preferentially used。
        :return:
        """
        raise NotImplementedError


__all__ = [_Serializable, _SerializeField, _serializer]
