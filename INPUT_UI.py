#streamlitの起動＝>ターミナルでstreamlit run ファイル名.py

# インポート
import pandas as pd
import time
import streamlit as st　　# フロントエンドを扱うstreamlitの機能をインポート
from PIL import Image

# 画像のディレクトリ指定
image_directory = "/Users/kazukimaehashi/Downloads/tech0/Step3/"

#バナー指定
image = Image.open('Group 22.png')
st.image(image, use_column_width=True)

#SERVICE説明
html_message = "<p style='text-align: center; font-size: small;'>SERVICE</p>"
st.markdown(html_message, unsafe_allow_html=True)
html_message0 = "<p style='text-align: center; font-size: small;'>新しい居住地。<br>転勤で引越しをするときは慌ただしく転居先を決める必要があります。<br>見知らぬ地への転勤であなたは大事にしたいポイントを押さえられていますか。<br>あなたが物件選びで重視したいポイントを教えてください。<br>「最終判断後押しくん」は物件情報だけではわからない、あなたが大事にするポイントをスコア化して<br>物件の最終決め手を後押しします。</p>"
st.markdown(html_message0, unsafe_allow_html=True)

############################################################################################

image1 = Image.open('image1.png')
st.image(image1, use_column_width=True)

############################################################################################

# # 画像のファイル名
# image_filenames = ["workscore.png", "livingscore.png", "childscore.png", "safetyscore.png"]

# # 画像のフルパスリストを作成
# image_paths = [image_directory + filename for filename in image_filenames]

# # 画像を読み込んでリサイズ
# images = [Image.open(image_path).resize((300, 300)) for image_path in image_paths]

# # 列の数を指定
# num_columns = len(images)

# # 列を作成
# columns = st.columns(num_columns)

# # 画像を列に表示
# for i, column in enumerate(columns):
#     column.image(images[i], caption=f"Image {i+1}")

#############################################################################################    

    

# フォームごとに異なるキーを指定
key0 = 'form0'
key1 = 'form1'
key2 = 'form2'
key3 = 'form3'

#住所入力
html_message1 = "<p style='text-align: center; font-size: small;'>勤務先の住所を入力してください</p>"
st.markdown(html_message1, unsafe_allow_html=True)
office = st.text_input("", key=key0)

# URL入力
html_message2 = "<p style='text-align: center; font-size: small;'>検討している物件のURLを3件まで入力してください</p>"
st.markdown(html_message2, unsafe_allow_html=True)

URL1 = st.text_input("", key=key1)
URL2 = st.text_input("", key=key2)
URL3 = st.text_input("", key=key3)

