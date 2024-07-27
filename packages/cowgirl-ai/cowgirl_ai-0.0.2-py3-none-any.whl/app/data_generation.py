import logging
from typing import List, Union
from core.assistant.core_assistant import CoreAssistant
from cowgirl_ai.error_handler import error_handler
from cowgirl_ai.search.search import Search

logging.basicConfig(level=logging.INFO, datefmt="%Y-%m-%d", format="%(levelname)s - %(message)s")

class DataGeneration(CoreAssistant):
    """
    Data Generation Assistant
    -------------------------

    Generates data based on user input, output as json format for further transformations
    """

    def __init__(self):
        super().__init__(assistant_name="You are a Data Generation Assistant")
        self.temperature = 0.1  # Leave a little room for inference
        self.description = "Data generation and optimization bot. Just create structured data relating to the prompt"
        self.response_format = {"type": "json_object" }
        self.instructions = (
            "No chat response needed, just respond with the code. No backticks needed"
            "Return chat results as json object"
            "Add supporting factual attributes"
        )

    
    @error_handler
    def generate(self, prompt: str) -> str:
        """
        Generates refined code based on the provided prompt.

        Args:
            prompt (str): The original code to refine.

        Returns:
            str: The refined code.

        Usage::
            generator = DataGenerator()
            generator.generate(prompt=prompt)
        """
        completion = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=[
                {"role": "system", "content": self.description},
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": prompt}
            ],
            n=1,
        )
        return completion.choices[0].message.content


    
    @error_handler
    def stream(self, prompt: str) -> str:
        """
        Generates refined code based on the provided prompt.

        Args:
            prompt (str): The original code to refine.

        Returns:
            str: The refined code.

        Usage::
            generator = DataGeneration()
            full_response = generator.stream(prompt='5 indoor house plants')
        """
        # response_format = {"type": "text"}  
        completion = self.client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=[
                {"role": "system", "content": self.description},
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": prompt}
            ],
            n=1,
            stream=True,
            response_format=self.response_format
        )
        
        full_response = ""
        for chunk in completion:
            content = chunk.choices[0].delta.content
            if content:
                full_response += content
                print(content, end="")  # Print each chunk as it comes in for streaming effect
        return full_response

if __name__ == "__main__":
    generator = DataGeneration()
    full_response = generator.stream(prompt='5 indoor house plants')