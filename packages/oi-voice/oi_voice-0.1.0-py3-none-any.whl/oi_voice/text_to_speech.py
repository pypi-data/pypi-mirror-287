import requests

def text_to_speech(text):
    api_key = "f8b22f75a6072f7c0c943f8b1a269760c4c8627c"
    url = "https://api.deepgram.com/v1/synthesize"
    headers = {
        "Authorization": f"Token {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice": "en-US"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        with open("output.wav", "wb") as f:
            f.write(response.content)
        return "output.wav"
    else:
        import logging
        logging.error(f"Text-to-Speech conversion failed with status code {response.status_code}: {response.text}")
        raise Exception("Text-to-Speech conversion failed. Please check the logs for more details.")
