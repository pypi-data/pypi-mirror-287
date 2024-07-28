from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.trixel_management_server import TrixelManagementServer
from ...models.http_validation_error import HTTPValidationError
from typing import Dict
from typing import cast



def _get_kwargs(
    trixel_id: int,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/trixel/{trixel_id}/TMS".format(trixel_id=trixel_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, HTTPValidationError, TrixelManagementServer]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TrixelManagementServer.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, HTTPValidationError, TrixelManagementServer]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trixel_id: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, HTTPValidationError, TrixelManagementServer]]:
    """ Get the TMS responsible for a specific trixel.

     Get the TMS responsible for a Trixel.

    Args:
        trixel_id (int): The Trixel id for which the TMS is determined.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, TrixelManagementServer]]
     """


    kwargs = _get_kwargs(
        trixel_id=trixel_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trixel_id: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, HTTPValidationError, TrixelManagementServer]]:
    """ Get the TMS responsible for a specific trixel.

     Get the TMS responsible for a Trixel.

    Args:
        trixel_id (int): The Trixel id for which the TMS is determined.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, TrixelManagementServer]
     """


    return sync_detailed(
        trixel_id=trixel_id,
client=client,

    ).parsed

async def asyncio_detailed(
    trixel_id: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, HTTPValidationError, TrixelManagementServer]]:
    """ Get the TMS responsible for a specific trixel.

     Get the TMS responsible for a Trixel.

    Args:
        trixel_id (int): The Trixel id for which the TMS is determined.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, TrixelManagementServer]]
     """


    kwargs = _get_kwargs(
        trixel_id=trixel_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trixel_id: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, HTTPValidationError, TrixelManagementServer]]:
    """ Get the TMS responsible for a specific trixel.

     Get the TMS responsible for a Trixel.

    Args:
        trixel_id (int): The Trixel id for which the TMS is determined.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, TrixelManagementServer]
     """


    return (await asyncio_detailed(
        trixel_id=trixel_id,
client=client,

    )).parsed
