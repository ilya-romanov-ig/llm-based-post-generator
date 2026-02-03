import streamlit as st
from pathlib import Path
from ollama import chat
from config import *
from prompt_generator import generate

def main():
    root_path = Path(__file__).resolve().parent.parent
    few_shots_path = root_path / 'few_shots'
    theme = st.text_input('Тема / ключевые слова')
    platform = st.selectbox('Платформа', PLATFORM)
    length = st.slider('Длина поста', POST_MIN_LENGTH, POST_MAX_LENGTH, 120)
    count = st.slider('Количество постов', POST_MIN_VARIANTS, POST_MAX_VARIANTS, 1)
    tone = st.selectbox('Тон', POST_TONE)

    if st.button('Сгенерировать'):
        if platform == 'Telegram':
            path = few_shots_path / 'tg_few_shot.json'
        elif platform == 'VK':
            path = few_shots_path / 'vk_few_shot.json'
        elif platform == 'Yandex Dzen':
            path = few_shots_path / 'dzen_few_shot.json'

        prompt = generate(path, theme, count, platform, tone, length)

        response = chat(model='qwen2.5:7b-instruct', messages=[{'role': 'user', 'content': prompt}])
        st.markdown(response['message']['content'])

if __name__ == '__main__':
    main()