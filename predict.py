# B站视频播放量预测分析（进阶加分模块）
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
import os

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

if not os.path.exists("image"):
    os.mkdir("image")

def play_predict():
    """
    播放量预测模型
    特征：点赞数、投币数、收藏数、弹幕数
    目标：预测播放量
    """
    # 1. 读取清洗好的数据
    df = pd.read_csv("data/bilibili_hot_clean.csv", encoding="utf-8-sig")
    print("✅ 数据加载成功，共", len(df), "条")

    # 2. 选择特征（影响播放量的因素）
    features = ["点赞数", "投币数", "收藏数", "弹幕数"]
    X = df[features]
    y = df["播放量"]

    # 3. 划分训练集 & 测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. 训练线性回归模型
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 5. 模型预测
    y_pred = model.predict(X_test)

    # 6. 模型评估（报告里必须写！）
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print("\n===== 模型评估结果 =====")
    print(f"R² 决定系数：{r2:.2f}")
    print(f"平均绝对误差：{mae:.0f}")
    print("======================\n")

    # 7. 特征重要性（哪个指标对播放量影响最大）
    print("📊 特征对播放量影响权重：")
    for f, w in zip(features, model.coef_):
        print(f"{f}：{w:.2f}")

    # 8. 绘制预测结果对比图
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.7, color="#4169e1")
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--")
    plt.title("播放量真实值 ↔ 预测值 对比")
    plt.xlabel("真实播放量")
    plt.ylabel("预测播放量")
    plt.tight_layout()
    plt.savefig("image/播放量预测结果.png", dpi=300)
    plt.close()

    print("\n🎉 预测分析完成！图表已保存至 img/")
    print("✅ 加分项【播放量预测】已完成！")

if __name__ == "__main__":
    play_predict()