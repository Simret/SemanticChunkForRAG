# Load json file

import json
import re

def semantic_chunk(content, max_tokens=300):
    # Split text into sentences to keep semantic integrity
    sentences = re.split(r'(?<=[.!?])\s+', content)
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        tokens_in_sentence = len(sentence.split())  # Approximate token count
        
        # Add sentence to chunk if within token limit
        if len(current_chunk.split()) + tokens_in_sentence > max_tokens:
            chunks.append(current_chunk.strip())  # Save the chunk
            current_chunk = sentence  # Start a new chunk with current sentence
        else:
            current_chunk += " " + sentence
    
    # Add remaining chunk
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

def process_json(file_path, max_tokens=500):
    with open('Json.json', 'r') as f:
        data = json.load(f)
    data
    chunked_data = []
    for entry in data:
        content = entry.get("Content", "")
        if content:
            chunks = semantic_chunk(content, max_tokens=max_tokens)
            for i, chunk in enumerate(chunks):
                chunked_data.append({
                    "id": entry.get("id"),
                    "URL": entry.get("URL"),
                    "Title": entry.get("Title"),
                    "Chunk_Number": i + 1,
                    "Content_Chunk": chunk
                })
    
    return chunked_data

# Use the function and save the result
chunked_data = process_json('Json.json', max_tokens=500)
with open('chunked_content.json', 'w') as f:
    json.dump(chunked_data, f, indent=2)
