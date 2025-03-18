import pythainlp
import nltk
from nltk.tokenize import word_tokenize
import re

# Download necessary NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

class ThaiTokenizer:
    """Class for tokenizing Thai text"""
    
    def __init__(self):
        pass
    
    def tokenize(self, text):
        """Tokenize Thai text into words
        
        Args:
            text (str): Thai text without spaces
            
        Returns:
            list: List of Thai words
        """
        return pythainlp.word_tokenize(text)
    
    def get_sample_texts(self, mode='easy'):
        """Get sample texts for the game based on difficulty
        
        Args:
            mode (str): Difficulty level ('easy' or 'challenge')
            
        Returns:
            list: List of Thai texts without spaces
        """
        if mode == 'easy':
            return [
                "วันนี้อากาศดีมาก",
                "ฉันชอบกินข้าวผัด",
                "น้องสาวของฉันชื่อนุ่น",
                "เธอไปโรงเรียนทุกวัน",
                "แมวตัวนี้น่ารักจัง"
            ]
        else:  # challenge mode
            return [
                "การเดินทางไปต่างประเทศต้องเตรียมตัวให้พร้อม",
                "นักเรียนทุกคนต้องตั้งใจเรียนเพื่ออนาคตที่ดี",
                "อาหารไทยมีรสชาติเผ็ดและหลากหลาย",
                "การออกกำลังกายเป็นประจำทำให้สุขภาพแข็งแรง",
                "เทคโนโลยีในปัจจุบันพัฒนาไปอย่างรวดเร็ว"
            ]

class EnglishTokenizer:
    """Class for tokenizing English text"""
    
    def __init__(self):
        # Common English words to help with segmentation
        self.common_words = set([
            "the", "and", "to", "of", "a", "in", "is", "that", "for", "it", "with", "as", "was", "on", "be", 
            "at", "by", "this", "are", "or", "an", "from", "but", "not", "what", "all", "were", "when", "we", 
            "there", "can", "my", "has", "will", "one", "would", "so", "no", "which", "their", "they", "you", 
            "he", "she", "his", "her", "our", "your", "its", "if", "about", "who", "them", "some", "could", 
            "into", "than", "then", "now", "only", "just", "do", "more", "these", "also", "any", "first", 
            "very", "new", "may", "should", "such", "like", "time", "out", "up", "over", "after", "through", 
            "most", "before", "between", "here", "those", "must", "well", "back", "where", "how", "too", 
            "even", "want", "because", "many", "work", "life", "day", "take", "long", "right", "look", 
            "think", "see", "come", "way", "down", "get", "make", "know", "find", "give", "use", "year", 
            "good", "each", "need", "still", "high", "last", "might", "great", "old", "other", "say", "same", 
            "tell", "does", "set", "three", "small", "put", "end", "big", "show", "try", "us", "again", 
            "much", "own", "part", "place", "ask", "keep", "help", "talk", "turn", "study", "seem", "open", 
            "next", "case", "fact", "point", "world", "build", "self", "both", "toward", "site", "light", 
            "today", "bring", "name", "room", "friend", "go", "run", "while", "start", "every", "stay", 
            "word", "side", "people", "kind", "head", "far", "black", "long", "high", "school", "important", 
            "write", "state", "never", "become", "between", "family", "leave", "while", "mean", "different", 
            "move", "boy", "girl", "old", "enough", "another", "above", "below", "country", "plant", "animal", 
            "father", "mother", "brother", "sister", "quick", "brown", "fox", "jump", "lazy", "dog", "pizza", 
            "beautiful", "amazing", "artificial", "intelligence", "changing", "environmental", "protection", 
            "communication", "technology", "advances", "rapidly", "international", "business", "requires", 
            "cultural", "understanding", "mathematical", "equations", "complex"
        ])
    
    def tokenize(self, text):
        """Tokenize English text into words
        
        Args:
            text (str): English text without spaces
            
        Returns:
            list: List of English words
        """
        # Since the input has no spaces, we need to segment it ourselves
        # This is a simple greedy algorithm for word segmentation
        words = []
        i = 0
        while i < len(text):
            # Try to find the longest word starting at position i
            found = False
            for j in range(min(len(text), i + 20), i, -1):  # Try words up to 20 chars long
                word = text[i:j].lower()
                if word in self.common_words or len(word) == 1:  # Single letters are valid words (a, I)
                    words.append(text[i:j])
                    i = j
                    found = True
                    break
            
            # If no word was found, take a single character as a word
            if not found:
                words.append(text[i:i+1])
                i += 1
        
        return words
    
    def get_sample_texts(self, mode='easy'):
        """Get sample texts for the game based on difficulty
        
        Args:
            mode (str): Difficulty level ('easy' or 'challenge')
            
        Returns:
            list: List of English texts without spaces
        """
        if mode == 'easy':
            return [
                "thequickbrownfox",
                "ilikepizza",
                "shegoestoschool",
                "todayisabeautifulday",
                "myfriendsareamazing"
            ]
        else:  # challenge mode
            return [
                "artificialintelligenceischangingtheworld",
                "environmentalprotectionisimportant",
                "communicationtechnologyadvancesrapidly",
                "internationalbusinessrequiresculturalunderstanding",
                "mathematicalequationscanbecomplex"
            ]