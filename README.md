# Amazon Reviews Scraper with Natural Language Understanding (powered by IBM Watson)

_In this project a basic amazon reviews scraper and sentiment analysis prebuilt functions are proposed as starting point to Watson Natural Language Understanding API usage._

### Pre-requisites 📋

_It is mandatory to get an IBM Lite tier account. Follow the next steps to get free tier access:_
1. From the IBM (must be created an IBM ID first) home page search "natural language understanding"
![Alt text](figures/readme/NLU_search.png?raw=true "Title")
2. Provision a Lite instance (up to 15.000 API monthly calls over small corpuses and sentiment+keywords analysis)

![Alt text](figures/readme/NLU_provisioning.png?raw=true "Title")

3. Get the service API credentials

![Alt text](figures/readme/IBM_credentials.png?raw=true "Title")

4. Store credentials as .json file in

```
config/creentials/credentials.json
```

with the following structure:
```
{
  "APIkey": "API key here",
  "URL": "URL here"
}
```

## Start 🚀

_Just clone the repository_

```
git clone https://github.com/danielp2797/Amazon-reviews-scrap-and-sentiment-analysis-with-IBM-Watson
```
then install src package from setup.py file in the project root directory
```
pip install -e .
```
and finally install requirements
```
pip install -r requirements.txt
```


## Usage 📦
_Select an Amazon's product review page as for example:_
```
https://www.amazon.com/-/es/Pantalla-Retina-pulgadas-espacial-renovado/product-reviews/B07F93611L/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews
```
and run the main.py as follows:
```
python3 main.py <url>
```
If it works, you will see this verbose in your console:

![Alt text](figures/readme/proof_of_concept.png?raw=true "Title")

The scraped results are stored in
```
data/reviews/raw
```
as .csv file with the system timestamp as the file name. An example of the .csv structure is:

|title|content                      |date  |variant                                      |images|verified|author    |rating            |product                                                                                                             |url|
|-----|-----------------------------|------|---------------------------------------------|------|--------|----------|------------------|--------------------------------------------------------------------------------------------------------------------|---|
|Loooovvee itttt|I’ll absolutely love my iPad I’ve always wanted one and when I seen that they had them for a good price which was 140 I had to get it it is so convenient and I absolutely love it. The company even put a screen protector on it which I absolutely love because I didn’t have the buy one, so I really love that I bought it used so of course it’s just a little things that I worry about because it is secondhand but overall it’s absolutely lovely and I love it.|Calificado en Estados Unidos 🇺🇸 el 24 de octubre de 2022|Tamaño: Paquete de 5 Wireless communication technology: Wi-Fi Color: Gris (Space Grey)|      |Yes     |Maya gayle|5.0 de 5 estrellas|Apple iPad de 9.7 pulgadas (reacondicionado) (modelo 2018) con Wi-Fi solamente. 32 GB, iPad MR7F2LL/A, gris espacial|   |

Once we have the data, is time to move on notebooks. Take a look at
```
notebooks/00-Starting.ipynb
```
There is a simple sentiment analysis and keywords extraction. In the sample case led to the following word cloud plot:
![Alt text](figures/sample/sample_analysis.png?raw=true "Title")
with interesting insights, such as:
1. We should care about battery life
2. Look the condition of the charger
3. It seems that "great" and "condition" are commonly contained in reviews, so people, generally, is satisfied with the product.

## I hope it will help you 🎁
