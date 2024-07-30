from transformers import pipeline, AutoTokenizer
from wide_analysis.data.process_data import prepare_dataset
import pandas as pd
import pysbd

def extract_highest_score_label(res):
    flat_res = [item for sublist in res for item in sublist]
    highest_score_item = max(flat_res, key=lambda x: x['score'])
    highest_score_label = highest_score_item['label']
    highest_score_value = highest_score_item['score']    
    return highest_score_label, highest_score_value


def get_offensive_label(url):
    date = url.split('/')[-1].split('#')[0]
    title = url.split('#')[-1]
    df = prepare_dataset('title', start_date=date,url=url, title=title)
    text = df['discussion'].iloc[0]
    #offensive language detection model
    model_name = "cardiffnlp/twitter-roberta-base-offensive"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = pipeline("text-classification", model=model_name, top_k= None)

    #sentence tokenize the text using pysbd
    seg = pysbd.Segmenter(language="en", clean=False)
    text_list = seg.segment(text)

    res = []
    for t in text_list:
        results = model(t)
        highest_label, highest_score = extract_highest_score_label(results)
        result = {'sentence': t,'offensive_label': highest_label, 'score': highest_score}
        res.append(result)
    return res