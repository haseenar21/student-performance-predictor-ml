import joblib
import streamlit as st
import pandas as pd

model = joblib.load("performance_model.pkl")
df = pd.read_csv("StudentPerformanceFactors.csv")

st.set_page_config(page_title = "STUDENT PERFORMANCE PREDICTOR", layout = "wide")

col1, col2 = st.columns([3, 1])
with col1:
    st.title("Student Exam Score Predictor")
    st.write("PREDICT THE SCORE HERE : ")

with col2:
    st.write("📊 Dataset Size: 6,670")
    st.write("🎯 Best R² Score: 0.76")
    st.write("🤖 Best Model: Ridge Regression")
# st.write("📊Dataset Size:6,670   🎯Best R² Score:0.76   🤖Best Model:Ridge Regression")

col1, col2 = st.columns(2)

with col1:
    top_row = st.container(border=True)

    with top_row:
        st.header("📚 Academic Information")
        hours_studied = st.slider("📚 Hours Studied", 0, 50, 10)
        attendance = st.slider("🏫 Attendance (%)", 0, 100, 75)
        previous_scores = st.number_input("📝 Previous Scores", 0, 100, 70)
        tutoring_sessions = st.number_input("👨‍🏫 Tutoring Sessions", 0, 20, 2)

    bottom_row = st.container(border=True)

    with bottom_row:
        st.header("🧠 Student Lifestyle")
        sleep_hours = st.slider("😴 Sleep Hours", 0, 12, 7)
        physical_activity = st.number_input("🏃 Physical Activity", 0, 20, 3)
        motivation_level = st.segmented_control("Motivation Level", ["Low", "Medium", "High"],default="Low")
        extracurricular_activities = st.selectbox("🥅 Extracurricular Activities",["Yes","No"])
        learning_disabilities = st.checkbox("Learning Disabilities",["Yes","No"])
        gender = st.radio("Gender",["Male","Female"],horizontal=True)
        peer_influence = st.selectbox("Peer Influence",["Positive","Negative","Neutral"])
        
        

with col2:
    top_row = st.container(border=True)
    

    with top_row:
        st.header("🏫 School Environment")
        school_type = st.radio("🏫 School Type", ["Public", "Private"],horizontal=True)
        internet_access = st.checkbox("🌐 Internet Access",["Yes","No"])
        teacher_quality = st.selectbox("👩🏻‍🏫 Teacher Quality", ["High", "Medium", "Low"])
        access_to_resources = st.radio("📚 Access to Resources", ["High", "Medium", "Low"])
    
    bottom_row = st.container(border=True)
    with bottom_row:
        st.header("🏠 Family & Home Environment")
        parental_involvement = st.segmented_control("Parental Involvement", ["Low", "Medium", "High"],default="Medium")
        family_income = st.radio("Family Income",["Low", "Medium", "High"])
        parental_education = st.selectbox("Parental Education Level",["High School", "College", "Postgraduate"])
        distance_from_home = st.segmented_control("Distance from Home",["Near", "Moderate", "Far"],default="Moderate")


predict_btn = st.button("PREDICT YOUR SCORE",use_container_width=True)
if predict_btn:
    input_dict ={
        "Hours_Studied": hours_studied,
        "Attendance": attendance,
        "Previous_Scores": previous_scores,
        "Access_to_Resources": access_to_resources,
        "Extracurricular_Activities": extracurricular_activities,
        "Sleep_Hours": sleep_hours,
        "Parental_Involvement": parental_involvement,
        "Motivation_Level": motivation_level,
        "Internet_Access": internet_access,
        "Tutoring_Sessions": tutoring_sessions,
        "Family_Income": family_income,
        "Teacher_Quality": teacher_quality,
        "School_Type": school_type,
        "Physical_Activity": physical_activity,
        "Learning_Disabilities": learning_disabilities,
        "Parental_Education_Level": parental_education,
        "Distance_from_Home": distance_from_home,
        "Gender": gender,
        "Peer_Influence": peer_influence
    }

    input_data = pd.DataFrame([input_dict])

    prediction = model.predict(input_data)
    score = int(prediction[0])

    if score >= 85:
        label = "🔥 Excellent Performance"
        emoji = "🟢"
    elif score >= 70:
        label = "👍 Good Performance"
        emoji = "🟡"
    else:
        label = "⚠️ Needs Improvement"
        emoji = "🔴"

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown(f"# 🎯 {score}")
        st.markdown(f"## {emoji} {label}")
        st.progress(score)
        st.markdown("---")

    profile_df =pd.DataFrame({
        "Feature": list(input.keys()),
        "Value": list(input.values())
    })
    st.subheader("📊 Your Performance Profile")
    st.bar_chart(profile_df.set_index("Feature"),horizontal=True,height=500)