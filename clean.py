# 02_clean.py
import pandas as pd
import os

# 读取原始数据
df = pd.read_csv("data/bilibili_hot_raw.csv", encoding="utf-8-sig")
print("清洗前数据总量：", len(df))

# 基础数据清洗
# 1. 去除重复数据
df.drop_duplicates(subset=["标题", "UP主"], inplace=True)
# 2. 剔除播放量为空/异常数据
df = df[df["播放量"] > 0]
# 3. 重置索引
df.reset_index(drop=True, inplace=True)

# 保存清洗后数据
df.to_csv("data/bilibili_hot_clean.csv", index=False, encoding="utf-8-sig")
print("数据清洗完成，有效数据总量：", len(df))
print("清洗后数据已保存至 data/bilibili_hot_clean.csv")