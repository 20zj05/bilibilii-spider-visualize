# 03_visualize.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 全局字体配置，和你代码保持一致
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建图片保存文件夹
if not os.path.exists("image"):
    os.mkdir("image")

def save_and_analyze():
    """
    3. 数据存储与可视化分析模块
    """
    # 读取清洗后数据
    df = pd.read_csv("data/bilibili_hot_clean.csv", encoding="utf-8-sig")

    # --- 简单的数据分析与可视化 ---
    # 分析1：各分区上榜视频数量 Top 10
    plt.figure(figsize=(12, 6))
    area_counts = df['分区'].value_counts().head(10)
    sns.barplot(x=area_counts.index, y=area_counts.values, palette='viridis')
    plt.title('B站排行榜各分区视频数量分布 (Top 10)', fontsize=16)
    plt.xlabel('分区名称', fontsize=12)
    plt.ylabel('视频数量', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("image/分区分布图.png", dpi=300)
    print("已生成【分区分布图.png】")

    # 分析2：播放量与互动数据（点赞、投币）的关系
    plt.figure(figsize=(10, 6))
    plt.scatter(df['播放量'], df['点赞数'], alpha=0.6, label='点赞数')
    plt.scatter(df['播放量'], df['投币数'], alpha=0.6, label='投币数')
    plt.title('视频播放量与点赞/投币数关系图', fontsize=16)
    plt.xlabel('播放量', fontsize=12)
    plt.ylabel('互动数量', fontsize=12)
    plt.legend()
    plt.tight_layout()
    plt.savefig("image/播放互动关系图.png", dpi=300)
    print("已生成【播放互动关系图.png】")
    plt.close('all')

if __name__ == "__main__":
    save_and_analyze()