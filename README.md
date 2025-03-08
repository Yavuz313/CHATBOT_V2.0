### 📌 **Vistula University AI Assistant – Project Detailed Report**  

---

## **📍 1. PROJECT OVERVIEW & OBJECTIVE**  
This project is designed to develop an **AI-powered chatbot** for **Vistula University students**, helping them get **accurate and quick answers** regarding university-related queries.  

🔹 **Key Objectives:**  
✔️ Enable students to **access university information quickly**  
✔️ Enhance the **university support system** with AI automation  
✔️ Implement an **automated Q&A system** powered by AI  
✔️ Provide an **admin panel for easy data management**  
✔️ Improve **response quality by tracking AI accuracy**  

---

## **📍 2. TECHNICAL STACK**  
This project is built with **modern AI and data processing technologies** to ensure efficiency and reliability.  

| **Technology / Library** | **Purpose** |
|------------------|----------------------|
| **Streamlit** | User interface (Chatbot & Admin Panel) |
| **LangChain** | AI-based Q&A processing |
| **OpenAI GPT (Llama 3 Model)** | AI-powered response generation |
| **Tavily AI** | Web search for additional data |
| **ChromaDB** | Vector-based data retrieval |
| **Hugging Face Transformers** | Embedding model for vector-based matching |
| **RapidFuzz** | Measuring response accuracy |
| **dotenv** | Managing API keys securely |
| **Python JSON** | Storing and managing the Q&A dataset |

---

## **📍 3. PROJECT STRUCTURE & FILES**  
This project consists of **multiple AI-powered modules**, including a **chatbot system and an admin panel** for data management.  

📂 **Project Folder Structure:**  

```
📁 chatbot_v2
│── 📄 app.py                 → Chatbot user interface
│── 📄 admin_dashboard.py      → Admin panel for data management
│── 📄 qa_loader.py            → Q&A database management
│── 📄 rag_chain.py            → AI response processing and retrieval
│── 📄 auto_tester.py          → AI model accuracy testing
│── 📄 Q&A_cleaned.json        → Q&A dataset (Not included in this repository)
│── 📁 logs/                   → Test results and error logs
│── 📁 vistula_chroma/         → Vector database (Not included in this repository)
│── 📄 .env                    → API keys (Excluded for security reasons)
```
📌 **Due to privacy concerns regarding university-related data, some essential files, including Q&A datasets and vector database files, are not included in this repository.**  

---

## **📍 4. DETAILED ANALYSIS OF PROJECT MODULES**  

### **🟢 4.1. Chatbot System (`app.py`)**
📌 **Purpose:**  
- Enables users to **ask questions** and generates **AI-powered responses**.  
- Maintains a **conversation history** for better user experience.  
- Includes a **sidebar menu for navigating to the admin panel**.  

✅ **Key Features:**  
✔️ **Automated Q&A processing** (AI-based)  
✔️ **Maintains conversation history**  
✔️ **User-friendly interface with admin panel access**  

---

### **🔵 4.2. Admin Panel (`admin_dashboard.py`)**
📌 **Purpose:**  
- Allows **administrators to manage the Q&A database**.  
- **Fix incorrect responses** and **add new questions** to the dataset.  
- Displays **AI performance metrics for accuracy tracking**.  

✅ **Key Features:**  
✔️ **Edit and update database** (Add/Modify Q&A)  
✔️ **Analyze AI response accuracy**  
✔️ **Easily accessible via the sidebar menu**  

---

### **🟠 4.3. Data Management (`qa_loader.py`)**
📌 **Purpose:**  
- Reads **Q&A data from JSON files** and **loads them into a vector database**.  
- Uses **Hugging Face embeddings** to **convert text into vectors** for efficient retrieval.  
- Stores **vectorized Q&A pairs in ChromaDB** for quick searches.  

✅ **Key Features:**  
✔️ **Fast Q&A retrieval via vector database**  
✔️ **Efficient AI data structuring with ChromaDB**  

---

### **🟣 4.4. AI Response Processing (`rag_chain.py`)**
📌 **Purpose:**  
- Processes user questions and **retrieves relevant answers**.  
- **Searches the database first**, then queries AI **if no match is found**.  
- Optionally uses **web search (Tavily AI)** for extended answers.  

✅ **Key Features:**  
✔️ **Prioritizes internal database over AI guesses**  
✔️ **Web search fallback for missing data**  
✔️ **AI-generated responses based on verified knowledge**  

---

### **🟡 4.5. AI Performance Testing (`auto_tester.py`)**
📌 **Purpose:**  
- Tests **AI-generated responses** for accuracy.  
- Compares AI-generated answers **against the correct responses**.  
- Logs results in **admin panel for further analysis**.  

✅ **Key Features:**  
✔️ **Uses RapidFuzz to measure response accuracy**  
✔️ **Automatically tracks AI performance**  

---

## **📍 5. PROJECT SUCCESS & FUTURE IMPROVEMENTS**  
✅ **AI was trained with university-specific data and achieved high accuracy.**  
✅ **Admin panel allows real-time updates to the Q&A dataset.**  
✅ **Automated testing system ensures AI accuracy.**  
✅ **Live chatbot delivers fast and relevant responses to students.**  

🚀 **This project successfully provides an AI-powered knowledge assistant for universities!** 🔥🔥🔥  

### **🔮 Future Improvements:**  
🔹 **Fine-tune the AI model for better natural responses.**  
🔹 **Implement more advanced embeddings for improved accuracy.**  
🔹 **Enhance the admin panel with analytics and insights.**  
🔹 **Integrate an email or feedback system for better user engagement.**  

---

📌 **Note:** Due to privacy concerns, **some essential files such as Q&A datasets and vector database files are not included in this repository**. If you are a collaborator and require access, please contact the project administrator.  

🚀 **If you have any questions or want to contribute, feel free to reach out!** 🔥🔥🔥
