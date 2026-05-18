# backend/app/ml_pipeline.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
import joblib

class ABSAPipeline:
    def __init__(self):
        """
        Initializing the 2 ML Models and the Vectorizer.
        This will be shown to the supervisor for approval.
        """
        # 1. The Translator (Converts text to numbers)
        self.vectorizer = TfidfVectorizer(max_features=5000)
        
        # 2. Model 1: The Sorter (Predicts the Aspect)
        # We use a linear kernel as it performs best for high-dimensional text data
        self.aspect_model = SVC(kernel='linear')
        
        # 3. Model 2: The Tally Counter (Predicts the Sentiment)
        # We use Naive Bayes as it is the standard for probability-based text classification
        self.sentiment_model = MultinomialNB()

    def train_models(self, dataset_path: str):
        """
        TODO: Once approved, write the code here to load the PyABSA dataset,
        fit the vectorizer, and train the aspect_model and sentiment_model.
        """
        pass

    def save_models(self, save_directory: str):
        """
        TODO: Once trained, use joblib to save the .pkl files here.
        """
        pass

    def predict(self, new_review: str):
        """
        TODO: Write the code to vectorize the new_review and return 
        the predictions from both models.
        """
        pass