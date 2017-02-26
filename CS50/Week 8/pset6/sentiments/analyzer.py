import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        
        self.tokenizer = nltk.tokenize.TweetTokenizer()
        self.positive_words = set()
        self.negative_words = set()
        
        with open(positives, 'r') as pos_list:
            for line in pos_list:
                if line[0] != ';':
                    self.positive_words.add(line.rstrip().strip().lower())
        
        with open(negatives, 'r') as neg_list:
            for line in neg_list:
                if line[0] != ';':
                    self.negative_words.add(line.rstrip().strip().lower())

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        score = 0
        words = self.tokenizer.tokenize(text)
        for word in words:
            if word.lower() in self.positive_words:
                score += 1
            elif word.lower() in self.negative_words:
                score -= 1
        
        return score
