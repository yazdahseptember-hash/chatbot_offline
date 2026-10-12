import requests
import json

def call_ollama_model(model , prompt , stream=False):
    url = 'http://localhost:11434/api/generate'

    parameters = {'model' :model,
                  'prompt':prompt,
                  'stream': stream
                  }

    paylod = json.dumps(parameters)
    response = requests.post(url , data=paylod , headers={'content-type' : 'application/json'})

    if response.status_code != 200:
        return 'error'
    else:
        response = response.json()['response']
        return response


if __name__ == '__main__':
    prompt = input('ask your question? ')
    model = 'qwen2.5-coder:7b'
    response = call_ollama_model(model , prompt)
    print('result' , response)