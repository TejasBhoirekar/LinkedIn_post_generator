# LinkedIn Post Generator 📝

A simple, clean, and fast **Streamlit** web app that helps generate thoughtful and meaningful LinkedIn posts on topics like **Self Improvement, Leadership, Career, Patriarchy**, and more — powered by **Llama 3.2 (open-source)**, **Langchain**, and **Groq Cloud**.

---

## Features

- Generate long-form or short-form posts on popular topics.
- Powered by open-source LLM **Llama 3.2** via Groq Cloud.
- Built using **Langchain** for prompt management and chaining.
- Streamlit UI for easy interaction.

---

![image alt](https://github.com/TejasBhoirekar/LinkedIn_post_generator/blob/main/working.jpeg?raw=true)

## Tech Stack

- Python
- Langchain
- Llama 3.2 (via Groq)
- Streamlit
- Groq Cloud

---

## Setup

To get started we first need to get an API_KEY from here: https://console.groq.com/keys. Inside .env update the value of GROQ_API_KEY with the API_KEY you created.

```bash
# Clone the repository
git clone https://github.com/your-username/linkedin-post-generator.git
cd linkedin-post-generator

# Create & activate conda environment
conda activate streamlit_env

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
