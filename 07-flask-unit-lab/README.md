### ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Programming


<!---
This assignment was developed by Cody Soyland

Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Hit me up on Slack @Susi Remondi
--->

# Unit 7 Lab: Flask

## Overview
Welcome to the Flask unit lab! Let's use Flask to give ourselves a web interface for our command-line Rotten Tomatoes application.

This web program takes user input to find a movie and display relevant information. The user can then drill down into an individual movie's details.


-------------

## Deliverables

Keep working in the same `movie_app.py` that we've been working on and start your application from the command line to check your work in your local web browser accessing the Flask local dev server. Don't forget the `flask` command-line argument!

Your program will be accessible by a local web browser, use the Flask microframework for a user interface, and leverage the code already written in previous labs to query the OMDB API.

---------------

## Requirements

Your program has three main components: a landing page, a search results page, and a movie details page.

Your program's functionality should look like this:

1. Movie Search

    ![](https://gist.github.com/sonylnagale/e064a3414930c0870e369c24b2723b61/raw/f2efde3eb35a8ad718740a9ebe2b24c8887ab290/movie-search.png)

1. Movie Details

    ![](https://gist.github.com/sonylnagale/e064a3414930c0870e369c24b2723b61/raw/f2efde3eb35a8ad718740a9ebe2b24c8887ab290/movie-details.png)

-------------

## Directions

1. Start off by importing the correct pieces from `flask`.
1. Don't forget to initialize your app!
1. Create an `@app.route` to handle user traffic to the home page.
1. Leverage the functionality we wrote in the prior labs to take user input and display the search results.
1. Be sure to test this functionality!
1. Create a new template for a movie detail page.
1. Create another route for the movie drill-down detail page's details.
1. Test your site with a variety of inputs.
