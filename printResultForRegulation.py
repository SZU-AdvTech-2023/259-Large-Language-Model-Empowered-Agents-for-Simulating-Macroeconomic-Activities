import json
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# 从JSON文件中读取数据
with open("resultDetail.json", "r") as file:
    data_sets = json.load(file)

labels = ['Ours', 'LEN', 'CAT', 'Composite', 'AI-Eco']

# 使用GridSpec来精确控制子图的位置和宽度
fig = plt.figure(figsize=(15, 6))
gs = GridSpec(1, 2, width_ratios=[3, 3])  # 调整两个子图的宽度比例，这里设置为相同宽度

# 菲利普斯曲线
ax1 = fig.add_subplot(gs[0])
ax1.set_facecolor('white')  # 设置背景颜色
ax1.set_title("Phillips Curve", fontsize=18)
ax1.set_xlabel("Unemployment Rate", fontsize=16)
ax1.set_ylabel("Wage Inflation", fontsize=16)

for i, data_set in enumerate(data_sets):
    unemployment_rates = [entry["UnemploymentRate"] for entry in data_set]
    wage_inflations = [entry["InflationRate"] for entry in data_set]
    ax1.scatter(unemployment_rates, wage_inflations, label=labels[i])

ax1.legend().set_visible(False)
ax1.xaxis.grid(False)  # 关闭横向网格线
ax1.yaxis.grid(False)  # 关闭纵向网格线

# 奥肯定律
ax2 = fig.add_subplot(gs[1])
ax2.set_facecolor('white')  # 设置背景颜色
ax2.set_title("Okun's Law", fontsize=18)
ax2.set_xlabel("Unemployment Rate Growth", fontsize=16)
ax2.set_ylabel("GDP Growth", fontsize=16)

for i, data_set in enumerate(data_sets):
    # 计算失业率增长率
    unemployment_rates = [entry["UnemploymentRate"] for entry in data_set]
    unemployment_growth_rates = [0] + [((ur - unemployment_rates[idx - 1]) / unemployment_rates[idx - 1]) * 100 for
                                       idx, ur in enumerate(unemployment_rates)][1:]

    gdp_growth_rates = [entry["GDPGrowthRate"] for entry in data_set]
    ax2.scatter(unemployment_growth_rates, gdp_growth_rates, label=labels[i])

ax2.xaxis.grid(False)  # 关闭横向网格线
ax2.yaxis.grid(False)  # 关闭纵向网格线

# 调整下方横向统一图例的位置和字体大小
plt.tight_layout()
plt.subplots_adjust(bottom=0.15)
# 添加横向统一图例
plt.legend(labels, loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=len(labels), fontsize=16)

plt.tight_layout()
plt.show()


