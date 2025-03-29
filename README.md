
## 📌 **Proje Adı:** Mood Analysis – Türkçe Metinler Üzerinden Duygu ve Duygusal Durum Tespiti (NLP)

---

### 📖 **Proje Açıklaması (Description)**

Bu proje, Türkçe metinler üzerinde duygu analizi (sentiment analysis) ve daha derin duygusal durum tespiti (mood classification) gerçekleştiren bir doğal dil işleme (NLP) uygulamasıdır. Proje; Hugging Face’in çok dilli duygu analiz modellerini, Türkçe kök bulma işlemleri için Zemberek NLP kütüphanesini ve klasik ön işleme tekniklerini bir arada kullanarak metinlerdeki hem genel duygu yönelimini (pozitif, negatif, nötr) hem de detaylı duygusal hali (korku, sevinç, öfke, üzüntü, şaşkınlık, tiksinme) belirlemeyi amaçlar.

---

### ⚙️ **Kullanılan Teknolojiler ve Kütüphaneler**
- Python 3.10+
- `transformers` (Hugging Face)
- `torch` (PyTorch) – Duygu analiz modeli için
- `nltk` – Türkçe durak kelime temizliği için
- `Zemberek-Python` – Türkçe kök (lemma) çıkarımı
- `re` – Regex ile özel karakter temizleme

---

### 🧠 **Proje Bileşenleri**
| Bileşen | Açıklama |
|--------|----------|
| `TextCleaner` | Metin ön işleme: özel karakter temizliği, durak kelime çıkarımı, küçük harfe çevirme |
| `get_stems()` | Zemberek ile kelimelerin köklerini bulma |
| `SentimentAnalyzer` | Hugging Face ile genel duygu tespiti + kelime köklerine dayalı duygusal durum sınıflandırması |
| `emotions/*.txt` | Her duygu için kök kelime listeleri (örneğin: `fear.txt`, `joy.txt`, `anger.txt` vs.) |
| `Main.py` | Projeyi test eden ana çalışma dosyası |

---

### 🧪 **Örnek Girdi / Çıktı**

```python
text = "Eve misafir gelecek, çok korkuyorum."
```

> 🔍 **Çıktı:**
```
Genel Duygu: Negatif
Duygu Durumu: Korku
```

---

### 🎯 **Projenin Hedefi**
- Türkçe serbest metinlerde:
  - Genel duygu analizi (pozitif/negatif/nötr)
  - Derin duygu analizi: (korku, öfke, sevinç, üzüntü, tiksinme, şaşkınlık vs.)
- Eğitim, müşteri geri bildirimleri, sosyal medya yorumları gibi alanlarda kullanılabilecek çok yönlü bir altyapı sunmak

---

### 📦 **Kurulum**

```bash
pip install torch transformers nltk zemberek-python
```

### 📁 `nltk` stopwords kurulumu:
```python
import nltk
nltk.download('stopwords')
```

---

### 🚀 **Çalıştırma**

```bash
python Main.py
```

