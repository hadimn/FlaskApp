## 🐦 Flask Twitter Scraper & Analyzer

This Flask web application scrapes, analyzes, and visualizes tweets using the `snscrape` library.

### 🔍 Features

* **Tweet scraping** via [snscrape](https://github.com/JustAnotherArchivist/snscrape) without needing official Twitter API credentials.
* **Data analysis** of tweet content:

  * Extracts metadata (timestamp, username, likes, replies, retweets).
  * Performs basic sentiment analysis or frequency counts.
* **Visualization**, such as bar charts or time series (likely using libraries like Plotly, Matplotlib, or Seaborn).
* **Web interface** built with Flask:

  * Input form for specifying search terms, dates, and tweet limits.
  * Results pages with tables and embedded charts.

### 📁 Repository Structure

```
├── app.py             # Main Flask application: routes and views
├── requirements.txt   # Python dependencies
├── Procfile           # For deployment (e.g., Heroku)
├── static/            # CSS, JavaScript, and image assets
├── templates/         # Jinja2 HTML templates for pages
├── README.md          # Project overview (this file)
└── .gitignore         # Files and folders to exclude from Git
```

### ⚙️ Setup & Usage

1. **Clone the repo**

   ```bash
   git clone https://github.com/hadimn/FlaskApp.git
   cd FlaskApp
   ```
2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app locally**

   ```bash
   flask run
   ```

   or

   ```bash
   python app.py
   ```
4. **Use the web UI**

   * Open [http://localhost:5000](http://localhost:5000)
   * Enter a keyword/hashtag, adjust options, submit.
   * View scraped tweets alongside charts and analytics.

### 📦 Deployment

* Use `Procfile` to deploy to platforms like Heroku.
* Ensure environment variables (if any) are configured appropriately.
* Commit and push — then deploy using your preferred CI/CD flow.

### 📚 Dependencies

* `Flask` – Web framework
* `snscrape` – Twitter scraping
* `Pandas` – Data manipulation
* `Matplotlib` or `Plotly` – Visualization
* Template and static assets for Bootstrap/Simple styling

### 🚀 Next Steps / Enhancements

* Dropdown menus for date range and tweet count.
* Advanced sentiment or topic analysis with NLP libraries.
* Export options (CSV, JSON) for enriched data sharing.
* Dockerfile or GitHub Actions to automate deployment.
