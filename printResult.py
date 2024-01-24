import json
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# 从JSON文件中读取数据
with open("result.json", "r") as file:
    data_sets = json.load(file)

# 准备颜色和线条样式
colors = ['#bb3e03', '#0a9396', '#ee9b00', '#94d2bd', '#005f73']
linestyles = ['solid', 'dashed', 'dashed', 'dashed', 'dashed']
labels = ['Ours', 'LEN', 'CAT', 'Composite', 'AI-Eco']

# 使用GridSpec来精确控制子图的位置
fig = plt.figure(figsize=(15, 8))
gs = GridSpec(3, 2, height_ratios=[1, 1, 0.1], hspace=0.5)

axs = [
    fig.add_subplot(gs[0, 0]),
    fig.add_subplot(gs[0, 1]),
    fig.add_subplot(gs[1, 0]),
    fig.add_subplot(gs[1, 1]),
]

# 绘制折线图
for i, data_set in enumerate(data_sets):
    years = [entry["Year"] for entry in data_set]
    inflation_rates = [entry["InflationRate"] for entry in data_set]
    gdp_growth_rates = [entry["GDPGrowthRate"] for entry in data_set]
    gdp_values = [entry["GDP (Trillion USD)"] for entry in data_set]
    unemployment_rates = [entry["UnemploymentRate"] for entry in data_set]

    axs[0].plot(years, inflation_rates, label=labels[i], color=colors[i], linestyle=linestyles[i])
    axs[1].plot(years, unemployment_rates, label=labels[i], color=colors[i], linestyle=linestyles[i])
    axs[2].plot(years, gdp_values, label=labels[i], color=colors[i], linestyle=linestyles[i])
    axs[3].plot(years, gdp_growth_rates, label=labels[i], color=colors[i], linestyle=linestyles[i])

# 添加图例
axs[0].set_title('Inflation Rate', fontsize=14)
axs[1].set_title('Unemployment Rate', fontsize=14)
axs[2].set_title('GDP (Trillion USD)', fontsize=14)
axs[3].set_title('GDP Growth Rate', fontsize=14)

# 添加横向统一图例
fig.legend(labels, loc='lower center', bbox_to_anchor=(0.5, 0.05), ncol=len(labels), fontsize=16)

# 设置坐标轴标签的字体大小
for ax in axs:
    ax.tick_params(axis='both', which='major', labelsize=16)

# 保存为PDF文件，设置高分辨率
plt.savefig("output_figure.pdf", bbox_inches='tight', dpi=400)

plt.show()


