import gensim

model = gensim.models.KeyedVectors.load_word2vec_format('model.vec', binary=False)
# print(model.similarity('国王', '王妃'))
print('model loaded')

entries = ['アルプス', 'コミック', '億万長者', 'ルール', '飛行機', 'ルート', 'ライター', '南極', 'パイロット', '草原', '靴下', '手袋', 'モスクワ', 'レーザー', 'タップ', '氷', 'カボチャ', 'トリップ', '死', 'パーツ', 'イス', '雪だるま', '森', 'レース', 'ノート']

while True:
    hint = input("Please Enter Hint Word: ")
    similarities = [model.similarity(hint, entry) for entry in entries]
    results = [[similarity, entry] for (entry, similarity) in zip(entries, similarities)]
    print(sorted(results, reverse=True))