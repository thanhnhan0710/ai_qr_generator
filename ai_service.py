import google.generativeai as genai
import os
from dotenv import load_dotenv

# Nạp API key từ file .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_desciption(name, category, base_desc):
    prompt = f"""
    Viết mô tả hấp dẫn cho sản phẩm:
    - Tên: {name}
    - Loại: {category}
    - Mô tả cơ bản: {base_desc}
    Viết một đoạn mô tả ngắn (3–5 câu) và 1 slogan ngắn gọn.
    """

    try:
        model = genai.GenerativeModel(model_name="gemini-flash-latest")

        response = model.generate_content(prompt)
        text = response.text.strip()

        # Tách phần mô tả và slogan
        parts = text.split("Slogan:")
        ai_desc = parts[0].strip()
        slogan = parts[1].strip() if len(parts) > 1 else "Không có slogan"
        return ai_desc, slogan

    except Exception as e:
        print(f"❌ Lỗi khi gọi Gemini API: {e}")
        return "Không thể tạo mô tả", "Không thể tạo slogan"
