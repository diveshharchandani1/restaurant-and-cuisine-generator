# � Restaurant Generator AI 🥘

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app/)
![LangChain](https://img.shields.io/badge/LangChain-13.0%2B-blue)
![Ollama](https://img.shields.io/badge/Ollama-0.1%2B-orange)

An AI-powered restaurant name and menu generator that creates culinary concepts based on selected cuisines, powered by Llama3-2B LLM through LangChain.

## ✨ Features
- **Cuisine Selection**: Choose from various international cuisines via dropdown
- **AI-Powered Generation**: 
  - Generate creative restaurant names
  - Suggest relevant menu items
- **Sequential Workflow**: Uses LangChain's SequentialChain for multi-step generation
- **Simple UI**: Streamlit-based interface for easy interaction

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.ai/) installed locally
- Llama3-2B model installed (run `ollama pull llama3:2b`)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/diveshharchandani1/restaurant-generator-ai.git
cd restaurant-generator-ai
```

2. Install dependencies:
```bash 
pip install -r requirements.txt
```

Usage
1. Start the Streamlit app:
```bash
streamlit run main.py
```

2. In the browser:
Select a cuisine from the dropdown
Click "Generate" to create restaurant concept
View results in the formatted output section


🧠 Project Structure

.

└── main.py                 # Streamlit UI implementation

└── langchain_helper.py     # LangChain model and chain configurations

└── test.ipynb              # Jupyter Notebook for initial testing

└── requirements.txt        # Dependency list

└── README.md               # This documentation



🔧 Technical Stack
- Language Model: Llama3-2B via Ollama
- Framework: LangChain (LLMChain, SequentialChain)
- UI: Streamlit
- Language: Python 3.8+


🤖 Implementation Details

The system uses two sequential LLMChains:

1. Name Generation Chain:
- Takes cuisine as input
- Generates restaurant name


2. Menu Generation Chain:
- Uses cuisine and generated name as input
- Creates 5-8 relevant menu items

Chains are connected using SequentialChain for maintained context.


📦 Dependencies

- streamlit>=1.31
- langchain>=0.1.0
- ollama>=0.1.0
- ipython (for testing)


🙏 Acknowledgements

-  Ollama team for model serving
- LangChain for LLM orchestration
- Streamlit for UI components
- Meta for Llama3 model