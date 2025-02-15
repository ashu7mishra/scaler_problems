from __future__ import annotations
from typing import Type, Any

from .config_manager import FileBasedConfigurationManager


class FileBasedConfigurationManagerImpl(FileBasedConfigurationManager):
    @staticmethod
    def get_instance() -> FileBasedConfigurationManager:
        return FileBasedConfigurationManagerImpl()

    @staticmethod
    def reset_instance() -> None:
        pass

    def get_configuration(self, key: str) -> str:
        raise NotImplementedError("Unimplemented method 'get_configuration'")

    def get_configuration_with_type(self, key: str, type_: Type) -> Any:
        raise NotImplementedError("Unimplemented method 'get_configuration_with_type'")

    def set_configuration(self, key: str, value: str) -> None:
        raise NotImplementedError("Unimplemented method 'set_configuration'")

    def remove_configuration(self, key: str) -> None:
        raise NotImplementedError("Unimplemented method 'remove_configuration'")

    def clear(self) -> None:
        raise NotImplementedError("Unimplemented method 'clear'")
