from __future__ import annotations
from typing import Type, Any, Dict, Optional

import threading

from .config_manager import FileBasedConfigurationManager


class FileBasedConfigurationManagerImpl(FileBasedConfigurationManager):
    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_instance() -> FileBasedConfigurationManager:
        if FileBasedConfigurationManagerImpl.__instance is None:
            with FileBasedConfigurationManagerImpl.__lock:
                if FileBasedConfigurationManagerImpl.__instance is None:
                    FileBasedConfigurationManagerImpl.__instance = FileBasedConfigurationManagerImpl()

        return FileBasedConfigurationManagerImpl.__instance

    @staticmethod
    def reset_instance() -> None:
        with FileBasedConfigurationManagerImpl.__lock:
            FileBasedConfigurationManagerImpl.__instance = None

    def get_configuration(self, key: str) -> str:
        # raise NotImplementedError("Unimplemented method 'get_configuration'")
        return self.get_properties().get(key, None)

    def get_configuration_with_type(self, key: str, type_: Type) -> Any:
        # raise NotImplementedError("Unimplemented method 'get_configuration_with_type'")
        value = self.get_properties().get(key)
        return  self.convert(value, type_) if value is not None else None

    def set_configuration(self, key: str, value: str) -> None:
        # raise NotImplementedError("Unimplemented method 'set_configuration'")
        self.properties().update({key: value})

    def set_configuration_with_value(self, key: str, value: Any) -> None:
        self.properties().update(key, str(value))

    def remove_configuration(self, key: str) -> None:
        # raise NotImplementedError("Unimplemented method 'remove_configuration'")
        self.properties().pop(key, None)

    def clear(self) -> None:
        # raise NotImplementedError("Unimplemented method 'clear'")
        self.properties().clear()