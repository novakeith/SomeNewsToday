# Some News Today (dot Py)
### Python command line tool to retrieve news using Gnews.IO and email it to yourself

This is fairly straightforward and simple so far, although I do plan on adding new features. Essentially,
this uses the GNews.IO API to grab the top 10 articles of the day and send them to your email. You can
also specify a keyword argument at runtime to search for specific news.

I expect this could be useful combined with a cron job.

__Examples__:
Grab the top 10 headlines:
```python3 SomeNewsToday.py```

Grab 10 news articles related to Apple:
```python3 SomeNewsToday.py Apple```

Eventually I'll be adding in functionality for multiple searches via the command line, better templating for emails, a web 
based interface for modifying searches and config files, etc.

### Speaking of Config files...
Remember to edit config.py with your API key and other information!
