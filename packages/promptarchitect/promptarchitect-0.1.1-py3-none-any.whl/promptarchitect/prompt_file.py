import logging
import os

import coloredlogs

# Configuring logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
coloredlogs.install(level="INFO")


class DuplicateKeyError(Exception):
    """
    Exception raised when a duplicate key is attempted to be added to a dictionary.
    """

    def __init__(self, key, message="Duplicate key was detected"):
        self.key = key
        self.message = f"{message}: {key}"
        super().__init__(self.message)


class PromptFile:
    """
    A class to read the prompt file and return the prompt as a string.

    Attributes:
    filename (str): The name of the file containing the prompt.
    prompt (str): The prompt text.
    metadata (dict): The metadata extracted from the prompt file.
    tests (dict): The test prompts extracted from the prompt file.
    """

    def _get_metadata(self, prompt: str) -> dict:
        """
        Extracts the metadata from the prompt.

        Args:
            prompt (str): The prompt text.

        Returns:
            dict: The extracted metadata as key-value pairs.
        """

        # Split the prompt into lines
        lines = prompt.split("\n")

        # Create an empty dictionary to store the metadata
        metadata = {}

        # Loop through the lines
        for line in lines:
            # Check if the line contains metadata
            # In the form of <!-- key: value -->
            if line.startswith("<!--"):
                if not line.endswith("-->"):
                    raise ValueError(
                        f"Invalid metadata format {line}. \n\nExpected <!-- key: value -->"  # noqa: E501
                    )
            if line.startswith("<!--") and line.endswith("-->"):
                if "TEST-CASES" in line:
                    break
                try:
                    # Split the line into key and value
                    key, value = line[4:-4].split(":")
                    key = key.strip()
                    value = value.strip()

                    # Store the key-value pair in the metadata dictionary
                    if key in metadata:
                        # Duplicate key found
                        # Raise an error
                        logger.error(
                            f"Duplicate key {key} found in metadata. Expected unique keys."  # noqa: E501
                        )
                        raise DuplicateKeyError(f"{key}", message="")
                    metadata[key] = value

                    # For the implementation we don't need the read
                    # the input and output files over and over again.
                    # if "input" == key:
                    #     # remove extenstion from the filename
                    #     stripped_value = os.path.splitext(value)[0]
                    #     metadata[key.strip()] = stripped_value

                    if "output" == key:
                        # remove extenstion from the filename
                        stripped_value = os.path.splitext(value)[0]
                        metadata["topic"] = stripped_value
                except ValueError:
                    logger.error(
                        f"Invalid metadata format {line}. \n\nExpected <!-- key: value -->"  # noqa: E501
                    )

        return metadata

    def _get_prompt_text(self, prompt: str) -> str:
        """
        Extracts the prompt text from the prompt.

        Args:
            prompt (str): The prompt text.

        Returns:
            str: The extracted prompt text.
        """
        # Split the prompt into lines
        lines = prompt.split("\n")

        # Remove all lines that start with <!--
        lines = [line for line in lines if not line.startswith("<!--")]
        prompt_text = "\n".join(lines)
        return prompt_text.strip()

    def _get_prompt_tests(self, prompt: str) -> dict:
        """
        Extracts the test prompts from the prompt.

        Args:
            prompt (str): The prompt text.

        Returns:
            dict: The extracted test prompts as key-value pairs.
        """
        # Split the prompt into lines
        lines = prompt.split("\n")

        # Create an empty dictionary to store the metadata
        test_prompts = {}
        tests = {}

        # Loop through the lines to find the start of the test section
        for idx, line in enumerate(lines):
            # Check if the line contains metadata
            # In the form of <!-- key: value -->

            if line.startswith("<!--") and line.endswith("-->"):
                if (
                    "TEST-CASES" in line
                ):  # TODO: #1 Add to the readme that the test section should start with <!-- TEST-CASES --> # noqa: E501
                    # Now we are in the test section
                    # We can start reading the tests
                    # Split the lines from here
                    tests = lines[idx + 1 :]
                    break

        # Get all the tests under the test section
        for test in tests:
            # A test line starts with <!-- test and need two digits after the space
            if not test.lower().startswith("<!-- test"):
                continue

            if test.lower().startswith("<!-- test"):
                # Check if the test has a number
                if not test[10:12].isdigit():
                    logger.error(
                        f"Invalid test format {test}. \n\nTest number missing.\n\nExpected format <!-- test 01: Test description -->"  # noqa: E501
                    )  # noqa: E501

            # Split the line into key and value
            # Split at the first colon
            if ":" not in test:
                continue

            key, value = test.split(":", 1)
            key = key.replace("<!--", "").strip()
            key = key.replace(" ", "_")
            value = value.replace("-->", "").strip()

            # Store the key-value pair in the metadata dictionary
            test_prompts[key] = value

        return test_prompts

    def read_input(self, filename: str) -> str:
        """
        Reads the input file and returns the input as a string.

        Args:
            filename (str): The name of the file containing the input.

        Returns:
            str: The input text.
        """
        if not os.path.exists(filename):
            logger.warning(f"File {filename} not found.")
            return ""

        with open(filename, "r") as file:
            input_text = file.read()

        return input_text

    def __init__(self, filename: str = "prompt.txt"):
        """
        Initialize the PromptFile class with the filename of the prompt file.

        Args:
            filename (str): The name of the file containing the prompt.
            Defaults to 'prompt.txt'.
        """

        self.filename = filename
        self.metadata = {}

        # Read the contents of the prompt file
        with open(self.filename, "r") as file:
            self.text = file.read()

        # Get the prompt text from the prompt file
        self.prompt = self._get_prompt_text(self.text)
        self.metadata = self._get_metadata(self.text)
        self.tests = self._get_prompt_tests(self.text)

    def read_prompt(self) -> str:
        """
        Read the prompt file and return the prompt as a string.

        Returns:
            str: The prompt text.
        """
        if not os.path.exists(self.filename):
            logger.error(f"File {self.filename} not found.")
            return ""

        with open(self.filename, "r") as file:
            prompt = file.read()

        return prompt

    def to_dict(self):
        """
        Converts the PromptFile object to a dictionary.

        Returns:
            dict: The PromptFile object as a dictionary.
        """
        return {
            "filename": self.filename,
            "prompt": self.prompt,
            "metadata": self.metadata,
            "tests": self.tests,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a PromptFile object from a dictionary.

        Args:
            data (dict): The dictionary containing the PromptFile object data.

        Returns:
            PromptFile: The PromptFile object created from the dictionary.
        """
        obj = cls(data["filename"])
        obj.prompt = data["prompt"]
        obj.metadata = data["metadata"]
        obj.tests = data["tests"]
        return obj
