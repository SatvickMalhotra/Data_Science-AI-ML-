# Movie Recommendation System🎬🎬

## Introduction📖📖📖
Welcome to the *Movie Recommendation System* – a sophisticated tool designed for movie enthusiasts and cinephiles alike. Utilizing advanced algorithms, this system offers personalized movie suggestions based on genre and movie titles, leveraging the renowned IMDB's weighted rating formula for precision and reliability.

## Why This System?⚙️⚙️⚙️
In the era of streaming and abundant choices, finding the right movie can be overwhelming. This system simplifies the decision-making process, providing tailored suggestions that resonate with individual preferences and past viewing habits.

## Key Features👩🏻‍💼👩🏻‍💼
- **Dual Recommendation Engines**:
  - **Genre-Based**: Dive into a world of movies sorted by genres. Whether you're in the mood for a thriller, romance, or a sci-fi adventure, get the best picks at your fingertips.
  - **Title-Based**: Discover movies similar to your favorites. This engine analyzes titles and recommends films that share similar themes, styles, or narratives.
- **Powered by IMDB's Weighted Rating Formula**:

-Weighted Rating (WR) = (v/v+m) * R + (m/v+m) * C

Where:
- `v` = Number of votes for the movie
- `m` = Minimum votes required to be listed
- `R` = Average rating of the movie
- `C` = Mean vote across the whole report

## How to Use📋📋📋📋📋
To make the most of this Movie Recommendation System, follow these simple steps:

1. **Genre-Based Recommendations**:
   - Open `movie-recommender-genre.ipynb`.
   - Select your preferred genre from the list.
   - The system will provide a list of movies tailored to your genre choice.

2. **Title-Based Recommendations**:
   - Navigate to `movie_recommender_name.ipynb`.
   - Enter a movie title you enjoy.
   - The system will suggest similar movies based on your input.

Both notebooks are designed for ease of use, guiding you through each step.

## Benefits🫱🏼‍🫲🏾🫱🏼‍🫲🏾🫱🏼‍🫲🏾🫱🏼‍🫲🏾
The Movie Recommendation System offers several advantages:

- **Personalized Recommendations**: Tailors movie suggestions to your specific tastes, whether you're driven by genre or inspired by a particular movie title.

- **Time-Saving**: Reduces the time spent browsing through endless options, bringing you closer to your next favorite movie.

- **Discover New Favorites**: Helps you explore and uncover movies that you might not have found on your own, broadening your cinematic horizons.

- **Data-Driven Decisions**: Utilizes the robust IMDB's weighted rating formula, ensuring that the recommendations are not only popular but also critically acclaimed.

By integrating these benefits, the Movie Recommendation System enhances your movie-watching experience, making it more enjoyable and tailored to your preferences.


## Installation
To set up the recommendation system:
```bash
git clone [Repository-URL]
pip install -r requirements.txt
