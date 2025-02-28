# Genç Başarı Eğitim Vakfı ÖDEV2 - CRUD İşlemleri #

from requests import get
from pprint import pprint

# Haberleri çekecek fonksiyon
def take_news():
    endpoint = "https://newsapi.org/v2/everything?q=tesla&from=2025-01-28&sortBy=publishedAt&apiKey=d7d3a26abf80435f82d3152d4a9ddb0e"
    response = get(url=endpoint)
    data = response.json()
    
# Haberleri listeye kaydedelim
    news_list = []
    for article in data.get("articles", []):
        news_list.append({
            "title": article["title"],
            "author": article["author"],
            "content": article["content"],
            "publishedAt": article["publishedAt"],
            "source": article["source"]["name"]
        })
    return news_list

news_db = take_news()   #Haberleri çeken fonksiyonu çağırdık
#pprint(news_db)



def read_news():
    num = 1  # Manuel sayaç başlatılıyor
    for news in news_db:                                                            # Liste içinde düzenli okuma sağlanıyor
        print(f"\n{num}. {news['title']} \n- {news['author']} \n- {news['source']} \n- ({news['publishedAt']})")    
        num += 1  # Sayaç her döngüde 1 artırılıyor
read_news()



yazar_adı = input("Yazar Adı Giriniz: ")                                            # Kullanıcıdan yazar adı aldık
filtered_news = [i for i in news_db if i["author"] == yazar_adı]                    # Yazar adına göre filtreleme yaptık
if filtered_news:
    pprint(filtered_news)
else:
    print(f"{yazar_adı} isimli yazar için haber bulunamadı.")



kaynak = input("Kaynak Giriniz: ")
filtered_news = [i for i in news_db if i["source"] == kaynak]                       # Kaynak adına göre filtreleme yaptık
if filtered_news:
    pprint(filtered_news)
else:
    print(f"{kaynak} için haber bulunamadı.")



def update_news():
    new_title = input("Yeni haber başlığı: ")                                         # Kullanıcıdan veri alarak haber ekleme
    new_author = input("Yazar adı: ")
    new_source = input("Kaynak: ")
    new_date = input("Yayın tarihi (YYYY-MM-DD): ")

    news_db.append({                                                                  # Haberi listeye ekle
        "title": new_title,
        "author": new_author,
        "source": new_source,
        "publishedAt": new_date
    })
    print("Yeni haber eklendi!")

update_news()
read_news()                                                                        



def update_news(new_title, new_author, new_date, new_source):
    news_db.append({                                                                # parametrelerin listeye eklenmesi için
        "title": new_title,
        "author": new_author,
        "source": new_source,
        "publishedAt": new_date
    })
    print("Yeni haber eklendi!")

update_news("Yeni Tesla Modeli Tanıtıldı", "Elon Musk", "SpaceX.co", "2025-02-28")  # Parametreleri ekleme
update_news("asdfghjk", "Sümeyye Kotan", "smyye.com", "2025-02-28")
read_news() 



def delete_author(author):                                                          # Yazar adıyla silme işlemi
    global news_db
    for i in range(len(news_db)):                                                   # news_db listesindeki her bir haber için kontrol et
        if news_db[i]["author"] == author:
            del news_db[i]                                                          # del fonksiyonu ile haberi sil
    print(f"'{author}' tarafından yazılan tüm haberler silindi!")

delete_author("Sümeyye Kotan")
read_news()
