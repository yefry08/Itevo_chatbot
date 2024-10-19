import gradio as gr
from deep_translator import GoogleTranslator
from typing import List, Tuple

# List of supported languages (you can expand this list)
LANGUAGES = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Chinese': 'zh-CN',
    'Japanese': 'ja'
}

def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    """Translate text from source language to target language."""
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    return translator.translate(text)

def chat(message: str, history: List[Tuple[str, str]], source_lang: str, target_lang: str) -> Tuple[str, List[Tuple[str, str]]]:
    """Process chat message, translate, and update history."""
    # Translate the incoming message to the target language
    translated_message = translate_text(message, LANGUAGES[source_lang], LANGUAGES[target_lang])
    
    # Add both original and translated messages to the history
    history.append((f"{message} ({source_lang})", f"{translated_message} ({target_lang})"))
    
    return "", history

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Language Translation Chatbot")
    
    with gr.Row():
        source_lang = gr.Dropdown(choices=list(LANGUAGES.keys()), label="Source Language", value="English")
        target_lang = gr.Dropdown(choices=list(LANGUAGES.keys()), label="Target Language", value="Spanish")
    
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    msg.submit(chat, [msg, chatbot, source_lang, target_lang], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch()