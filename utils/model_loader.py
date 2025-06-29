import os
from dotenv import load_dotenv
from typing import Optional, Literal, Any 
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from langchain_openai import ChatOpenAI
from langchain_groq import Groq

class ConfigLoader:
    def __init__(self):
        print(f"Loading Config...")
        self.config = load_config()

    def __get_item(self, key):
        return self.config[key]
    
class ModelLoader(BaseModel):
    model_provider: Literal["openai", "groq"] = "openai"
    config: Optional[ConfigLoader] = Field(default=None, exclude=None)

    def model_post_init(self, __context:Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitary_type_allowed = True

    def load_llm(self):
        # Loads and returns the LLM based on the provider specified in the config
        print(f"LLM Loading...")
        print(f"Loading Model from the provider: {self.model_provider}")

        if self.model_provider == "openai":
            print(f"Loading OpenAI Model...")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.config["llm"]["openai"]["model"]
            llm = ChatOpenAI(model_name="gpt-4o-mini", api_key=openai_api_key)
        elif self.model_provider == "groq":
            print(f"Loading Groq Model...")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model"]
            llm = Groq(model_name=model_name, api_key=groq_api_key)
                
