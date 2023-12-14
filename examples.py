import math
import json
import pandas as pd
import requests
import matplotlib.pyplot as plt
import sys
import seaborn as sns
import datetime

from PIL import Image

# Printing system version and current date
print(sys.version)
print("Today is", datetime.datetime.today())

# Azure endpoint and version information
endpoint = "your_endpoint"
version = "?api-version=2023-02-01-preview&modelVersion=latest"

# URLs for image and text vectorization
vec_img_url = endpoint + "/retrieval:vectorizeImage" + version
vec_txt_url = endpoint + "/retrieval:vectorizeText" + version

# Request headers with necessary information
headers = {
    'Content-type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'your_key'
}

# Function to embed image using Azure CV 4.0
def image_embedding(imageurl):
    """Embedding image using Azure CV 4.0"""
    image = {'url': imageurl}
    r = requests.post(vec_img_url, data=json.dumps(image), headers=headers)
    image_emb = r.json()['vector']
    return image_emb

# Function to embed text using Azure CV 4.0
def text_embedding(promptxt):
    """Embedding text using Azure CV 4.0"""
    prompt = {'text': promptxt}
    r = requests.post(vec_txt_url, data=json.dumps(prompt), headers=headers)
    text_emb = r.json()['vector']
    return text_emb

# Function to calculate cosine similarity between two vectors
def get_cosine_similarity(vector1, vector2):
    """Get cosine similarity value"""
    dot_product = sum(vector1[i] * vector2[i] for i in range(min(len(vector1), len(vector2))))
    magnitude1 = math.sqrt(sum(x * x for x in vector1))
    magnitude2 = math.sqrt(sum(x * x for x in vector2))
    similarity = dot_product / (magnitude1 * magnitude2)
    return similarity

# Function to get similarity results between an image and multiple prompts
def similarity_results(image_emb, prompts):
    """Get similarity results"""
    simil_values_list = [get_cosine_similarity(image_emb, text_embedding(prompt)) for prompt in prompts]
    sorted_results = sorted(zip(prompts, simil_values_list), key=lambda x: x[1], reverse=True)

    df = pd.DataFrame(columns=['prompt', 'similarity'])
    for idx, (prompt, simil_val) in enumerate(sorted_results):
        df.loc[idx, 'prompt'] = prompt
        df.loc[idx, 'similarity'] = simil_val

    df["similarity"] = df.similarity.astype(float)
    return df

# Image URLs and their respective embeddings
imageurl1 = "https://github.com/glauberss2007/AI-Image-Retrieval-Matching/images/i4.jpg?raw=true"
image_emb1 = image_embedding(imageurl1)

# Display the image
plt.imshow(Image.open(requests.get(imageurl1, stream=True).raw))
plt.axis('off')
plt.show()

# Text embeddings and cosine similarity calculations for specific texts
text1 = text_embedding("a dog")
get_cosine_similarity(image_emb1, text1)

text2 = text_embedding("a car")
get_cosine_similarity(image_emb1, text2)

# Prompts for similarity comparison
prompts = [
    'bird', 'a truck', 'a car', 'a blue car', 'a white car', 'a BMW white car',
    'a tesla car', 'a mercedes car', 'a man', 'a ford car'
]

# Calculate similarity results between image_emb1 and prompts
df = similarity_results(image_emb1, prompts)

# Visualize similarity results using a color gradient
cm = sns.light_palette("green", as_cmap=True)
df.style.background_gradient(cmap=cm)

# Image URL 2 and its embedding
imageurl2 = "https://github.com/glauberss2007/AI-Image-Retrieval-Matching/images/xboxps5.jpg?raw=true"
image_emb2 = image_embedding(imageurl2)

# Display the image
plt.imshow(Image.open(requests.get(imageurl2, stream=True).raw))
plt.axis('off')
plt.show()

# Prompts for similarity comparison for image_emb2
prompts = [
    'PS5', 'Xbox', 'play station', 'Sony', 'controller', 'Microsoft',
    'games console', 'guitar', 'fish', 'apple', 'car', 'street', 'truck',
    'Miami', 'black controller', 'white controller'
]

# Calculate similarity results between image_emb2 and prompts
df = similarity_results(image_emb2, prompts)

# Visualize similarity results using a color gradient
cm = sns.light_palette("green", as_cmap=True)
df.style.background_gradient(cmap=cm)

# Image URL 3 and its embedding
imageurl3 = "https://github.com/glauberss2007/AI-Image-Retrieval-Matching/images/sodas.jpg?raw=true"
image_emb3 = image_embedding(imageurl3)

# Display the image
plt.imshow(Image.open(requests.get(imageurl3, stream=True).raw))
plt.axis('off')
plt.show()

# Prompts for similarity comparison for image_emb3
prompts = [
    'a can', 'coca cola', 'pepsi', '7 up', 'water', 'wine', 'beer', 'gin',
    'alcohol', 'lemon', 'drink', 'I do not know', 'food', 'soda bottles', 'coke bottle'
]

# Calculate similarity results between image_emb3 and prompts
df = similarity_results(image_emb3, prompts)

# Visualize similarity results using a color gradient
cm = sns.light_palette("green", as_cmap=True)
df.style.background_gradient(cmap=cm)

# Image URL 4 and its embedding
imageurl4 = "https://github.com/glauberss2007/AI-Image-Retrieval-Matching/images/i4.jpg?raw=true"
image_emb4 = image_embedding(imageurl4)

# Display the image
plt.imshow(Image.open(requests.get(imageurl4, stream=True).raw))
plt.axis('off')
plt.show()

# Image URL 5 and its embedding
imageurl5 = "https://github.com/glauberss2007/AI-Image-Retrieval-Matching/images/i4_2.jpg?raw=true"
whitebmw = image_embedding(imageurl5)

# Display the image
plt.imshow(Image.open(requests.get(imageurl5, stream=True).raw))
plt.axis('off')
plt.show()

# Image URL 6 and its embedding
imageurl6 = "https://github.com/glauberss2007/AI-Image-Retrieval-Matching/images/cat.jpg?raw=true"
cat = image_embedding(imageurl6)

# Display the image
plt.imshow(Image.open(requests.get(imageurl6, stream=True).raw))
plt.axis('off')
plt.show()

# Calculate cosine similarities between different image embeddings
get_cosine_similarity(image_emb4, whitebmw)
get_cosine_similarity(image_emb4, cat)
