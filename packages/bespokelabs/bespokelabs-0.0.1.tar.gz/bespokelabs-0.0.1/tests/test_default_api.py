# coding: utf-8

from fastapi.testclient import TestClient


from bespokelabs-python-client.models.fact_check_request import FactCheckRequest  # noqa: F401
from bespokelabs-python-client.models.fact_check_response import FactCheckResponse  # noqa: F401
from bespokelabs-python-client.models.http_validation_error import HTTPValidationError  # noqa: F401
from bespokelabs-python-client.models.llm import LLM  # noqa: F401
from bespokelabs-python-client.models.synthetic_data_download_response import SyntheticDataDownloadResponse  # noqa: F401
from bespokelabs-python-client.models.synthetic_data_generate_response import SyntheticDataGenerateResponse  # noqa: F401


def test_factcheck_v0_argus_factcheck_post(client: TestClient):
    """Test case for factcheck_v0_argus_factcheck_post

    Factcheck
    """
    fact_check_request = {"claim":"claim","contexts":["contexts","contexts"]}

    headers = {
        "APIKeyHeader": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v0/argus/factcheck",
    #    headers=headers,
    #    json=fact_check_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_synthetic_data_download_v0_synthetic_data_download_session_id_post(client: TestClient):
    """Test case for synthetic_data_download_v0_synthetic_data_download_session_id_post

    Synthetic Data Download
    """

    headers = {
        "APIKeyHeader": "special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v0/synthetic_data/download/{session_id}".format(session_id='session_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_synthetic_data_generate_v0_synthetic_data_generate_post(client: TestClient):
    """Test case for synthetic_data_generate_v0_synthetic_data_generate_post

    Synthetic Data Generate
    """

    headers = {
        "APIKeyHeader": "special-key",
    }
    data = {
        "seed_qa_file": '/path/to/file',
        "context_files": ['/path/to/file'],
        "domain": 'domain_example',
        "num_rounds": 10,
        "llm": bespokelabs-python-client.LLM(),
        "rater_llm": bespokelabs-python-client.LLM(),
        "rating_threshold": 3.0
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v0/synthetic_data/generate",
    #    headers=headers,
    #    data=data,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

