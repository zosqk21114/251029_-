import streamlit as st

st.title("박채림의 첫 번째 앱✨")
st.subheader("배고픈데..")
st.write("하하하! 어쩔 수 없지!")
st.write("https://naver.com")
st.link_button("naver 바로가기","https://naver.com")
name=st.text_input("이름을 입력해주세요. : ")
if st.button("환영인사"):
    st.write(name+"님 안녕하세요!")
    st.balloons()
st.image("https://img.freepik.com/free-vector/graident-ai-robot-vectorart_78370-4114.jpg?semt=ais_hybrid&w=740&q=80")
st.image("https://blog.kakaocdn.net/dna/CH4Ie/btqCSXeoDiS/AAAAAAAAAAAAAAAAAAAAAEjvz-VtAORzLplgUvKVyG2cCs_h0GYa0w0CR7zPAfDy/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1761922799&allow_ip=&allow_referer=&signature=MvWb8yd%2BjIAxoGiRtSUijNJxy4k%3D")
st.success("성공!")
st.warning("경고!")
st.error("오류!")
st.info("안내문")
