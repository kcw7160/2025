import streamlit as st

# MBTI별 직업 추천 데이터 (이모지 추가 버전)
mbti_jobs = {
    "INTJ": ["🧠 전략 기획자", "🔬 연구원", "📊 데이터 사이언티스트"],
    "INTP": ["💻 개발자", "📚 교수", "🧩 컨설턴트"],
    "ENTJ": ["👔 CEO", "⚖️ 변호사", "📈 경영 컨설턴트"],
    "ENTP": ["🚀 창업가", "📢 마케팅 전문가", "✍️ 작가"],
    "INFJ": ["💬 심리상담가", "🖋️ 작가", "🏫 교사"],
    "INFP": ["🎨 예술가", "📖 작가", "🤝 사회복지사"],
    "ENFJ": ["🌟 리더십 코치", "📚 교사", "🎤 홍보 담당자"],
    "ENFP": ["✨ 광고 기획자", "🎭 배우", "🎨 창의적 디자이너"],
    "ISTJ": ["📑 회계사", "📋 관리자", "🏛️ 공무원"],
    "ISFJ": ["🩺 간호사", "📖 교사", "🗂️ 행정직"],
    "ESTJ": ["📊 경영자", "🗂️ 프로젝트 매니저", "⚖️ 판사"],
    "ESFJ": ["🗣️ 상담사", "🩺 의료 종사자", "👥 HR 담당자"],
    "ISTP": ["⚙️ 엔지니어", "✈️ 파일럿", "🏋️ 스포츠 코치"],
    "ISFP": ["🎨 디자이너", "🎵 음악가", "🌿 치료사"],
    "ESTP": ["💼 영업 전문가", "📰 기자", "🚒 소방관"],
    "ESFP": ["🎤 배우", "🎉 이벤트 플래너", "🎬 연예 기획자"],
}

# 🌈 웹앱 꾸미기
st.set_page_config(page_title="MBTI 진로 추천", page_icon="✨", layout="centered")

# 🌟 제목 & 설명
st.markdown("""
# 🌈 MBTI 기반 진로 추천 웹앱 🎓✨
당신의 성격 유형(MBTI)에 딱 맞는 직업을 찾아보세요! 🚀  
**재미로 보는 진로 탐색** 🎉
""")

# 🎯 MBTI 선택
selected_mbti = st.selectbox("👉 당신의 MBTI를 선택하세요 👇", list(mbti_jobs.keys()))

# 🔮 추천 결과 출력
if selected_mbti:
    st.markdown(f"## 🧭 {selected_mbti} 유형의 추천 직업 ✨")
    st.write("당신의 성향에 딱 맞는 직업들이에요! 💡")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")

# 🎉 푸터
st.markdown("---")
st.markdown("🌟 **Tip:** 진로 선택은 MBTI 외에도 다양한 요소(흥미, 가치관, 능력)를 고려하는 게 좋아요! 🌟")
st.markdown("👩‍💻 Made with ❤️ using Streamlit")
