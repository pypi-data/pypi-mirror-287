# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .batch_result import (
    BatchResultResource,
    AsyncBatchResultResource,
    BatchResultResourceWithRawResponse,
    AsyncBatchResultResourceWithRawResponse,
    BatchResultResourceWithStreamingResponse,
    AsyncBatchResultResourceWithStreamingResponse,
)
from .batch_status import (
    BatchStatusResource,
    AsyncBatchStatusResource,
    BatchStatusResourceWithRawResponse,
    AsyncBatchStatusResourceWithRawResponse,
    BatchStatusResourceWithStreamingResponse,
    AsyncBatchStatusResourceWithStreamingResponse,
)

__all__ = ["BatchProcessingResource", "AsyncBatchProcessingResource"]


class BatchProcessingResource(SyncAPIResource):
    @cached_property
    def batch_status(self) -> BatchStatusResource:
        return BatchStatusResource(self._client)

    @cached_property
    def batch_result(self) -> BatchResultResource:
        return BatchResultResource(self._client)

    @cached_property
    def with_raw_response(self) -> BatchProcessingResourceWithRawResponse:
        return BatchProcessingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchProcessingResourceWithStreamingResponse:
        return BatchProcessingResourceWithStreamingResponse(self)


class AsyncBatchProcessingResource(AsyncAPIResource):
    @cached_property
    def batch_status(self) -> AsyncBatchStatusResource:
        return AsyncBatchStatusResource(self._client)

    @cached_property
    def batch_result(self) -> AsyncBatchResultResource:
        return AsyncBatchResultResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBatchProcessingResourceWithRawResponse:
        return AsyncBatchProcessingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchProcessingResourceWithStreamingResponse:
        return AsyncBatchProcessingResourceWithStreamingResponse(self)


class BatchProcessingResourceWithRawResponse:
    def __init__(self, batch_processing: BatchProcessingResource) -> None:
        self._batch_processing = batch_processing

    @cached_property
    def batch_status(self) -> BatchStatusResourceWithRawResponse:
        return BatchStatusResourceWithRawResponse(self._batch_processing.batch_status)

    @cached_property
    def batch_result(self) -> BatchResultResourceWithRawResponse:
        return BatchResultResourceWithRawResponse(self._batch_processing.batch_result)


class AsyncBatchProcessingResourceWithRawResponse:
    def __init__(self, batch_processing: AsyncBatchProcessingResource) -> None:
        self._batch_processing = batch_processing

    @cached_property
    def batch_status(self) -> AsyncBatchStatusResourceWithRawResponse:
        return AsyncBatchStatusResourceWithRawResponse(self._batch_processing.batch_status)

    @cached_property
    def batch_result(self) -> AsyncBatchResultResourceWithRawResponse:
        return AsyncBatchResultResourceWithRawResponse(self._batch_processing.batch_result)


class BatchProcessingResourceWithStreamingResponse:
    def __init__(self, batch_processing: BatchProcessingResource) -> None:
        self._batch_processing = batch_processing

    @cached_property
    def batch_status(self) -> BatchStatusResourceWithStreamingResponse:
        return BatchStatusResourceWithStreamingResponse(self._batch_processing.batch_status)

    @cached_property
    def batch_result(self) -> BatchResultResourceWithStreamingResponse:
        return BatchResultResourceWithStreamingResponse(self._batch_processing.batch_result)


class AsyncBatchProcessingResourceWithStreamingResponse:
    def __init__(self, batch_processing: AsyncBatchProcessingResource) -> None:
        self._batch_processing = batch_processing

    @cached_property
    def batch_status(self) -> AsyncBatchStatusResourceWithStreamingResponse:
        return AsyncBatchStatusResourceWithStreamingResponse(self._batch_processing.batch_status)

    @cached_property
    def batch_result(self) -> AsyncBatchResultResourceWithStreamingResponse:
        return AsyncBatchResultResourceWithStreamingResponse(self._batch_processing.batch_result)
