# app.py
import random
import textwrap
import streamlit as st

st.set_page_config(page_title="문학 인용구 추천기", page_icon="📚", layout="centered")

# -----------------------------
# 감정 선택지 확장
# -----------------------------
ALL_EMOTIONS = [
    "기쁨","즐거움","희망","설렘","감동","감사","사랑","평온","만족","열정","자부심","흥미",
    "슬픔","그리움","외로움","허무","분노","불안","공포","죄책감","후회","절망","혼란","좌절",
    "향수","놀람","경외","연민","위로","성찰","결의","기대","지루함","해방감"
]

# -----------------------------
# 간단한 예시 데이터 (실제 사용 시 더 많이 추가)
# -----------------------------
QUOTES = [
    {"text": "죽는 날까지 하늘을 우러러 한 점 부끄럼이 없기를...", "author": "윤동주", "work": "서시", "era": "현대시", "emotion": ["희망","성찰"]},
    {"text": "나 보기가 역겨워 가실 때에는 말없이 고이 보내 드리오리다.", "author": "김소월", "work": "진달래꽃", "era": "현대시", "emotion": ["그리움","슬픔"]},
    {"text": "밤이 깊을수록 별은 더 또렷하다.", "author": "속담", "work": "민간어록", "era": "통속", "emotion": ["위로","희망"]},
    {"text": "꽃이 피면 지는 것이 자연의 이치거늘, 지는 것 또한 꽃이니 서러워 말지어다.", "author": "고전 어구", "work": "고전 정서", "era": "고전", "emotion": ["허무","위로"]},
]

# -----------------------------
# 함수
# -----------------------------
def pick_quotes(emotion: str):
    cand = [q for q in QUOTES if emotion in q["emotion"]]
    random.shuffle(cand)
    return cand

def format_quote(q):
    wrapped = textwrap.fill(q["text"], width=30)
    meta = f"— {q['author']} 〈{q['work']}〉 · {q['era']}"
    return wrapped, meta

# -----------------------------
# 메인 화면
# -----------------------------
st.title("📚 문학 인용구 추천기")
st.caption("감정을 선택하면 그 정서와 어울리는 문학 구절을 추천합니다.")

# ✅ 감정을 객관식 선택 (드롭다운으로 확장)
chosen_emotion = st.selectbox("감정을 선택하세요", ALL_EMOTIONS)

st.subheader(f"✨ {chosen_emotion}에 어울리는 구절")

pool = pick_quotes(chosen_emotion)

if not pool:
    st.info("해당 감정과 직접 연결된 인용구가 없어 무작위 추천을 드립니다.")
    q = random.choice(QUOTES)
else:
    q = random.choice(pool)

wrapped, meta = format_quote(q)
st.markdown(f"> {wrapped}")
st.caption(meta)
