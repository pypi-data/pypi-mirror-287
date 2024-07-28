from typing import overload, Any, Hashable


class DeepDict:

    hooks_before_set = []

    def __init__(self, dict: dict):
        self.__dict = dict

    @property
    def origin(self) -> dict:
        return self.__dict

    def __str__(self) -> str:
        return str(self.__dict)

    def __truediv__(self, path: str | list) -> 'DeepDict':
        return self.path(path)

    def __getattr__(self, name: str) -> 'DeepDict':
        return self.path(name)

    def path(self, path: list[Hashable] | str) -> 'DeepDict':
        if isinstance(path, str):
            path = path.split('.')
        for key in path:
            if key not in self.__dict:
                self.__dict[key] = dict()
            elif key in self.__dict and not isinstance(self.__dict[key], dict):
                raise ValueError(f'{self}, {path} is not dict path')
            self.__dict = self.__dict[key]
        return DeepDict(self.__dict)

    @overload
    def set(self, keys: Hashable, values: Any) -> 'DeepDict': ...

    @overload
    def set(self, keys: list[Hashable], values: list) -> 'DeepDict': ...

    def set(self, keys: list[Hashable] | Hashable, values: list | Any) -> 'DeepDict':
        if self.hooks_before_set:
            for hook in self.hooks_before_set:
                if isinstance(values, list):
                    values = list(map(hook, values))
                else:
                    values = hook(values)
        if not isinstance(keys, list):
            self.__dict[keys] = values
            return self
        if len(keys) != len(values):
            raise ValueError('keys and values must have same length')
        for key, value in zip(keys, values):
            if not value:
                continue
            self.__dict[key] = value
        return self

    def alist(self, list_property: Hashable) -> list:
        if list_property not in self.__dict:
            self.__dict[list_property] = []
        return self.__dict[list_property]
