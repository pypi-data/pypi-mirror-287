from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import Union
from typing import cast, List
from typing import Dict
from ...models.measurement_type_enum import MeasurementTypeEnum
from typing import cast
from ...types import UNSET, Unset
from ...models.http_validation_error import HTTPValidationError



def _get_kwargs(
    *,
    types: Union[Unset, List[MeasurementTypeEnum]] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,

) -> Dict[str, Any]:
    

    

    params: Dict[str, Any] = {}

    json_types: Union[Unset, List[str]] = UNSET
    if not isinstance(types, Unset):
        json_types = []
        for types_item_data in types:
            types_item = types_item_data.value
            json_types.append(types_item)


    params["types"] = json_types

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/trixel",
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, List[int]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(List[int], response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, List[int]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    types: Union[Unset, List[MeasurementTypeEnum]] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,

) -> Response[Union[HTTPValidationError, List[int]]]:
    """ Retrieve an overview of all trixels, which contain at least one sensors of the specified types.

     Get a list of trixel ids with at least one sensor (filtered by measurement type).

    Args:
        types (Union[Unset, List[MeasurementTypeEnum]]): List of measurement types which restrict
            results. If none are provided, all types are used.
        limit (Union[Unset, int]): Limits the number of results. Default: 100.
        offset (Union[Unset, int]): Skip the first n results. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List[int]]]
     """


    kwargs = _get_kwargs(
        types=types,
limit=limit,
offset=offset,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    types: Union[Unset, List[MeasurementTypeEnum]] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,

) -> Optional[Union[HTTPValidationError, List[int]]]:
    """ Retrieve an overview of all trixels, which contain at least one sensors of the specified types.

     Get a list of trixel ids with at least one sensor (filtered by measurement type).

    Args:
        types (Union[Unset, List[MeasurementTypeEnum]]): List of measurement types which restrict
            results. If none are provided, all types are used.
        limit (Union[Unset, int]): Limits the number of results. Default: 100.
        offset (Union[Unset, int]): Skip the first n results. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List[int]]
     """


    return sync_detailed(
        client=client,
types=types,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    types: Union[Unset, List[MeasurementTypeEnum]] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,

) -> Response[Union[HTTPValidationError, List[int]]]:
    """ Retrieve an overview of all trixels, which contain at least one sensors of the specified types.

     Get a list of trixel ids with at least one sensor (filtered by measurement type).

    Args:
        types (Union[Unset, List[MeasurementTypeEnum]]): List of measurement types which restrict
            results. If none are provided, all types are used.
        limit (Union[Unset, int]): Limits the number of results. Default: 100.
        offset (Union[Unset, int]): Skip the first n results. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List[int]]]
     """


    kwargs = _get_kwargs(
        types=types,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    types: Union[Unset, List[MeasurementTypeEnum]] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,

) -> Optional[Union[HTTPValidationError, List[int]]]:
    """ Retrieve an overview of all trixels, which contain at least one sensors of the specified types.

     Get a list of trixel ids with at least one sensor (filtered by measurement type).

    Args:
        types (Union[Unset, List[MeasurementTypeEnum]]): List of measurement types which restrict
            results. If none are provided, all types are used.
        limit (Union[Unset, int]): Limits the number of results. Default: 100.
        offset (Union[Unset, int]): Skip the first n results. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List[int]]
     """


    return (await asyncio_detailed(
        client=client,
types=types,
limit=limit,
offset=offset,

    )).parsed
