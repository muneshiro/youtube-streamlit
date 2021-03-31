import streamlit as st 
import pandas as pd
import numpy as np
from PIL import Image 
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'


st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

#st.table(df.style.highlight_max(axis=0))

#"""
# 章
## 節
### 項

#```python
#import streamlit as st 
#import numpy as np
#import pandas as pd
#```
#"""
df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b', 'c'])
df
st.line_chart(df)

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns=['lat', 'lon'])
st.map(df)

st.write('Display Image')



if st.checkbox('Show Image'):
    img = Image.open('IMG_4990.jpg')
    st.image(img, caption='taiwan', use_column_width = True)

option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1,11)),

)

'あなたが好きな数字は', option, 'です。'


st.write('Interactive Widgets')

text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味:', text 

condition = st.slider('あなたの今の調子は', 0, 100, 50)
'コンディション:',condition

left_column, right_column = st.beta_columns(2)
button = left_column.button('右コラムに文字を表示')
if button:
    right_column.write('ここは右コラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')


upload_file = st.file_uploader("Choose an image...", type='jpg')
if upload_file is not None:
    img = Image.open(upload_file)
    st.image(img, caption='Uploaded image.', use_column_width=True)