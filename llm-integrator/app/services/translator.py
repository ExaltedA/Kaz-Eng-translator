import logging
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from pathlib import Path

logger = logging.getLogger(__name__)

class ModelDownloader:
    def __init__(self, model_name: str, model_path: Path):
        self.model_name = model_name
        self.model_path = model_path

    def download_if_not_exists(self):
        # Check if the model already exists
        if not self.model_path.exists():
            logger.info(f"Model not found locally at {self.model_path}. Downloading...")
            self._download_model()
        else:
            logger.info(f"Model found locally at {self.model_path}. Using cached model.")

    def _download_model(self):
        # Download the model and tokenizer, then save them locally
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
        tokenizer.save_pretrained(self.model_path)
        model.save_pretrained(self.model_path)
        logger.info(f"Model {self.model_name} successfully downloaded and cached.")

class ModelLoader:
    def __init__(self, model_path: Path):
        self.model_path = model_path

    def load(self):
        # Load model and tokenizer from the local folder
        tokenizer = AutoTokenizer.from_pretrained(self.model_path, use_fast=False)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.model_path)
        return tokenizer, model

class TranslatorService:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.model_path = Path(f"app/local_models/{model_name.replace('/', '__')}")
        self.device = 0 if torch.cuda.is_available() else -1

        # ModelDownloader will download the model if it's not cached
        self.downloader = ModelDownloader(self.model_name, self.model_path)
        self.downloader.download_if_not_exists()

        # ModelLoader will load the model
        self.loader = ModelLoader(self.model_path)

    def translate(self, text: str) -> str:
        # Load the model and tokenizer, and initialize the pipeline
        tokenizer, model = self.loader.load()
        translation_pipeline = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=self.device)
        return translation_pipeline(text, max_new_tokens=50)[0]['generated_text']
