import pandas as pd

# 식품 섭취 데이터는 사용하지 않는 것으로 결정(2018-11-15)
df_ALL = pd.read_sas("./HN16_ALL.sas7bdat", format = 'sas7bdat', encoding='iso-8859-1')
# df_ffq = pd.read_sas("./hn16_ffq.sas7bdat", format = 'sas7bdat', encoding='iso-8859-1')

# 19세 이상으로만 제한
df_data = df_ALL.loc[(18 < df_ALL.age), :]
# df_data.shape

# 혈압치료중인 대상 제외
df_data = df_data.loc[(1 < df_data.DI1_pt) | (df_data.DI1_pt < 1), :]
# df_data.shape

# 모든 값이 NaN값이 컬럼 삭제
df_data = df_data.dropna(axis=1, how='all')
# df_data.shape

# 고혈압 유병여부 NaN값 대상 삭제
df_data = df_data.dropna(subset=['HE_HP'])
# df_data.shape

# index 재 생성을 위해 ID로 인덱스 생성 후 인덱스 삭제
df_data =  df_data.set_index('ID')
df_data = df_data.reset_index()

# 고혈압 유병여부
# 1. 정상
# 2. 고혈압전단계
# 3. 고혈압
# classification을 위해3. 고혈압을 2.로 변경하여 이산형으로 수정

#df_data.loc[df_data.HE_HP == 3.0, 'HE_HP'] = 2.0
print("HE_HP :\n")
print(pd.value_counts(df_data.HE_HP.values, sort=False).sort_index()) # 고혈압 유병 여부