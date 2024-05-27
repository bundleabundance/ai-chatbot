# AI Chatbot

This project is a basic AI chatbot using OpenAI's GPT-3.5-turbo model. The chatbot answers user questions through a web interface built with Flask.

## Features

- Chatbot interface using OpenAI's GPT-3.5-turbo model
- Securely loads API keys using `dotenv`
- Simple and clean web interface for user interaction

## Prerequisites

- Python 3.11+
- OpenAI API Key
- Flask
- `python-dotenv`


## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/bundleabundance/ai-chatbot
    cd ai-chatbot
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the root directory of your project:
      ```plaintext
      OPENAI_API_KEY=your_openai_api_key_here
      ```

## Usage

1. **Run the Flask application**:
    ```sh
    flask run
    ```

2. **Access the chatbot**:
    Open your web browser and go to `http://127.0.0.1:5000`.

3. **Interact with the chatbot**:
    Type your questions in the chat interface and get responses from the AI chatbot.

## Project Structure

ai-chatbot/
│
├── app.py # Main application file
├── config.py # Configuration file for environment variables
├── models.py # Model file with OpenAI API interaction
├── static/ # Static files (CSS, JS)
│ └── styles.css
├── templates/ # HTML templates
│ └── index.html
├── .env # Environment variables file
├── .gitignore # Git ignore file
├── README.md # Project documentation
└── requirements.txt # Python dependencies

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for their powerful API
- Flask for the web framework.