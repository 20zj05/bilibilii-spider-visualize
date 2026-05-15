# 01_spider.py
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

# 设置中文字体，防止可视化图表中文乱码（Windows系统常用SimHei，Mac系统可用Arial Unicode MS）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def fetch_bilibili_rankings():
    """
    1. 数据抓取模块：通过B站官方API获取排行榜数据
    """
    # 伪装成真实浏览器，规避基础反爬
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://www.bilibili.com/'
    }

    # B站排行榜API接口
    url = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'

    try:
        print("正在爬取B站排行榜数据...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 检查HTTP请求是否成功
        data = response.json()

        if data['code'] == 0:
            video_list = []
            # 2. 数据解析与提取
            for item in data['data']['list']:
                video_info = {
                    '排名': item.get('rank', 0),
                    '标题': item.get('title', ''),
                    'UP主': item.get('owner', {}).get('name', ''),
                    '播放量': item.get('stat', {}).get('view', 0),
                    '弹幕数': item.get('stat', {}).get('danmaku', 0),
                    '点赞数': item.get('stat', {}).get('like', 0),
                    '投币数': item.get('stat', {}).get('coin', 0),
                    '收藏数': item.get('stat', {}).get('favorite', 0),
                    '分享数': item.get('stat', {}).get('share', 0),
                    '分区': item.get('tname', ''),
                    '视频时长(秒)': item.get('duration', 0),
                    '综合得分': item.get('pts', 0)
                }
                video_list.append(video_info)
            print(f"成功爬取 {len(video_list)} 条视频数据！")
            return video_list
        else:
            print(f"API请求失败，错误码: {data['message']}")
            return []
    except Exception as e:
        print(f"爬取过程中发生异常: {str(e)}")
        return []


if __name__ == "__main__":
    raw_data = fetch_bilibili_rankings()
    if raw_data:
        df_raw = pd.DataFrame(raw_data)
        df_raw.to_csv("data/bilibili_hot_raw.csv", index=False, encoding="utf-8-sig")
        print("原始爬虫数据已保存至 data/bilibili_hot_raw.csv")