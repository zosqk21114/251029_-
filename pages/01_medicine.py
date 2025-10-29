import streamlit as st

# ----------------------------
# 기본 설정
# ----------------------------
st.set_page_config(page_title="💊 AI 약 추천 + 상세정보", page_icon="💊", layout="centered")

# ----------------------------
# 제목 섹션
# ----------------------------
st.markdown("""
<h1 style='text-align:center;'>🤖 AI 기반 증상별 약 추천 + 상세정보</h1>
<p style='text-align:center; font-size:18px;'>
AI가 증상을 분석해 약을 추천하고,<br>
클릭 시 상세 정보를 보여드립니다 💊
</p>
""", unsafe_allow_html=True)

# ----------------------------
# 약 데이터베이스
# ----------------------------
medicine_db = {
    "타이레놀": {
        "효능": "두통, 발열, 근육통 완화",
        "성분": "아세트아미노펜 500mg",
        "복용법": "성인 1회 1~2정, 1일 최대 4회",
        "주의사항": [
            "과량 복용 시 간 손상 위험이 있습니다.",
            "음주 전후 복용은 피하세요.",
            "4시간 간격으로 복용하세요."
        ]
    },
    "이부프로펜": {
        "효능": "염증 완화, 두통, 생리통, 근육통 완화",
        "성분": "이부프로펜 200mg",
        "복용법": "성인 1회 1~2정, 1일 최대 3회",
        "주의사항": [
            "공복 복용을 피하세요.",
            "위장 장애가 있는 경우 주의하세요."
        ]
    },
    "게보린": {
        "효능": "두통, 치통, 생리통 완화",
        "성분": "아세트아미노펜, 카페인, 이소프로필안티피린",
        "복용법": "성인 1회 1정, 1일 최대 3회",
        "주의사항": [
            "카페인 음료와 함께 복용하지 마세요.",
            "수면 장애를 유발할 수 있습니다."
        ]
    },
    "클라리틴": {
        "효능": "알레르기 비염, 재채기, 콧물 완화",
        "성분": "로라타딘 10mg",
        "복용법": "성인 1일 1정",
        "주의사항": [
            "졸음이 거의 없으나 개인차가 있습니다.",
            "간 기능 이상 시 복용 전 의사 상담 필요."
        ]
    },
    "겔포스": {
        "효능": "속쓰림, 위산 과다, 위통 완화",
        "성분": "알루미늄 하이드록사이드, 마그네슘 하이드록사이드",
        "복용법": "성인 1회 1포, 식전 또는 위통 시 복용",
        "주의사항": [
            "과량 복용 시 설사나 변비를 유발할 수 있습니다.",
            "신장 질환자는 복용 전 의사와 상담하세요."
        ]
    },
}

symptom_map = {
    "두통": ["타이레놀", "이부프로펜", "게보린"],
    "속쓰림": ["겔포스"],
    "알레르기": ["클라리틴"]
}

# ----------------------------
# AI 증상 분류 (간단 버전)
# ----------------------------
def classify_symptom(text):
    text = text.lower()
    if any(x in text for x in ["두통", "머리", "지끈"]):
        return "두통"
    elif any(x in text for x in ["속쓰림", "위", "명치"]):
        return "속쓰림"
    elif any(x in text for x in ["알레르기", "콧물", "비염"]):
        return "알레르기"
    else:
        return None

# ----------------------------
# 사용자 입력
# ----------------------------
st.markdown("---")
user_input = st.text_area("🩺 증상을 입력하세요:", height=100, placeholder="예: 머리가 지끈거리고 열이 나요")

if st.button("🔍 AI 약 추천 받기"):
    if not user_input.strip():
        st.warning("⚠️ 증상을 입력해주세요.")
    else:
        symptom = classify_symptom(user_input)
        if symptom and symptom in symptom_map:
            st.success(f"✅ AI가 인식한 증상: **{symptom}**")

            st.markdown("### 💊 추천 약 목록:")
            for med_name in symptom_map[symptom]:
                with st.container():
                    if st.button(f"💊 {med_name}", key=med_name):
                        selected_medicine = med_name
                        st.session_state["selected_medicine"] = selected_medicine
        else:
            st.error("❌ AI가 해당 증상을 인식하지 못했습니다. 다른 표현으로 시도해보세요.")

# ----------------------------
# 상세 정보 표시 섹션
# ----------------------------
if "selected_medicine" in st.session_state:
    med = st.session_state["selected_medicine"]
    if med in medicine_db:
        data = medicine_db[med]

        st.markdown("---")
        st.markdown(f"## 💊 {med} 상세 정보")
        st.markdown(f"**🧾 효능:** {data['효능']}")
        st.markdown(f"**🧬 성분:** {data['성분']}")
        st.markdown(f"**⏰ 복용법:** {data['복용법']}")

        st.markdown("**⚠️ 복용 시 주의사항:**")
        for note in data["주의사항"]:
            st.markdown(f"- {note}")

        # 닫기 버튼
        if st.button("🔙 목록으로 돌아가기"):
            del st.session_state["selected_medicine"]
            st.experimental_rerun()

# ----------------------------
# 푸터
# ----------------------------
st.markdown("""
<hr>
<p style='text-align:center; color:gray; font-size:14px;'>
Made with ❤️ using Streamlit · 약 상세정보 버전
</p>
""", unsafe_allow_html=True)
