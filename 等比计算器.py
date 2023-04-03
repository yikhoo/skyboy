import math

# 设置开始价格和结束价格
start_price = 1200
end_price = 1500

# 设置网格数量
n = 12

# 计算步长比率
ratio = math.pow(end_price/start_price, 1/n)

# 初始化网格价格数组
prices = [0] * (n+1)

# 计算每个网格的价格
for i in range(n+1):
    prices[i] = start_price * math.pow(ratio, i)

# 计算最佳盈利比
profit_ratios = [0] * n
for i in range(n):
    profit_ratios[i] = (prices[i+1] - prices[i]) / prices[i]

best_profit_ratio = sum(profit_ratios) / n

# 输出结果
print(f"开始价格：{start_price}")
print(f"结束价格：{end_price}")
print(f"网格数量：{n}")
print(f"步长比率：{ratio}")
print(f"每个网格的价格：{prices}")
print(f"每个网格的盈利比率：{profit_ratios}")
print(f"最佳盈利比率：{best_profit_ratio}")
