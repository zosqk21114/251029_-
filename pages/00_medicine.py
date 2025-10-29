import streamlit as st
import random

# ----------------------------
# 페이지 설정
# ----------------------------
st.set_page_config(page_title="💊 증상 기반 약 추천 AI", page_icon="🤖", layout="centered")

# ----------------------------
# 제목 섹션
# ----------------------------
st.markdown("""
<h1 style='text-align:center;'>🤖 AI 기반 증상별 약 추천 서비스</h1>
<p style='text-align:center; font-size:18px;'>
증상을 입력하면 AI가 자동으로 분석하고,<br>
해당 증상에 맞는 약과 복용 시 주의사항을 안내해드립니다. 💊
</p>
""", unsafe_allow_html=True)

# ----------------------------
# 데이터베이스: 약, 성분, 주의사항
# ----------------------------
medicine_db = {
    "두통": {
        "약": ["타이레놀", "이부프로펜", "게보린"],
        "성분": ["아세트아미노펜", "이부프로펜", "카페인"],
        "주의사항": [
            "과량 복용 시 간 손상 위험이 있습니다.",
            "음주 전후에는 복용을 피하세요.",
            "공복에는 복용하지 마세요."
        ]
    },
    "기침": {
        "약": ["코푸시럽", "판피린티정", "브론서럽"],
        "성분": ["덱스트로메토르판", "구아이페네신", "디펜히드라민"],
        "주의사항": [
            "졸음을 유발할 수 있으니 운전 시 주의하세요.",
            "기침이 2주 이상 지속되면 의사 진료가 필요합니다."]
    },
    "콧물": {
        "약": ["클라리틴", "지르텍", "액티피드"],
        "성분": ["로라타딘", "세티리진", "클로르페니라민"],
        "주의사항": [
            "졸음을 유발할 수 있습니다.",
            "장기간 복용은 피하세요."
        ]
    },
    "속쓰림": {
        "약": ["겔포스", "스멕타", "오메프라졸"],
        "성분": ["알루미늄 하이드록사이드", "규산염", "오메프라졸"],
        "주의사항": [
            "식사 전 복용 시 효과가 좋습니다.",
            "위산 분비 억제제와 병용 시 주의하세요."
        ]
    },
    "근육통": {
        "약": ["탁센", "이부프로펜", "나프록센"],
        "성분": ["이부프로펜", "나프록센"],
        "주의사항": [
            "공복 복용을 피하세요.",
            "위장 장애가 있을 경우 의사와 상의하세요."
        ]
    },
    "열": {
        "약": ["타이레놀", "펜잘", "게보린"],
        "성분": ["아세트아미노펜"],
        "주의사항": [
            "4~6시간 간격으로 복용하세요.",
            "체온이 39도 이상 지속되면 병원 진료가 필요합니다."
        ]
    },
    "알레르기": {
        "약": ["지르텍", "클라리틴", "알레그라"],
        "성분": ["세티리진", "로라타딘", "페폭사티딘"],
        "주의사항": [
            "졸릴 수 있으므로 운전 전 복용은 피하세요.",
            "장기간 복용 시 의사 상담이 필요합니다."
        ]
    }
}

# ----------------------------
# AI 기반 증상 분류 (간단 예시)
# ----------------------------
def ai_classify_symptom(text):
    text = text.lower()
    if any(x in text for x in ["머리", "지끈", "두통", "편두통"]):
        return "두통"
    elif any(x in text for x in ["기침", "기침이", "목아파"]):
        return "기침"
    elif any(x in text for x in ["콧물", "코막힘", "비염"]):
        return "콧물"
    elif any(x in text for x in ["속쓰림", "위", "속이 쓰려"]):
        return "속쓰림"
    elif any(x in text for x in ["근육", "결림", "통증", "몸살"]):
        return "근육통"
    elif any(x in text for x in ["열", "체온", "뜨거워"]):
        return "열"
    elif any(x in text for x in ["알레르기", "재채기", "가렵"]):
        return "알레르기"
    else:
        return None

# ----------------------------
# 사용자 입력 섹션
# ----------------------------
st.markdown("---")
st.subheader("🩺 증상을 입력하세요:")
user_input = st.text_area("예: 머리가 지끈거리고 열이 나요", height=100, placeholder="여기에 증상을 적어주세요...")

# ----------------------------
# 버튼 섹션
# ----------------------------
if st.button("🔍 AI로 약 추천 받기"):
    if not user_input.strip():
        st.warning("⚠️ 증상을 입력해주세요.")
    else:
        predicted_symptom = ai_classify_symptom(user_input)

        if predicted_symptom:
            st.success(f"✅ AI가 인식한 증상: **{predicted_symptom}**")

            data = medicine_db[predicted_symptom]
            st.markdown(f"### 💊 추천 약 목록:")
            for med in data["약"]:
                st.markdown(f"""
                <div style='
                    background-color:#f9f9f9;
                    border-radius:12px;
                    padding:12px 18px;
                    margin:8px 0;
                    box-shadow:0 2px 5px rgba(0,0,0,0.1);
                '>
                <strong>💊 {med}</strong>
                </div>
                """, unsafe_allow_html=True)

            st.markdown(f"### 🧬 주요 성분:")
            st.markdown(", ".join(data["성분"]))

            st.markdown("### ⚠️ 복용 시 주의사항:")
            for note in data["주의사항"]:
                st.markdown(f"- {note}")
        else:
            st.error("❌ AI가 증상을 인식하지 못했습니다. 조금 더 구체적으로 적어주세요!")

# ----------------------------
# 푸터
# ----------------------------
st.markdown("""
<hr>
<p style='text-align:center; color:gray; font-size:14px;'>
Made with ❤️ using Streamlit · AI symptom classifier demo
</p>
""", unsafe_allow_html=True)
