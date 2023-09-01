import json
from pelican import signals

def generate_article_json(generator):
    articles = []
    for article in generator.articles:

        try:
            article_data = {
                "title": article.title,
                "slug": article.slug,
                "date": article.date.strftime('%Y-%m-%d'),
                # Add more fields as needed
            }
            articles.append(article_data)

        except Exception as e:
            pass

  

    with open(f"{generator.output_path}/articles.json", "w") as json_file:
        json.dump(articles, json_file, indent=4)

def register():
    signals.article_generator_pretaxonomy.connect(generate_article_json)
