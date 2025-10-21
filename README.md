🧠 Dự án: Tạo Mô Tả & Mã QR Cho Sản Phẩm Bằng AI
🚀 Giới thiệu

Ứng dụng giúp người dùng tạo mô tả sản phẩm hấp dẫn và mã QR chứa thông tin sản phẩm bằng công nghệ AI Gemini của Google.
Giao diện được xây dựng bằng Streamlit, dễ sử dụng và có thể triển khai nhanh trên web nội bộ hoặc cloud.

🎯 Tính năng chính

✅ Tự động sinh mô tả sản phẩm và slogan ngắn gọn bằng AI
✅ Sinh mã QR chứa thông tin (tên, loại, mô tả, đường dẫn,...)
✅ Hiển thị và cho phép tải mã QR về
✅ Giao diện thân thiện, chạy trực tiếp trên trình duyệt
✅ Hỗ trợ cấu hình API key qua file .env

🏗️ Công nghệ sử dụng
Thành phần	Mô tả
Python 3.10+	Ngôn ngữ chính
Streamlit	Xây dựng giao diện web
Google Generative AI (Gemini API)	Sinh mô tả sản phẩm bằng AI
qrcode	Tạo mã QR từ dữ liệu sản phẩm
dotenv	Quản lý biến môi trường
Pillow (PIL)	Xử lý hình ảnh QR
📁 Cấu trúc thư mục
AI_Product_Label_Generator/
│
├── app.py                 # File chính (Streamlit hoặc Flask)
├── ai_service.py          # Xử lý phần AI (gọi OpenAI / Gemini)
├── qr_service.py          # Sinh mã QR Code
├── excel_service.py       # Lưu dữ liệu vào Excel
├── requirements.txt       # Thư viện cần cài
├── data/
│   ├── products.xlsx      # File lưu dữ liệu sản phẩm
│   └── qrcodes/           # Lưu ảnh QR đã tạo
└── assets/
    └── logo.png           # Logo website (nếu có)

⚙️ Cài đặt và chạy ứng dụng
1️⃣ Clone dự án
git clone https://github.com/<tên-người-dùng>/TaoQRMoTa.git
cd TaoQRMoTa

2️⃣ Tạo môi trường ảo (tuỳ chọn)
python -m venv venv
venv\Scripts\activate

3️⃣ Cài đặt thư viện
pip install -r requirements.txt

4️⃣ Tạo file .env

Trong thư mục gốc, tạo file .env và thêm:

GOOGLE_API_KEY=your_google_api_key_here

5️⃣ Chạy ứng dụng
python -m streamlit run app.py


Sau đó mở trình duyệt và truy cập:

http://localhost:8501

💡 Ví dụ kết quả

Mô tả sản phẩm:

“Nước yến thiên nhiên cao cấp được chưng cất từ tổ yến thật, giúp tăng cường sức khỏe và bổ sung năng lượng mỗi ngày.”
Slogan: “Tăng sức khỏe – Sáng mỗi ngày!”

Mã QR tạo ra chứa toàn bộ thông tin sản phẩm và có thể quét bằng điện thoại.

🧩 Hàm AI sử dụng
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_description(name, category, base_desc):
    prompt = f"""
    Viết mô tả hấp dẫn cho sản phẩm:
    - Tên: {name}
    - Loại: {category}
    - Mô tả cơ bản: {base_desc}
    Viết một đoạn mô tả ngắn (3–5 câu) và 1 slogan ngắn gọn.
    """
    model = genai.GenerativeModel(model_name="gemini-2.5-flash")
    response = model.generate_content(prompt)
    text = response.text.strip()

    parts = text.split("Slogan:")
    ai_desc = parts[0].strip()
    slogan = parts[1].strip() if len(parts) > 1 else "Không có slogan"
    return ai_desc, slogan

🧾 requirements.txt mẫu
streamlit
qrcode
pillow
python-dotenv
google-generativeai

🛠 Gợi ý triển khai thực tế

Có thể deploy ứng dụng lên Streamlit Cloud hoặc Render.com

Thêm tính năng lưu dữ liệu sản phẩm vào MySQL hoặc Firebase

Tích hợp tính năng upload ảnh sản phẩm và tạo QR kèm ảnh

Thêm lựa chọn xuất mô tả ra file PDF hoặc docx

💬 Liên hệ & bản quyền

📧 Tác giả: Phạm Thành Nhân
Điện thoại: 0385479058
📍 Phiên bản: 1.0
🗓 Cập nhật: 10/2025
⚙️ Giấy phép: MIT License

