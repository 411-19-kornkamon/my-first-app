import streamlit as st
st.title("แอพพลิเคชั่นแปลง พ.ศ. เป็น ค.ศ.")

bh_year=st.number_input("กรอกปีพ.ศ.ที่ต้องการแปลง,value=2569")
ce_year=bh-year-543
st.header(f"ปี ค.ศ คือ : {ce_year}")
