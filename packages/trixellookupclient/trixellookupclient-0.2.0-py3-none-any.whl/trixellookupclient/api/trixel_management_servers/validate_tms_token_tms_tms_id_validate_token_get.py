from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import Dict
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    tms_id: int,
    *,
    token: str,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/TMS/{tms_id}/validate_token".format(tms_id=tms_id,),
    }


    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = response.json()
        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tms_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,

) -> Response[Union[Any, HTTPValidationError]]:
    """ Check if a TMS authentication token is valid.

     Endpoint which allows to check if a TMS authentication token is valid.

    Args:
        tms_id (int): ID of the TMS.
        token (str): TMS authentication token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
     """


    kwargs = _get_kwargs(
        tms_id=tms_id,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    tms_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,

) -> Optional[Union[Any, HTTPValidationError]]:
    """ Check if a TMS authentication token is valid.

     Endpoint which allows to check if a TMS authentication token is valid.

    Args:
        tms_id (int): ID of the TMS.
        token (str): TMS authentication token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
     """


    return sync_detailed(
        tms_id=tms_id,
client=client,
token=token,

    ).parsed

async def asyncio_detailed(
    tms_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,

) -> Response[Union[Any, HTTPValidationError]]:
    """ Check if a TMS authentication token is valid.

     Endpoint which allows to check if a TMS authentication token is valid.

    Args:
        tms_id (int): ID of the TMS.
        token (str): TMS authentication token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
     """


    kwargs = _get_kwargs(
        tms_id=tms_id,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    tms_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,

) -> Optional[Union[Any, HTTPValidationError]]:
    """ Check if a TMS authentication token is valid.

     Endpoint which allows to check if a TMS authentication token is valid.

    Args:
        tms_id (int): ID of the TMS.
        token (str): TMS authentication token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
     """


    return (await asyncio_detailed(
        tms_id=tms_id,
client=client,
token=token,

    )).parsed
