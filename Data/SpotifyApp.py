import streamlit as st
import pandas as pd
import os

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Spotify Genre Segmentation",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------
st.markdown("""
<style>

.stApp{
    background:#121212;
    color:white;
}

h1,h2,h3{
    color:#1DB954;
}

div[data-testid="stMetric"]{
    background:#1E1E1E;
    padding:15px;
    border-radius:15px;
    border:1px solid #1DB954;
    text-align:center;
}

.song-card{
    background:#181818;
    border-left:5px solid #1DB954;
    padding:20px;
    border-radius:15px;
    margin-bottom:15px;
}

.song-card:hover{
    background:#282828;
}

footer{
visibility:hidden;
}

</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv(
        "Spotify_Clustered_Results.csv.csv",
        encoding="latin1"
    )


df = load_data()


# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

# Spotify Logo
logo_path = "spotify_logo.png"

if os.path.exists(logo_path):
    st.sidebar.image(
        logo_path,
        width=150
    )
else:
    st.sidebar.warning("Spotify logo not found")


st.sidebar.markdown(
"""
<h2 style='text-align:center;color:#1DB954;'>
🎵 Spotify AIML Project
</h2>
""",
unsafe_allow_html=True
)


st.sidebar.markdown("""
### AIML Project

**Algorithm**

✅ K-Means Clustering


**Dataset**

Spotify Songs Dataset


**Objective**

Recommend songs based on similar clusters.

---
""")


st.sidebar.metric(
    "Songs",
    len(df)
)

st.sidebar.metric(
    "Artists",
    df["track_artist"].nunique()
)

st.sidebar.metric(
    "Genres",
    df["playlist_genre"].nunique()
)

st.sidebar.metric(
    "Clusters",
    df["Cluster"].nunique()
)


st.sidebar.markdown("---")


st.sidebar.info(
"""
Developed using

- Python
- Pandas
- Scikit-learn
- Streamlit
"""
)



# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.markdown("""
<h1 style='text-align:center;font-size:50px'>
🎵 Spotify Genre Segmentation & Recommendation
</h1>


<h4 style='text-align:center'>
Machine Learning using K-Means Clustering
</h4>


<p style='text-align:center'>
Discover similar songs based on their audio characteristics.
</p>

""",
unsafe_allow_html=True)


st.divider()



# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------

st.subheader("📊 Dashboard")


c1,c2,c3,c4 = st.columns(4)


c1.metric(
    "🎵 Songs",
    len(df)
)

c2.metric(
    "👨‍🎤 Artists",
    df["track_artist"].nunique()
)

c3.metric(
    "🎼 Genres",
    df["playlist_genre"].nunique()
)

c4.metric(
    "🎯 Clusters",
    df["Cluster"].nunique()
)



st.divider()



# -------------------------------------------------
# SONG SELECTION
# -------------------------------------------------

st.subheader("🎧 Select a Song")


song = st.selectbox(
    "",
    sorted(df["track_name"].dropna().unique())
)


selected = df[
    df["track_name"] == song
].iloc[0]



# -------------------------------------------------
# SONG DETAILS
# -------------------------------------------------

st.subheader("🎵 Song Information")


col1,col2 = st.columns([1,2])


with col1:

    if os.path.exists(logo_path):
        st.image(
            logo_path,
            width=200
        )



with col2:

    st.markdown(f"""

### {selected['track_name']}


**Artist:** {selected['track_artist']}


**Genre:** {selected['playlist_genre']}


**Popularity:** ⭐ {selected['track_popularity']}


**Cluster:** {selected['Cluster']}

""")



st.divider()



# -------------------------------------------------
# RECOMMENDATION FUNCTION
# -------------------------------------------------

def recommend(song_name):

    cluster = df[
        df["track_name"] == song_name
    ]["Cluster"].values[0]


    rec = df[
        (df["Cluster"] == cluster)
        &
        (df["track_name"] != song_name)
    ]


    rec = rec.sort_values(
        "track_popularity",
        ascending=False
    )


    return rec.head(10)



# -------------------------------------------------
# BUTTON
# -------------------------------------------------

if st.button(
    "🎵 Recommend Similar Songs",
    use_container_width=True
):

    progress = st.progress(0)


    for i in range(100):
        progress.progress(i+1)


    st.success(
        "Recommendation Completed!"
    )


    st.balloons()


    recommendations = recommend(song)


    st.subheader(
        "🎶 Recommended Songs"
    )


    for _,row in recommendations.iterrows():

        st.markdown(f"""

<div class="song-card">


### 🎵 {row['track_name']}


👨‍🎤 **Artist:** {row['track_artist']}


🎼 **Genre:** {row['playlist_genre']}


⭐ **Popularity:** {row['track_popularity']}


🎯 **Cluster:** {row['Cluster']}


</div>

""",
unsafe_allow_html=True)



    csv = recommendations.to_csv(
        index=False
    ).encode("utf-8")


    st.download_button(

        "📥 Download Recommendations",

        csv,

        "recommended_songs.csv",

        "text/csv"

    )



st.divider()



# -------------------------------------------------
# VISUALIZATION
# -------------------------------------------------

left,right = st.columns(2)


with left:

    st.subheader(
        "📈 Genre Distribution"
    )

    genre = df[
        "playlist_genre"
    ].value_counts()


    st.bar_chart(
        genre
    )



with right:

    st.subheader(
        "🎯 Cluster Distribution"
    )


    cluster = df[
        "Cluster"
    ].value_counts().sort_index()


    st.bar_chart(
        cluster
    )



st.divider()



# -------------------------------------------------
# TOP SONGS
# -------------------------------------------------

st.subheader(
    "🔥 Top Popular Songs"
)


popular = df.sort_values(
    "track_popularity",
    ascending=False
)[
[
"track_name",
"track_artist",
"playlist_genre",
"track_popularity"
]
].head(10)


st.dataframe(
    popular,
    use_container_width=True
)



st.divider()



# -------------------------------------------------
# DATA EXPLORER
# -------------------------------------------------

with st.expander(
    "📂 View Dataset"
):

    st.dataframe(df)


st.divider()


st.markdown("""

<center>


### 🎵 Spotify Genre Segmentation & Recommendation System


Developed using Python • Streamlit • Scikit-learn • K-Means Clustering


© 2026


</center>

""",
unsafe_allow_html=True)