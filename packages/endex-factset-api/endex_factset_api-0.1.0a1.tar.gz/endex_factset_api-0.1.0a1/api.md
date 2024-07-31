# FactSetFundamentals

Types:

```python
from endex_factset_api.types import FundamentalsResponse
```

Methods:

- <code title="post /fundamentals">client.fact_set_fundamentals.<a href="./src/endex_factset_api/resources/fact_set_fundamentals.py">create</a>(\*\*<a href="src/endex_factset_api/types/fact_set_fundamental_create_params.py">params</a>) -> <a href="./src/endex_factset_api/types/fundamentals_response.py">FundamentalsResponse</a></code>
- <code title="get /fundamentals">client.fact_set_fundamentals.<a href="./src/endex_factset_api/resources/fact_set_fundamentals.py">list</a>(\*\*<a href="src/endex_factset_api/types/fact_set_fundamental_list_params.py">params</a>) -> <a href="./src/endex_factset_api/types/fundamentals_response.py">FundamentalsResponse</a></code>

# Segments

Types:

```python
from endex_factset_api.types import SegmentsResponse
```

Methods:

- <code title="post /segments">client.segments.<a href="./src/endex_factset_api/resources/segments.py">create</a>(\*\*<a href="src/endex_factset_api/types/segment_create_params.py">params</a>) -> <a href="./src/endex_factset_api/types/segments_response.py">SegmentsResponse</a></code>
- <code title="get /segments">client.segments.<a href="./src/endex_factset_api/resources/segments.py">list</a>(\*\*<a href="src/endex_factset_api/types/segment_list_params.py">params</a>) -> <a href="./src/endex_factset_api/types/segments_response.py">SegmentsResponse</a></code>

# CompanyReports

## FinancialStatement

Types:

```python
from endex_factset_api.types.company_reports import FinancialResponse
```

Methods:

- <code title="get /company-reports/financial-statement">client.company_reports.financial_statement.<a href="./src/endex_factset_api/resources/company_reports/financial_statement.py">retrieve</a>(\*\*<a href="src/endex_factset_api/types/company_reports/financial_statement_retrieve_params.py">params</a>) -> <a href="./src/endex_factset_api/types/company_reports/financial_response.py">FinancialResponse</a></code>

## Profile

Types:

```python
from endex_factset_api.types.company_reports import ProfileResponse
```

Methods:

- <code title="get /company-reports/profile">client.company_reports.profile.<a href="./src/endex_factset_api/resources/company_reports/profile.py">retrieve</a>(\*\*<a href="src/endex_factset_api/types/company_reports/profile_retrieve_params.py">params</a>) -> <a href="./src/endex_factset_api/types/company_reports/profile_response.py">ProfileResponse</a></code>

## Fundamentals

Types:

```python
from endex_factset_api.types.company_reports import CompanyFundamentalsResponse
```

Methods:

- <code title="get /company-reports/fundamentals">client.company_reports.fundamentals.<a href="./src/endex_factset_api/resources/company_reports/fundamentals.py">retrieve</a>(\*\*<a href="src/endex_factset_api/types/company_reports/fundamental_retrieve_params.py">params</a>) -> <a href="./src/endex_factset_api/types/company_reports/company_fundamentals_response.py">CompanyFundamentalsResponse</a></code>

# Metrics

Types:

```python
from endex_factset_api.types import MetricsResponse
```

Methods:

- <code title="get /metrics">client.metrics.<a href="./src/endex_factset_api/resources/metrics.py">list</a>(\*\*<a href="src/endex_factset_api/types/metric_list_params.py">params</a>) -> <a href="./src/endex_factset_api/types/metrics_response.py">MetricsResponse</a></code>

# BatchProcessing

## BatchStatus

Types:

```python
from endex_factset_api.types.batch_processing import BatchStatusResponse
```

Methods:

- <code title="get /batch-status">client.batch_processing.batch_status.<a href="./src/endex_factset_api/resources/batch_processing/batch_status.py">retrieve</a>(\*\*<a href="src/endex_factset_api/types/batch_processing/batch_status_retrieve_params.py">params</a>) -> <a href="./src/endex_factset_api/types/batch_processing/batch_status_response.py">BatchStatusResponse</a></code>

## BatchResult

Types:

```python
from endex_factset_api.types.batch_processing import BatchResultResponse
```

Methods:

- <code title="get /batch-result">client.batch_processing.batch_result.<a href="./src/endex_factset_api/resources/batch_processing/batch_result.py">retrieve</a>(\*\*<a href="src/endex_factset_api/types/batch_processing/batch_result_retrieve_params.py">params</a>) -> <a href="./src/endex_factset_api/types/batch_processing/batch_result_response.py">BatchResultResponse</a></code>
