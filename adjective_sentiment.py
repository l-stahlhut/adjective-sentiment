#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s): Laura Stahlhut
# date: 28.22.2021


import sys
import re
import os


def create_sentiment_dict(filename):
    """takes a list of adjectives with their sentiment (tab seperated file) and returns a sentiment dictionary."""
    d = {}
    # open file, read lines
    with open(os.path.join("data/", filename), 'r') as f:
        adjectives = f.readlines()
        for line in adjectives:
            key = ''.join(re.findall(r'\w*-?\w+?\t',line)).strip('\t')
            value = ''.join(re.findall(r'\w+$',line))
            value = ''.join([str(1) if value == "positive" else str(0) if value == 'neutral' else str(-1)])

            d[key] = value

    return d


def calculate_avg_sentiment(filename, sentiment_dict):
    """Calculates the average sentiment score of the adjectives within a file."""
    adj_list = []
    with open(os.path.join("data/", filename), 'r') as f2:
        words = f2.readlines()
        for line in words:
            if re.findall(r'JJ$', line):
                line = re.sub(r'\tJJ\n', '', line)
                adj_list.append(line)


    scores = []

    for adj in adj_list:
        for k in sentiment_dict:
            if adj == k:
                scores.append(int(sentiment_dict[k]))

    average_score = sum(scores)/len(scores)

    return average_score


def main():
    sentiment_dict = create_sentiment_dict(sys.argv[1])
    adjectives_text = calculate_avg_sentiment(sys.argv[2], sentiment_dict)
    print("The averege blablba is: " + str(adjectives_text))


if __name__ == '__main__':
	main()



