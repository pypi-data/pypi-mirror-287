# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, EndexFactsetAPIError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "EndexFactsetAPI",
    "AsyncEndexFactsetAPI",
    "Client",
    "AsyncClient",
]


class EndexFactsetAPI(SyncAPIClient):
    fact_set_fundamentals: resources.FactSetFundamentalsResource
    segments: resources.SegmentsResource
    company_reports: resources.CompanyReportsResource
    metrics: resources.MetricsResource
    batch_processing: resources.BatchProcessingResource
    with_raw_response: EndexFactsetAPIWithRawResponse
    with_streaming_response: EndexFactsetAPIWithStreamedResponse

    # client options
    access_token: str

    def __init__(
        self,
        *,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous endex-factset-api client instance.

        This automatically infers the `access_token` argument from the `ENDEX_FACTSET_ACCESS_TOKEN` environment variable if it is not provided.
        """
        if access_token is None:
            access_token = os.environ.get("ENDEX_FACTSET_ACCESS_TOKEN")
        if access_token is None:
            raise EndexFactsetAPIError(
                "The access_token client option must be set either by passing access_token to the client or by setting the ENDEX_FACTSET_ACCESS_TOKEN environment variable"
            )
        self.access_token = access_token

        if base_url is None:
            base_url = os.environ.get("ENDEX_FACTSET_API_BASE_URL")
        if base_url is None:
            base_url = f"https://api.factset.com/content/factset-fundamentals/v2"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.fact_set_fundamentals = resources.FactSetFundamentalsResource(self)
        self.segments = resources.SegmentsResource(self)
        self.company_reports = resources.CompanyReportsResource(self)
        self.metrics = resources.MetricsResource(self)
        self.batch_processing = resources.BatchProcessingResource(self)
        self.with_raw_response = EndexFactsetAPIWithRawResponse(self)
        self.with_streaming_response = EndexFactsetAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        access_token = self.access_token
        return {"Authorization": f"Bearer {access_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            access_token=access_token or self.access_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncEndexFactsetAPI(AsyncAPIClient):
    fact_set_fundamentals: resources.AsyncFactSetFundamentalsResource
    segments: resources.AsyncSegmentsResource
    company_reports: resources.AsyncCompanyReportsResource
    metrics: resources.AsyncMetricsResource
    batch_processing: resources.AsyncBatchProcessingResource
    with_raw_response: AsyncEndexFactsetAPIWithRawResponse
    with_streaming_response: AsyncEndexFactsetAPIWithStreamedResponse

    # client options
    access_token: str

    def __init__(
        self,
        *,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async endex-factset-api client instance.

        This automatically infers the `access_token` argument from the `ENDEX_FACTSET_ACCESS_TOKEN` environment variable if it is not provided.
        """
        if access_token is None:
            access_token = os.environ.get("ENDEX_FACTSET_ACCESS_TOKEN")
        if access_token is None:
            raise EndexFactsetAPIError(
                "The access_token client option must be set either by passing access_token to the client or by setting the ENDEX_FACTSET_ACCESS_TOKEN environment variable"
            )
        self.access_token = access_token

        if base_url is None:
            base_url = os.environ.get("ENDEX_FACTSET_API_BASE_URL")
        if base_url is None:
            base_url = f"https://api.factset.com/content/factset-fundamentals/v2"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.fact_set_fundamentals = resources.AsyncFactSetFundamentalsResource(self)
        self.segments = resources.AsyncSegmentsResource(self)
        self.company_reports = resources.AsyncCompanyReportsResource(self)
        self.metrics = resources.AsyncMetricsResource(self)
        self.batch_processing = resources.AsyncBatchProcessingResource(self)
        self.with_raw_response = AsyncEndexFactsetAPIWithRawResponse(self)
        self.with_streaming_response = AsyncEndexFactsetAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        access_token = self.access_token
        return {"Authorization": f"Bearer {access_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            access_token=access_token or self.access_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class EndexFactsetAPIWithRawResponse:
    def __init__(self, client: EndexFactsetAPI) -> None:
        self.fact_set_fundamentals = resources.FactSetFundamentalsResourceWithRawResponse(client.fact_set_fundamentals)
        self.segments = resources.SegmentsResourceWithRawResponse(client.segments)
        self.company_reports = resources.CompanyReportsResourceWithRawResponse(client.company_reports)
        self.metrics = resources.MetricsResourceWithRawResponse(client.metrics)
        self.batch_processing = resources.BatchProcessingResourceWithRawResponse(client.batch_processing)


class AsyncEndexFactsetAPIWithRawResponse:
    def __init__(self, client: AsyncEndexFactsetAPI) -> None:
        self.fact_set_fundamentals = resources.AsyncFactSetFundamentalsResourceWithRawResponse(
            client.fact_set_fundamentals
        )
        self.segments = resources.AsyncSegmentsResourceWithRawResponse(client.segments)
        self.company_reports = resources.AsyncCompanyReportsResourceWithRawResponse(client.company_reports)
        self.metrics = resources.AsyncMetricsResourceWithRawResponse(client.metrics)
        self.batch_processing = resources.AsyncBatchProcessingResourceWithRawResponse(client.batch_processing)


class EndexFactsetAPIWithStreamedResponse:
    def __init__(self, client: EndexFactsetAPI) -> None:
        self.fact_set_fundamentals = resources.FactSetFundamentalsResourceWithStreamingResponse(
            client.fact_set_fundamentals
        )
        self.segments = resources.SegmentsResourceWithStreamingResponse(client.segments)
        self.company_reports = resources.CompanyReportsResourceWithStreamingResponse(client.company_reports)
        self.metrics = resources.MetricsResourceWithStreamingResponse(client.metrics)
        self.batch_processing = resources.BatchProcessingResourceWithStreamingResponse(client.batch_processing)


class AsyncEndexFactsetAPIWithStreamedResponse:
    def __init__(self, client: AsyncEndexFactsetAPI) -> None:
        self.fact_set_fundamentals = resources.AsyncFactSetFundamentalsResourceWithStreamingResponse(
            client.fact_set_fundamentals
        )
        self.segments = resources.AsyncSegmentsResourceWithStreamingResponse(client.segments)
        self.company_reports = resources.AsyncCompanyReportsResourceWithStreamingResponse(client.company_reports)
        self.metrics = resources.AsyncMetricsResourceWithStreamingResponse(client.metrics)
        self.batch_processing = resources.AsyncBatchProcessingResourceWithStreamingResponse(client.batch_processing)


Client = EndexFactsetAPI

AsyncClient = AsyncEndexFactsetAPI
