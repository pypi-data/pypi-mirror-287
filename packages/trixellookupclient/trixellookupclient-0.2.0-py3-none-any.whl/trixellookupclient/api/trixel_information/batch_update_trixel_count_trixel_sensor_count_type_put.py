from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import Dict
from ...models.measurement_type_enum import MeasurementTypeEnum
from typing import cast
from ...models.batch_update_trixel_count_trixel_sensor_count_type_put_updates import BatchUpdateTrixelCountTrixelSensorCountTypePutUpdates
from ...models.http_validation_error import HTTPValidationError



def _get_kwargs(
    type: MeasurementTypeEnum,
    *,
    body: BatchUpdateTrixelCountTrixelSensorCountTypePutUpdates,
    token: str,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/trixel/sensor_count/{type}".format(type=type,),
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = response.json()
        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
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
    type: MeasurementTypeEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BatchUpdateTrixelCountTrixelSensorCountTypePutUpdates,
    token: str,

) -> Response[Union[Any, HTTPValidationError]]:
    """ Update the sensor count for multiple trixels for a given type.

     Update (or insert new) multiple trixel sensor counts within the DB.

    Args:
        type (MeasurementTypeEnum): Supported measurement types.
        token (str): TMS authentication token.
        body (BatchUpdateTrixelCountTrixelSensorCountTypePutUpdates): A map which contains the new
            sensors count for multiple trixels.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
     """


    kwargs = _get_kwargs(
        type=type,
body=body,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    type: MeasurementTypeEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BatchUpdateTrixelCountTrixelSensorCountTypePutUpdates,
    token: str,

) -> Optional[Union[Any, HTTPValidationError]]:
    """ Update the sensor count for multiple trixels for a given type.

     Update (or insert new) multiple trixel sensor counts within the DB.

    Args:
        type (MeasurementTypeEnum): Supported measurement types.
        token (str): TMS authentication token.
        body (BatchUpdateTrixelCountTrixelSensorCountTypePutUpdates): A map which contains the new
            sensors count for multiple trixels.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
     """


    return sync_detailed(
        type=type,
client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    type: MeasurementTypeEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BatchUpdateTrixelCountTrixelSensorCountTypePutUpdates,
    token: str,

) -> Response[Union[Any, HTTPValidationError]]:
    """ Update the sensor count for multiple trixels for a given type.

     Update (or insert new) multiple trixel sensor counts within the DB.

    Args:
        type (MeasurementTypeEnum): Supported measurement types.
        token (str): TMS authentication token.
        body (BatchUpdateTrixelCountTrixelSensorCountTypePutUpdates): A map which contains the new
            sensors count for multiple trixels.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
     """


    kwargs = _get_kwargs(
        type=type,
body=body,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    type: MeasurementTypeEnum,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BatchUpdateTrixelCountTrixelSensorCountTypePutUpdates,
    token: str,

) -> Optional[Union[Any, HTTPValidationError]]:
    """ Update the sensor count for multiple trixels for a given type.

     Update (or insert new) multiple trixel sensor counts within the DB.

    Args:
        type (MeasurementTypeEnum): Supported measurement types.
        token (str): TMS authentication token.
        body (BatchUpdateTrixelCountTrixelSensorCountTypePutUpdates): A map which contains the new
            sensors count for multiple trixels.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
     """


    return (await asyncio_detailed(
        type=type,
client=client,
body=body,
token=token,

    )).parsed
