from PIL import Image, ImageDraw, ImageFont
import os

def create_meme(image_path, top_text, bottom_text):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    
    # Размер шрифта зависит от размера картинки
    font_size = int(img.width / 10)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    # Функция для написания текста с черной обводкой
    def draw_text(text, y):
        # Обводка
        draw.text((2, y), text, font=font, fill="black", stroke_width=3, stroke_fill="black")
        # Белый текст
        draw.text((2, y), text, font=font, fill="white")

    # Верхний текст
    if top_text:
        draw_text(top_text.upper(), 10)
    
    # Нижний текст
    if bottom_text:
        draw_text(bottom_text.upper(), img.height - font_size - 10)

    # Сохраняем
    img.save("meme_result.png")
    print("Мем успешно создан: meme_result.png")

if __name__ == "__main__":
    top = os.environ.get("TOP_TEXT", "КОГДА ТЫ")
    bottom = os.environ.get("BOTTOM_TEXT", "СОБРАЛ МОД С ПЕРВОГО РАЗА")
    create_meme("image.jpg", top, bottom)2
