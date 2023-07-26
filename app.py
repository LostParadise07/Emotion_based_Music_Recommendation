from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import Recommenders as Recommenders
global s1,data
s1=0
data=0
rec_song=0

def load_data():
    song_df_1 = pd.read_csv('triplets_file.csv')
    song_df_2 = pd.read_csv('song_data.csv')
    song_df = pd.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on='song_id', how='left')
    song_df['song'] = song_df['title'] + ' - ' + song_df['artist_name']
    song_df = song_df.head(20000)
    return song_df

def model1(s1, song_df):
    ir = Recommenders.item_similarity_recommender_py()
    ir.create(song_df, 'user_id', 'song')

    try:
        df3 = song_df[song_df['title'].str.contains(str(s1), case=False, na=False)][['song']]
        if not df3.empty:
            t1 = df3.iloc[0, 0]
            ir.get_similar_items([str(t1)])
            rec_song = Recommenders.df5
        else:
            rec_song = pd.DataFrame(columns=['song'])
    except KeyError:
        rec_song = pd.DataFrame(columns=['song'])

    return rec_song

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/",methods=['POST'])
def search():
    text=request.form['searchsong']
    s1 = text
    song_df = load_data()
    rec_song = model1(s1, song_df)
    print(rec_song)
    #xyz=['NAME', 'Alejandro - Lady GaGa', "Just Dance - Lady GaGa / Colby O'Donis", 'Creep (Explicit) - Radiohead', 'Love Story - Taylor Swift', 'Lucky (Album Version) - Jason Mraz & Colbie Caillat', 'Savior - Rise Against', 'Heartbreak Warfare - John Mayer', 'The Only Exception (Album Version) - Paramore', 'OMG - Usher featuring will.i.am', 'Bulletproof - La Roux']
    return render_template("recommend.html",data=rec_song)


if __name__=="__main__":
    app.run(debug=True)