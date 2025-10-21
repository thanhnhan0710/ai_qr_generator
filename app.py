import streamlit as st
from ai_service import generate_desciption
from  qr_service import generate_qr
from excel_service import save_to_excel
from datetime import datetime

st.set_page_config(page_title="AI Product Lable Generator", page_icon="🧠")

st.title("🧠 AI Prcduct Lable Generator")
st.write("Nhập thông tin sản phẩm, để AI giúp bạn tạo nhãn chuyên nghiệp và mã QR.")

#--Input Form--
with st.form("product_form"):
  name= st.text_input("Tên sản phầm:")
  category= st.text_input("Loại sản phẩm:")
  base_desc=st.text_area("Mô tả cơ bản:")
  submitted= st.form_submit_button("Tạo mô tả AI + QR code")

if submitted:
  if not name:
    st.error("Vui lòng nhập tên sản phẩm.")
  else:
    with st.spinner("AI đang xử lý..."):
      ai_desc, slogan= generate_desciption(name, category, base_desc)
      qr_path= generate_qr(name, ai_desc, slogan)

      save_to_excel(name,category, ai_desc, slogan, qr_path)
    st.success("🎉 Tạo thành công!")
    st.subheader("✨ Mô tả AI:")
    st.write(ai_desc)
    st.subheader("💬 Slogan:")
    st.write(f"_{slogan}_")
    st.image(qr_path, caption="Mã QR sản phẩm")

    st.download_button("📥 Tải file Excel", data= open("data/products.xlsx","rb"), file_name="products.xlsx")
