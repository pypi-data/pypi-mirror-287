# Unofficial Anakin AI Python Client

An unofficial Python client for interacting with the [Anakin AI](https://anakin.ai) API. This client allows you to easily integrate Anakin AI's powerful AI capabilities into your Python projects.

## Features

- Easy-to-use Python interface for Anakin AI API
- Support for both Quick Apps and Chatbot Apps
- Streaming and non-streaming response handling
- Flexible input handling for various app configurations

## Installation

Install the Anakin AI Python Client using pip:

```bash
pip install anakin-ai
```

If you encounter any issues with dependencies, you can manually install the required packages:

```bash
pip install anakin-ai requests
```

## Setup

Before using the client, you need to set up your Anakin AI API key:

1. Visit the Anakin AI website: https://anakin.ai and sign in to your account. You need to upgrade to a Pro account for using API feature.
2. Go to Account settings, and generate a new API Access Token.
   ![Generate an Anakin AI API Key](https://assets.anakin.ai/uploads/help/2024/05/07/8a26c2e93976c0f172842a3439a14810.png)
3. Set your local environment:
   ```bash
   # Set up a test environment:
   python -m venv anakin_test_env
   source anakin_test_env/bin/activate  # On Windows, use: anakin_test_env\Scripts\activate

   # Install Dependencies
   pip install -e .

   # Set up your API key:
   # Export your Anakin AI API key as an environment variable:
   export ANAKIN_AI_API_KEY="your_actual_api_key_here"
   # On Windows, use:
   set ANAKIN_AI_API_KEY=your_actual_api_key_here
   ```
4. Create a Quick App or Chatbot App in Anakin AI.

   ![](https://assets.anakin.ai/www/_next/static/media/feature-text-generation.1d76b8ca.webp)

   For example, if the URL is: https://app.anakin.ai/apps/28887, your APP_ID is 28887.

For detailed instructions on API setup, visit the [Anakin AI API Integration documentation](https://anakin.ai/docs/app-integration/api-integration).

## Usage

Here's how to use the Anakin AI Python Client for both Quick Apps and Chatbot Apps:

### Quick App

```python
from anakin_ai import AnakinAI
import os
import json

# Initialize the client with your API key
api_key = os.getenv("ANAKIN_AI_API_KEY")
client = AnakinAI(api_key)

# Run a Quick App
QUICK_APP_ID = "YOUR_APP_ID"  # Replace with your actual Quick App ID
inputs = {
    "Input": "Generate a marketing slogan for a cloud service that emphasizes reliability, performance, and efficiency."
}

# Streaming response
print("Testing Quick App with streaming:")
for chunk in client.run_quick_app(QUICK_APP_ID, inputs, stream=True):
    print(chunk, end='', flush=True)
print("\n\nStreaming completed.")

# Non-streaming response
print("\nTesting Quick App without streaming:")
result = client.run_quick_app(QUICK_APP_ID, inputs, stream=False)
print("Quick App Result:", json.dumps(result, indent=2))
```

### Chatbot App

```python
from anakin_ai import AnakinAI
import os
import json

# Initialize the client with your API key
api_key = os.getenv("ANAKIN_AI_API_KEY")
client = AnakinAI(api_key)

# Use a Chatbot App
CHATBOT_APP_ID = "YOUR_APP_ID"  # Replace with your actual Chatbot App ID

# Streaming response
print("Testing Chatbot with streaming:")
content = "What's your name? Are you the clever one?"
for chunk in client.chat_with_bot(CHATBOT_APP_ID, content, stream=True):
    print(chunk, end='', flush=True)
print("\n\nStreaming completed.")

# Non-streaming response
print("\nTesting Chatbot without streaming:")
content = "Tell me a joke about AI."
result = client.chat_with_bot(CHATBOT_APP_ID, content, stream=False)
print("Chatbot Result:", json.dumps(result, indent=2))

# Chatbot conversation example
print("\nTesting Chatbot conversation:")
messages = [
    "Hello, who are you?",
    "What can you do?",
    "Tell me a fun fact about AI."
]
for message in messages:
    print(f"\nUser: {message}")
    response = client.chat_with_bot(CHATBOT_APP_ID, message, stream=False)
    print("Chatbot:", response['content'])
```

Replace `"YOUR_APP_ID"` with your actual Anakin AI App IDs for Quick App and Chatbot App respectively.

## Differences between Quick App and Chatbot App calls

1. **Method names**: 
   - For Quick Apps, use `client.run_quick_app()`
   - For Chatbot Apps, use `client.chat_with_bot()`

2. **Input format**:
   - Quick Apps take a dictionary of inputs: `{"Input": "Your prompt here"}`
   - Chatbot Apps take a single string as content: `"Your message here"`

3. **URL endpoints**:
   - Quick Apps use: `/quickapps/{app_id}/runs`
   - Chatbot Apps use: `/chatbots/{app_id}/messages`

4. **Use case**:
   - Quick Apps are best for generating content based on specific inputs
   - Chatbot Apps are designed for interactive conversations

Both types of apps support streaming and non-streaming responses.

## Documentation

For more detailed information about the Anakin AI API and its capabilities, please refer to the [official Anakin AI documentation](https://anakin.ai/docs).

## Contributing

Contributions to the Anakin AI Python Client are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This is an unofficial client library and is not affiliated with, officially maintained, or endorsed by Anakin AI.
