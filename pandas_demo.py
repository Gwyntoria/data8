try:
    from io import StringIO

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

except Exception as e:
    print("缺少必要库或导入失败：", e)
    print("请确保已安装 pandas 和 numpy：pip install pandas numpy")
    raise SystemExit(1)

print("pandas 版本：", pd.__version__)
print("numpy 版本：", np.__version__)
print("\n")

# --------------------------------------------------
# 1) Series 与 DataFrame 的基础
# --------------------------------------------------

# ! Series 和 DataFrame 的定义与关系
# * Series：一维的数据结构，可以看作是带标签的一维数组。
# *     由两部分组成：索引（index） + 数据（values）。
# *     类似 Python 的字典（键 == 索引，值 == 数据），但顺序固定且支持向量化运算。
# * DataFrame：二维的数据结构，可以看作是多个 Series 按列组合而成的表格。
# *     行索引（row index） + 列索引（column index）。
# *     每一列本质上就是一个 Series。
# *     类似电子表格或 SQL 表格，支持复杂的数据操作与分析。

# * DataFrame 是 Series 的容器：
# *     DataFrame 的每一列 == 一个 Series（共享相同的行索引）。
# *     DataFrame 相当于一个“有序的 Series 字典”。

# ! 增删改查
# * 新增列直接赋值 df["new_col"] = ...
# * 新增行使用 pd.concat([...])

# * 删除列使用 df.drop(columns=[...])
# * 删除行使用 df.drop(index=[...])

# * 修改数据推荐使用 loc 定位，避免链式赋值警告（SettingWithCopyWarning）。
# *     df.loc[row_condition] 用于查询行，row_condition 是布尔索引，例如 df["col"] > val 生成的 Series。
# *     df.loc[df["col"] > val, "col"] = new_val
# *     第一个参数是行选择条件，第二个参数是列名。
# *     批量修改列数据可使用向量化操作或 apply 函数。
# *     批量修改行数据可结合 loc 和布尔索引。
# *     避免直接对筛选结果赋值（链式赋值），推荐使用 loc。

# * 新增和修改都会改变原 DataFrame，除非使用 inplace=False（默认）。
# * 删除默认返回新 DataFrame，不改变原 df，除非 inplace=True。


print("== 1. Series 与 DataFrame 基础 ==\n")

# 创建 Series
s = pd.Series([10, 20, 30], index=["a", "b", "c"], name="example_series")
print("Series 示例：\n", s)

# 创建 DataFrame
df = pd.DataFrame(
    {
        "name": ["Alice", "Bob", "Cathy"],
        "age": [25, 30, 22],
        "score": [85.5, 92.3, 78.0],
    }
)
print("\nDataFrame 示例：")
print(df)

print("\ndf.head() =>")
print(df.head())

print("\ndf.info() =>")
df.info()

print("\ndf.describe() =>")
print(df.describe(include="all"))
print("\n")

# --------------------------------------------------
# 2) 选择、索引与切片（loc / iloc / 布尔索引）
# --------------------------------------------------

print("== 2. 索引与选择 ==\n")

print("选择 name 列 =>\n", df["name"])
print("\n使用 loc 按标签选择第一行 df.loc[0] =>\n", df.loc[0])
print("\n使用 iloc 按位置选择第一行第一列 df.iloc[0, 0] =>", df.iloc[0, 0])

# 布尔索引
age_bool_indices = df["age"] > 23
print("\n布尔索引条件 (age > 23) =>\n", age_bool_indices)
print("\n布尔索引（选择 age > 23）=>\n", df[age_bool_indices])

# 复合选择
print("\n复合使用 loc：选择 age > 23 的 name 列 =>\n", df.loc[age_bool_indices, "name"])
print("\n")

# --------------------------------------------------
# 3) 列/行的增加、删除与修改
# --------------------------------------------------

print("== 3. 列/行的增加、删除与修改 ==\n")

# 新增列
df["passed"] = df["score"] > 80  # df["score"] > 80 创建了一个布尔 Series
print("新增列 passed:\n", df)

# 删除列（返回新 DF，不改变原 df）
df2 = df.drop(columns=["score"])
print("\n删除 score 列后的 df2:\n", df2)

# 新增行
new_row = pd.DataFrame(
    {
        "name": ["David"],
        "age": [28],
        "score": [88.0],
        "passed": [True],
    }
)
df = pd.concat([df, new_row], ignore_index=True)
print("\n新增一行 David 后的 df:\n", df)

# 删除行
df_drop = df.drop(index=1)  # 删除第二行（Bob 的数据）
print("\n删除 Bob 后的 df_drop:\n", df_drop)

# 使用查询删除行
df_drop_2 = df.drop(df[df["name"] == "Bob"].index)
print("\n删除所有名字为 Bob 的行后的 df_drop_2:\n", df_drop_2)

# 修改数据
df.loc[df["name"] == "Bob", "score"] = 95.0
print("\n修改 Bob 的 score 后:\n", df)

# 批量修改列数据
print("\n批量修改列数据示例：")

# 示例：将 name 列的所有值转换为大写
df["name"] = df["name"].str.upper()
print("\n将 name 列转换为大写：\n", df)

# 示例：对 age 列加 1
df["age"] = df["age"] + 1
print("\n将 age 列加 1：\n", df)

# 将 age 列加 2，score 列减 5
df.loc[df["age"] > 25, "age"] += 2
df.loc[df["score"] > 95, "score"] -= 5
print("\n批量修改 age 列加 2，score 列减 5：\n", df)

# 批量修改行数据示例：
print("\n批量修改行数据示例：")

# 示例：对 score 列应用自定义函数（如平方）
df["score"] = df["score"].apply(lambda x: x**2 if pd.notnull(x) else x)
print("\n将 score 列平方（忽略缺失值）：\n", df)

# 更改数据类型
print("\n将 age 转为 int（示例）：")
df["age"] = df["age"].astype("int64")
print(df.dtypes)
print("\n")

# --------------------------------------------------
# 4) 读取与写入（示例使用内存 CSV）
# --------------------------------------------------
print("== 4. IO: 读取与写入 (CSV 示例) ==\n")
csv_data = """id,name,age,score
1,Alice,25,85.5
2,Bob,30,92.3
3,Cathy,22,78.0
"""

print("使用 pandas.read_csv 从内存字符串读取示例 CSV：")
df_csv = pd.read_csv(StringIO(csv_data))
print(df_csv)

# 写出到 CSV（内存）
buf = StringIO()
df_csv.to_csv(buf, index=False)
print("\n导出 CSV（字符串形式）：\n", buf.getvalue())

# 大文件分块读取（chunksize）示例：
print("\n分块读取演示（chunksize=2）：")
for chunk in pd.read_csv(StringIO(csv_data), chunksize=2):
    print("块：\n", chunk)
print("\n")

# --------------------------------------------------
# 5) 处理缺失值
# --------------------------------------------------
print("== 5. 缺失值处理 ==\n")
df_na = pd.DataFrame(
    {
        "A": [1, None, 3],
        "B": [4, 5, None],
    }
)
print("示例 DataFrame 含缺失值：\n", df_na)
print("isnull():\n", df_na.isnull())  # 检测缺失值
print("notnull():\n", df_na.notnull())  # 检测非缺失值
print("dropna():\n", df_na.dropna())  # 删除含缺失值的行
print("fillna(0):\n", df_na.fillna(0))  # 用 0 填充缺失值
print("\n")

# --------------------------------------------------
# 6) 数据类型转换与优化
# --------------------------------------------------
print("== 6. 数据类型转换与优化 ==\n")
print("示例：将 age 转为 category（当取值有限时可节省内存）：")
df_csv["age_cat"] = df_csv["age"].astype("category")
print(df_csv.dtypes)
print("\n")

# --------------------------------------------------
# 7) 时间序列基础
# --------------------------------------------------
print("== 7. 时间序列基础 ==\n")
ts = pd.DataFrame(
    {
        "date": pd.date_range("2025-01-01", periods=6, freq="D"),
        "value": [10, 12, 13, 15, 14, 16],
    }
)
ts = ts.set_index("date")
print("时间序列示例（索引为 datetime）：\n", ts)
print("\n按 2 天重采样取平均（resample）：\n", ts.resample("2D").mean())
print("\n")

# --------------------------------------------------
# 8) groupby 聚合
# --------------------------------------------------
print("== 8. groupby 聚合 ==\n")
df_sales = pd.DataFrame(
    {
        "store": ["A", "A", "B", "B"],
        "item": ["x", "y", "x", "y"],
        "sales": [10, 15, 7, 9],
    }
)
print("原始销售数据：\n", df_sales)
print("\n按 store 分组汇总 sales.sum():\n", df_sales.groupby("store")["sales"].sum())
print(
    "\n按 store 和 item 分组并同时计算 sum & mean：\n",
    df_sales.groupby(["store", "item"]).agg({"sales": ["sum", "mean"]}),
)
print("\n")

# --------------------------------------------------
# 9) 合并（merge）、拼接（concat）
# --------------------------------------------------
print("== 9. merge 与 concat 示例 ==\n")
left = pd.DataFrame({"id": [1, 2, 3], "name": ["A", "B", "C"]})
right = pd.DataFrame({"id": [1, 3, 4], "score": [90, 80, 70]})
print("left:\n", left)
print("right:\n", right)
print(
    "\nleft merge right on id (left join) =>\n",
    pd.merge(left, right, on="id", how="left"),
)

print("\n行拼接 concat 示例：")
print(pd.concat([left, right], axis=0, ignore_index=True))
print("\n")

# --------------------------------------------------
# 10) pivot_table 与 melt
# --------------------------------------------------
print("== 10. pivot_table 与 melt ==\n")
df_pivot = df_sales.pivot_table(
    index="store", columns="item", values="sales", aggfunc="sum", fill_value=0
)
print("pivot_table 结果：\n", df_pivot)
print(
    "\nmelt 将宽表转成长表：\n",
    df_pivot.reset_index().melt(id_vars="store", value_name="sales"),
)
print("\n")

# --------------------------------------------------
# 11) 类别数据（Categorical）
# --------------------------------------------------
print("== 11. Categorical 示例 ==\n")
df_cat = pd.DataFrame({"color": ["red", "blue", "red", "green"]})
df_cat["color"] = df_cat["color"].astype("category")
print(df_cat)
print("类别信息：", df_cat["color"].cat.categories)
print("\n")

# --------------------------------------------------
# 12) 绘图（需要 matplotlib）
# --------------------------------------------------
print("== 12. 绘图示例 ==\n")
try:
    print("尝试绘制时间序列图（当前环境可能无法显示图形）...")
    ax = ts.plot(title="time series example")
    ax.set_ylabel("value")
    # 在脚本中运行时如果是交互式环境会显示；在非交互环境请保存到文件：
    plt.tight_layout()
    # plt.savefig("pandas_ts_example.png")
    # print("已将图保存为 pandas_ts_example.png")
    plt.ion()
    plt.show()
    plt.pause(1)
    plt.close()
except Exception as e:
    print("绘图失败或 matplotlib 未安装：", e)
print("\n")

# --------------------------------------------------
# 13) 常见陷阱：SettingWithCopyWarning 与 链式赋值
# --------------------------------------------------
print("== 13. 常见陷阱与正确赋值示例 ==\n")
df_warn = pd.DataFrame(
    {
        "age": [20, 25, 30],
        "score": [80, 85, 90],
    }
)
print("原始 df_warn:\n", df_warn)

# 对子表直接赋值会触发 SettingWithCopyWarning
sub = df_warn[df_warn["age"] > 20]
try:
    sub["score"] = sub["score"] * 1.1  # 可能触发警告
    print("sub =>\n", sub)
    print("原 df_warn 未变（因为 sub 是副本）:\n", df_warn)
except Exception as e:
    print("示例赋值出错：\n", e)

# 推荐做法：使用 loc 在原 DataFrame 上操作
df_warn["score"] = df_warn["score"].astype(float)  # 确保是浮点数，避免整数乘法问题
df_warn.loc[df_warn["age"] > 20, "score"] *= 1.1
print("\n使用 loc 修改后的 df_warn:\n", df_warn)
print("\n")
