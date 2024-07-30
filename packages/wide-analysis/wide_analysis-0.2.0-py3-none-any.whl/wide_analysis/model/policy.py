from transformers import pipeline, AutoTokenizer
from wide_analysis.data.process_data import prepare_dataset
import pandas as pd
import pysbd


def extract_response(text, model_name, access_token):
    label_mapping = {'Wikipedia:Notability': 0,
            'Wikipedia:What Wikipedia is not': 1,
            'Wikipedia:Neutral point of view': 2,
            'Wikipedia:Verifiability': 3,
            'Wikipedia:Wikipedia is not a dictionary': 4,
            'Wikipedia:Wikipedia is not for things made up one day': 5,
            'Wikipedia:Criteria for speedy deletion': 6,
            'Wikipedia:Deletion policy': 7,
            'Wikipedia:No original research': 8,
            'Wikipedia:Biographies of living persons': 9,
            'Wikipedia:Arguments to avoid in deletion discussions': 10,
            'Wikipedia:Conflict of interest': 11,
            'Wikipedia:Articles for deletion': 12
            }
    if access_token is None:
        raise ValueError("Please provide a valid access token")
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    pipe = pipeline("text-classification", model=model_name, tokenizer=tokenizer, top_k=None)

    tokens = tokenizer(text, truncation=True, max_length=512)
    truncated_text = tokenizer.decode(tokens['input_ids'], skip_special_tokens=True)
    
    results = pipe(truncated_text)
    
    final_scores = {key: 0.0 for key in label_mapping}
    for result in results[0]:
        for key, value in label_mapping.items():
            if result['label'] == f'LABEL_{value}':
                final_scores[key] = result['score']
                break
    
    return final_scores

def get_policy(url, access_token=''):
    date = url.split('/')[-1].split('#')[0]
    title = url.split('#')[-1]
    print(date)
    print(title.replace('_', ' '))
    df = prepare_dataset('title', start_date=date, url=url, title=title)
    text = df['discussion'].iloc[0]
    seg = pysbd.Segmenter(language="en", clean=False)
    text_list = seg.segment(text)
    model = 'research-dump/bert-large-uncased_wikistance_policy_v1'
    res_list = []
    
    for t in text_list:
        res = extract_response(t, model, access_token)
        highest_key = max(res, key=res.get)
        highest_score = res[highest_key]
        result = {'sentence': t, 'policy': highest_key, 'score': highest_score}
        res_list.append(result)
    
    return res_list

