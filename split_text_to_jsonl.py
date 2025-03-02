import json
import argparse

def split_text_to_jsonl(input_file, output_file, chunk_size=5500):
    with open(input_file, 'r', encoding='utf-8') as infile:
        text = infile.read()
    
    # Split text into chunks of specified size (default: 5500 characters)
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    
    # Write each chunk as a JSON line
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for chunk in chunks:
            json_line = json.dumps({"text": chunk})
            outfile.write(json_line + '\n')
    print(f"File has been split into {len(chunks)} chunks and saved to {output_file}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split a text file into JSONL format with a specified chunk size.')
    parser.add_argument('input_file', type=str, help='Path to the input text file')
    parser.add_argument('output_file', type=str, help='Path to the output JSONL file')
    parser.add_argument('--chunk_size', type=int, default=5500, help='Size of each chunk in characters (default: 5500)')
    
    args = parser.parse_args()
    split_text_to_jsonl(args.input_file, args.output_file, args.chunk_size)
