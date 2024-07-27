import csv
import re
import io
import pandas as pd
from fuzzywuzzy import fuzz, process

def read_csv(file_name):
    df = pd.read_csv(file_name)
    return df

def preprocess_url1(url):
    # Add your preprocessing rules here
    return url

def preprocess_url2(url):
    # Add your preprocessing rules here
    return url

def get_best_match(url, url_list):
    scorers = [fuzz.token_sort_ratio, fuzz.token_set_ratio, fuzz.partial_token_sort_ratio]
    best_match_data = max((process.extractOne(url, url_list, scorer=scorer) for scorer in scorers), key=lambda x: x[1])
    best_match, best_score = best_match_data[0], best_match_data[1]
    return best_match, best_score

def compare_urls(df, column1, column2, threshold=60):
    result = []

    preprocessed_url1_list = [preprocess_url1(url) for url in df[column1]]
    preprocessed_url2_list = [preprocess_url2(url) for url in df[column2]]

    for url, preprocessed_url1 in zip(df[column1], preprocessed_url1_list):
        best_match, best_score = get_best_match(preprocessed_url1, preprocessed_url2_list)

        if best_score < threshold:
            best_match = 'No Match'

        result.append({'Source URL': url, 'Best Match Destination URL': best_match, 'Match Score': best_score})

    return result

def compare_urls_in_csv(file_name, column1, column2, threshold=60):
    df = read_csv(file_name)
    result = compare_urls(df, column1, column2, threshold)
    result_df = pd.DataFrame(result)
    result_df.to_csv("result.csv", index=False)
    print("Comparison results saved to result.csv")
    return result_df
