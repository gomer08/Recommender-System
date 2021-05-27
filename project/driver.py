import contextlib
import sys
import time

import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import RegexpTokenizer, WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer
import string
from pyke import knowledge_engine, krb_traceback, goal

engine = knowledge_engine.engine(__file__)

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm

def classify(tweet,location):
    #tokenizing, furnishing, stemmer
    tweeted = {'tweet':[tweet]}
    df2 = pd.DataFrame(tweeted)
    df2 = clean_text(df2, 'tweet')
    df2.tweet = df2.tweet.apply(furnished)
    df2.tweet = df2.tweet.apply(stemmer)
    df2 = df2.drop_duplicates(ignore_index=True)
    words = df2['tweet']
    
    #vectorizing
    df = pd.read_csv('classified_tweets.csv')
    df = df.drop("Unnamed: 0",axis=1)
    X_train, X_test, y_train, y_test = train_test_split(df.tweets, df.classification)
    vectorizer = TfidfVectorizer(max_features = 1000, decode_error='ignore')
    vectorizer.fit(X_train)
    cls = svm.SVC(kernel='linear')
    cls.fit(vectorizer.transform(X_train), y_train)
    y_pred = cls.predict(vectorizer.transform(X_test))
    word_matrix = vectorizer.transform(words)
    classification = cls.predict(word_matrix)
    action = ''
    for element in classification:
        action += element
    list_of_words = convert(words)
    new_words = ''
    for el in list_of_words:
        new_words += ' '
        new_words += el
    new_row = {'tweets': new_words, 'classification': action}
    df = df.append(new_row, ignore_index=True)
    df.to_csv('classified_tweets.csv')    
    #getting recommendation for list
    print('Your Tweet is a/n %s' % (action))
    print('Listing your possible action/listing things you may do')
    print(action)
    bc_get_action(action, location)

def bc_get_coords(city = 'Quezon City'):
    engine.reset()
    coords = []
    engine.activate('bc_rules')
    try:
        with engine.prove_goal(
        'bc_rules.place_coords($lat, $long, $city)', city = city) as gen:
            for vars, plan in gen:
                coords.append(vars['lat'])
                coords.append(vars['long'])
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)
    return coords


def bc_get_hotline(location = 'Quezon City'):
    engine.reset()      

    engine.activate('bc_rules')
    print("Listing All Possible Hotline You can Call: ")
    try:
        with engine.prove_goal(
               'bc_rules.place_agency($location, $number, $agency)', location=location) as gen:
            for vars, plan in gen:
                print("%s, Number of %s in %s" % (vars['number'],  vars['agency'], location))
        with engine.prove_goal(
               'bc_rules.place_agency_all_location($location, $number, $agency)', location= 'All_Region') as gen:
            for vars, plan in gen:
                print("%s, Number of %s in %s" % (vars['number'],  vars['agency'], location))
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)
    
def bc_get_evac(city = 'Quezon City'):
    engine.reset()      

    engine.activate('bc_rules')
    print("Listing All Possible Evacuation Area You can Go: ")
    try:
        with engine.prove_goal(
               'bc_rules.place_evac_region($city, $center)', city=city) as gen:
            for vars, plan in gen:
                print("In the City of %s, go to %s" % (city, vars['center']))
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)
    
def bc_get_support(agency='NCMH'):
    engine.reset()      

    engine.activate('bc_rules')
    try:
        with engine.prove_goal(
               'bc_rules.place_specific($location, $number, $agency)', agency=agency) as gen:
            for vars, plan in gen:
                print("You can call this number %s by the %s" % (vars['number'],  agency))
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)
        
def bc_get_action(label = 'call_for_action', location = 'NCR'):
    engine.reset()      
    engine.activate('bc_rules')
    print()
    actions = ['evacuate', 'call_hotlines']
    donate = ['contact_organization']
    n_action = 0
    try:
        with engine.prove_goal(
               'bc_rules.plan_action($label, $action)', label=label) as gen:
            for vars, plan in gen:
                if vars['action'] in actions:
                    if vars['action'] == 'evacuate':
                        print("Evacuate to the Nearest Evacuation Area")
                        bc_get_evac(location)
                    if vars['action'] == 'call_hotlines':
                        bc_get_hotline(location)
                if vars['action'] in donate:
                    if vars['action'] == 'contact_organization':
                        bc_get_org(location)
                if label == 'emotional_support':
                    bc_get_quote()
                    bc_get_support()
                if label == 'situational_update':
                    bc_get_situation()
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)    
    
import random
def bc_get_quote():

    starting_num = 1
    total_quotes = 25
    random_num = str(random.randint(starting_num, total_quotes))
    
    engine.reset()
    engine.activate('bc_rules')
    print()
    print("Here's a quote :)")
    try:
        with engine.prove_goal(
                'bc_rules.place_inspirational_quotes($num, $q)', num=random_num) as gen:
            for vars, plan in gen:
                print("Your inspirational quote is \n%s" % (vars['q']))
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)
    
def bc_get_situation():
    starting_num = 1
    max_signal = 4
    random_num = str(random.randint(starting_num, max_signal))

    engine.reset()
    engine.activate('bc_rules')
    print("Listing All Possible Actions: ")
    try:
        with engine.prove_goal(
               'bc_rules.place_situation($signal, $situation)', signal=random_num) as gen:
            for vars, plan in gen:
                print("For signal no. %s, we recommend to %s" % (random_num, vars['situation']))
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)
    
def bc_get_org(city = 'Quezon City'):
    engine.reset()

    engine.activate('bc_rules')
    print("Listing All Possible Organizations You Can Donate To: ")
    try:
        with engine.prove_goal(
               'bc_rules.place_org($location, $org)', location=city) as gen:
            for vars, plan in gen:
                print("In the City of %s, go to %s" % (city, vars['org']))
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)

def count_action(words):
    engine.reset()
    engine.activate('bc_rules')
    emotional_support = 0
    situational_update = 0
    call_for_action = 0
    donation =0
    for w in words:
        try:
            with engine.prove_goal(
                   'bc_rules.get_action_suggest($word, $update)', word=w) as gen:
                for vars, plan in gen:
                    if vars['update'] == 'emotional_support':
                        emotional_support +=1
                    if vars['update'] == 'situational_update':
                        situational_update +=1
                    if vars['update'] == 'donation':
                        donation +=1
                    if vars['update'] == 'call_for_action':
                        call_for_action +=1
        except Exception:
            krb_traceback.print_exc()
            sys.exit(1)
    variables = {'situational_update':situational_update, 'emotional_support':emotional_support,  'donation':donation, 'call_for_action':call_for_action}
    return max(variables, key=variables.get)
        
    
def convert(lst):
    return (lst[0].split())

def clean_text(df, text_field):
    import re
    df[text_field] = df[text_field].str.lower()
    df[text_field] = df[text_field].apply(lambda elem: re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", elem))
    return df

def furnished(text):
    final_text = []
    tokenizer = RegexpTokenizer(r'\w+')
    lemmatizer = WordNetLemmatizer()
    punctuation = list(string.punctuation)
    w_tokenizer = WhitespaceTokenizer()
    stopwords = ["ako","sa","akin","ko","aking","sarili","kami","atin",
                     "ang","aming","amin","ating","ka","iyong","iyo","inyong",
                     "siya","kanya","mismo","ito","nito","kanyang","sila",
                     "nila","kanila","kanilang","kung","ano","alin","sino",
                     "kanino","na","mga","iyon","am","ay","maging","naging",
                     "mayroon","may","nagkaroon","pagkakaroon","gumawa",
                     "ginagawa","ginawa","paggawa","ibig","dapat","maaari",
                     "marapat","kong","ikaw","tayo","hindi","namin","gusto",
                     "nais","niyang","nilang","niya","huwag","ginawang",
                     "gagawin","maaaring","sabihin","narito","kapag","ni",
                     "nasaan","bakit","paano","kailangan","walang","katiyakan",
                     "isang","at","pero","o","dahil","bilang","hanggang",
                     "habang","ng","pamamagitan","para","tungkol","laban",
                     "pagitan","panahon","bago","pagkatapos","itaas","ibaba",
                     "mula","pataas","pababa","palabas","ibabaw","ilalim",
                     "muli","pa","minsan","dito","doon","saan","lahat",
                     "anumang","kapwa","bawat","ilan","karamihan","iba",
                     "tulad","lamang","pareho","kaya","kaysa","masyado",
                     "napaka","isa","bababa","kulang","marami","ngayon",
                     "kailanman","sabi","nabanggit","din","kumuha","pumunta",
                     "pumupunta","ilagay","makita","nakita","katulad",
                     "mahusay","likod","kahit","paraan","noon","gayunman",
                     "dalawa","tatlo","apat","lima","una","pangalawa","akin",
                     "aking","ako","alin","am","amin","aming","ang","ano",
                     "anumang","apat","at","atin","ating","ay","bababa",
                     "bago","bakit","bawat","bilang","dahil","dalawa","dapat",
                     "din","dito","doon","gagawin","gayunman","ginagawa",
                     "ginawa","ginawang","gumawa","gusto","habang","hanggang",
                     "hindi","huwag","iba","ibaba","ibabaw","ibig","ikaw",
                     "ilagay","ilalim","ilan","inyong","isa","isang","itaas",
                     "ito","iyo","iyon","iyong","ka","kahit","kailangan",
                     "kailanman","kami","kanila","kanilang","kanino","kanya",
                     "kanyang","kapag","kapwa","karamihan","katiyakan",
                     "katulad","kaya","kaysa","ko","kong","kulang","kumuha",
                     "kung","laban","lahat","lamang","likod","lima","maaari",
                     "maaaring","maging","mahusay","makita","marami","marapat",
                     "masyado","may","mayroon","mga","minsan","mismo","mula",
                     "muli","na","nabanggit","naging","nagkaroon","nais",
                     "nakita","namin","napaka","narito","nasaan","ng","ngayon",
                     "ni","nila","nilang","nito","niya","niyang","noon","o",
                     "pa","paano","pababa","paggawa","pagitan","pagkakaroon",
                     "pagkatapos","palabas","pamamagitan","panahon","pangalawa",
                     "para","paraan","pareho","pataas","pero","pumunta",
                     "pumupunta","sa","saan","sabi","sabihin","sarili","sila",
                     "sino","siya","tatlo","tayo","tulad","tungkol","una",
                     "walang", 'them', 'nor', 'o', 'against', 'they', 'shan', 't', 
                     'him', 'more', 'with', 'as', 'below', "hadn't", 'should', 'does',
                      'up', 'yourselves', 'than', 'themselves', 'ourselves', 'have', 
                      'any', 'himself','same', "you'd", 'did', "shan't", 'between', 
                      'from', 'mustn', 'into', 'didn', 'can', 'at', 'll', 'hasn', 'out',                          "you're", 'she', 'he', "she's", 'having','doing', 'when', 'the',                           'an', 'isn', "wouldn't", 'so', 'their', "mightn't",'but', 'those',                          "aren't", 'because', "you'll", 'and', 'its', 'further','were', 
                       're', 'weren', 'to', 'on', 'then', 'off', 'will', 'don', 'some',                            'm','ve', "that'll", 'very', 'hers', 'being', 's', 'herself',                             "you've", 'in','whom', 'ain', "needn't", 'your', "won't", "weren't",                        'of', 'itself', 'only','now', 'couldn', "isn't", 'ma', "don't",                            'where', 'before', 'which', 'hadn','needn', 'theirs', 'these', 'it',                        'be', 'by', 'been', 'here', 'y', 'over', 'is', 'this', 'you',                              'again', 'too', 'yours', 'wouldn', 'ours', 'i', 'each', 
                     'during', "couldn't", "haven't", 'or', 'above', "it's", "doesn't", 
                     'yourself', 'no', 'under', 'through', 'won', 'while', 'own', 'am',                           'our', 'other', 'his', 'had', 'a', 'about', 'are', 'my', 'such',                           'down', 'haven','few', 'once', 'most', 'we', 'shouldn', 'all',                             'there', 'how', 'wasn', 'myself', 'until', 'that', "shouldn't",                             'both', "mustn't", 'why', 'has', 'what', 'do', 'after', 'her', 'd',                         'aren', 'who', "should've", 'mightn', 'for', 'me', 'just', "didn't",                       'not', 'if', "hasn't", 'was', 'doesn', "wasn't"]
    for i in w_tokenizer.tokenize(text):
        if i.lower() not in stopwords:
            word = lemmatizer.lemmatize(i)
            final_text.append(word.lower())
    return " ".join(final_text)

def stemmer(text):
    ps=nltk.porter.PorterStemmer()
    text= ' '.join([ps.stem(word) for word in text.split()])
    return text
