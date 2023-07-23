<div align="center">
  <h1>Music Recommendation System</h1>
  <p>This is a web application built using Flask that provides music recommendations based on user input. The recommendations are generated using item similarity collaborative filtering.</p>
</div>

<div align="center">
  <h2>Getting Started</h2>
</div>

<div align="center">
  <h3>Prerequisites</h3>
  <ul>
    <li>Python 3.x</li>
    <li>Flask</li>
    <li>pandas</li>
    <li>numpy</li>
    <li>scikit-learn</li>
  </ul>
</div>

<div align="center">
  <h3>Installation</h3>
</div>

<div align="center">
  <ol>
    <li>Clone the repository to your local machine:</li>
    <pre>git clone https://github.com/LostParadise07/Search_based_Music_Recommendation</pre>
    <li>Install the required packages:</li>
    <pre>pip install -r requirements.txt</pre>
    <li>Run the Flask app:</li>
    <pre>cd Music-Recommendation-System</pre>
    <pre>python3 app.py</pre>
  </ol>
</div>

<div align="center">
  <p>The app will be running at <code>http://127.0.0.1:5000/</code>.</p>
</div>

<div align="center">
  <h2>Usage</h2>
</div>

<div align="center">
  <ol>
    <li>Open your web browser and go to <code>http://127.0.0.1:5000/</code>.</li>
    <li>Enter the name of a song you like in the search box and click the "Search" button.</li>
    <li>The system will provide a list of recommended songs based on the input song.</li>
    <li>Click on any recommended song to view more details.</li>
  </ol>
</div>

<div align="center">
  <h2>Data</h2>
</div>

<div align="center">
  <p>The recommendation system uses two CSV files for data:</p>
  <ol>
    <li><code>triplets_file.csv</code>: Contains user-song interactions with columns <code>user_id</code>, <code>song_id</code>, and <code>listen_count</code>.</li>
    <li><code>song_data.csv</code>: Contains song details with columns <code>song_id</code>, <code>title</code>, <code>release</code>, <code>artist_name</code>, and <code>year</code>.</li>
  </ol>
  <p>Both CSV files are required for the app to work properly. Make sure to have these files available in the project directory.</p>
</div>

<div align="center">
  <h2>Model</h2>
</div>

<div align="center">
  <p>The recommendation model uses item similarity collaborative filtering to find songs similar to the input song based on user interactions. It computes the cosine similarity between song vectors and recommends songs with the highest similarity scores.</p>
</div>

<div align="center">
  <h2>Contributing</h2>
</div>

<div align="center">
  <p>Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or create a pull request.</p>
</div>

<div align="center">
  <h2>Acknowledgments</h2>
</div>

<div align="center">
  <ul>
    <li>The recommendation algorithm is based on the <code>Recommenders</code> library.</li>
    <li>The song data used in this project is for demonstration purposes and obtained from public datasets.</li>
  </ul>
</div>

<div align="center">
  <p>Feel free to customize this README to add more details about your specific project or implementation. Happy coding!</p>
</div>
