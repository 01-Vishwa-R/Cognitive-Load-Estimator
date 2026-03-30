
# 🧠 Cognitive Load Estimator

An AI-powered web application that predicts a student's cognitive load and provides personalized recommendations to improve learning efficiency.

---

## 📌 Overview

Cognitive Load refers to the amount of mental effort being used in the working memory while learning. This project uses Machine Learning to estimate three types of cognitive load:

- **Intrinsic Load** → Difficulty of the topic  
- **Extraneous Load** → Distractions and external factors  
- **Germane Load** → Learning effectiveness and understanding  

The system not only predicts these levels but also provides actionable recommendations and precautions to help students study more effectively.

---

## 🚀 Features

- 🤖 AI-based prediction of cognitive load  
- 📊 Classification into Low / Medium / High levels  
- 🧠 Explanation of each cognitive load type  
- 💡 Personalized study recommendations  
- ⚠️ Smart precautions to avoid burnout and distractions  
- 🌐 Interactive UI using Streamlit  

---

## 🛠️ Tech Stack

- **Python 3.11**
- **Pandas** – Data processing  
- **Scikit-learn** – Machine Learning model  
- **Joblib** – Model saving/loading  
- **Streamlit** – Web interface  

---

## 📂 Project Structure


<img width="809" height="263" alt="Screenshot 2026-03-30 232745" src="https://github.com/user-attachments/assets/94079ae1-a022-4d87-a6ed-3cbd4dd6ed34" />


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```git clone https://github.com/01-Vishwa-R/Cognitive-Load-Estimator.git```
```cd Cognitive-Load-Estimator```

### 2️⃣ Install dependencies

```pip install pandas scikit-learn streamlit joblib```

### 3️⃣ Train the model

```python models/train_model.py```

### 4️⃣ Run the application

```python -m streamlit run app/app.py```

### **5️⃣ Open in browser**

``http://localhost:8501``

---

## 🧪 How It Works

User inputs study-related parameters (e.g., study hours, sleep, distractions)

The trained ML model predicts:
   - Intrinsic Load
   - Extraneous Load
   - Germane Load

The system:
  - Explains what each load means
  - Generates personalized recommendations
  - Suggests precautions for better learning


---

## 🧠 Example Output

```Intrinsic: High```  
```Extraneous: High  ```
```Germane: Medium``` 

---

## 💡 Recommendations

- Reduce distractions
- Use Pomodoro technique
- Break topics into smaller parts

---

## ⚠️ Precautions

- Avoid multitasking
- Take regular breaks

---

## 🎯 Use Cases

- Students optimizing study habits
- EdTech platforms for adaptive learning
- Cognitive behavior analysis
- Academic workload management

---
## 📈 Future Improvements
- Real-time tracking using sensors or wearables
- Integration with learning platforms
- Advanced deep learning models
- Personalized dashboards and analytics

---

## 👨‍💻 Author

Vishwa R
- GitHub: https://github.com/01-Vishwa-R

## 📜 License

This project is for educational purposes.
