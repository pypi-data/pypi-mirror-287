import typing

from .types import ConnectorBase
from ._connector import Connector
from .exceptions import *
from ._profile import _Profile
from ._storage import _Storage
from ._project import _Project
from ._users import _Users
from ._auth import TouchpointClientAuth
from._decorators import use_error_details

DEFAULT_TIMEOUT = 300

__all__ = ["TouchPointClient"]


class TouchPointClient:
    """
    https://api.v15.touchpoint-analytics.ru/swagger/
    """
    _connector: ConnectorBase

    def __init__(self,
                 api_url: str,
                 *,
                 connector: ConnectorBase = None,
                 auth: typing.Optional[TouchpointClientAuth] = None,
                 client_id: typing.Optional[str] = None,
                 auth_url: typing.Optional[str] = None,
                 username: typing.Optional[str] = None,
                 password: typing.Optional[str] = None,
                 client_secret: typing.Optional[str] = None,
                 timeout: int = DEFAULT_TIMEOUT):
        """
        Инициализация клиента

        :param api_url: Базовый URL для выполнения запросов
        :param connector: Объект для выполнения HTTP запросов. Если не передан используются следующие параметры для его создания.
        :param auth: Объект для выполнения авторизация. Используется если не передан connector. Если не передан, используются следующие параметры для его создания.
        :param client_id: Идентификатор приложения.
        :param client_secret: Секретный ключ приложения.
        :param auth_url: URL для аутентификации по протоколу OAuth 2
        :param username: Имя пользователя, для аутентификации
        :param password: Пароль
        :param timeout:
        """
        if connector is None:
            if auth:
                self._auth = auth
            elif username and password and client_id and auth_url:
                self._auth = TouchpointClientAuth(client_id, auth_url, username=username, password=password, client_secret=client_secret, timeout=timeout)
            else:
                raise AuthError(404, "Some authentication params missing")
            connector = Connector(api_url, auth=self._auth, timeout=timeout)
        self._connector = connector
        self._storage = _Storage(self._connector)
        self._profile = _Profile(self._connector)
        self._users = _Users(self._connector)

    @property
    def profile(self) -> _Profile:
        """
        Возвращает объект для выполнения API запросов к личной информации пользователя

        :return: Объект :class:`_Profile <_Profile>`
        :rtype: TouchPointClient._Profile
        """
        return self._profile

    @property
    def storage(self) -> _Storage:
        """
        Возвращает объект для выполнения API запросов к файловому хранилищу TouchPoint

        :return: Объект :class:`TouchPointClient._Storage`
        :rtype: TouchPointClient._Storage
        """
        return self._storage

    @property
    def users(self) -> _Users:
        """
        Возвращает объект для выполнения API запросов управления пользователями TouchPoint

        :return: Объект :class:`TouchPointClient._Users`
        :rtype: TouchPointClient._Users
        """
        return self._users

    def project(self, project_id: str) -> _Project:
        """
        Возвращает объект для выполнения API запросов к указанному проекту TouchPoint

        :param project_id: Идентификатор проекта

        :return: Объект :class:`TouchPointClient._Project`
        :rtype: TouchPointClient._Project
        """
        return _Project(self._connector, project_id)

    @use_error_details
    def projects(self, *,
                 error_details: bool = False,
                 **kwargs) -> typing.List[dict]:
        r"""
        Получить список проектов, в которых участвует пользователь

        :param error_details: Выводить подробную информацию об ошибке.
        :param kwargs: Дополнительные параметры, которые принимает ``requests.get``.
        :raises touchpoint_client.exceptions.RequestError: Если REST возвращает код ответа отличный от 200.

        :return: Список проектов
        :rtype: typing.List[dict]
        """
        res = self._connector.get(f"projects", **kwargs)
        if res.status_code in (200,):
            return res.json()
        raise RequestError(res.status_code, res.text)
