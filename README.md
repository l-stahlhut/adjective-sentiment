# Adjective Sentiment dictionary

This script calculates the mean sentiment of the adjectives in a text. 
-1, 0 and 1 denote a negative, neutral and positive sentiment respectively. 

## How to use the script
The script requires
- a file with a list of adjectives and their respective sentiment in the form of **adjective_sentiment.txt**. A sentiment dictionary is created from this list. 
- a text with POS-tags in the form of **test_news.txt** or **test_hobbies.txt**. The tag 'JJ' stands for adjectives. This data is from the Brown corpus. 

Example: 
```python
$ python3 adjective_sentiment.py adjective_sentiment.txt test_hobbies.txt
```



## License
[MIT](https://choosealicense.com/licenses/mit/)