# extract csv file from code

import os
import openai

# Add actual API Key
openai.api_key ="sk-<actual key>"

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


# text = f"""
# You should express what you want a model to do by \ 
# providing instructions that are as clear and \ 
# specific as you can possibly make them. \ 
# This will guide the model towards the desired output, \ 
# and reduce the chances of receiving irrelevant \ 
# or incorrect responses. Don't confuse writing a \ 
# clear prompt with writing a short prompt. \ 
# In many cases, longer prompts provide more clarity \ 
# and context for the model, which can lead to \ 
# more detailed and relevant outputs.
# """

text = f"""
See Private Securities Offering Legend for Crescat Global Macro Fund on Page 2
Crescat Capital LLC
44 Cook Street, Suite 100
Denver, CO 80206
Phone: (303) 271-9997
Year Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec CGMF HFRXGL S&P 500
2023 -9.7% -9.6% -0.7% -4.8% -22.8% 0.3% 9.2%
2022 3.5% 13.3% 7.7% 11.4% -0.7% -11.4% 9.1% 2.9% -3.8% -1.0% -3.6% 3.2% 31.6% -4.4% -18.1%
2021 1.6% -0.7% -10.0% 6.8% 19.3% -6.1% -1.9% -15.5% -10.8% 2.6% 0.1% 3.7% -14.5% 3.7% 28.7%
2020 -8.9% -2.5% 20.7% -0.5% -0.6% 17.0% 12.6% 8.5% -6.6% 3.5% -10.2% 25.9% 65.6% 6.8% 18.4%
2019 -13.1% -6.7% -3.7% -8.8% 12.2% -7.3% 1.3% 16.4% -6.5% 0.2% -5.9% 1.5% -21.7% 8.6% 31.5%
2018 -5.1% 8.6% 0.2% -0.3% 2.1% 8.4% 0.2% -4.0% 0.0% 17.1% -4.4% 14.8% 40.8% -6.7% -4.4%
2017 -0.9% -2.3% -0.3% -2.4% 0.4% -3.0% -6.6% 1.5% -2.1% -3.4% -3.4% -3.1% -23.0% 6.0% 21.8%
2016 4.4% 2.7% -5.1% 0.5% -0.7% 0.3% -0.9% -3.7% -3.0% -3.1% 8.9% 1.9% 1.5% 2.5% 12.0%
2015 4.1% 2.3% 0.0% -3.1% 2.5% -1.6% 1.7% 4.8% 2.8% -1.0% 2.0% 0.2% 15.5% -3.6% 1.4%
2014 12.7% 4.8% -4.8% -1.8% -2.2% 4.4% -2.5% 4.2% -2.4% 2.4% 6.4% 3.3% 25.8% -0.6% 13.7%
2013 5.9% -0.5% 6.0% -8.4% 4.7% -7.7% 7.6% 0.3% -2.0% -1.6% 0.5% 2.8% 6.3% 6.7% 32.4%
2012 -1.4% -1.6% -1.5% -3.3% -0.2% 0.6% 3.4% 8.0% 7.3% -5.7% 0.1% -2.4% 2.4% 3.5% 16.0%
2011 -9.4% 5.4% -0.3% -0.4% -6.7% -5.4% 2.2% 5.1% -4.6% 1.0% 2.0% -4.1% -15.2% -8.9% 2.1%
2010 -4.1% 1.6% -1.1% 3.7% -4.9% -0.2% -6.0% 3.5% 7.0% 7.6% 15.3% 4.8% 28.5% 5.2% 15.1%
2009 9.3% -3.3% 0.3% -5.4% 26.3% -4.8% 0.0% -6.5% 6.3% 6.2% 6.9% -2.6% 32.5% 13.4% 26.5%
2008 6.9% 17.5% -0.3% -1.1% 13.1% -0.2% -17.5% -13.7% -7.6% -0.1% -14.8% 4.6% -18.1% -23.3% -37.0%
2007 1.4% 9.7% 1.8% 2.6% -1.8% 4.6% 11.2% 4.7% 10.5% 9.7% -2.6% 8.8% 78.6% 4.2% 5.5%
2006 3.8% -11.1% 8.6% 21.6% 0.5% 3.5% 11.2% -11.2% -4.5% 2.1% 6.5% 3.0% 33.9% 9.3% 15.8%
CGMF HFRXGL S&P 500
-27.7% -1.9% 2.7%
10.5% 3.5% 14.5%
9.0% 1.7% 11.4%
Ten Year 6.5% 1.4% 12.2%
10.4% 0.9% 9.4%
CGMF HFRXGL S&P 500
454.6% 17.5% 372.9%
$555 $118 $473
0.95 0.11 0.80
0.64 -0.06 0.77
0.37 -0.05 0.53
14.31 4.46 10.64
- 99.3% 17.6%
- -51.4% -38.0%
- -1.9 -0.5
- 13.2% 15.2%
Beta - 0.42 -0.13
Correlation - 0.09 -0.08
Full Year or YTD
Liquidity: 90 day notice (3-year Partial Lock Up)
Downside Capture
Up/ Down Capture Ratio
Upside Capture
Annualized Alpha $500,000; $1,000,000; $5,000,000
Incentive Allocation:
Management Fee: 2%, 1.5%, 1.25%
Crescat is a global macro asset management firm. Our mission is to grow and protect wealth over the long
term. We deploy tactical investment themes based on proprietary value-driven equity and macro models.
Our goal is industry leading absolute and risk-adjusted returns over complete business cycles with low
correlation to common benchmarks.
Terms
Downside Deviation (0%)
Three Year
Minimum Investment:
Service Providers: JP Morgan, Canaccord - Custodian/Prime Broker, Deloitte - Auditor
May Redeem 25% after Year 1 and Year 2
Five Year
Cumulative Return
Cumulative VAMI
Omega Ratio (0%)
Sortino Ratio (0%)
Since Inception
Historical Data - Since Inception
Crescat’s flagship hedge fund invests long and short around the world. We aim to capitalize on both
cyclical and secular macro themes throughout global equity, commodity, currency, and fixed income
markets.
Firm Mission and Investment Philosophy
20%, 15%, 12.5%
One Year
Sharpe Ratio (0%)
Growth Of Initial $1,000,000
Net Monthly Performance
Risk and Return Measures vs. Benchmarks Since Inception
Annualized Returns Strategy Description
CRESCAT GLOBAL MACRO
HEDGE FUND COMPOSI"""
# prompt = f"""
# Summarize the text delimited by triple backticks \ 
# into a single sentence.
# ```{text}```
# """

prompt = f"""
Extract performance returns percentages in text delimited by triple backticks \ 
1. Provide them in csv format with year and Months as headers
2. Extract returns for Benchmarks like S&P 500
3. Share details about the strategy 
4. Share contact information with email address
```{text}```
"""
response = get_completion(prompt)
print(response)


# models = openai.Model.list()

# # print the first model's id
# print(models.data[0].id)

# # create a chat completion
# chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

# # print the chat completion
# print(chat_completion.choices[0].message.content)