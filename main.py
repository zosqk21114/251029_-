import streamlit as st

st.title("박채림의 첫 번째 앱✨")
st.subheader("오늘 저녁 뭐먹지?")
st.write("하하하! 오늘 석식 고구마튀김")
st.write("https://naver.com")
st.link_button("naver 바로가기","https://naver.com")
name=st.text_input("이름을 입력해주세요. : ")
if st.button("환영인사"):
    st.write(name+"님 안녕하세요!")
    st.balloons()
st.image("https://img.freepik.com/free-vector/graident-ai-robot-vectorart_78370-4114.jpg?semt=ais_hybrid&w=740&q=80")

st.success("성공!")
st.warning("경고!")
st.error("오류!")
st.info("안내문")
