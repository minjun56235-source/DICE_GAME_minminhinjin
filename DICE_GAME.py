import streamlit as st
import random
import time

# --- Page Configuration ---
st.set_page_config(page_title="Pastel Dice Game", page_icon="🎲", layout="centered")

# --- Custom CSS for Pastel Theme ---
st.markdown("""
    <style>
    .main {
        background-color: #fdf6f0;
    }
    .stButton>button {
        background-color: #ffcfdf;
        color: #4b4b4b;
        border-radius: 12px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #fdbccf;
        border: none;
    }
    .dice-container {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .score-text {
        color: #8bbabb;
        font-size: 24px;
        font-weight: bold;
    }
    h1, h2, h3 {
        color: #6d6d6d;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Session State Initialization ---
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'last_dice' not in st.session_state:
    st.session_state.last_dice = None
if 'message' not in st.session_state:
    st.session_state.message = ""
if 'message_type' not in st.session_state:
    st.session_state.message_type = "info"

# --- Header ---
st.title("🎲 파스텔 주사위 맞추기")
st.write("1부터 6 사이의 숫자를 맞혀보세요!")

# --- Score Display ---
st.markdown(f"<p class='score-text'>현재 점수: {st.session_state.score}</p>", unsafe_allow_html=True)

# --- Game Logic ---
with st.container():
    st.markdown("<div class='dice-container'>", unsafe_allow_html=True)
    
    # User Input
    user_guess = st.number_input("당신의 선택은?", min_value=1, max_value=6, step=1, key="guess_input")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("주사위 던지기!"):
            # Simulate rolling animation
            with st.spinner('주사위가 구르는 중...'):
                time.sleep(0.5)
                dice_result = random.randint(1, 6)
                st.session_state.last_dice = dice_result
                
                if user_guess == dice_result:
                    st.session_state.score += dice_result
                    st.session_state.message = f"축하합니다! 정답입니다! 주사위 눈이 {dice_result}이(가) 나와서 {dice_result}점을 얻었습니다."
                    st.session_state.message_type = "success"
                else:
                    st.session_state.score -= dice_result
                    st.session_state.message = f"아쉬워요! 주사위 눈은 {dice_result}였습니다. {dice_result}점이 감점되었습니다."
                    st.session_state.message_type = "error"
    
    with col2:
        if st.button("점수 초기화"):
            st.session_state.score = 0
            st.session_state.message = "점수가 초기화되었습니다."
            st.session_state.message_type = "info"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# --- Feedback Section ---
if st.session_state.last_dice:
    st.subheader(f"지난 결과: {st.session_state.last_dice}")
    if st.session_state.message_type == "success":
        st.success(st.session_state.message)
    elif st.session_state.message_type == "error":
        st.error(st.session_state.message)
    else:
        st.info(st.session_state.message)

# --- Instructions ---
with st.expander("게임 방법"):
    st.write("""
    1. 1부터 6까지의 숫자 중 하나를 입력합니다.
    2. '주사위 던지기!' 버튼을 누릅니다.
    3. 숫자를 맞히면 주사위 눈금만큼 점수를 얻고, 틀리면 그만큼 점수를 잃습니다.
    """)
