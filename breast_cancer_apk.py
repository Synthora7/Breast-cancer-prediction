import streamlit as st
import joblib 




# Load the model
model = joblib.load('breast_cancer_model.pkl')

st.title('🎗️:red[_Breast Cancer Prediction_]')
# st.title("_Streamlit_ is :blue[cool] :ribbon:")

st.write("""
### Please provide the following information

""")


clump_thickness = st.slider("Clump Thickness (1-10)", 1, 10)
uniformity_cell_size = st.slider("Uniformity of Cell Size (1-10)", 1, 10)
uniformity_cell_shape = st.slider("Uniformity of Cell Shape (1-10)", 1, 10)
bare_nuclei = st.slider("Bare Nuclei (1-10)", 1, 10)
bland_chromatin = st.slider("Bland Chromatin (1-10)", 1, 10)
normal_nucleoli = st.slider("Normal Nucleoli (1-10)", 1, 10)


import time
if st.button("Predict"):
    with st.spinner("Predicting..."):
        time.sleep(2)   
        st.success("Prediction Ready ✅")


    pred = model.predict([[clump_thickness,
                            uniformity_cell_size,
                            uniformity_cell_shape,
                            bare_nuclei,
                            bland_chromatin,
                            normal_nucleoli]])

    # Result print karo
    if pred == 2:
        st.success("Prediction: Benign (Non-cancerous)")
        st.image("https://raw.githubusercontent.com/Synthora7/Breast-cancer-prediction/main/Benign.JPG
")
    else:
        st.warning("Prediction: Malignant (Cancerous)")
        st.image("Malignant.jpg")


st.sidebar.markdown("### ℹ️ About")
st.sidebar.info("This app helps in predicting Breast Cancer using ML.")

st.sidebar.markdown("#### 👨‍💻 Developed by [Pawan Kumar]")
st.sidebar.markdown('### Features Used')
st.sidebar.markdown('- Clump Thickness')
st.sidebar.markdown('- Uniformity of Cell Size')
st.sidebar.markdown('- Uniformity of Cell Shape')
st.sidebar.markdown('- Bare Nuclei')
st.sidebar.markdown('- Bland Chromatin')

st.sidebar.markdown('- Normal Nucleoli')


