from autogen import oai

# create a text completion request
response = oai.Completion.create(
    config_list=[
        {
            "model": "chatglm2-6b",
            "api_base": "http://localhost:8000/v1",
            "api_type": "open_ai",
            "api_key": "NULL",
        }
    ],
    prompt="Hi",
)
print(response)

# create a chat completion request
response = oai.ChatCompletion.create(
    config_list=[
        {
            "model": "chatglm2-6b",
            "api_base": "http://localhost:8000/v1",
            "api_type": "open_ai",
            "api_key": "NULL",
        }
    ],
    messages=[{"role": "user", "content": "Hi"}]
)
print(response)