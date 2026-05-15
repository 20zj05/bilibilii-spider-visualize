# 01_spider.py  最终稳定版（B站官方API）
import requests
import pandas as pd
import os
import time

# 创建数据文件夹
if not os.path.exists("data"):
    os.mkdir("data")

# B站 全站热门榜 官方API（最稳定，永不失效）
url = "https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.bilibilibili.com/"
}

print("正在从 B站官方API 获取热门数据...")

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()

    # 提取视频列表
    video_list = data["data"]["list"]
    result = []

    for video in video_list:
        # 安全获取数据
        title = video.get("title", "")
        bvid = video.get("bvid", "")
        up_name = video["owner"].get("name", "")
        play = video["stat"].get("view", 0)
        danmaku = video["stat"].get("danmaku", 0)
        like = video["stat"].get("like", 0)
        favorite = video["stat"].get("favorite", 0)
        share = video["stat"].get("share", 0)
        pub_time = video.get("pubdate", 0)

        result.append({
            "排名": len(result) + 1,
            "标题": title,
            "BV号": bvid,
            "UP主": up_name,
            "播放量": play,
            "弹幕数": danmaku,
            "点赞数": like,
            "收藏数": favorite,
            "分享数": share,
            "发布时间": pub_time
        })

    # 保存CSV
    df = pd.DataFrame(result)
    df.to_csv("data/bilibili_hot_raw.csv", index=False, encoding="utf-8-sig")

    print(f"\n✅ 爬取成功！共 {len(result)} 条数据")
    print("📁 已保存到：data/bilibili_hot_raw.csv")

except Exception as e:
    print("❌ 出错了：", e)