import pickle
import numpy as np
import pandas as pd
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
df = pd.read_csv('발라드.csv', encoding='cp949')
def get_title_to_idx():
    return pickle.load(open("ballad_title_to_idx.pkl" , 'rb'))
def get_cosine_tfidf():
    return pickle.load(open("ballad_sims_cosine_tfidf.pkl", 'rb'))

def print_hi():
    title_to_idx = get_title_to_idx()
    title_idx = title_to_idx['생일 축하합니다, 그냥']
    print(f'current index : {title_idx}')
    print(type(title_idx))
    cosine_tfidf = get_cosine_tfidf()
    top_ten = np.argsort(cosine_tfidf[title_idx])[::-1][1:11]
    print(type(top_ten))
    print(top_ten)
    print(df.iloc[top_ten].title.values)
    print(type(df.iloc[top_ten].title.values))
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # title_list = df.title.values.tolist()
    # lyric_list = df.lyrics.values.tolist()
    # dictionary = dict(zip(title_list, lyric_list))
    # 비슷한 노래 추천 dict
    reco_list = top_ten.tolist()
    reco_music = df.iloc[top_ten].title.values.tolist()
    recommend_dict ={"추천리스트":{"추천10곡": reco_music,"추천Index":reco_list}}
    return recommend_dict

@app.route('/reco')
def get_json():
    dic = print_hi()
    return jsonify(dic)
@app.route('/reco',methods = ['POST'])
def post_get_json():
    dic = request.get_json()
    return jsonify(dic)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi()
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/