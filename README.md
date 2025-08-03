# LangGraph Chatbot

LangGraph Chatbot is an interactive chatbot framework built using [LangGraph](https://github.com/langchain-ai/langgraph), designed to provide flexible, multi-turn conversational AI experiences. This repository serves as a starting point for building custom chatbots leveraging the power of LangGraph, Python, and popular LLM platforms.

## Features

- Multi-turn conversation handling
- Easily extensible for custom logic and tools
- Integration with major LLMs (e.g., OpenAI, Hugging Face)
- Modular architecture for maintainability
- Example scripts for quick start

## Getting Started

### Prerequisites

- Python 3.8+
- [Poetry](https://python-poetry.org/) or `pip`
- Access to an LLM API (e.g., OpenAI key)

### Installation

```bash
git clone https://github.com/Shezan57/langgraph_chatbot.git
cd langgraph_chatbot
poetry install
```
Or use pip:
```bash
pip install -r requirements.txt
```

### Configuration

1. Set up your API keys (OpenAI, etc.) in a `.env` file or as environment variables.
2. Edit the configuration files or scripts as needed for your use case.

### Usage

Example to run the chatbot:

```bash
python main.py
```

You can customize its behavior by modifying the graph logic in `chatbot_graph.py` or other source files.

## File Structure

```
langgraph_chatbot/
├── main.py              # Entry point for the chatbot
├── chatbot_graph.py     # Defines the LangGraph logic
├── utils/               # Utility functions
├── requirements.txt
├── README.md
└── ...
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for bug fixes, enhancements, or new features.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://github.com/langchain-ai/langchain)
- Contributors and community
