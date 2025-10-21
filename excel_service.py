import pandas as pd
import os
from datetime import datetime

def save_to_excel(name, category, desc, slogan, qr_path):
  os.makedirs("data", exist_ok=True)
  file_path= "data/products.xlsx"

  new_data= {
    "Tên sản phẩm": [name],
    "Loại": [category],
    "Mô tả AI": [desc],
    "Slogan": [slogan],
    "Đường dẫn QR": [qr_path],
    "Ngày tạo": [datetime.now().strftime("%Y-%m-%d %H:%M")]
  }

  new_df=pd.DataFrame(new_data)
  if os.path.exists(file_path):
    old_df=pd.read_excel(file_path)
    df=pd.concat([old_df,new_df], ignore_index=True)
  else:
    df=new_df
  df.to_excel(file_path, index=False)