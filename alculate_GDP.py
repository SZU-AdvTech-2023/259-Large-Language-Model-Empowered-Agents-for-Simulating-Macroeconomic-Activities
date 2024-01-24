import json

def calculate_gdp_stats(data):
    results = []

    for year_data in data:
        total_gdp = 0.0
        for entry in year_data:
            work = entry.get("work", 0.0)
            consumption = entry.get("consumption", 0.0)
            total_gdp += work + consumption

        year = year_data[0].get("Year", None)
        inflation_rate = year_data[0].get("InflationRate", None)
        gdp_growth_rate = year_data[0].get("GDPGrowthRate", None)

        result = {
            "Year": year,
            "InflationRate": inflation_rate,
            "GDPGrowthRate": gdp_growth_rate,
            "GDP (Trillion USD)": total_gdp,
            "UnemploymentRate": year_data[0].get("UnemploymentRate", None)
        }

        results.append(result)

    return results

# 读取JSON数据
with open('workAndConsume.json', 'r') as file:
    json_data = json.load(file)

# 计算所有年份的GDP统计数据
gdp_stats = calculate_gdp_stats(json_data)

# 输出结果
for stats in gdp_stats:
    print(stats)

