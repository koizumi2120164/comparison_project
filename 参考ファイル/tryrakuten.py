import requests
import pandas as pd
import json
from pandas import json_normalize
 
 
#urlの作成
base_url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?' #楽天市場商品検索API

item_parameters = {
            'applicationId': '1059665974949401126', #アプリIDikb2120228
            'format': 'json',
            "keyword" : "カーペット用洗剤",
            #'categoryId':'31-335' 例として鶏肉料理のカテゴリID入れています
}

#jsonデータの取得
#各カテゴリの4位までのレシピ情報取得
r = requests.get(base_url, params=item_parameters)
item_data = r.json()

#各レシピ情報の格納用に、データフレーム用意
df_rank = pd.DataFrame(columns=[
    'product_name', #順位
    'description',
    'image1', #レシピ説明文
    'price2', #レシピID
    'link2', #レシピタイトル
])
for i in range(0, len(item_data["Items"])):
    item = item_data["Items"][i]["Item"]
    df_rank = df_rank.append(
            {'product_name':item["itemName"],
             'description':item["catchcopy"],
             'image1':item['mediumImageUrls'][0]["imageUrl"],
             'price1':item['itemPrice'],
             'link1':item['itemUrl'],}, 
            ignore_index=True)

#データフレームをcsvに出力
df_rank.to_csv('洗剤・柔軟剤・クリーナー5.csv', index=False,  encoding='utf_8_sig')
 
 