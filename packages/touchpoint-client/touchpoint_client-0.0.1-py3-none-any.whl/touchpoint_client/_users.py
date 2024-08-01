from .exceptions import *
from .types import *
from ._decorators import use_error_details
import typing

__all__ = ["_Users"]


class _Users:
    """
    Доступ к личной информации
    """
    def __init__(self, client: ConnectorBase):
        self._client: ConnectorBase = client

    @use_error_details
    def permissions(self, *, error_details: bool = False, **kwargs):
        """
        Получить все разрешения на аккаунт

        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        res = self._client.get("permissions", **kwargs)
        if res.status_code in (200,):
            return res.json()
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def projects_permissions(self, *, error_details: bool = False, **kwargs) -> typing.List[str]:
        """
        Получить все разрешения на проект

        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        res = self._client.get("projects/permissions", **kwargs)
        if res.status_code in (200,):
            return res.json()
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def users(self, *, error_details: bool = False, **kwargs) -> typing.List[dict]:
        """
        Получить список пользователей

        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        res = self._client.get("users", **kwargs)
        if res.status_code in (200,):
            return res.json()
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def create_user(self,
              username: str,
              password: str,
              account_role_id: str,
              personal_settings: typing.Optional[dict] = None,
              *,
              error_details: bool = False,
              **kwargs) -> typing.List[dict]:
        r"""Получить список пользователей

        :param username: Имя пользователя, которое является его электронной почтой
        :param password: Пароль пользователя
        :param account_role_id: Идентификатор роли на аккаунт
        :param personal_settings: Персональные настройки пользователя
        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        assert username, "username cannot be empty"
        assert password, "password cannot be empty"
        assert account_role_id, "account_role cannot be empty"
        body = {
            "username": username,
            "password": password,
            "account_role_id": account_role_id,
        }
        if personal_settings:
            body["personal_settings"] = personal_settings
        res = self._client.post("users", json=body, **kwargs)
        if res.status_code in (201,200):
            return res.json()
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def user(self, user_id: str, *, error_details: bool = False, **kwargs) -> typing.Optional[dict]:
        r"""Получить пользователья по идентификатору

        :param user_id: Идентификатор пользователя
        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        assert user_id, "user_id is required"
        res = self._client.get(f"users/{user_id}", **kwargs)
        if res.status_code in (200,):
            return res.json()
        try:
            if res.status_code in (404,) and res.json()["code"] == 3:
                return
        except:
            pass
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def update_user(self,
                    user_id: str,
                    *,
                    account_role_id: typing.Optional[str] = None,
                    personal_settings: typing.Optional[dict] = None,
                    error_details: bool = False,
                    **kwargs) -> typing.Optional[dict]:
        r"""Получить пользователья по идентификатору

        :param user_id: Идентификатор пользователя
        :param user_data: Данные пользователя для обновления
        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        assert user_id, "user_id is required"
        assert account_role_id or personal_settings is not None, "account_role or personal_settings must not be empty"

        body = {}
        if account_role_id:
            body["account_role_id"] = account_role_id,
        if personal_settings is not None:
            body["personal_settings"] = personal_settings,
        res = self._client.patch(f"users/{user_id}", json=body, **kwargs)
        if res.status_code in (200,):
            return res.json()
        try:
            if res.status_code in (404,) and res.json()["code"] == 3:
                return
        except:
            pass
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def groups(self, *, error_details: bool = False, **kwargs) -> typing.List[dict]:
        """
        Получить список групп

        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        res = self._client.get("groups", **kwargs)
        if res.status_code in (200,):
            return res.json()["data"]
        raise RequestError(res.status_code, res.text)

    def create_group(self,
              name: str,
              *,
              error_details: bool = False,
              **kwargs) -> typing.List[dict]:
        r"""Получить список пользователей

        :param name: Имя группы
        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        assert name, "name cannot be empty"
        body = {
            "name": name,
        }
        res = self._client.post("groups", json=body, **kwargs)
        if res.status_code in (201,200):
            return res.json()
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def group(self, group_id: str, *, error_details: bool = False, **kwargs) -> typing.Optional[dict]:
        r"""Получить группу по идентификатору

        :param group_id: Идентификатор пользователя
        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        assert group_id, "group_id is required"
        res = self._client.get(f"groups/{group_id}", **kwargs)
        if res.status_code in (200,):
            return res.json()
        try:
            if res.status_code in (404,) and res.json()["code"] == 3:
                return
        except:
            pass
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def update_group(self,
                     group_id: str,
                     *,
                     name: str,
                     error_details: bool = False,
                     **kwargs) -> typing.Optional[dict]:
        r"""Обновить данный группы

        :param group_id: Идентификатор группы
        :param name: Имя группы
        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        assert group_id, "group_id is required"
        assert name, "account_role or personal_settings must not be empty"

        body = {
            "name": name,
        }
        res = self._client.patch(f"groups/{group_id}", json=body, **kwargs)
        if res.status_code in (200,):
            return res.json()
        try:
            if res.status_code in (404,) and res.json()["code"] == 3:
                return
        except:
            pass
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def group_users(self, group_id: str, *, error_details: bool = False, **kwargs) -> typing.Optional[dict]:
        r"""Получить пользователей группы

        :param group_id: Идентификатор группы
        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        assert group_id, "group_id is required"
        res = self._client.get(f"groups/{group_id}/users", **kwargs)
        if res.status_code in (200,):
            return res.json()["data"]
        try:
            if res.status_code in (404,) and res.json()["code"] == 3:
                return
        except:
            pass
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def create_group_user(self,
                          group_id: str,
                          user_id: str,
                          *,
                          error_details: bool = False,
                          **kwargs) -> typing.Optional[dict]:
        r"""Добавить пользователя в группу

        :param group_id: Идентификатор группы
        :param user_id: Идентификатор пользователя
        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        assert group_id, "group_id is required"
        res = self._client.put(f"groups/{group_id}/users/{user_id}", **kwargs)
        if res.status_code in (200,):
            return res.json()
        try:
            if res.status_code in (404,) and res.json()["code"] == 3:
                return
        except:
            pass
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def remove_group_user(self,
                          group_id: str,
                          user_id: str,
                          *,
                          error_details: bool = False,
                          **kwargs) -> bool:
        r"""Удалить пользователя из группы

        :param group_id: Идентификатор группы
        :param user_id: Идентификатор пользователя
        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        assert group_id, "group_id is required"
        res = self._client.delete(f"groups/{group_id}/users/{user_id}", **kwargs)
        if res.status_code in (204,):
            return True
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def subjects(self, *, error_details: bool = False, **kwargs) -> typing.List[dict]:
        """
        Получить субъекты

        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        res = self._client.get("subjects", **kwargs)
        if res.status_code in (200,):
            return res.json()["data"]
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def roles(self, *, error_details: bool = False, **kwargs) -> typing.List[dict]:
        """
        Получить список ролей на аккаунт

        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        res = self._client.get("roles", **kwargs)
        if res.status_code in (200,):
            return res.json()
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def create_role(self,
                    name: str,
                    permissions: typing.List[typing.Union[str, AccountPermissions]],
                    *,
                    error_details: bool = False,
                    **kwargs) -> dict:
        """
        Добавить роль на аккаунт

        :param name: Название роли
        :param permissions: Ограничения пользователя на аккаунт
        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        body = {
            "name": name,
            "permissions": list(map(str, permissions))
        }
        res = self._client.post("roles", json=body, **kwargs)
        if res.status_code in (200, 201):
            return res.json()
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def role(self,
             role_id: str,
             *,
             error_details: bool = False,
             **kwargs) -> typing.List[dict]:
        """
        Получить список ролей на аккаунт
        :param role_id: Идентификатор роли
        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        res = self._client.get(f"roles/{role_id}", **kwargs)
        if res.status_code in (200,):
            return res.json()
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def update_role(self,
                    role_id: str,
                    *,
                    name: typing.Optional[str] = None,
                    permissions: typing.Optional[typing.List[typing.Union[str, AccountPermissions]]] = None,
                    error_details: bool = False,
                    **kwargs) -> dict:
        """
        Обновить роль на аккаунт

        :param role_id: Идентификатор роли
        :param name: Название роли
        :param permissions: Ограничения пользователя на аккаунт
        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        assert role_id, "role_id is required"
        assert name or permissions is not None, "name or permissions is required"
        body = {}
        if name:
            body["name"] = name
        if permissions is not None:
            body["permissions"] = list(map(str, permissions))
        res = self._client.patch(f"roles/{role_id}", json=body, **kwargs)
        if res.status_code in (200, 201):
            return res.json()
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def remove_role(self,
             role_id: str,
             *,
             error_details: bool = False,
             **kwargs) -> typing.List[dict]:
        """
        Получить список ролей на аккаунт
        :param role_id: Идентификатор роли
        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        res = self._client.delete(f"roles/{role_id}", **kwargs)
        if res.status_code in (204,):
            return res.json()
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def projects_roles(self, *, error_details: bool = False, **kwargs) -> typing.List[dict]:
        """
        Получить список ролей на проект

        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        res = self._client.get("projects/roles", **kwargs)
        if res.status_code in (200,):
            return res.json()
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def create_projects_role(self,
                    name: str,
                    permissions: typing.List[typing.Union[str, ProjectPermissions]],
                    *,
                    error_details: bool = False,
                    **kwargs) -> dict:
        """
        Добавить роль на проект

        :param name: Название роли
        :param permissions: Ограничения пользователя на проект
        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        body = {
            "name": name,
            "permissions": list(map(str, permissions))
        }
        res = self._client.post("projects/roles", json=body, **kwargs)
        if res.status_code in (200, 201):
            return res.json()
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def projects_role(self,
             role_id: str,
             *,
             error_details: bool = False,
             **kwargs) -> typing.List[dict]:
        """
        Получить список ролей на проект
        :param role_id: Идентификатор роли
        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        res = self._client.get(f"projects/roles/{role_id}", **kwargs)
        if res.status_code in (200,):
            return res.json()
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def update_projects_role(self,
                    role_id: str,
                    *,
                    name: typing.Optional[str] = None,
                    permissions: typing.Optional[typing.List[typing.Union[str, AccountPermissions]]] = None,
                    error_details: bool = False,
                    **kwargs) -> dict:
        """
        Обновить роль на аккаунт

        :param role_id: Идентификатор роли
        :param name: Название роли
        :param permissions: Ограничения пользователя на аккаунт
        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """
        assert role_id, "role_id is required"
        assert name or permissions is not None, "name or permissions is required"

        body = {}
        if name:
            body["name"] = name
        if permissions is not None:
            body["permissions"] = list(map(str, permissions))
        res = self._client.patch(f"projects/roles/{role_id}", json=body, **kwargs)
        if res.status_code in (200, 201):
            return res.json()
        raise RequestError(res.status_code, res.text)

    @use_error_details
    def remove_projects_role(self,
             role_id: str,
             *,
             error_details: bool = False,
             **kwargs) -> typing.List[dict]:
        """
        Получить список ролей на аккаунт
        :param role_id: Идентификатор роли
        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.
        """

        res = self._client.delete(f"projects/roles/{role_id}", **kwargs)
        if res.status_code in (204,):
            return res.json()
        raise RequestError(res.status_code, res.text)