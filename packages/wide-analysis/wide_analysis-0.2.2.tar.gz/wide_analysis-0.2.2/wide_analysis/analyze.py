from wide_analysis.model.policy import get_policy
from wide_analysis.model.outcome import get_outcome
from wide_analysis.model.stance import get_stance
from wide_analysis.model.sentiment import get_sentiment
from wide_analysis.model.offensive import get_offensive_label

def analyze(url, task=''):
    if task == 'outcome':   
        explanation = input("Do you want an explanation? (True/False): ")
        if explanation=='True' or explanation=='true':
            explanation = True
            openai_access_token = input("Please provide your OpenAI access token: ")
        else:
            explanation = False
            openai_access_token=''
        return get_outcome(url, openai_access_token, explanation=explanation)
    elif task == 'policy':
        return get_policy(url)
    elif task == 'offensive':
        return get_offensive_label(url)
    elif task == 'sentiment':
        return get_sentiment(url)
    elif task == 'stance':
        return get_stance(url)
    else:
        raise ValueError("Invalid task. Choose from ['outcome', 'policy', 'offensive', 'sentiment', 'stance']")
