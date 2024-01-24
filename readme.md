### Project README

This repository contains code for simulating macroeconomic activities using a chatbot-based AI agent, with a focus on GDP calculation. The project is organized as follows:

#### File Structure

- **main.py**: The main program for interacting with the ChatGPT model.
- **prompt.py**: A script for generating prompts in batches.
- **baseline**: Implementation of baseline experiments based on the original paper "Large Language Model-Empowered Agents for Simulating Macroeconomic Activities."
- **calculate_GDP.py**: Code for calculating GDP, with the computation depending on the quantity of JSON data provided.
- **printResult.py**: Script for plotting line charts of experimental GDP results.
- **printResultForRegulation.py**: Script for plotting scatter plots depicting the impact of regulations.

#### Usage

1. Run `main.py` to interact with the ChatGPT model and simulate macroeconomic scenarios.
2. Use `prompt.py` to generate batches of prompts for experimentation.
3. Explore the `baseline` directory for baseline experiments following the original paper.
4. Adjust the JSON data input for GDP calculation in `calculate_GDP.py` based on the desired simulation scenario.
5. Run `printResult.py` to visualize the GDP results as line charts.
6. Execute `printResultForRegulation.py` to generate scatter plots illustrating the impact of regulations.

#### Notes

- Ensure the required dependencies are installed before running the code.
- Review the code comments for additional information and customization options.
- Experiment with different prompts and scenarios to observe variations in the AI agent's behavior.
