from promptarchitect.huggingface_completion import HuggingFaceCompletion

def test_initialization():
    completion = HuggingFaceCompletion(system_role="You are a helpful assistant.", model="mlx-community/Meta-Llama-3.1-8B-4bit")
    assert completion.system_role == "You are a helpful assistant."
    assert completion.model == "mlx-community/Meta-Llama-3.1-8B-4bit"

def test_loading_model():
    completion = HuggingFaceCompletion(system_role="You are a helpful assistant.", model="mlx-community/Meta-Llama-3.1-8B-4bit")
    assert completion.model is not None
    assert completion.tokenizer is not None

def test_generating_response():
    completion = HuggingFaceCompletion(system_role="You are a helpful assistant.", model="mlx-community/Meta-Llama-3.1-8B-4bit")
    prompt = "What is the capital of France?"
    response = completion.completion(prompt)
    assert response is not None
    assert "Paris" in response

def test_edge_case_empty_prompt():
    completion = HuggingFaceCompletion(system_role="You are a helpful assistant.", model="mlx-community/Meta-Llama-3.1-8B-4bit")
    prompt = ""
    response = completion.completion(prompt)
    assert response is not None

def test_edge_case_long_prompt():
    completion = HuggingFaceCompletion(system_role="You are a helpful assistant.", model="mlx-community/Meta-Llama-3.1-8B-4bit")
    prompt = "A" * 10000
    response = completion.completion(prompt)
    assert response is not None
