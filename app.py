app.py
"""
Тест "Какой вы архетип?
"""

import streamlit as st
import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))

from scoring import (
    calculate_scores,
    get_top_3_archetypes,
    get_all_archetypes_with_scores,
    scores_to_percentages,
    analyze_profile_type
)

from visualization import (
    apply_custom_styles,
    show_test_header,
    show_start_button,
    show_question_with_options,
    display_result
)

st.set_page_config(
    page_title="🎭 Тест: Какой вы архетип?",
    page_icon="🎭",
    layout="centered",
    initial_sidebar_state="collapsed"
)

@st.cache_data
def load_json_data():
    try:
        with open("data/archetypes.json", "r", encoding="utf-8") as f:
            archetypes_data = json.load(f)
        
        with open("data/questions.json", "r", encoding="utf-8") as f:
            questions_data = json.load(f)
        
        return archetypes_data, questions_data
    
    except FileNotFoundError as e:
        st.error(f"❌ Файл не найден: {e}")
        st.stop()
    
    except json.JSONDecodeError as e:
        st.error(f"❌ Ошибка в JSON файле: {e}")
        st.stop()

def init_session_state():
    if 'test_started' not in st.session_state:
        st.session_state.test_started = False
    
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = []
    
    if 'test_finished' not in st.session_state:
        st.session_state.test_finished = False

def handle_answer_selection(selected_option_index):
    st.session_state.user_answers.append(selected_option_index)
    st.session_state.current_question += 1
    
    total_questions = 8
    if st.session_state.current_question >= total_questions:
        st.session_state.test_finished = True
    
    st.rerun()

def show_current_question(questions_data):
    current_idx = st.session_state.current_question
    total_questions = len(questions_data['questions'])
    
    question_data = questions_data['questions'][current_idx]
    
    selected_option = show_question_with_options(
        question_data,
        question_number=current_idx + 1,
        total_questions=total_questions
    )
    
    if selected_option is not None:
        handle_answer_selection(selected_option)

def calculate_and_display_results(archetypes_data, questions_data):
    scores = calculate_scores(
        st.session_state.user_answers,
        questions_data
    )
    
    top_3_list = get_top_3_archetypes(scores, archetypes_data)
    all_archetypes_list = get_all_archetypes_with_scores(scores, archetypes_data)
    percentages = scores_to_percentages(scores)
    profile_type = analyze_profile_type(scores)
    
    display_result(
        scores=scores,
        percentages=percentages,
        top_3_list=top_3_list,
        all_archetypes_list=all_archetypes_list,
        profile_type=profile_type
    )

def main():
    apply_custom_styles()
    archetypes_data, questions_data = load_json_data()
    init_session_state()
    
    if not st.session_state.test_started:
        show_test_header()
        show_start_button()
    
    elif not st.session_state.test_finished:
        show_current_question(questions_data)
    
    else:
        calculate_and_display_results(archetypes_data, questions_data)

if __name__ == "__main__":
    main()
