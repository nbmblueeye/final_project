import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
        Create a unit Test for EmotionDetection
    """
    # Test text: I am glad this happened, Dominant Emotion: joy
    def test_joy(self):
        emotions = emotion_detector("I am glad this happened")
        self.assertEqual(emotions['dominant_emotion'], 'joy')

    # Test text: I am really mad about this, Dominant Emotion: anger
    def test_anger(self):
        emotions = emotion_detector("I am really mad about this")
        self.assertEqual(emotions['dominant_emotion'], 'anger')

    # Test text: I feel disgusted just hearing about this, Dominant Emotion: disgust
    def test_disgust(self):
        emotions = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(emotions['dominant_emotion'], 'disgust')

    # Test text: I am so sad about this, Dominant Emotion: sadness
    def test_sadness(self):
        emotions = emotion_detector("I am so sad about this")
        self.assertEqual(emotions['dominant_emotion'], 'sadness')

    # Test text: I am really afraid that this will happen, Dominant Emotion: fear
    def test_fear(self):
        emotions = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(emotions['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()