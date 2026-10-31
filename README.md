🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Python, Machine Learning, and Streamlit. The application recommends five movies similar to a selected movie using a precomputed similarity matrix and fetches movie posters through the TMDB API.

🔗 Live Application: Movie Recommendation System

⸻

📌 Project Overview

Finding movies that match our interests can be challenging when there are thousands of options available.

This project implements a content-based recommendation approach that identifies movies similar to a user’s selected movie using a precomputed similarity matrix.

Users can select a movie from the dropdown menu, click the Recommend button, and instantly receive five similar movie recommendations along with their posters.

⸻

✨ Features

* Movie Selection: Choose a movie from the available movie collection.
* Content-Based Recommendations: Recommends movies based on similarity scores.
* Top 5 Recommendations: Displays five movies similar to the selected movie.
* Movie Posters: Fetches movie posters dynamically using the TMDB API.
* Interactive Interface: Simple and user-friendly interface built with Streamlit.
* Error Handling: Handles API timeouts and unavailable movie posters.
* Live Deployment: Accessible online through Streamlit Community Cloud.

⸻

🛠️ Technology Stack

Technology	Purpose
Python	Core programming language
Pandas	Data manipulation and processing
Pickle	Loading precomputed model data
Requests	Making API requests
Streamlit	Web application development
TMDB API	Fetching movie posters
Git & GitHub	Version control and project hosting
Streamlit Community Cloud	Application deployment

⸻

⚙️ How It Works

The recommendation system follows these steps:

1. Loads the movie dataset from movie_dict.pkl.
2. Loads the precomputed similarity matrix from similarity.pkl.
3. Takes the user’s selected movie as input.
4. Finds the corresponding movie index.
5. Retrieves similarity scores for that movie.
6. Sorts movies according to their similarity scores.
7. Selects the five most similar movies, excluding the selected movie.
8. Fetches their posters using the TMDB API.
9. Displays the recommendations through Streamlit.

⸻

📂 Project Structure

Movie-Recommendation-System/
│
├── app.py                  # Main Streamlit application
├── main.py                 # Additional Python file
│
├── movie_dict.pkl          # Movie dataset
├── movies.pkl              # Additional movie data
├── similarity.pkl          # Precomputed similarity matrix
│
├── requirements.txt        # Python dependencies
├── .gitattributes          # Git LFS configuration
├── .gitignore              # Ignored files
│
├── Procfile                # Deployment configuration
└── setup.sh                # Setup configuration

Important: The application requires movie_dict.pkl and similarity.pkl to run successfully. The similarity.pkl file is stored using Git Large File Storage (Git LFS).

⸻

🚀 Installation and Setup

Follow these steps to run the project locally.

1. Clone the Repository

git lfs install
git clone https://github.com/NiharTambe20/Movie-Recommendation-System.git
cd Movie-Recommendation-System

2. Create a Virtual Environment

python -m venv venv

Activate the environment:

macOS / Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure TMDB API Key

The application uses the TMDB API to fetch movie posters.

Create an account on The Movie Database (TMDB) and obtain an API key.

Inside the project directory, create the following file:

.streamlit/secrets.toml

Add your API key:

TMDB_API_KEY = "YOUR_TMDB_API_KEY"

Security Note: Never upload your actual API key or secrets.toml file to GitHub. The application reads the key securely through Streamlit Secrets.

5. Run the Application

streamlit run app.py

The application will open in your browser.

⸻

📦 Dependencies

The project uses the following Python packages:

streamlit==1.50.0
pandas==2.3.3
requests==2.32.5

⸻

🌐 Live Deployment

The application is deployed using Streamlit Community Cloud.

You can access it here:

👉 Open Movie Recommendation System

⸻

👨‍💻 Author

Nihar Tambe

* GitHub: @NiharTambe20

⸻

📄 License

This project is intended for educational and portfolio purposes.
