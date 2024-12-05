# main.py
import pandas as pd
from preprocess import preprocess_text, lexical_diversity
from ner_model import get_entities
from text_classification import train_text_classification_model

def main():
    # Load your dataset
    file_path = "C:\\Users\\miche\\CS Files\\medical_nlp\\mtsamples.csv"  # Adjust this path to your file
    data = pd.read_csv(file_path)
    
    # Preprocessing
    print("Starting Preprocessing")
    data['processed_notes'] = data['transcription'].apply(preprocess_text)
    
    # Word Count and Frequency
    data['original_length'] = data['transcription'].apply(lambda x: len(str(x).split()))
    data['processed_length'] = data['processed_notes'].apply(lambda x: len(str(x).split()))
    
    # Named Entity Recognition (NER)
    data['original_entities'] = data['transcription'].apply(get_entities)
    data['processed_entities'] = data['processed_notes'].apply(get_entities)
    
    # Lexical Diversity
    data['original_diversity'] = data['transcription'].apply(lexical_diversity)
    data['processed_diversity'] = data['processed_notes'].apply(lexical_diversity)
    
    # Text Classification (if you have labels like 'medical_specialty')
    target_column = 'medical_specialty'  # Example target column
    train_text_classification_model(data, target_column)
    
    # Save processed data
    data.to_csv("processed_data.csv", index=False)
    print("Process is Complete")

if __name__ == "__main__":
    main()
