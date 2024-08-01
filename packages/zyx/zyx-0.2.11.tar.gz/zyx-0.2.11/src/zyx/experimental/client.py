# zyx ==============================================================================

__all__ = [
    'completion',
    '_CompletionClient',
    'embeddings',
]

import zyx
from typing import List, Optional, Union, Type
from pydantic.main import BaseModel

BaseMessage = Type["BaseMessage"]

# - client -----------------------------------------------------------------------

class _CompletionClient:
    def __init__(
        self,
        
        model : Optional[str] = "openai/gpt-4o-mini",
        temperature : Optional[float] = None,
        max_tokens : Optional[int] = None,
        api_key : Optional[str] = None,
        base_url : Optional[str] = None,
        
        verbose : Optional[bool] = False,
    ):
        """Base Langchain Helper Client for .completion() Abstraction"""
        self.verbose = verbose
        self._initialize_model(model, temperature, api_key, base_url, max_tokens)
        
    def _initialize_model(
        self,
        model : str,
        temperature : Optional[float] = None,
        max_tokens : Optional[int] = None,
        api_key : Optional[str] = None,
        base_url : Optional[str] = None,
    ):
        """Model Initialization Helper Function"""
        if self.verbose:
            zyx.logger.info(f"Initializing Completion Model: {model}")
        if base_url is not None:
            from langchain_openai.chat_models.base import ChatOpenAI
            try:
                self.model_name = model
                self.llm = ChatOpenAI(model = model, temperature = temperature, api_key = api_key, base_url = base_url, max_tokens = max_tokens)
                if self.verbose:
                    zyx.logger.info(f"Custom Endpoint Model: {model} Initialized Successfully")
            except Exception as e:
                raise e
        elif model.startswith("ollama/"):
            from langchain_community.chat_models.ollama import ChatOllama
            try:
                self.model_name = model[7:]
                self.llm = ChatOllama(model = self.model_name, temperature = temperature, max_tokens = max_tokens)
                if self.verbose:
                    zyx.logger.info(f"Ollama Model: {model} Initialized Successfully")
            except Exception as e:
                raise e
        else:
            from langchain_community.chat_models.litellm import ChatLiteLLM
            try:
                self.model_name = model
                self.llm = ChatLiteLLM(model = model, temperature = temperature, max_tokens = max_tokens)
                if self.verbose:  
                    zyx.logger.info(f"LiteLLM Model: {model} Initialized Successfully")
            except Exception as e: 
                raise e
    
    def _setup_query(
        self,
        messages: Union[str, list[dict]],
    ):  
        if self.verbose:
            zyx.logger.info(f"Formatting Messages...")
        if isinstance(messages, str):
            from langchain_core.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate
            template = ChatPromptTemplate.from_messages(
                [ HumanMessagePromptTemplate.from_template("{text}") ]
            )
            self.messages = template.format_messages(text = messages)
            if self.verbose:
                zyx.logger.info(f"Formatted.")
        elif isinstance(messages, list[dict]):
            from langchain_community.adapters.openai import convert_openai_messages
            self.messages = convert_openai_messages(messages)
            if self.verbose:
                zyx.logger.info(f"Formatted.")
        else:
            raise ValueError("Invalid messages type, please pass either a single string or a list of messages in the openai format.")
        
    def _response_handler(
        self,
        
        messages: Union[str, list[dict]],
        response_model : Optional[BaseModel] = None,
        tools : Optional[list] = None
    ):
        """Top Level Response Handling Function"""
        
        self._setup_query(messages)
            
        if self.verbose:
            zyx.logger.info("Running completion....")    
            
        if response_model is None and tools is None:
            return self.llm.invoke(
                input = self.messages,
            )
        elif response_model is not None and tools is None:
            self.llm = self.llm.with_structured_output(response_model)
            return self.llm.invoke(
                input = self.messages
            )
        elif response_model is not None and tools is not None:
            print("Not Implemented Yet")
            return None
        
if __name__ == "__main__":
    client = _CompletionClient(verbose = True)
    
    print(client._response_handler("Hello, how are you?"))
    
    class ResponseModel(BaseModel):
        character : str
        facts : list
        
    print(client._response_handler("Hello, how are you?", response_model = ResponseModel))


