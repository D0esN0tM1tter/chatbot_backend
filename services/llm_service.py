from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class LLMService:
    def __init__(self, model_name="gpt2", max_length=50, no_repeat_ngram_size=2):
        """
        Initializes the LLMService instance.

        Parameters:
        model_name (str): Name or path of the model from the Hugging Face Hub.
        max_length (int): Maximum length of the generated sequence.
        no_repeat_ngram_size (int): Prevents repetition in the generated sequence.
        """
        self.model_name = model_name
        self.max_length = max_length
        self.no_repeat_ngram_size = no_repeat_ngram_size
        self.model, self.tokenizer = self.load_model()

    def load_model(self):
        """
        Loads the model and its tokenizer from the Hugging Face Hub.
        
        Returns:
        tuple: Loaded model and tokenizer.
        """
        try:
            model = AutoModelForCausalLM.from_pretrained(self.model_name)
            model.eval()
            tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            return model, tokenizer
        except Exception as e:
            raise RuntimeError(f"Error loading the model and tokenizer: {str(e)}")

    def generate(self, message):
        """
        Generates a response from the model based on the input message.

        Parameters:
        message (str): Input text prompt for generation.

        Returns:
        str: Generated text response.
        """
        try:
            inputs = self.tokenizer.encode(
                message,
                return_tensors="pt",
            )

            with torch.no_grad():
                outputs = self.model.generate(
                    inputs,
                    max_length=self.max_length,
                    num_return_sequences=1,
                    no_repeat_ngram_size=self.no_repeat_ngram_size
                )

            response = self.tokenizer.decode(
                outputs[0],
                skip_special_tokens=True,
                clean_up_tokenization_spaces=True
            )

            return response

        except Exception as e:
            raise RuntimeError(f"Error generating a response: {str(e)}")
