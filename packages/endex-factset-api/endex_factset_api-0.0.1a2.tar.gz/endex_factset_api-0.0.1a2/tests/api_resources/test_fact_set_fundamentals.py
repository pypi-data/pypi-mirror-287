# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from endex_factset_api import EndexFactsetAPI, AsyncEndexFactsetAPI
from endex_factset_api.types import (
    FundamentalsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFactSetFundamentals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: EndexFactsetAPI) -> None:
        fact_set_fundamental = client.fact_set_fundamentals.create(
            data={
                "ids": ["FDS-US"],
                "metrics": ["FF_SALES"],
            },
        )
        assert_matches_type(FundamentalsResponse, fact_set_fundamental, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: EndexFactsetAPI) -> None:
        fact_set_fundamental = client.fact_set_fundamentals.create(
            data={
                "ids": ["FDS-US"],
                "periodicity": "QTR",
                "fiscal_period": {
                    "start": "2017-09-01",
                    "end": "2018-03-01",
                },
                "metrics": ["FF_SALES"],
                "currency": "USD",
                "update_type": "RP",
                "batch": "Y",
            },
        )
        assert_matches_type(FundamentalsResponse, fact_set_fundamental, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: EndexFactsetAPI) -> None:
        response = client.fact_set_fundamentals.with_raw_response.create(
            data={
                "ids": ["FDS-US"],
                "metrics": ["FF_SALES"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fact_set_fundamental = response.parse()
        assert_matches_type(FundamentalsResponse, fact_set_fundamental, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: EndexFactsetAPI) -> None:
        with client.fact_set_fundamentals.with_streaming_response.create(
            data={
                "ids": ["FDS-US"],
                "metrics": ["FF_SALES"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fact_set_fundamental = response.parse()
            assert_matches_type(FundamentalsResponse, fact_set_fundamental, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: EndexFactsetAPI) -> None:
        fact_set_fundamental = client.fact_set_fundamentals.list(
            ids=["string", "string", "string"],
            metrics=["FF_SALES", "FF_EPS", "FF_PE"],
        )
        assert_matches_type(FundamentalsResponse, fact_set_fundamental, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: EndexFactsetAPI) -> None:
        fact_set_fundamental = client.fact_set_fundamentals.list(
            ids=["string", "string", "string"],
            metrics=["FF_SALES", "FF_EPS", "FF_PE"],
            batch="Y",
            currency="USD",
            fiscal_period_end="2018-03-01",
            fiscal_period_start="2017-09-01",
            periodicity="ANN",
            update_type="RP",
        )
        assert_matches_type(FundamentalsResponse, fact_set_fundamental, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: EndexFactsetAPI) -> None:
        response = client.fact_set_fundamentals.with_raw_response.list(
            ids=["string", "string", "string"],
            metrics=["FF_SALES", "FF_EPS", "FF_PE"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fact_set_fundamental = response.parse()
        assert_matches_type(FundamentalsResponse, fact_set_fundamental, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: EndexFactsetAPI) -> None:
        with client.fact_set_fundamentals.with_streaming_response.list(
            ids=["string", "string", "string"],
            metrics=["FF_SALES", "FF_EPS", "FF_PE"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fact_set_fundamental = response.parse()
            assert_matches_type(FundamentalsResponse, fact_set_fundamental, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFactSetFundamentals:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncEndexFactsetAPI) -> None:
        fact_set_fundamental = await async_client.fact_set_fundamentals.create(
            data={
                "ids": ["FDS-US"],
                "metrics": ["FF_SALES"],
            },
        )
        assert_matches_type(FundamentalsResponse, fact_set_fundamental, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEndexFactsetAPI) -> None:
        fact_set_fundamental = await async_client.fact_set_fundamentals.create(
            data={
                "ids": ["FDS-US"],
                "periodicity": "QTR",
                "fiscal_period": {
                    "start": "2017-09-01",
                    "end": "2018-03-01",
                },
                "metrics": ["FF_SALES"],
                "currency": "USD",
                "update_type": "RP",
                "batch": "Y",
            },
        )
        assert_matches_type(FundamentalsResponse, fact_set_fundamental, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEndexFactsetAPI) -> None:
        response = await async_client.fact_set_fundamentals.with_raw_response.create(
            data={
                "ids": ["FDS-US"],
                "metrics": ["FF_SALES"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fact_set_fundamental = await response.parse()
        assert_matches_type(FundamentalsResponse, fact_set_fundamental, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEndexFactsetAPI) -> None:
        async with async_client.fact_set_fundamentals.with_streaming_response.create(
            data={
                "ids": ["FDS-US"],
                "metrics": ["FF_SALES"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fact_set_fundamental = await response.parse()
            assert_matches_type(FundamentalsResponse, fact_set_fundamental, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncEndexFactsetAPI) -> None:
        fact_set_fundamental = await async_client.fact_set_fundamentals.list(
            ids=["string", "string", "string"],
            metrics=["FF_SALES", "FF_EPS", "FF_PE"],
        )
        assert_matches_type(FundamentalsResponse, fact_set_fundamental, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncEndexFactsetAPI) -> None:
        fact_set_fundamental = await async_client.fact_set_fundamentals.list(
            ids=["string", "string", "string"],
            metrics=["FF_SALES", "FF_EPS", "FF_PE"],
            batch="Y",
            currency="USD",
            fiscal_period_end="2018-03-01",
            fiscal_period_start="2017-09-01",
            periodicity="ANN",
            update_type="RP",
        )
        assert_matches_type(FundamentalsResponse, fact_set_fundamental, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEndexFactsetAPI) -> None:
        response = await async_client.fact_set_fundamentals.with_raw_response.list(
            ids=["string", "string", "string"],
            metrics=["FF_SALES", "FF_EPS", "FF_PE"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fact_set_fundamental = await response.parse()
        assert_matches_type(FundamentalsResponse, fact_set_fundamental, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEndexFactsetAPI) -> None:
        async with async_client.fact_set_fundamentals.with_streaming_response.list(
            ids=["string", "string", "string"],
            metrics=["FF_SALES", "FF_EPS", "FF_PE"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fact_set_fundamental = await response.parse()
            assert_matches_type(FundamentalsResponse, fact_set_fundamental, path=["response"])

        assert cast(Any, response.is_closed) is True
