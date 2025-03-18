import random

class GameManager:
    """Class for managing the word segmentation game"""
    
    def __init__(self, thai_tokenizer, english_tokenizer):
        """Initialize the game manager with tokenizers
        
        Args:
            thai_tokenizer (ThaiTokenizer): Tokenizer for Thai language
            english_tokenizer (EnglishTokenizer): Tokenizer for English language
        """
        self.tokenizers = {
            'thai': thai_tokenizer,
            'english': english_tokenizer
        }
    
    def get_challenge(self, language, mode):
        """Get a random challenge text based on language and difficulty
        
        Args:
            language (str): Language of the challenge ('thai' or 'english')
            mode (str): Difficulty level ('easy' or 'challenge')
            
        Returns:
            dict: Challenge data including text and correct segmentation
        """
        if language not in self.tokenizers:
            return {'error': 'Unsupported language'}
        
        # Get sample texts for the specified language and mode
        sample_texts = self.tokenizers[language].get_sample_texts(mode)
        
        # Select a random text from the samples
        text = random.choice(sample_texts)
        
        # Get the correct segmentation
        correct_segments = self.tokenizers[language].tokenize(text)
        
        # Return the challenge data
        return {
            'text': text,
            'correct_segments': correct_segments,  # This will be hidden from the player
            'language': language,
            'mode': mode
        }
    
    def check_answer(self, language, text, user_segments):
        """Check if the user's segmentation is correct
        
        Args:
            language (str): Language of the text ('thai' or 'english')
            text (str): The original unsegmented text
            user_segments (list): List of segments provided by the user
            
        Returns:
            dict: Result including whether the answer is correct and score
        """
        if language not in self.tokenizers:
            return {'error': 'Unsupported language'}
        
        # Get the correct segmentation
        correct_segments = self.tokenizers[language].tokenize(text)
        
        # Check if the user's segmentation matches the correct one
        is_correct = (user_segments == correct_segments)
        
        # Calculate score based on correctness
        # For a simple scoring system: 10 points for each correct segment
        score = 0
        if is_correct:
            score = len(correct_segments) * 10
        else:
            # Partial scoring: count how many segments match
            # This is a simplified approach and might not be perfect
            # A more sophisticated approach would use edit distance or similar metrics
            correct_set = set(correct_segments)
            user_set = set(user_segments)
            matching_segments = len(correct_set.intersection(user_set))
            score = matching_segments * 5  # Half points for partial matches
        
        # Return the result
        return {
            'is_correct': is_correct,
            'score': score,
            'correct_segments': correct_segments,
            'user_segments': user_segments
        }