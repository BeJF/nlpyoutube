import os
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

#import nltk
#nltk.download("stopwords")

import googleapiclient.discovery

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyCzLzeKOj6Ovz7sT06DYG1Lc9v_uXgKmFE"
youtube = googleapiclient.discovery.build(
                api_service_name, api_version, developerKey = DEVELOPER_KEY)
video_id = "gmsWMb9ex9w"

def load_comments(match, comments_list):
    for item in match["items"]:
        comment = item["snippet"]["topLevelComment"]
        author = comment["snippet"]["authorDisplayName"]
        text = comment["snippet"]["textDisplay"]
        comments_list.append(text)
        #print("Comment by {}: {}".format(author, text))
        '''if 'replies' in item.keys():
            for reply in item['replies']['comments']:
                rauthor = reply['snippet']['authorDisplayName']
                rtext = reply["snippet"]["textDisplay"]
                print("\n\tReply by {}: {}".format(rauthor, rtext), "\n")'''

def get_comment_thread(youtube, video_id, next_page_token):
    results = youtube.commentThreads().list(
        part="snippet",
        maxResults=50,
        videoId=video_id,
        textFormat="plainText",
        pageToken=next_page_token
    ).execute()
    return results

comments_list = []
filtered_sentence = []

results = youtube.commentThreads().list(
        part="snippet",
        maxResults=5,
        videoId=video_id,
        textFormat="plainText",
    ).execute()
next_page_token = results["nextPageToken"]
load_comments(results, comments_list)

'''while next_page_token:

    match = get_comment_thread(youtube, video_id, next_page_token)
    print("nb of comments = ", len(comments_list))
    if "nextPageToken" in match :
        next_page_token = match["nextPageToken"]
    else :
        break
    load_comments(match, comments_list)'''

print(comments_list)

stop_words = set(stopwords.words("french")) #peut ajouter plus de stopwords
print(stop_words)
comments_tokenized = []

#quid qd plusieurs phrases dans un comment

for comment in comments_list :
    sentence = word_tokenize(comment)
    filtered_sentence = [w for w in sentence if not w in stop_words]
    '''for word in sentence :
        if word not in stop_words :
            filtered_sentence.append(word)'''
    comments_tokenized.append(filtered_sentence)
    #print(word_tokenize(comment))
    #print(sent_tokenize(comment))'''

print(comments_tokenized)
