from promptarchitect.completions.core import Completion
from transformers import AutoModelForCausalLM, AutoTokenizer

class HuggingFaceCompletion(Completion):
    def __init__(self, system_role: str = "", model: str = "", parameters={}):
        super().__init__(parameters)
        self.system_role = system_role
        self.model_name = model
        self.parameters = parameters
        self.cost = 0.0
        self.is_json = False
        self.response_message = ""
        self.latency = 0.0  # Latency of the completion in seconds

        # Load the model and tokenizer
        self.model = AutoModelForCausalLM.from_pretrained(model)
        self.tokenizer = AutoTokenizer.from_pretrained(model)

    def completion(self, prompt: str) -> str:
        """
        Perform a completion task with the given prompt using Huggingface model.
        """
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        self.response_message = response
        return response

    def to_dict(self):
        return {
            "system_role": self.system_role,
            "model": self.model_name,
            "parameters": self.parameters,
            "cost": self.cost,
            "is_json": self.is_json,
            "response_message": self.response_message,
            "latency": self.latency,
        }

    @classmethod
    def from_dict(cls, data):
        obj = cls(
            system_role=data["system_role"],
            model=data["model"],
            parameters=data["parameters"],
        )
        obj.cost = data.get("cost", 0.0)
        obj.is_json = data.get("is_json", False)
        obj.response_message = data.get("response_message", "")
        obj.latency = data.get("latency", 0.0)
        return obj
