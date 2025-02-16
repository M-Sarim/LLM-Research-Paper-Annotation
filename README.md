# 📌 LLM Research Paper Annotation  
**Automating research paper classification using Large Language Models (LLMs) and web scraping**   

## 🚀 Project Overview  
This project automates **research paper annotation** by:  
✅ Scraping research papers from **NeurIPS**  
✅ Using **LLMs (OpenAI GPT-4 / Google Gemini)** to classify papers  
✅ Storing the **category labels** in a structured dataset  

🔗 **Live Blog Post:** [Medium Post Here]  
🔗 **GitHub Repository:** [Repo Link Here]  

---

## 🛠️ Tech Stack  
- **Python** (Web Scraping, API Calls, Data Processing)  
- **BeautifulSoup** (Extracting research paper data)  
- **Google Gemini API** (LLM-powered annotation)    

---

## 📂 Repository Structure  
LLM-Research-Paper-Annotation/ │── 📄 README.md # Project Overview
│── 📄 .gitignore # Ignore unnecessary files
│── 📄 scraper.py # Scrapes NeurIPS research papers
│── 📄 annotate.py # Uses LLM to classify papers
│── 📄 dataset.csv # Scraped data (Title, Abstract)
│── 📁 blog/ # Blog post draft

---

## 📌 How It Works  
### **1️⃣ Scrape Research Papers**  
Run the scraper to fetch **titles & abstracts** from NeurIPS:  
python scraper.py
This generates dataset.csv.

2️⃣ Annotate Papers Using LLMs
Run the annotation script to classify papers:

python annotate.py
This generates annotated_dataset.csv with category labels.

3️⃣ Analyze Results
Use Jupyter Notebook to visualize classification distribution:

jupyter notebook analysis.ipynb
📊 Sample Dataset
Title	Abstract	Category
Deep Learning for XYZ	This paper explores...	Deep Learning
NLP Techniques for ABC	In this work, we...	NLP
🔍 Installation & Setup
1️⃣ Clone the Repository

git clone https://github.com/M-Sarim/LLM-Research-Paper-Annotation.git
cd LLM-Research-Paper-Annotation

3️⃣ Set Up API Key
Create a .env file and add your GEMINI API Key:

API_KEY=your_api_key_here

🚀 Future Improvements
✅ Fine-tune a custom LLM for better accuracy
✅ Expand categories for finer classification
✅ Build a web app for real-time classification

📜 License
This project is licensed under the MIT License.

🤝 Contributing
Feel free to open issues & pull requests! 🎯

📬 Contact
👤 Muhammad Sarim
📧 muhammad2004sarim@gmail.com

