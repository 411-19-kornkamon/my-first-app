import streamlit as st

st.markdown("# : red [ค่าดัชณีมวลกาย BMI]")
st.write("กรอกข้อมูลและน้ำหนักส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):", min_value=1.0, value=1.0)
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซ้นติเมตร):", min_value=1.0, value=1.0)

if st.button("คำนวณค่าBMI"):
   #แปลงส่วนสูงจาก cm เป็น เมตร แล้วคำนวณBMI
   height_m = height_cm / 100
   bmi = weight / (height_m ** 2)

   st.write("---") 
   st.header(f"ค่าBMIของคุณคือ: **{bmi:.2f}**")
  
