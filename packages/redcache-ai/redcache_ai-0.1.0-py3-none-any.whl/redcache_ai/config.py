import os

def load_config():
    return {
        "llm": {
            "provider": "openai",
            "config": {
                "model": "gpt-4",
                "temperature": 0.2,
                "max_tokens": 1500,
            }
        }
    }

def set_openai_api_key(api_key):
    os.environ["OPENAI_API_KEY"] = api_key 

    