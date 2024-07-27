import matplotlib.pyplot as plt
import streamlit as st

from generate_books_table import generate_books_table

df = generate_books_table()

st.set_page_config(page_title="Books Library", layout="wide")
st.sidebar.title("Menu")

menu_options = st.sidebar.selectbox(
    "Select a page",
    ["Home", "Romance", "Horror", "Sci-Fi", "Statistics"]
)

if menu_options == "Home":
    st.title("Home")
    st.dataframe(df)
elif menu_options == "Romance":
    st.title("Romance books")
    st.dataframe(df[df["Genre"] == "romance"])
elif menu_options == "Horror":
    st.title("Horror books")
    st.dataframe(df[df["Genre"] == "horror"])
elif menu_options == "Sci-Fi":
    st.title("Sci-Fi books")
    st.dataframe(df[df["Genre"] == "sci-fi"])
elif menu_options == "Statistics":
    st.title("Statistics")
    st.write("This section will contain statistics about the books library.")

    st.subheader("Number of books by genre")
    genre_counts = df["Genre"].value_counts()
    st.bar_chart(genre_counts)

    st.subheader("Average rating by genre")
    avg_ratings_by_genre = df.groupby("Genre")["Rating"].mean()
    fig, ax = plt.subplots(figsize=(4, 2))
    ax.pie(
        avg_ratings_by_genre,
        labels=avg_ratings_by_genre.index,
        autopct="%1.1f%%",
        startangle=90
    )
    ax.axis("equal")
    st.pyplot(fig)

    st.subheader("Number of books published per year")
    publication_counts = df["Publication Year"].value_counts().sort_index()
    st.line_chart(publication_counts)
