import random
import streamlit as st

# Fungsi untuk membuat soal linear
def generate_linear_equation():
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    x = random.randint(-10, 10)
    c = a * x + b
    return f"{a}x + ({b}) = {c}", x

# Inisialisasi state
if 'questions' not in st.session_state:
    st.session_state.questions = [generate_linear_equation() for _ in range(5)]
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = [False] * 5

# Judul aplikasi
st.title("🧠 Teka-Teki Matematika Aljabar Linear")
st.markdown("Tebak nilai **x** dari persamaan berikut. Total 5 soal!")

# Ambil soal sekarang
current = st.session_state.current_question
if current < 5:
    soal, jawaban = st.session_state.questions[current]
    st.subheader(f"Soal {current + 1} dari 5:")
    st.latex(soal.replace("x", "x"))

    # Input jawaban
    user_answer = st.number_input("Masukkan nilai x:", step=1, format="%d", key=f"answer_{current}")

    # Tombol submit
    if st.button("Cek Jawaban", key=f"submit_{current}") and not st.session_state.answered[current]:
        if user_answer == jawaban:
            st.success("✅ Benar!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Salah! Jawaban yang benar: {jawaban}")
        st.session_state.answered[current] = True

    # Tombol soal selanjutnya
    if st.session_state.answered[current]:
        if st.button("Soal Selanjutnya ➡️"):
            st.session_state.current_question += 1
else:
    st.success(f"🎉 Permainan selesai! Skor akhir kamu: {st.session_state.score} / 5")

    # Tombol ulangi permainan
    if st.button("🔄 Main Lagi"):
        st.session_state.questions = [generate_linear_equation() for _ in range(5)]
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answered = [False] * 5