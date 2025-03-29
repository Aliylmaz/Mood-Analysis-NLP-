import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

class TextCleaner:
    def __init__(self):
        # Türkçe durak kelimeler seti
        self.stop_words = set(stopwords.words('turkish'))

    def remove_special_characters(self, text):
        """Metinden özel karakterleri kaldırır, Türkçe karakterler hariç."""
        return re.sub(r'[^a-zA-ZğüşıöçĞÜŞİÖÇ\s]', '', text)

    def to_lower(self, text):
        """Metni küçük harfe dönüştürür. Türkçe karakterlere uygun dönüştürme yapar."""
        return text.lower()

    def remove_stopwords(self, text):
        """Metinden durak kelimeleri kaldırır."""
        words = text.split()
        return ' '.join([word for word in words if word not in self.stop_words])

    def clean_text(self, text):
        """Tüm temizleme işlemlerini sırasıyla uygular."""
        text = self.remove_special_characters(text)
        text = self.to_lower(text)
        text = self.remove_stopwords(text)
        return text
