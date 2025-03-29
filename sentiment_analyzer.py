from transformers import pipeline

from zemberek import TurkishMorphology

morphology = TurkishMorphology.create_with_defaults()

def get_stems(text):
    # Metni kelimelere ayır
    words = text.split()

    # Her kelimenin kökünü bul
    stems = [morphology.analyze_and_disambiguate(word).best_analysis()[0].get_stem() for word in words]

    return stems






# txt dosyasından kelimeleri okuma fonksiyonu
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]


# Dosya içeriğini okuyup, duygu analizi yapacak sınıf
class SentimentAnalyzer:
    def __init__(self):
        # Hugging Face pipeline'ı Türkçe duygu analizi için yüklüyoruz
        self.analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

        # Her duygusal durum için kelime listelerini dosyadan yüklüyoruz
        self.sadness_keywords = read_file("emotions/sadness.txt")
        self.surprise_keywords = read_file("emotions/surprise.txt")
        self.anger_keywords = read_file("emotions/anger.txt")
        self.fear_keywords = read_file("emotions/fear.txt")
        self.disgust_keywords = read_file("emotions/disgusting.txt")
        self.joy_keywords = read_file("emotions/joy.txt")
        self.trust_keywords = read_file("emotions/trust.txt")
        self.anticipation_keywords = read_file("anticipation.txt")

    def analyze_sentiment(self, text):
        # Temel duygu analizi sonucunu alıyoruz
        result = self.analyzer(text)
        sentiment_label = result[0]['label']
        general_sentiment = self.get_general_sentiment(sentiment_label)

        # Duygu durumunu belirlemek için metni kontrol ediyoruz
        emotional_state = self.detect_emotional_state(text)

        return f"Genel Duygu: {general_sentiment}, Duygu Durumu: {emotional_state}"

    def get_general_sentiment(self, sentiment_label):
        # Modelden gelen genel duygu analizine göre sınıflandırma
        match sentiment_label:
            case '1 star':
                return "Negatif"
            case '2 stars':
                return "Negatif"
            case '3 stars':
                return "Nötr"
            case '4 stars':
                return "Pozitif"
            case '5 stars':
                return "Pozitif"
            case _:
                return "Bilinmeyen"

    def contains_keywords(self, text, keywords):
        stems = get_stems(text)
        return any(stem in keywords for stem in stems)

    def detect_emotional_state(self, text):
        stems = get_stems(text)

        scores = {
            "Üzüntü": sum(stem in self.sadness_keywords for stem in stems),
            "Şaşkınlık": sum(stem in self.surprise_keywords for stem in stems),
            "Öfke": sum(stem in self.anger_keywords for stem in stems),
            "Korku": sum(stem in self.fear_keywords for stem in stems),
            "Tiksinme": sum(stem in self.disgust_keywords for stem in stems),
            "Sevinç": sum(stem in self.joy_keywords for stem in stems),
            "Güven":sum(stem in self.trust_keywords for stem in stems),
            "Beklenti": sum(stem in self.anticipation_keywords for stem in stems)

        }

        max_emotion = max(scores, key=scores.get)

        if scores[max_emotion] == 0:
            return "Duygu durumu belirlenemedi"
        else:
            return max_emotion


# Test etmek için
analyzer = SentimentAnalyzer()
text = "zor günlere rağmen umudum hiç bitmedi"
result = analyzer.analyze_sentiment(text)
print(result)
