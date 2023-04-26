import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'
latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Interation {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'



left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く１')
expander.write('問い合わせ内容を書く２')
expander.write('問い合わせ内容を書く３')
expander.write('問い合わせ内容を書く４')
expander.write('問い合わせ内容を書く５')

# text = st.text_input('あなたの趣味は？')
# condition = st.slider('今の調子は？',0,100,66)

# 'あなたの趣味：',text
# 'コンディション：',condition



# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='李亜夢', use_column_width=True)

# st.table(df.style.highlight_max(axis=0))



#    df = pd.DataFrame(
#    np.random.rand(100, 2)/[50,50] + [35.69, 139.70],#新宿付近
#    columns=['lat','lon'] #緯度、経度、
#)
#st.map(df)
