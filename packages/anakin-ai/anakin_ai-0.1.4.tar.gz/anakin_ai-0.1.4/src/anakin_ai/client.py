import requests
import json
from typing import Dict, Generator, Union

class AnakinAI:
    BASE_URL = "https://api.anakin.ai/v1"
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "X-Anakin-Api-Version": "2024-05-06",
            "Content-Type": "application/json"
        }
    
    def run_quick_app(self, app_id: str, inputs: Dict[str, str], stream: bool = True) -> Union[Dict[str, str], Generator[str, None, None]]:
        url = f"{self.BASE_URL}/quickapps/{app_id}/runs"
        payload = {
            "inputs": inputs,
            "stream": stream
        }
        
        return self._make_request(url, payload, stream)

    def chat_with_bot(self, app_id: str, content: str, stream: bool = True) -> Union[Dict[str, str], Generator[str, None, None]]:
        url = f"{self.BASE_URL}/chatbots/{app_id}/messages"
        payload = {
            "content": content,
            "stream": stream
        }
        
        return self._make_request(url, payload, stream)

    def _make_request(self, url: str, payload: Dict, stream: bool) -> Union[Dict[str, str], Generator[str, None, None]]:
        response = requests.post(url, headers=self.headers, json=payload, stream=stream)
        response.raise_for_status()
        
        if stream:
            return self._stream_response(response)
        else:
            return self._process_non_stream_response(response)

    def _stream_response(self, response: requests.Response) -> Generator[str, None, None]:
        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                if line.startswith('data:'):
                    data = line[5:].strip()
                    if data == '[DONE]':
                        break
                    try:
                        json_data = json.loads(data)
                        if 'content' in json_data:
                            yield json_data['content']
                    except json.JSONDecodeError:
                        continue

    def _process_non_stream_response(self, response: requests.Response) -> Dict[str, str]:
        content = ""
        thread_id = None
        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                if line.startswith('data:'):
                    data = line[5:].strip()
                    if data == '[DONE]':
                        break
                    try:
                        json_data = json.loads(data)
                        if 'threadId' in json_data:
                            thread_id = json_data['threadId']
                        if 'content' in json_data:
                            content += json_data['content']
                    except json.JSONDecodeError:
                        continue
        
        return {"content": content, "threadId": thread_id}