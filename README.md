<h1>🎧 Mood-Based Song Recommender System</h1>

<p>
A <b>machine learning-based recommendation system</b> that suggests songs 
based on the user's <b>current mood</b> using Spotify audio features and clustering techniques.
</p>

<hr>

<h2>🚀 Overview</h2>
<p>
This project recommends songs according to different moods like 
<b>Happy, Sad, Energetic, Calm</b>, etc.  
It uses audio features from Spotify to classify and group songs, 
making it easy to generate mood-based playlists.
</p>

<hr>

<h2>😊 Supported Moods</h2>
<ul>
  <li>😄 Happy</li>
  <li>😢 Sad</li>
  <li>⚡ Energetic</li>
  <li>😌 Calm</li>
  <li>💖 Romantic</li>
</ul>

<hr>

<h2>📊 Dataset</h2>
<p>Spotify Open Dataset containing features like:</p>
<ul>
  <li>🎧 Danceability</li>
  <li>🔊 Energy</li>
  <li>🎵 Tempo</li>
  <li>🎤 Valence (positivity)</li>
  <li>🎚️ Loudness</li>
  <li>⏱️ Duration</li>
</ul>

<hr>

<h2>🧠 Algorithm</h2>
<p>
This system uses <b>K-Means Clustering</b> to group songs into mood-based clusters.
</p>
<ul>
  <li>Songs are grouped based on similar audio features</li>
  <li>Each cluster represents a specific mood</li>
  <li>Recommendations are generated from the selected mood cluster</li>
</ul>

<hr>

<h2>⚙️ How It Works</h2>
<ol>
  <li><b>Input Mood:</b> User selects a mood (e.g., Happy)</li>
  <li><b>Feature Matching:</b> System maps mood to audio features</li>
  <li><b>Clustering:</b> Songs are grouped using K-Means</li>
  <li><b>Recommendation:</b> Songs from the matching cluster are suggested</li>
</ol>

<hr>

<h2>🛠️ Tech Stack</h2>
<ul>
  <li>Python 🐍</li>
  <li>Pandas</li>
  <li>NumPy</li>
  <li>Scikit-learn</li>
  <li>Matplotlib</li>
</ul>

<hr>

<h2>📌 Installation</h2>
<pre>
git clone https://github.com/your-username/mood-song-recommender.git
cd mood-song-recommender
pip install -r requirements.txt
</pre>

<hr>

<h2>▶️ Usage</h2>
<pre>
python main.py
</pre>

<p><b>Example:</b></p>
<pre>
get_recommendations("Happy")
</pre>

<hr>

<h2>📈 Sample Output</h2>
<pre>
Mood: Happy

Recommended Songs:
1. Song A
2. Song B
3. Song C
</pre>

<hr>

<h2>🎯 Future Improvements</h2>
<ul>
  <li>🎤 Add emotion detection using voice/text</li>
  <li>📱 Build a mobile app</li>
  <li>🌐 Integrate Spotify API</li>
  <li>🤖 Use Deep Learning for better accuracy</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>
<p>
Contributions are welcome! Fork the repo and submit a pull request.
</p>

<hr>

<h2>📄 License</h2>
<p>MIT License</p>

<hr>

<h2>💡 Author</h2>
<p>Built with ❤️ by Rishab Jain</p>
