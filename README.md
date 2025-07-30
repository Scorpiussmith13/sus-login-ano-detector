# 🔐 Suspicious Login Anomaly Detector

This project detects suspicious or anomalous login behavior using an unsupervised learning approach. It is ideal for early-stage intrusion detection systems and cybersecurity monitoring.

## 🚀 Features

- ✅ Unsupervised Anomaly Detection
- ⏱️ Temporal Features (login time, frequency)
- 🌐 Location & Network Analysis (IP, region)
- 📱 Device Fingerprinting
- 🔄 Behavioral Pattern Analysis
- 📊 Model Evaluation Metrics (Precision, Recall, F1)

## 🧠 Algorithms Used

- Autoencoder
- Isolation Forest
- Ensemble Voting

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Scorpiussmith13/sus-login-ano-detector.git
cd sus-login-ano-detector
2. Create Virtual Environment (Optional but Recommended)

python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # macOS/Linux


3. Install Dependencies
pip install -r requirements.txt


4. Run Model / Notebook
python src/train_model.py
# or open and run notebooks/model_testing.ipynb


## 📌 To Do

- [x] Upload code and results to GitHub
- [x] Add `.gitignore` to exclude `venv/`
- [x] Create professional `README.md`
- [ ] Deploy model as REST API using FastAPI
- [ ] Add Prometheus & Grafana for live monitoring
- [ ] Migrate to advanced dataset (e.g., BETH dataset)
- [ ] Improve feature engineering for device fingerprinting
- [ ] Dockerize the app for production deployment

## 📄 License

This project is currently not licensed for public use. Please contact the author for permissions or intended use.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

🙋‍♂️ Author
Sourasish Das
TCS | Information Security | Aspiring AI Security Engineer
GitHub