from text_cleaner import TextCleaner
from sentiment_analyzer import SentimentAnalyzer

def main():
    # Sınıf örneklerini oluştur
    cleaner = TextCleaner()
    analyzer = SentimentAnalyzer()

    # Örnek bir metin
    text = "Bu filmi gerçekten çok beğendim. Çok güzel bir senaryosu var."

    # 1. Metin temizleme
    clean_text = cleaner.clean_text(text)
    print(f"Temizlenmiş Metin: {clean_text}")

    # 2. Duygu analizi
    sentiment = analyzer.analyze_sentiment(clean_text)
    print(f"Metindeki Duygu: {sentiment}")

if __name__ == "__main__":
    main()
