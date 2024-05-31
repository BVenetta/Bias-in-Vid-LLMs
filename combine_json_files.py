import os
import json
import argparse

def parse_args():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', help='Directory containing individual JSON files.', required=True)
    parser.add_argument('--output_file', help='Path to save the consolidated JSON file.', required=True)
    return parser.parse_args()

def combine_json_files(input_dir, output_file):
    """
    Combine individual JSON files into a single JSON file.
    
    Args:
        input_dir (str): Directory containing individual JSON files.
        output_file (str): Path to save the consolidated JSON file.
    """
    combined_results = []

    # Iterate through each file in the directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(input_dir, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                combined_results.extend(data)
    
    # Save the combined results to a single JSON file
    with open(output_file, 'w') as outfile:
        json.dump(combined_results, outfile)

if __name__ == "__main__":
    args = parse_args()
    combine_json_files(args.input_dir, args.output_file)
