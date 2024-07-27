import random

import numpy as np
import pandas as pd

GENRES = ["romance", "horror", "sci-fi"]
DATA = {
    "Title": [f"Book {i}" for i in range(1, 101)],
    "Author": [f"Author {i}" for i in range(1, 101)],
    "Genre": [random.choice(GENRES) for _ in range(100)],
    "Publication Year": np.random.randint(1950, 2024, 100),
    "Pages": np.random.randint(100, 1000, 100),
    "Publisher": [f"Publisher {i}" for i in range(1, 101)],
    "ISBN": [f"ISBN-{i}" for i in range(1, 101)],
    "Rating": np.random.uniform(1, 5, 100).round(2)
}


def generate_books_table() -> pd.DataFrame:
    return pd.DataFrame(DATA)
