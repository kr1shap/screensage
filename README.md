# **🌿 Screensage**  
---

## **Table of Contents**
- [Overview](#overview)
- [Tech Stack](#stack)
- [Set Up](#setup)
- [Contributions](#contributions)

---

## 🍃 Overview

<img width="245" alt="image" src="https://github.com/user-attachments/assets/08518807-7e4a-48cd-bab4-bca8b394f053" />

Screen Sage is a software designed to help both interviewers and interviewees with pre-screening interviews. 
The software takes a position/role a person is applying to, and generates questions to be during a pre-screening interview for the stated position. 
While running the program, five practice interview questions are generated by Cohere, and the user is prompted to type out their responses in the software. 
After the user answers all five questions, the software provides insightful and detailed feedback for each of the user's responses, along with a 'score' out of 100. 

As a result, interviewees can recieve feedback for what they can potentially improve on, and interviewers utilize the score/feedback generated to assess their candidacy. 
In fact, studies have shown that AI models can be trained to reason in a way that is less bias. In turn, this is a potential way to eliminate discriminatory biases during interview-like processes. 
Thus, interviewees can improve their responses for future applications (building confidence!), and the platform would be accessible for any company to use, helping smaller businesses within their hiring processes. 

---
## 🍀 Tech Stack
Front-end built with HTML, CSS. Utilized Flask for integrating Cohere's API. 

## 🌳 Set Up
### **1⃣ Clone the Repository**

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/screen-sage.git
cd screen-sage/server
```

### **2 Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4 Set Up Environment Variables**

Create a `.env` file inside the `server/` directory:

```ini
COHERE_API_KEY=your-cohere-api-key-here
```

Please make sure `.env` is **ignored** by Git by checking `.gitignore` !!

---

Once dependencies are installed, run:

```bash
python app.py
```

[or python3 depending on your version]. By default, the app runs at [**http://127.0.0.1:5000/**](http://127.0.0.1:5000/)

---
## Contributions

**By:** Parth Jairam, Aryan Patel, Michael Lee & Krisha



