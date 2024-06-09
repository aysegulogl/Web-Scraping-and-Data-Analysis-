import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# BBC News web sitesinden haber başlıklarını ve tarihlerini çekmek
url = 'https://www.bbc.com/news'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Haber başlıklarını ve tarihlerini çekme
articles = soup.find_all('h3', class_='gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text')
headlines = []
dates = []

for article in articles:
    headline = article.get_text()
    headlines.append(headline)
    dates.append(pd.Timestamp.now())  # Örnek olarak, şu anki tarih ve saati ekliyoruz

# Verileri bir DataFrame'e aktarma
data = pd.DataFrame({
    'headline': headlines,
    'date': dates
})

# Verileri analiz etme ve görselleştirme
print(data.head())

# Haber başlıklarının uzunluklarını hesaplama
data['headline_length'] = data['headline'].apply(len)

# Başlık uzunluklarının dağılımını görselleştirme
plt.figure(figsize=(10, 6))
plt.hist(data['headline_length'], bins=20, color='blue', edgecolor='black')
plt.title('Haber Başlıkları Uzunluk Dağılımı')
plt.xlabel('Başlık Uzunluğu')
plt.ylabel('Frekans')
plt.show()
