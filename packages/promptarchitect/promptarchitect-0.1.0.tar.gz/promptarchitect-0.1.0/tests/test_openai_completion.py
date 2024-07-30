from unittest.mock import MagicMock, patch

import pytest
from openai import OpenAIError
from promptarchitect.openai_completion import (
    DEFAULT_MODEL,
    OPENAI_PRICING,
    OpenAICompletion,
)


# Helper function to create a mock response
def create_mock_response(prompt_tokens, completion_tokens, message_content):
    return {
        "usage": MagicMock(
            prompt_tokens=prompt_tokens, completion_tokens=completion_tokens
        ),
        "choices": [MagicMock(message=MagicMock(content=message_content))],
    }


@pytest.fixture
def openai_completion():
    return OpenAICompletion(
        system_role="test_role", model=DEFAULT_MODEL, parameters={"temperature": 0.7}
    )


def test_init(openai_completion):
    assert openai_completion.system_role == "test_role"
    assert openai_completion.model == DEFAULT_MODEL
    assert openai_completion.parameters == {"temperature": 0.7}
    assert openai_completion.cost == 0.0
    assert openai_completion.is_json is False
    assert openai_completion.test_path == ""
    assert openai_completion.response_message == ""
    assert openai_completion.latency == 0.0


@patch("promptcraft.openai_completion.OpenAICompletion.client")
def test_calculate_cost(mock_client, openai_completion):
    mock_response = create_mock_response(
        prompt_tokens=100, completion_tokens=200, message_content="Test response"
    )
    cost = openai_completion._calculate_cost(mock_response)

    expected_cost = (
        100 * OPENAI_PRICING[DEFAULT_MODEL]["input_tokens"]
        + 200 * OPENAI_PRICING[DEFAULT_MODEL]["output_tokens"]
    )

    assert cost == expected_cost


@patch("promptcraft.openai_completion.OpenAICompletion.client.chat.completions.create")
def test_completion_success(mock_create, openai_completion):
    mock_create.return_value = create_mock_response(
        prompt_tokens=100, completion_tokens=200, message_content="Test response"
    )

    prompt = "Test prompt"
    response = openai_completion.completion(prompt)

    assert response == "Test response"
    assert openai_completion.cost > 0
    assert openai_completion.latency > 0


@patch("promptcraft.openai_completion.OpenAICompletion.client.chat.completions.create")
def test_completion_bad_request(mock_create, openai_completion):
    mock_create.side_effect = OpenAIError("Bad Request Error")

    with pytest.raises(ValueError, match="Bad Request Error"):
        openai_completion.completion("Test prompt")


def test_to_dict(openai_completion):
    data = openai_completion.to_dict()

    assert data == {
        "system_role": "test_role",
        "model": DEFAULT_MODEL,
        "parameters": {"temperature": 0.7},
        "cost": 0.0,
        "is_json": False,
        "test_path": "",
        "response_message": "",
        "latency": 0.0,
    }


def test_from_dict():
    EXPECTED_COST = 5.0
    EXPECTED_LATENCY = 1.2

    data = {
        "system_role": "test_role",
        "model": DEFAULT_MODEL,
        "parameters": {"temperature": 0.7},
        "cost": EXPECTED_COST,
        "is_json": True,
        "test_path": "/test/path",
        "response_message": "Test message",
        "latency": EXPECTED_LATENCY,
    }

    openai_completion = OpenAICompletion.from_dict(data)

    assert openai_completion.system_role == "test_role"
    assert openai_completion.model == DEFAULT_MODEL
    assert openai_completion.parameters == {"temperature": 0.7}
    assert openai_completion.cost == EXPECTED_COST
    assert openai_completion.is_json is True
    assert openai_completion.test_path == "/test/path"
    assert openai_completion.response_message == "Test message"
    assert openai_completion.latency == EXPECTED_LATENCY
