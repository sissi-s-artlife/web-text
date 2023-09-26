
import nltk
from nltk.corpus import webtext
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

# Download NLTK resources if needed
nltk.download('webtext', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Load the webtext corpus
corpus = webtext.raw('overheard.txt')  # You can choose other webtext documents as well

# Tokenize the text into words
tokens = word_tokenize(corpus)

# Remove punctuation and convert to lowercase
words = [word.lower() for word in tokens if word.isalnum()]

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# Word frequency analysis
word_freq = Counter(filtered_words)

# Create a simple bar chart for the top N words
N = 10  # You can change this to get more or fewer words
top_words = word_freq.most_common(N)

# Extract words and frequencies for the chart
words, frequencies = zip(*top_words)

# Create the bar chart
plt.figure(figsize=(10, 5))
plt.bar(words, frequencies)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title(f'Top {N} Words')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

