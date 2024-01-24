import json
import matplotlib.pyplot as plt
import numpy as np

# 读取 JSON 文件
with open('workAndConsume.json', 'r') as file:
    data = json.load(file)

# 提取月份、工作（work）和消费（consumption）数据
months = list(range(1, len(data) + 1))
work_values = [entry['work'] for entry in data]
consumption_values = [entry['consumption'] for entry in data]

# 创建图形
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制透明度更高的填充区域
ax.fill_between(months, work_values, color='#ffca3a', alpha=0.3)
ax.fill_between(months, consumption_values, color='#ff595e', alpha=0.3)

# 绘制折线图
ax.plot(months, work_values, label='Work', color='#ffca3a', marker='o')
ax.plot(months, consumption_values, label='Consumption', color='#ff595e', marker='o')

# 添加标签和标题
plt.xlabel('Month')
plt.ylabel('Values')
plt.title('Work and Consumption Over Months')
plt.legend()

# 保存图形为文件（可以选择不同的格式，如 PNG、JPG、SVG 等）
plt.savefig('工作和消费意愿折线图.png')

# 显示图形
plt.show()
