import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity



movies_dict=pickle.load(open('movies.pkl','rb'))
new_df=pd.DataFrame(movies_dict)
selected_movies=new_df['title'].values


cv=CountVectorizer(max_features=5000,stop_words="english")
vectors=cv.fit_transform(new_df['tags']).toarray()
similarity=cosine_similarity(vectors)


def recommend(obj):
    i=new_df[new_df['title']==obj].index[0]
    distances=similarity[i]
    top_movies=sorted(list(enumerate(similarity[i])),reverse=True,key=lambda x:x[1])[1:6]
    l=[]
    for i in top_movies:
        l.append(new_df.iloc[i[0]].title)
    return l  