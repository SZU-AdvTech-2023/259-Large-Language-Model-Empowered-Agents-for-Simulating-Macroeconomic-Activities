import openai
import pandas as pd
from prompt import generate_prompts

openai.api_key = "write your openAI key here"

# Load scenarios from Excel file
scenarios_df = pd.read_excel('scenarios.xlsx')  # Replace 'your_excel_file.xlsx' with your actual file path
scenarios = scenarios_df.to_dict(orient='records')

# Generate prompts for each scenario
all_prompts = generate_prompts(scenarios)

# Write generated prompts to a text file
with open('generated_prompts.txt', 'w') as file:
    for i, prompt in enumerate(all_prompts, start=1):
        file.write(f"\nGenerated Prompt {i}:\n{prompt}\n")

# Uncomment the following lines when you have available tokens
"""
# Iterate over prompts and get responses
for i, prompt in enumerate(all_prompts, start=1):
    response = chat_with_gpt3(prompt)

    # Display results
    print(f"\nChatGPT Response for Prompt {i}:\n{response}")

    quota_remaining = int(response.headers['x-remaining-predictions'])
    print(f"剩余配额: {quota_remaining}")
"""
