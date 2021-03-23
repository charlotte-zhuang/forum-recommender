# STEM-Away Forum Post Recommender

This project is a submission to the [STEM-Away ML pathway hub](https://stemaway.com/t/level-1-module-1-self-assessment-and-preparation/6946). It will create a forum post recommender that uses the text body of posts to perform clustering.

## Gathering Data

[Sitepoint Community](https://www.sitepoint.com/community/) was used as the training data. The latest 3000 posts as of 23 March, 2021, were scraped for their title, category, tags, and body.

Most posts did not have any tags, so that may not end up being useful. Additional information that can help with building a recommender include the author and users who comment on the post, popularity, and the text in the comments. These were not gathered as I am focusing on just NLP in the interest of brevity. It could be interesting to construct a social network using user interactions.
