from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions,SentimentOptions


def sentiment_and_keyword(st, service):
    return (service.analyze(text=st, features=Features(keywords=KeywordsOptions(sentiment=True, emotion=True, limit=3),
                                                       sentiment=SentimentOptions())).get_result())

if __name__ == '__main__':
    print('1')