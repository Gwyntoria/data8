import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    """
    ## Plotting Example
    This is a simple example of how to create a plot using Matplotlib.
    """

    print(plt.get_backend())  # 输出当前使用的后端

    plt.ion()  # 开启交互模式

    # 生成一些数据
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # 创建一个图形和坐标轴
    plot_fig = plt.figure()
    plt.plot(x, y, label="sin(x)", color="blue", linewidth=2, linestyle="-")
    plt.title("Sin Curve")
    plt.xlabel("X")
    plt.ylabel("Sin(x)")
    plt.grid(True)  # 添加网格线
    plt.legend(loc="upper right")  # 添加图例

    # 添加注释
    plt.annotate(
        "Peak",
        xy=(np.pi / 2, 1),
        xytext=(2, 1.2),
        arrowprops=dict(facecolor="black", shrink=0.05),
    )

    # 保存图片
    # plt.savefig("sin_curve_example.png")
    # 显示图形
    plot_fig.show()

    # 直方图
    plt.figure()
    data = np.random.randn(1000)
    plt.hist(data, bins=30, color="skyblue", edgecolor="black")
    plt.title("Histogram")
    plt.show()

    # 散点图
    plt.figure()
    x = np.random.rand(50)
    y = np.random.rand(50)
    plt.scatter(x, y, color="red")
    plt.title("Scatter Plot")
    plt.show()

    # 条形图
    plt.figure()
    categories = ["A", "B", "C", "D"]
    values = [10, 15, 7, 20]
    plt.bar(categories, values, color="green")
    plt.title("Bar Chart")
    plt.show()

    # 使用多个子图同时显示多张图片
    sub_fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    # 第一张子图：正弦曲线
    axs[0, 0].plot(
        np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100)), color="blue"
    )
    axs[0, 0].set_title("Sin Curve")

    # 第二张子图：直方图
    data = np.random.randn(1000)
    axs[0, 1].hist(data, bins=30, color="skyblue", edgecolor="black")
    axs[0, 1].set_title("Histogram")

    # 第三张子图：散点图
    x = np.random.rand(50)
    y = np.random.rand(50)
    axs[1, 0].scatter(x, y, color="red")
    axs[1, 0].set_title("Scatter Plot")

    # 第四张子图：条形图
    categories = ["A", "B", "C", "D"]
    values = [10, 15, 7, 20]
    axs[1, 1].bar(categories, values, color="green")
    axs[1, 1].set_title("Bar Chart")

    # 调整布局
    sub_fig.tight_layout()
    # 显示图形
    plt.show()
    plt.pause(2)

    # 关闭所有图形以释放内存
    plt.close("all")

    # 实现一个持续绘画的折线图
    plt.ion()  # 开启交互模式
    fig, ax = plt.subplots()
    x_data_list, y_data_list = [], []
    (line_list,) = ax.plot(x_data_list, y_data_list, color="blue")

    ax.set_xlim(0, 10)
    ax.set_ylim(-1.5, 1.5)
    ax.set_title("Dynamic Line Plot")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    for i in range(100):
        x_data_list.append(i * 0.1)
        y_data_list.append(np.sin(i * 0.1))
        line_list.set_xdata(x_data_list)
        line_list.set_ydata(y_data_list)
        ax.set_xlim(0, max(x_data_list) + 1)  # 动态调整x轴范围
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.1)  # 暂停以显示更新

    # plt.ioff()  # 关闭交互模式
    plt.show()
    plt.pause(2)  # 如果 plt.ioff() 被注释掉，则需要这行代码来暂停显示
    plt.close("all")  # 关闭所有图形以释放内存
