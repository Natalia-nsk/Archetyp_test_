src/visualization.py
"""
Модуль визуализации результатов теста
"""

import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #000000;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
    }
    
    .stApp {
        background: linear-gradient(135deg, #2D1B69 0%, #1A0F3D 100%);
    }
    
    .main-title {
        color: #FFFFFF;
        text-align: center;
        font-size: 48px;
        font-weight: 700;
        margin: 40px 0;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }
    
    .result-card {
        background: #FFFFFF;
        border-radius: 20px;
        padding: 40px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    .archetype-icon-large {
        font-size: 100px;
        text-align: center;
        margin: 20px 0;
    }
    
    .top-archetype {
        display: flex;
        align-items: center;
        padding: 20px;
        margin: 15px 0;
        background: #F8F9FA;
        border-radius: 15px;
        animation: slideInRight 0.5s ease-out;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(100px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .archetype-icon-small {
        font-size: 40px;
        margin-right: 20px;
    }
    
    .archetype-name {
        font-size: 28px;
        font-weight: 700;
        text-transform: uppercase;
        flex-grow: 1;
    }
    
    .archetype-percentage {
        font-size: 32px;
        font-weight: 700;
        color: #2D1B69;
    }
    
    .other-archetypes {
        text-align: right;
        margin-top: 30px;
        padding: 20px;
        background: #F8F9FA;
        border-radius: 15px;
    }
    
    .other-archetype-item {
        display: inline-block;
        margin: 5px 15px;
        font-size: 16px;
        color: #666;
    }
    
    .divider {
        border-top: 2px solid #E0E0E0;
        margin: 30px 0;
    }
    
    .stProgress > div > div > div > div {
        background-color: #2D1B69;
    }
    
    .stButton > button {
        background-color: #FFFFFF;
        border: 3px solid #2D1B69;
        border-radius: 15px;
        color: #2D1B69;
        font-weight: 600;
        font-size: 18px;
        padding: 15px 30px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #2D1B69;
        color: #FFFFFF;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(45, 27, 105, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

def show_question_with_options(question_data, question_number, total_questions):
    progress = question_number / total_questions
    st.progress(progress)
    st.markdown(f"<p style='color: #FFFFFF; text-align: center;'>Вопрос {question_number} из {total_questions}</p>", 
                unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='result-card'>
        <h3 style='text-align: center; margin-bottom: 30px;'>{question_data['text']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    for i, option in enumerate(question_data['options']):
        letter = chr(65 + i)
        
        col1, col2, col3 = st.columns([1, 6, 1])
        with col2:
            button_label = f"{letter}. {option['text']}"
            
            if st.button(
                button_label,
                key=f"q{question_number}_opt{i}",
                use_container_width=True
            ):
                return i
    
    return None

def show_result_header():
    st.markdown("""
    <h1 class='main-title'>Какой у тебя архетип?</h1>
    """, unsafe_allow_html=True)

def show_primary_archetype(archetype_data, percentage):
    st.markdown("<div class='result-card'>", unsafe_allow_html=True)
    
    st.markdown(f"<div class='archetype-icon-large'>{archetype_data['icon']}</div>", 
                unsafe_allow_html=True)
    
    st.markdown(f"<h2 style='text-align: center;'>ВАШ ВЕДУЩИЙ АРХЕТИП</h2>", 
                unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center; color: #2D1B69; margin-top: 10px;'>{archetype_data['name'].upper()}</h1>", 
                unsafe_allow_html=True)
    
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    
    st.markdown(f"**{archetype_data['description']}**")
    st.markdown("<br>", unsafe_allow_html=True)
    
    traits_text = ", ".join(archetype_data['traits'])
    st.markdown(f"*{traits_text}*")
    
    st.markdown("</div>", unsafe_allow_html=True)

def show_profile_dual(archetype1_data, percentage1, archetype2_data, percentage2):
    st.markdown("<div class='result-card'>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center;'>ВАШ ПРОФИЛЬ</h2>", 
                unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>У вас многогранная личность, сочетающая черты нескольких архетипов</p>", 
                unsafe_allow_html=True)
    
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    
    st.markdown(f"### {archetype1_data['icon']} {archetype1_data['name'].upper()} ({percentage1}%)")
    st.markdown(f"*{archetype1_data['description']}*")
    st.markdown(f"**Черты:** {', '.join(archetype1_data['traits'])}")
    
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    
    st.markdown(f"### {archetype2_data['icon']} {archetype2_data['name'].upper()} ({percentage2}%)")
    st.markdown(f"*{archetype2_data['description']}*")
    st.markdown(f"**Черты:** {', '.join(archetype2_data['traits'])}")
    
    st.markdown("</div>", unsafe_allow_html=True)

def show_top_3_animated(top_3_list, percentages):
    st.markdown("<div class='result-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; margin-bottom: 30px;'>ВАШ ТОП-3 АРХЕТИПА</h3>", 
                unsafe_allow_html=True)
    
    for i, (archetype_data, score) in enumerate(top_3_list[:3]):
        percentage = percentages[archetype_data['id']]
        delay = i * 0.3
        
        st.markdown(f"""
        <div class='top-archetype' style='animation-delay: {delay}s;'>
            <span class='archetype-icon-small'>{archetype_data['icon']}</span>
            <span class='archetype-name'>{archetype_data['name'].upper()}</span>
            <span class='archetype-percentage'>({percentage}%)</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def show_other_archetypes_sidebar(all_archetypes_list, percentages, top_3_ids):
    st.markdown("<div class='other-archetypes'>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: 600; margin-bottom: 15px;'>ОСТАЛЬНЫЕ АРХЕТИПЫ:</p>", 
                unsafe_allow_html=True)
    
    other_archetypes = [
        (arch_data, score) for arch_data, score in all_archetypes_list 
        if arch_data['id'] not in top_3_ids and score > 0
    ]
    
    mid_point = len(other_archetypes) // 2
    
    row1_html = ""
    for arch_data, score in other_archetypes[:mid_point]:
        percentage = percentages[arch_data['id']]
        row1_html += f"<span class='other-archetype-item'>{arch_data['name']} ({percentage}%)</span>"
    
    st.markdown(row1_html, unsafe_allow_html=True)
    
    row2_html = ""
    for arch_data, score in other_archetypes[mid_point:]:
        percentage = percentages[arch_data['id']]
        row2_html += f"<span class='other-archetype-item'>{arch_data['name']} ({percentage}%)</span>"
    
    st.markdown(row2_html, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def display_result(scores, percentages, top_3_list, all_archetypes_list, profile_type):
    show_result_header()
    
    if profile_type == "focused":
        primary_arch, primary_score = top_3_list[0]
        primary_percentage = percentages[primary_arch['id']]
        show_primary_archetype(primary_arch, primary_percentage)
    
    elif len(top_3_list) >= 2 and top_3_list[0][1] == top_3_list[1][1]:
        arch1, score1 = top_3_list[0]
        arch2, score2 = top_3_list[1]
        perc1 = percentages[arch1['id']]
        perc2 = percentages[arch2['id']]
        show_profile_dual(arch1, perc1, arch2, perc2)
    
    else:
        primary_arch, primary_score = top_3_list[0]
        primary_percentage = percentages[primary_arch['id']]
        show_primary_archetype(primary_arch, primary_percentage)
    
    show_top_3_animated(top_3_list, percentages)
    
    top_3_ids = [arch_data['id'] for arch_data, _ in top_3_list[:3]]
    show_other_archetypes_sidebar(all_archetypes_list, percentages, top_3_ids)

def show_test_header():
    st.markdown("""
    <div style='text-align: center; padding: 60px 20px;'>
        <h1 style='color: #FFFFFF; font-size: 56px; margin-bottom: 20px;'>
            🎭 Какой у тебя архетип?
        </h1>
        <p style='color: #FFFFFF; font-size: 24px; opacity: 0.9;'>
            Ответьте на 8 вопросов и узнайте свой архетип личности
        </p>
    </div>
    """, unsafe_allow_html=True)

def show_start_button():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎯 НАЧАТЬ ТЕСТ", use_container_width=True, type="primary"):
            st.session_state['test_started'] = True
            st.rerun()
