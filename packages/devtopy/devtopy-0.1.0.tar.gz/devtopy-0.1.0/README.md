# DevToPy

DevToPy is a Python client library for interacting with the dev.to API. It provides easy access to key dev.to features including article retrieval, posting, user information management, and more.

## Installation

You can install DevToPy using pip:

```bash
pip install devtopy
```

## Quick Start

Here's a quick example of how to use DevToPy:

```python
from devtopy import DevTo

# Initialize the client with your API key
client = DevTo(api_key="your_api_key_here")

# Get the latest articles
latest_articles = client.articles.get_latest_articles()

# Publish a new article
new_article = client.articles.publish(
    title="My New Article",
    body_markdown="This is the content of my article.",
    tags=["python", "api"],
    published=True
)

# Get your own articles
my_articles = client.articles.get_my_articles()

# Get comments for an article
article_comments = client.comments.get_article_comments(article_id="123")

# Toggle a reaction on an article
client.reactions.toggle(
    category=client.reactions.ReactionCategory.LIKE,
    reactable_id=123,
    reactable_type=client.reactions.ReactableType.ARTICLE
)
```

## Features

DevToPy now supports the following operations:

- Articles: Retrieve, publish, update, and manage articles
- Comments: Get comments for articles and podcast episodes
- Followed Tags: Manage followed tags
- Organizations: Retrieve organization information and users
- Podcast Episodes: Get podcast episode information
- Profile Images: Retrieve user profile images
- Reactions: Add and toggle reactions on articles, comments, and users
- Tags: Retrieve tag information
- Users: Get user information, invite users
- Videos: Retrieve articles with videos

## API Reference

For detailed information on all available methods, please refer to the [API documentation](https://developers.forem.com/api/v1).

## Requirements

- Python 3.8+
- pydantic >= 2.8.2
- requests >= 2.32.3

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

