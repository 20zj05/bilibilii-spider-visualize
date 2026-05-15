# bilibilii-spider-visualize
py选修课大作业，一个爬虫可视化

```plantuml
项目说明
│
├── .venv/                  
├── data/                   # 数据文件夹：原始数据 + 清洗后数据
│   ├── bilibili_hot_raw.csv    # 爬虫爬下来的原始数据
│   └── bilibili_hot_clean.csv  # 清洗完成、可分析的数据
│
├── img/                    # 可视化图表自动保存到这里（报告用）
│
├── spider.py            # 第1步：B站热门爬虫代码
├── clean.py             # 第2步：数据清洗代码
├── visualize.py         # 第3步：画图 + 分析代码
├── requirements.txt        # 依赖文件
└── README.md               # 项目说明

```