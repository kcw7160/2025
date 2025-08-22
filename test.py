import streamlit as st

# 제목
st.title("📚 감정 기반 문학 인용구 추천")
st.write("감정을 선택하면 그에 맞는 문학 구절을 추천해드립니다.")

# 카테고리별 색상과 이모지
category_info = {
    "희": {"color": "#FFD700", "emoji": "😊"}, 
    "노": {"color": "#FF4500", "emoji": "😡"},  
    "애": {"color": "#1E90FF", "emoji": "😢"}, 
    "락": {"color": "#FF69B4", "emoji": "❤️"} 
}

# 감정 목록
emotions = {
    "희": ["기쁨", "행복", "감사", "안도", "자부심", "만족", "감격", "즐거움", "희망", "편안"],
    "노": ["분노", "짜증", "억울", "실망", "질투", "좌절", "불만", "화남", "격분", "모욕감"],
    "애": ["슬픔", "우울", "그리움", "후회", "외로움", "상실감", "실의", "눈물", "비애", "고독"],
    "락": ["사랑", "연정", "설렘", "열정", "로맨스", "매혹", "호감", "달콤함", "기대", "열망"]
}

# 전체 감정 리스트
all_emotions = sum(emotions.values(), [])

# 감정별 문학 구절 (예시: 미상 구절)
quotes = {emotion:[f"{emotion}에 맞는 문학 구절 1", f"{emotion}에 맞는 문학 구절 2"] for emotion in all_emotions}

# 감정 선택 UI (컬럼 4개)
st.subheader("오늘의 감정을 선택하세요:")
cols = st.columns(4)
selected_emotion = None
for i, emotion in enumerate(all_emotions):
    col = cols[i % 4]
    category = next((k for k, v in emotions.items() if emotion in v), None)
    emoji = category_info[category]["emoji"]
    if col.button(f"{emoji} {emotion}", key=f"{emotion}_{i}"):
        selected_emotion = emotion

# 선택된 감정 출력
if selected_emotion and selected_emotion in quotes:
    category = next((k for k, v in emotions.items() if selected_emotion in v), None)
    color = category_info[category]["color"]
    emoji = category_info[category]["emoji"]
    st.markdown(f"<h2 style='color:{color}'>{emoji} {selected_emotion} 감정에 맞는 문학 구절:</h2>", unsafe_allow_html=True)
    for quote in quotes[selected_emotion]:
        st.markdown(
            f"""
            <div style='background-color:{color}; 
                        color:white;
                        padding:15px; 
                        border-radius:10px; 
                        box-shadow: 3px 3px 10px rgba(0,0,0,0.2);
                        margin-bottom:10px;
                        font-size:16px;'>{quote}</div>
            """, unsafe_allow_html=True
        )
