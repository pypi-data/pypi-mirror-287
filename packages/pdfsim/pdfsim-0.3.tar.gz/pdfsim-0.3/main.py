import PyPDF2
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import argparse
from skimage.metrics import structural_similarity as ssim
import cv2
import pdfplumber

# Ensure necessary resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

def extract_text_from_pdf(pdf_path):
    text=""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def preprocess_text(text):
    # Tokenize text
    tokens = word_tokenize(text)
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalpha() and word.lower() not in stop_words]
    return tokens

def extract_general_features(text):
    features = defaultdict(list)
    # Extract all lines
    lines = text.split('\n')
    for line in lines:
        # Generic regex to capture potential key-value pairs
        match = re.match(r'^(.*?):\s*(.*)$', line)
        if match:
            key = match.group(1).strip().lower().replace(" ", "_")
            value = match.group(2).strip()
            features[key].append(value)
        else:
            tokens = preprocess_text(line)
            for token in tokens:
                features[token.lower()].append(line.strip())
    return dict(features)

def calculate_cosine_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return cosine_sim[0][0]

def calculate_jaccard_similarity(list1, list2):
    set1, set2 = set(list1), set(list2)
    return len(set1 & set2) / len(set1 | set2)

def calculate_image_similarity(image1_path, image2_path):
    img1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
    if img1 is None or img2 is None:
        return 0  # Handle case where image reading fails

    img1 = cv2.resize(img1, (300, 300))
    img2 = cv2.resize(img2, (300, 300))

    score, _ = ssim(img1, img2, full=True)
    return score

def convert_pdf_to_image(pdf_path):
    images = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            img = page.to_image()
            img_path = f"/tmp/page_{page.page_number}.png"
            img.save(img_path)
            images.append(img_path)
    return images

def calculate_similarity(feature1, feature2):
    score = 0
    total_fields = 0
    
    for key in set(feature1.keys()) | set(feature2.keys()):
        if key in feature1 and key in feature2:
            total_fields += 1
            if isinstance(feature1[key], list) and isinstance(feature2[key], list):
                score += calculate_jaccard_similarity(feature1[key], feature2[key])
            else:
                score += calculate_cosine_similarity(' '.join(feature1[key]), ' '.join(feature2[key]))
    
    return score / total_fields if total_fields > 0 else 0

def process_database(directory_path):
    database = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf') or filename.endswith('.PDF'):
            file_path = os.path.join(directory_path, filename)
            print(filename)
            text = extract_text_from_pdf(file_path)
            features = extract_general_features(text)
            features['filename'] = filename
            features['image_paths'] = convert_pdf_to_image(file_path)
            database.append(features)
    return database

def find_most_similar(feature, database, top_n=1):
    similarities = []
    
    for db_feature in database:
        textual_similarity = calculate_similarity(feature, db_feature)
        image_similarity_scores = []
        for img1_path in feature['image_paths']:
            for img2_path in db_feature['image_paths']:
                image_similarity_scores.append(calculate_image_similarity(img1_path, img2_path))
        
        image_similarity = sum(image_similarity_scores) / len(image_similarity_scores) if image_similarity_scores else 0
        total_similarity = 0.7 * textual_similarity + 0.3 * image_similarity
        similarities.append((db_feature, total_similarity))
    
    return sorted(similarities, key=lambda x: x[1], reverse=True)[:top_n]

def main():
    parser = argparse.ArgumentParser(description='PDF Similarity Matcher')
    parser.add_argument('-d' ,'--database', type=str, required=True, help='Path to the database directory containing PDFs')
    parser.add_argument('-i' ,'--input', type=str, required=True, help='Path to the input pdf PDF')
    parser.add_argument('-t' ,'--top', type=int, default=1, help='Number of top similar pdfs to display (default: 1)')
    parser.add_argument('-kv', action='store_true', help='Enable detailed key-value feature output for similar PDFs. When this flag is used, additional information about the features of each similar PDF will be displayed.')

    args = parser.parse_args()

    
    print("Processing database...")
    database = process_database(args.database) #   contains the feature of all pdf's in the directory
    
    print("Processing input pdf...")
    input_text = extract_text_from_pdf(args.input)
    feature = extract_general_features(input_text)
    feature['image_paths'] = convert_pdf_to_image(args.input)
    
    print("Finding most similar pdf...")
    similar_features = find_most_similar(feature, database, args.top)
    
    print("\nTop similar pdfs:")
    for i, (feature, similarity_score) in enumerate(similar_features, 1):
        print(f"\n{i}. Similar pdf: {feature['filename']}")
        print(f"   Similarity score: {similarity_score:.2f}")
        if(args.kv):
            print("   Features:")
            for key, value in feature.items():
                if key != 'filename':
                    print(f"   - {key}: {value}")

if __name__ == "__main__":
    main()

