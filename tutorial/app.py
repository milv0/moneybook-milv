import streamlit as st

st.title("가계부")

date = st.date_input("날짜 입력")
money = st.text_input('금액 입력')

cate = ['식비','교통비','의류','병원']
category = st.selectbox("카테고리 선택",cate)

option_1 = st.checkbox('입금')
option_2 = st.checkbox('출금')

btn_clicked = st.button("Confirm", key='go',disabled = False)

if option_1 and option_2 :
    con = st.container()
    con.write('중복입력')


if option_1 and btn_clicked:
  con = st.container()
  con.write(f"{date}  {str(category)} + {int(money)}")
  
if option_2 and btn_clicked:
    
    con = st.container()
    con.write(f"{date}  {str(category)} - {int(money)}")