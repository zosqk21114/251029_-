import streamlit as st
from datetime import datetime, timedelta

# ----------------------------
# 기본 설정
# ----------------------------
st.set_page_config(page_title="💊 약 복용 알림 및 기록", page_icon="⏰", layout="centered")

# ----------------------------
# 제목
# ----------------------------
st.markdown("""
<h1 style='text-align:center;'>⏰ 약 복용 알림 & 기록 페이지</h1>
<p style='text-align:center; font-size:18px;'>
복용한 약을 기록하고, 다음 복용 시간도 관리해보세요 💊
</p>
""", unsafe_allow_html=True)

# ----------------------------
# 세션 상태 초기화
# ----------------------------
if "records" not in st.session_state:
    st.session_state["records"] = []

# ----------------------------
# 약 복용 입력 섹션
# ----------------------------
st.markdown("### 💊 복용 정보 입력")

col1, col2 = st.columns(2)
with col1:
    medicine_name = st.text_input("약 이름", placeholder="예: 타이레놀, 겔포스 등")
with col2:
    dose = st.number_input("복용 개수 (정/포)", min_value=1, max_value=10, value=1)

time_taken = st.time_input("⏰ 복용 시각", datetime.now().time())
interval_hours = st.number_input("다음 복용까지 (시간)", min_value=1, max_value=24, value=6)

if st.button("✅ 복용 기록 추가"):
    if not medicine_name.strip():
        st.warning("⚠️ 약 이름을 입력해주세요.")
    else:
        record = {
            "약 이름": medicine_name,
            "복용 개수": dose,
            "복용 시각": datetime.combine(datetime.today(), time_taken),
            "다음 복용 시간": datetime.combine(datetime.today(), time_taken) + timedelta(hours=interval_hours)
        }
        st.session_state["records"].append(record)
        st.success(f"💊 {medicine_name} 복용 기록이 추가되었습니다!")

# ----------------------------
# 기록 표시 섹션
# ----------------------------
st.markdown("---")
st.markdown("### 📋 복용 기록")

if len(st.session_state["records"]) == 0:
    st.info("아직 복용 기록이 없습니다.")
else:
    for i, r in enumerate(st.session_state["records"]):
        next_time = r["다음 복용 시간"].strftime("%H:%M")
        taken_time = r["복용 시각"].strftime("%H:%M")

        st.markdown(f"""
        <div style='
            background-color:#f8f9fa;
            border-radius:12px;
            padding:12px 18px;
            margin:8px 0;
            box-shadow:0 2px 5px rgba(0,0,0,0.1);
        '>
        <strong>💊 {r["약 이름"]}</strong><br>
        복용 개수: {r["복용 개수"]} 정<br>
        복용 시각: {taken_time}<br>
        다음 복용: 🕒 <b>{next_time}</b>
        </div>
        """, unsafe_allow_html=True)

    # ----------------------------
    # 복용 완료/삭제 버튼
    # ----------------------------
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ 모든 기록 삭제"):
            st.session_state["records"].clear()
            st.warning("모든 복용 기록이 삭제되었습니다.")
    with col2:
        st.info("💡 다음 복용 시간이 되면 알림(또는 알림음)을 추가할 수도 있습니다.")

# ----------------------------
# 푸터
# ----------------------------
st.markdown("""
<hr>
<p style='text-align:center; color:gray; font-size:14px;'>
Made with ❤️ using Streamlit · 복용 기록 기능
</p>
""", unsafe_allow_html=True)
