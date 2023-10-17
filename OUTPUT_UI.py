import streamlit as st
import pandas as pd
import random

# Streamlitアプリのタイトル
st.title("最終判断あと押し君")


# 重要度の入力を横並びにする
col1, col2, col3, col4 = st.columns(4)
weight_work = col1.number_input('働きやすさの重要度　 (%): ', min_value=0, max_value=100, step=1)
weight_life = col2.number_input('暮らしやすさの重要度 (%): ', min_value=0, max_value=100, step=1)
weight_kids = col3.number_input('育てやすさの重要度　 (%): ', min_value=0, max_value=100, step=1)
weight_safe = col4.number_input('安心しやすさの重要度 (%): ', value=100 - weight_work - weight_life - weight_kids, min_value=0, max_value=100, step=1)


# 暮らしやすさの重要度と内訳の入力
life_expander = st.expander("暮らしやすさの詳細", expanded=False)
with life_expander:
    hospital_weight = st.number_input('病院の重要度 (%): ', value=33, min_value=0, max_value=100, step=1)
    supermarket_weight = st.number_input('スーパーの重要度 (%): ', value=33, min_value=0, max_value=100, step=1)
    restaurant_weight = 100 - hospital_weight - supermarket_weight
    st.write(f'飲食店の重要度: {restaurant_weight}%')

# 育てやすさの重要度と内訳の入力
kids_expander = st.expander("育てやすさの詳細", expanded=False)
with kids_expander:
    nursery_weight = st.number_input('保育園の重要度 (%): ', value=25, min_value=0, max_value=100, step=1)
    elementary_weight = st.number_input('小学校の重要度 (%): ', value=25, min_value=0, max_value=100, step=1)
    kindergarten_weight = st.number_input('幼稚園の重要度 (%): ', value=25, min_value=0, max_value=100, step=1)
    park_weight = 100 - nursery_weight - elementary_weight - kindergarten_weight
    st.write(f'公園の重要度: {park_weight}%')

# 残りの重要度を自動計算
weight_safe = 100 - weight_work - weight_life - weight_kids
st.write(f"安心しやすさの重要度: {weight_safe}%")

# 好みの食事ジャンル入力
place_name_favorite = st.text_input("好みの食事ジャンル(例：ラーメン):")


# 住所入力
addresses = [st.text_input(f'候補物件{i+1}の住所: ') for i in range(3)]
workplace = st.text_input('勤務地の住所: ')


# スコアリングロジックを実装 (今回はサンプルとしてランダムなスコアを生成)
def scoring_logic(address):
    return random.randint(50, 100)

# ...[前述のコード]...

# ボタンがクリックされたかどうかの状態を初期化
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

if st.button("Score Check!"):
    # 各入力値の合計が100であることを確認
    if (hospital_weight + supermarket_weight + restaurant_weight != 100) or (nursery_weight + elementary_weight + kindergarten_weight + park_weight != 100):
        st.error("各小項目の重要度の合計が100%になるようにしてください。")
    else:
        st.session_state.button_clicked = True

if st.session_state.button_clicked:
    # ここで各住所のスコアリングを行う
    data_output = []
    for address in addresses:
        scores = {
            "候補物件住所": address,
            "総スコア": random.randint(50, 100),
            "働きやすさスコア": random.randint(50, 100),
            "生活スコア": random.randint(50, 100),
            "子育てスコア": random.randint(50, 100),
            "安心スコア": random.randint(50, 100),
        }
        data_output.append(scores)
    df_output = pd.DataFrame(data_output)
    st.write(df_output)

    # 生活スコアの詳細
    if st.checkbox('生活スコアの詳細を見る'):
        columns = st.columns(3)
        for i, address in enumerate(addresses):
            with columns[i]:
                st.write(f"住所: {address}")
                st.write(f"スーパーの施設数: {random.randint(1, 10)}")
                st.write(f"最も近いスーパーの名前: {'スーパー' + str(random.randint(1, 10))}")
                st.write(f"最も近いスーパーまでの所要時間(徒歩): {random.randint(5, 15)}分")
                # ...[略]...

    # 子育てスコアの詳細
    if st.checkbox('子育てスコアの詳細を見る'):
        columns = st.columns(3)
        for i, address in enumerate(addresses):
            with columns[i]:
                st.write(f"住所: {address}")
                st.write(f"保育園数: {random.randint(1, 5)}")
                st.write(f"最も近い保育園の名前: {'保育園' + str(random.randint(1, 5))}")
                st.write(f"最も近い保育園までの所要時間: {random.randint(5, 15)}分")
                # ...[略]...