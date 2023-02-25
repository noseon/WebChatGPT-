import requests
import json

def web_acess(word,result):
    params = (
        ('q', f'{word}'),
        ('max_results', f'{result}'),
        ('region', 'wt-wt'),
    )

    headers = {
        'authority': 'ddg-webapp-aagd.vercel.app',
        'accept': '*/*',
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://chat.openai.com',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50',
    }
    response = requests.get('https://ddg-webapp-aagd.vercel.app/search', headers=headers, params=params)
    json_data = response.json()

    Result_ = ""
    for result in json_data:
        Result_ += "\"" + result["title"] + "\"" + "\n"
        Result_ += "\"" + result["body"] + "\"" + "\n"
        Result_ += "URL: " + result["href"] + "\n\n"
        
    return Result_

Question = "teletubbies"
quantity_result = 5
text = web_acess(Question,quantity_result)
print(text)