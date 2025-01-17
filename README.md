# Mindful Moments

**Mindful Moments** is an AI-powered chatbot that provides real-time support and information on mental health topics such as anxiety, depression, and stress management. Leveraging advanced machine learning and a comprehensive database of mental health FAQs, it offers personalized advice and practical strategies to help users enhance their well-being. *Note: This chatbot is for educational purposes and not a substitute for professional medical advice.*

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Personalized Support:** Tailors responses based on user queries to deliver relevant and actionable advice.
- **Comprehensive Knowledge Base:** Utilizes a vast dataset of mental health FAQs to ensure accurate and reliable information.
- **Real-Time Interaction:** Offers instant responses, making mental health support accessible anytime, anywhere.
- **User-Friendly Interface:** Provides an engaging and intuitive chat experience through an interactive UI built with Gradio.
- **AI Integration:** Powered by advanced language models via the Groq API for enhanced response quality.

## Demo

![Mindful Moments Demo](![Uploading image.png…]()
)

Experience **Mindful Moments** in action! [Launch the Demo](#) *(https://huggingface.co/spaces/Muhirwa12a/mentalhealthchatbot)*

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/muhirwa23/mindful-moments.git
   cd mindful-moments
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your Groq API key:

   ```env
   groq_api_keys=your_groq_api_key_here
   ```

5. **Prepare the Dataset**

   Ensure your mental health FAQ dataset is named `dataset1.csv` and placed in the root directory. The CSV should have the following columns:
   
   - `Questions`: The frequently asked questions.
   - `Answers`: Corresponding answers to the questions.

## Usage

Run the chatbot locally using Gradio:

```bash
python app.py
```

This will launch the Gradio interface, and you can interact with **Mindful Moments** through your web browser.

## Project Structure

```
mindful-moments/
│
├── dataset1.csv
├── app.py
├── README.md
├── requirements.txt
├── .env
└── ... (other project files)
```

- **`dataset1.csv`**: Contains the mental health FAQs.
- **`app.py`**: The main application script.
- **`requirements.txt`**: Lists all the Python dependencies.
- **`.env`**: Stores environment variables (e.g., Groq API keys).

## Technologies Used

- **Python & Pandas:** For data manipulation and processing.
- **SentenceTransformers:** To generate context embeddings.
- **LangChain & Chroma:** For building the retrieval-augmented generation (RAG) pipeline.
- **Gradio:** To create an interactive and user-friendly chat interface.
- **Groq API:** Utilized for the language model backend.
- **HuggingFaceEmbeddings:** For embedding generation.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**

2. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add your message here"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE). *(Ensure you have a LICENSE file in your repository)*

## Contact

**Muhirwa Jean Bosco**  
23 Years Old | Statistician | Machine Learning Engineer | Developer | AI Researcher  
Email: [muhirwaJbsc@gmail.com](mailto:muhirwaJbsc@gmail.com)  
LinkedIn: [www.linkedin.com/in/muhirwa-jean-bosco](https://www.linkedin.com/in/muhirwa-jean-bosco)  
GitHub: [github.com/muhirwa23](https://github.com/muhirwa23)  
Hugging Face: [huggingface.co/muhirwa12a](https://huggingface.co/muhirwa12a)

---

### Additional Notes:

- **Demo Section:** Replace `demo_screenshot.png` with an actual screenshot of your chatbot demo and update the demo link accordingly if you host it somewhere.
  
- **LICENSE:** Ensure you add a `LICENSE` file to your repository if you mention it in the README. The MIT License is commonly used and easy to implement.

- **Environment Variables:** Remember to add `.env` to your `.gitignore` file to prevent sensitive information like API keys from being pushed to your repository.

- **Dependencies:** Make sure your `requirements.txt` includes all the necessary packages. You can generate it using:

  ```bash
  pip freeze > requirements.txt
  ```
