📌 Hidden Markov Model for POS Tagging
📖 Overview

This project implements a Hidden Markov Model (HMM) to perform Part-of-Speech (POS) tagging in Natural Language Processing (NLP). The model predicts the most probable sequence of POS tags for a given input sentence using probabilistic methods.

The system is built using Python and deployed with a Flask web interface, allowing users to input sentences and view predicted tags interactively.

🎯 Aim

To develop an HMM-based system that:

Analyzes sequential data
Infers hidden states (POS tags)
Computes the most probable tag sequence using the Viterbi Algorithm
🧠 Key Concepts
Hidden States → POS tags (Noun, Verb, etc.)
Observed Data → Words in a sentence
Transition Probability → Probability of tag given previous tag
Emission Probability → Probability of word given a tag
Viterbi Algorithm → Finds the most probable sequence of hidden states
📂 Dataset
File: corpus.txt
Format: word/tag

Example:

I/Pronoun love/Verb NLP/Noun
She/Pronoun eats/Verb rice/Noun
Features:
Synthetic dataset
Covers common grammar structures
Includes tags like:
Noun, Verb, Pronoun, Adjective, Adverb, Determiner
⚙️ Technologies Used
Python → Core implementation
Flask → Web framework
HTML & CSS → Frontend UI
collections.defaultdict → Data structures for probabilities
🔄 Workflow / Methodology
1. Data Preprocessing
Load dataset
Split into word-tag pairs
2. Model Training
Compute:
Emission probabilities
Transition probabilities
Start probabilities
3. Probability Normalization
Convert counts into valid probabilities
4. Viterbi Algorithm
Dynamic programming approach
Finds top probable POS sequences
5. Web Integration
User inputs sentence
Model predicts tags
Results displayed on webpage
🚀 Features
Predicts POS tags for any sentence
Displays:
Best tag sequence
Probability of prediction
Comparison with alternative paths
Interactive web interface
📊 Output Example

Input:

I love NLP

Output:

I → Pronoun  
love → Verb  
NLP → Noun  

Also shows probability comparison:

Path 1 → Best
Path 2 → Alternative
📁 Project Structure
├── app.py                # Flask application
├── corpus.txt           # Training dataset
├── templates/
│   └── index.html       # Frontend UI
├── static/
│   └── styles.css       # Styling
├── hmm_model.py         # HMM logic (optional separation)
└── README.md
▶️ How to Run
1. Clone the Repository
git clone <your-repo-link>
cd <project-folder>
2. Install Dependencies
pip install flask
3. Run the Application
python app.py
4. Open in Browser
http://127.0.0.1:5000/
📈 Results

<img width="871" height="604" alt="Screenshot 2026-04-02 at 1 42 33 PM" src="https://github.com/user-attachments/assets/ee053866-c632-4e27-9ab6-581d98b9f7f8" />

Successfully predicts POS tags using HMM
Displays best sequence with probability
Compares multiple possible paths for accuracy

(Sample UI output is shown on page 10 of the report)

🧾 Conclusion

This project demonstrates how Hidden Markov Models can effectively model sequential data in NLP. By combining probabilistic reasoning with dynamic programming (Viterbi), the system accurately predicts POS tags without relying on predefined grammar rules.

🔮 Future Enhancements
Use large real-world datasets (e.g., Penn Treebank)
Apply smoothing techniques
Improve accuracy with advanced models (CRF, BiLSTM)
Add REST API support
👨‍💻 Contributors
S. Sunil
T. Saketh
T. Sai Sanjay
U. Geetika
V. Raju
Y. Hansika
Y. Maneesha
Y. Ganesh Kumar
Y. Praveen Bhagavan
📜 License

This project is for academic purposes
