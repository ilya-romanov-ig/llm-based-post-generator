import json
from config import PROMPT_TEMPLATE

def generate(few_shot_path, theme, post_count, platform, tone, post_length):
    with open(few_shot_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    examples = list(data.values())

    example_texts = ""

    for ex in examples:
        example_texts += f"""Тема: {ex["theme"]}
Платформа: {ex["platform"]}
Тон: {ex["tone"]}

Пост: 
{ex["text"]}

Хэштеги: {' '.join(ex["hashtags"])}
"""
    
    prompt = PROMPT_TEMPLATE.format(
        examples=example_texts,
        count=post_count,
        user_theme=theme,
        user_platform=platform,
        user_tone=tone,
        user_post_lenght=post_length
    )

    return prompt