import gradio as gr
from deep_translator import GoogleTranslator
from typing import List, Tuple
import os
import logging
import sqlite3
from datetime import datetime
import hashlib
import unittest

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load API key from environment variable
API_KEY = os.getenv('GOOGLE_TRANSLATE_API_KEY')
if not API_KEY:
    logging.warning("Google Translate API key not found. Using free tier with limited usage.")

# List of supported languages
LANGUAGES = {
    'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de',
    'Chinese': 'zh-CN', 'Japanese': 'ja', 'Russian': 'ru', 'Arabic': 'ar'
}

# Database setup
def setup_database():
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS chats
                 (id INTEGER PRIMARY KEY, user_id TEXT, timestamp TEXT, 
                  source_lang TEXT, target_lang TEXT, original_text TEXT, translated_text TEXT)''')
    conn.commit()
    return conn

# Hashing function for user IDs (for privacy)
def hash_user_id(user_id: str) -> str:
    return hashlib.sha256(user_id.encode()).hexdigest()

def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    try:
        translator = GoogleTranslator(source=source_lang, target=target_lang, api_key=API_KEY)
        return translator.translate(text)
    except Exception as e:
        logging.error(f"Translation error: {e}")
        return "Error: Could not translate text."

def chat(message: str, history: List[Tuple[str, str]], source_lang: str, target_lang: str, user_id: str) -> Tuple[str, List[Tuple[str, str]]]:
    translated_message = translate_text(message, LANGUAGES[source_lang], LANGUAGES[target_lang])
    
    # Store in database
    conn = setup_database()
    c = conn.cursor()
    c.execute("INSERT INTO chats (user_id, timestamp, source_lang, target_lang, original_text, translated_text) VALUES (?, ?, ?, ?, ?, ?)",
              (hash_user_id(user_id), datetime.now().isoformat(), source_lang, target_lang, message, translated_message))
    conn.commit()
    conn.close()

    history.append((f"{message} ({source_lang})", f"{translated_message} ({target_lang})"))
    return "", history

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Advanced Language Translation Chatbot")
    
    with gr.Row():
        source_lang = gr.Dropdown(choices=list(LANGUAGES.keys()), label="Source Language", value="English")
        target_lang = gr.Dropdown(choices=list(LANGUAGES.keys()), label="Target Language", value="Spanish")
    
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")
    user_id = gr.Textbox(label="User ID (for demo purposes)")

    msg.submit(chat, [msg, chatbot, source_lang, target_lang, user_id], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

# Unit tests
class TestTranslationChatbot(unittest.TestCase):
    def test_translation(self):
        result = translate_text("Hello", "en", "es")
        self.assertEqual(result.lower(), "hola")

    def test_user_id_hashing(self):
        user_id = "test_user"
        hashed_id = hash_user_id(user_id)
        self.assertEqual(len(hashed_id), 64)  # SHA-256 produces 64 character hex string

if __name__ == "__main__":
    # Run tests
    unittest.main(exit=False)
    
    # Launch the Gradio interface
    demo.launch(share=True)