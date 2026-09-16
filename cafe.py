import streamlit as st
st.title("cafe PAUdd")
st.title("รายการน้ำ")
st.write("มัจฉะดูไบช็อกโกแล็ต 80 เอสเพรสโซ  50 ลาเต้ 50 แฟลตไวท์ 40")
st.title("ท็อปปิ้ง")
st.write("วิปครีม 15 ไข่มุก 10")
price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)
vat = price * 0.07
net_price = price - vat
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): {vat:.2f} บาท")
st.header(f"• ราคาสุทธิ : {net_price:.2f} บาท")
st.divider()
