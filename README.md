# Slackbot made by Jaram members
## Instuction
1. Get API key from Naver API portal. This API key should have access to Naver NMT API.   
2. Get API key from Slack.
3. Make a JSON file with name `credentials.json` and place it on the root of this repository.   
This JSON file should be formatted like this:    
`{
    "SLACKBOT_TOKEN": <Token From Slack>, 
    "PAPAGO_CLIENT_ID": <Naver API Client ID>,
    "PAPAGO_CLIENT_SECRET": <Naver API Client Secret>
}`
4. Apply all the patches in `_patches` folder.
5. Run `python3 main.py` to start bot.

## Usage 
- Movie Schedule: `영화`
     - If message is formatted properly, bot will send message which contains movie schedule of cinema near HYU@Erica.
     - Example: Sending `영화` will responded by message `*블랙 팬서* ...   
        *조선명탐정: 흡혈괴마의 비밀* ...   
        *골든슬럼버* ...   
        *인시디어스4: 라스트 키* ...`
- Coinone Currency: `코인원 (빗코|비트코인|빗캐|이더|아이오타|...)`
     - If message is formatted properly, bot will send message which contains current coinone cryptocurrency currency(to KRW).
     - Check `CoinoneBot/cointickerbot.py` for all supported currencies.
     - Example: Sending `코인원 이더` will responded by message `2018-02-18 18:46:58 기준 가격 *KRW 1,040,100*`.
- Packt Ebook: `(eBook|ebook|Ebook|이북|e북)`
    - If message is formatted properly, bot will send message which contains title of today's Packt free eBook.
    - Example: Sending `eBook` will responded by message `AWS Administration - The Definitive Guide`.
- Github Stalking: `!github_(un)?register <UserID>`
    - If message is formatted properly, bot will inform you with confirmtion message.
    - Example: Sending `!github_register <UserId>` will responded by message `Registered user <UserID>`    
- Spell Check: `맞춤법:<Text>`
     - If message is formatted properly, bot will send message which contains message with fixed typos.
     - Example: Sending `맞춤법:외않되요` will responded by bot with message `왜 안 돼요`.
- Translator: `(한영|영한):<Text>`
     - If message is formatted properly, bot will send message which contains translated message of sent text.
     - Example: Sending `한영:안녕하세요` will responded by bot with message `Hello`.
- Shuttle Coke Bot
    - Usage: WIP...

## Deploying on Heroku
1. Connect [this repository](https://github.com/thy2134/WinterWorkshopSlackbot) to your heroku app.
2. Execute `heroku config:set -a <Heroku App Name> TOKEN=<Token from Slack>`.
3. Execute `heroku config:set -a <Heroku App Name> PAPAGO_CLIENT_ID=<Token from Slack>; heroku config:set -a <Heroku App Name> PAPAGO_CLIENT_SECRET=<Token from Slack>`.
4. Start slack_bot dyno from dashboard.