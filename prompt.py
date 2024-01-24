
def generate_prompts(scenarios):
    base_text = (
        "You're {name}, a {age}-year-old individual living in {city}. "
        "As with all Americans, a portion of your monthly income is taxed by the federal government. "
        "This taxation system is tiered, income is taxed cumulatively within defined brackets, "
        "combined with a redistributive policy: after collection, the government evenly redistributes "
        "the tax revenue back to all citizens, irrespective of their earnings. Now it's {year}. In the "
        "previous month, you worked as a(an) {occupation}. If you continue working this month, "
        "your expected income will be {income:.2f}, which is decreased compared to the last month due "
        "to the deflation. Besides, your consumption was {consumption:.2f}. Your "
        "tax deduction amounted to {tax_deduction:.2f}. However, as part of the government's redistribution "
        "program, you received a credit of {tax_credit:.2f}. In this month, the government sets the brackets: "
        "[{brackets}] and their corresponding rates: [{rates}]. Income earned within each bracket is taxed only "
        "at that bracket's rate. Meanwhile, deflation has led to a price decrease in the consumption market, "
        "with the average price of essential goods now at {avg_goods_price:.2f}. Your current savings account "
        "balance is {savings_balance:.2f}. Interest rates, as set by your bank, stand at {interest_rate:.2%}. "
        "With all these factors in play, and considering aspects like your living costs, any future aspirations, "
        "and the broader economic trends, how is your willingness to work this month? Furthermore, how would you "
        "plan your expenditures on essential goods, keeping in mind goods price? Please share your decisions in "
        "a JSON format. The format should have two keys: 'work' (a value between 0 and 1 with intervals of 0.02, "
        "indicating the willingness or propensity to work) and 'consumption' (a value between 0 and 1 with intervals "
        "of 0.02, indicating the proportion of all your savings and income you intend to spend on essential goods)."
    )

    all_prompts = []

    for scenario in scenarios:
        # Convert brackets and rates lists to strings
        scenario['brackets'] = ', '.join(map(str, scenario['brackets']))
        scenario['rates'] = ', '.join(map(str, scenario['rates']))

        prompt_text = base_text.format(**scenario)
        all_prompts.append(prompt_text)

    return all_prompts
