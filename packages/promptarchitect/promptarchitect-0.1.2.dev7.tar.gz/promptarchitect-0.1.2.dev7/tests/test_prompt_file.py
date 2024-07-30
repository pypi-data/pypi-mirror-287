import pytest
from promptarchitect.prompt_file import DuplicateKeyError, PromptFile

# Sample prompt data to use in tests
valid_prompt_content = """
<!-- key: value -->
<!-- input: input.txt -->
<!-- output: output.txt -->
<!-- TEST-CASES -->
<!-- test 01: Test description 1 -->
<!-- test 02: Test description 2 -->

This is a test prompt.
"""

duplicate_key_prompt_content = """
<!-- key: value1 -->
<!-- key: value2 -->
This is a test prompt with duplicate keys.
"""


# Define fixtures to use in your tests
@pytest.fixture
def valid_prompt_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "prompt.txt"
    p.write_text(valid_prompt_content)
    return p


@pytest.fixture
def duplicate_key_prompt_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "duplicate_prompt.txt"
    p.write_text(duplicate_key_prompt_content)
    return p


# Test cases for the PromptFile class
def test_prompt_file_initialization(valid_prompt_file):
    prompt_file = PromptFile(filename=str(valid_prompt_file))
    assert prompt_file.prompt == "This is a test prompt."
    assert prompt_file.metadata == {
        "key": "value",
        "input": "input",
        "output": "output",
        "topic": "output",
    }
    assert prompt_file.tests == {
        "test_01": "Test description 1",
        "test_02": "Test description 2",
    }


def test_prompt_file_duplicate_keys(duplicate_key_prompt_file):
    with pytest.raises(DuplicateKeyError) as excinfo:
        PromptFile(filename=str(duplicate_key_prompt_file))
    assert "Duplicate key was detected: key" in str(excinfo.value)


def test_prompt_file_to_dict(valid_prompt_file):
    prompt_file = PromptFile(filename=str(valid_prompt_file))
    data_dict = prompt_file.to_dict()
    assert data_dict == {
        "filename": str(valid_prompt_file),
        "prompt": "This is a test prompt.",
        "metadata": {"key": "value", "input": "input", "output": "output"},
        "tests": {"test_01": "Test description 1", "test_02": "Test description 2"},
    }


def test_prompt_file_from_dict(valid_prompt_file):
    data = {
        "filename": str(valid_prompt_file),
        "prompt": "This is a test prompt.",
        "metadata": {
            "key": "value",
            "input": "input",
            "output": "output",
            "topic": "output",
        },
        "tests": {"test_01": "Test description 1", "test_02": "Test description 2"},
    }
    prompt_file = PromptFile.from_dict(data)
    assert prompt_file.filename == str(valid_prompt_file)
    assert prompt_file.prompt == "This is a test prompt."
    assert prompt_file.metadata == {
        "key": "value",
        "input": "input",
        "output": "output",
    }
    assert prompt_file.tests == {
        "test_01": "Test description 1",
        "test_02": "Test description 2",
    }


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
