import numpy as np


if __name__ == "__main__":
    # * =============== 1. ndarray 的创建 ==============

    ## 1.1 从列表创建数组
    ### 一维数组
    arr1 = np.array([1, 2, 3, 4, 5])
    print(f"一维数组: {arr1}")
    print(f"形状: {arr1.shape}")

    ### 二维数组
    arr2 = np.array(
        [
            [1, 2, 3],
            [4, 5, 6],
        ]
    )
    print(f"二维数组:\n{arr2}")
    print(f"形状: {arr2.shape}")  # (2, 3) 表示2行3列

    ### 三维数组（可以理解为二维 Table 中的样本特征全为一维 List）
    arr3 = np.array(
        [
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]],
        ]
    )
    print(f"三维数组:\n{arr3}")
    print(f"形状: {arr3.shape}")  # (2, 2, 2)

    ## 1.2 特殊创建函数

    ### 全零数组
    zeros = np.zeros((3, 4))  # 3x4的全零数组
    print(f"全零数组:\n{zeros}")

    ### 全一数组
    ones = np.ones((2, 3))
    print(f"全一数组:\n{ones}")

    ### 单位矩阵
    identity = np.eye(3)  # 3x3单位矩阵
    print(f"单位矩阵:\n{identity}")

    ### 指定值填充
    full_array = np.full((2, 2), 7)  # 2x2数组，所有元素为7
    print(f"指定值数组:\n{full_array}")

    ### 等差数列
    arange_arr = np.arange(0, 10, 2)  # 起点0，终点10（不包含），步长2
    print(f"等差数列: {arange_arr}")

    ### 等间隔数列
    linspace_arr = np.linspace(0, 1, 5)  # 0到1之间生成5个等间距的数
    print(f"等间隔数列: {linspace_arr}")

    ### 随机数组
    random_arr = np.random.random((2, 3))  # 2x3的随机数数组（0-1之间）
    print(f"随机数组:\n{random_arr}")

    ## 1.3 数组属性

    print(f"数组: \n{arr3}")
    print(f"维度: {arr3.ndim}")  # 维度数
    print(f"形状: {arr3.shape}")  # 各维度大小
    print(f"大小: {arr3.size}")  # 总元素个数
    print(f"数据类型: {arr3.dtype}")  # 数据类型
    print(f"元素字节大小: {arr3.itemsize}")  # 每个元素占的字节数

    # * =============== 2. ndarray 索引、切片 ==============

    arr = np.array(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
        ]
    )

    ## 2.1 基本索引
    print(f"第一行第二列: {arr[0, 1]}")  # 注意：索引从0开始
    print(f"最后一行: {arr[2, :]}")
    print(f"最后一列: {arr[:, 3]}")

    ## 2.2 切片操作
    print(f"前两行: \n{arr[0:2, :]}")
    print(f"第2-3列: \n{arr[:, 1:3]}")
    print(f"右下角2x2子数组: \n{arr[1:3, 2:4]}")

    ## 2.3 负索引
    print(f"最后一行: {arr[-1, :]}")
    print(f"倒数第二列: {arr[:, -2]}")

    ## 2.4 布尔索引
    print(f"大于10的元素:\n{arr[arr > 10]}")
    print(f"第一列大于5的行:\n{arr[arr[:, 0] > 5, :]}")

    # * =============== 3. ndarray 操作 ==============

    ## 3.1 形状操作

    arr = np.arange(12)  # [0, 1, 2, ..., 11]
    print(f"原始数组: {arr}")

    # 改变形状
    reshaped = arr.reshape(3, 4)
    print(f"重塑为3x4:\n{reshaped}")

    # 展平数组
    flattened = reshaped.flatten()
    print(f"展平后: {flattened}")

    # 转置
    transposed = reshaped.T
    print(f"转置后:\n{transposed}")

    # 增加维度
    expanded = np.expand_dims(arr, axis=0)  # 在第0维增加一个维度
    print(f"扩展维度后形状: {expanded.shape}")

    ## 3.2 数组连接

    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    # 垂直连接（按行）
    vertical = np.vstack((a, b))
    print(f"垂直连接:\n{vertical}")

    # 水平连接（按列）
    horizontal = np.hstack((a, b))
    print(f"水平连接:\n{horizontal}")

    # 沿指定轴连接
    concatenated = np.concatenate((a, b), axis=1)  # axis=1表示沿列方向
    print(f"连接结果:\n{concatenated}")

    ## 3.3 数组拆分 (分割)

    ### 垂直拆分
    v_split = np.vsplit(vertical, 2)  # 拆分为2个子数组
    print("垂直拆分结果:\n")
    for arr in v_split:
        print(arr)

    ### 水平拆分
    h_split = np.hsplit(horizontal, 2)  # 拆分为2个子数组
    print("水平拆分结果:\n")
    for arr in h_split:
        print(arr)

    ## 3.4 数组复制
    original = np.array([1, 2, 3])
    shallow_copy = (
        original.view()
    )  # 浅复制，等同于 shallow_copy = original，相当于指针引用
    deep_copy = original.copy()  # 深复制
    original[0] = 10
    print(f"原始数组: {original}")  # [10, 2, 3]
    print(f"浅复制数组: {shallow_copy}")  # [10, 2, 3] (受影响)
    print(f"深复制数组: {deep_copy}")  # [1, 2, 3] (不受影响)

    # * =============== 4. 数组运算 ==============

    ## 4.1 基本算术运算

    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])

    ### 元素级运算
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")
    print(f"a ** 2 = {a**2}")  # 平方

    ### 数组与标量运算
    print(f"a + 10 = {a + 10}")
    print(f"a * 2 = {a * 2}")

    ## 4.2 矩阵运算

    A = np.array(
        [
            [1, 2],
            [3, 4],
        ]
    )
    B = np.array(
        [
            [5, 6],
            [7, 8],
        ]
    )

    ### 矩阵乘法
    matrix_mult = np.dot(A, B)
    print(f"矩阵乘法:\n{matrix_mult}")

    ### 另一种写法
    matrix_mult2 = A @ B
    print(f"矩阵乘法(@):\n{matrix_mult2}")

    ### 元素级乘法
    element_mult = A * B
    print(f"元素级乘法:\n{element_mult}")

    ## 4.3 统计函数

    data = np.array(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    )

    print(f"Matrix:\n{data}")
    print(f"总和: {np.sum(data)}")
    print(f"均值: {np.mean(data)}")
    print(f"标准差: {np.std(data)}")
    print(f"方差: {np.var(data)}")
    print(f"最大值: {np.max(data)}")
    print(f"最小值: {np.min(data)}")
    print(f"最大值位置: {np.argmax(data)}")

    ### 沿特定轴计算
    print(f"每列的和: {np.sum(data, axis=0)}")  # axis=0表示沿行方向（对列求和）
    print(f"每行的和: {np.sum(data, axis=1)}")  # axis=1表示沿列方向（对行求和）
    print(f"每列的均值: {np.mean(data, axis=0)}")
    print(f"每行的均值: {np.mean(data, axis=1)}")

    # * =============== 5. 条件操作和布尔索引 ==============

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    ## 布尔条件
    condition = arr > 5
    print(f"大于5的条件: {condition}")

    ## 布尔索引
    filtered = arr[arr > 5]
    print(f"大于5的元素: {filtered}")

    ## 多重条件
    result = arr[(arr > 3) & (arr < 8)]  # 注意：使用&而不是and
    print(f"3到8之间的元素: {result}")

    ## where函数
    replaced = np.where(arr > 5, "大", "小")
    print(f"条件替换: {replaced}")

    ## nonzero函数
    indices = np.nonzero(arr > 7)
    print(f"大于7的元素索引: {indices}")

    # * =============== 6. 广播机制（Broadcasting） =============

    # 广播允许不同形状的数组进行算术运算
    a = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3
    b = np.array([10, 20, 30])  # 1x3

    # b会被自动广播到2x3的形状
    result = a + b
    print(f"广播加法:\n{result}")

    # 标量广播
    c = 100
    result2 = a + c
    print(f"标量广播:\n{result2}")

    # * =============== 7. 其他实用函数 ==============

    ## 排序
    arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

    sorted_arr = np.sort(arr)
    print(f"排序后: {sorted_arr}")

    ### 获取排序索引
    indices = np.argsort(arr)
    print(f"排序索引: {indices}")

    ## 唯一值
    arr = np.array([1, 2, 2, 3, 3, 3, 4])
    unique_vals = np.unique(arr)
    print(f"唯一值: {unique_vals}")

    ## 计数
    counts = np.bincount(arr)
    print(f"计数: {counts}")

    ## 随机选择
    arr = np.array([10, 20, 30, 40, 50])
    random_choice = np.random.choice(arr, size=3, replace=False)  # 不重复选择3个元素
    print(f"随机选择: {random_choice}")

    ## 排列
    arr = np.array([1, 2, 3, 4, 5])
    permuted = np.random.permutation(arr)
    print(f"随机排列: {permuted}")

    ## clip
    arr = np.array([-10, 0, 10, 20, 30])
    clipped = np.clip(arr, 0, 20)  # 将值限制在0到20之间
    print(f"裁剪后: {clipped}")

    # * ============== 8. 实际案例演示 ==============

    ## 图像处理
    print("===== 图像处理示例 =====")

    # 假设我们有一个灰度图像，使用二维数组表示
    # np.random.seed(0)  # 为了结果可复现

    # 创建 image 数据矩阵 (5x5)，值在0-255之间
    image = np.random.randint(0, 256, (5, 5))

    print(f"原始图像:\n{image}")

    # 图像增强：提高亮度
    brighter = np.clip(image + 50, 0, 255)  # clip限制在0-255之间
    print(f"提亮后:\n{brighter}")

    # 图像反转（负片效果）
    inverted = 255 - image
    print(f"反转后:\n{inverted}")

    ## 机器学习中的数据预处理
    print("===== 机器学习数据预处理示例 =====")
    # 假设我们有一个数据集，每行是一个样本，每列是一个特征
    X = np.array(
        [
            [85, 90, 78, 92],  # sample 1
            [76, 88, 82, 85],  # sample 2
            [92, 95, 89, 94],  # sample 3
        ]
    )
    print(f"原始数据:\n{X}")

    # 指定 axis=0，沿着行方向（对每列）计算均值
    mean_axis0 = np.mean(X, axis=0)
    print(f"沿着行方向（每列）的均值:{mean_axis0}")

    # 每列减去列均值（特征中心化）
    X_centered = X - mean_axis0
    print(f"特征中心化后的结果:\n{X_centered}")

    # 特征标准化（Standardization）
    print("===== 特征标准化 =====")
    std_axis0 = np.std(X, axis=0)
    print(f"每列的标准差:{std_axis0}")

    X_standardized = (X - mean_axis0) / std_axis0  # (x - mean) / std
    print(f"特征标准化后的结果:\n{X_standardized}")

    print(f"标准化后每列的均值:{np.mean(X_standardized, axis=0)}")  # 接近 0
    print(f"标准化后每列的标准差:{np.std(X_standardized, axis=0)}")  # 接近 1

    # 特征归一化（Normalization）
    print("===== 特征归一化 =====")
    X_min = np.min(X, axis=0)
    X_max = np.max(X, axis=0)
    print(f"每列的最小值:{X_min}")
    print(f"每列的最大值:{X_max}")

    print(f"每列减去最小值:\n{X - X_min}")
    print(f"每列的范围:\n{X_max - X_min}")
    X_normalized = (X - X_min) / (X_max - X_min)  # (x - min) / (max - min)
    print(f"特征归一化后的结果:\n{X_normalized}")

    print(f"归一化后每列的最小值:{np.min(X_normalized, axis=0)}")  # 0.0
    print(f"归一化后每列的最大值:{np.max(X_normalized, axis=0)}")  # 1.0
