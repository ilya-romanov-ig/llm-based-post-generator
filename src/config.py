PLATFORM = ['Telegram', 'VK', 'Dzen']
POST_TONE = ['Весёлый', 'Профессиональный', 'Мотивирующий', 'Ироничный']
POST_MIN_LENGTH = 60
POST_MAX_LENGTH = 280
POST_MIN_VARIANTS = 1
POST_MAX_VARIANTS = 6

PROMPT_TEMPLATE = """Ты - SMM-специалист 2026 года.

Вот несколько примеров постов в моём стиле:

{examples}

Теперь напиши {count} разных постов в моём стиле.
Тема: {user_theme} 
Платформа: {user_platform} 
Тон: {user_tone} 
Длина: ≈ {user_post_lenght} символов
Обязательно: эмодзи (3-6), призыв к действию, 4-8 хэштегов


Посты:"""