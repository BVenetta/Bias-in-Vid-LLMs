import os
import random
import shutil
import argparse
from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser(description="Randomly select 1% of videos from a directory and copy them to a new directory.")
    parser.add_argument('--input_dir', type=str, required=True, help='Directory containing video files.')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory to save the selected video files.')
    return parser.parse_args()

def select_videos(input_dir, percentage):
    # Get list of all video files in the input directory
    video_files = [f for f in os.listdir(input_dir) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]
    # Calculate the number of videos to select (1% of total videos)
    num_to_select = max(1, int(len(video_files) * percentage / 100))
    # Randomly select the videos
    selected_files = random.sample(video_files, num_to_select)
    return selected_files

def copy_selected_videos(input_dir, output_dir, selected_files):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    for file in tqdm(selected_files, desc="Copying videos"):
        src_path = os.path.join(input_dir, file)
        dst_path = os.path.join(output_dir, file)
        shutil.copy(src_path, dst_path)

if __name__ == "__main__":
    args = parse_args()
    selected_files = select_videos(args.input_dir, 10)  # Select 1% of the videos
    copy_selected_videos(args.input_dir, args.output_dir, selected_files)
    print(f"Selected and copied {len(selected_files)} videos out of {len(os.listdir(args.input_dir))} from {args.input_dir} to {args.output_dir}")
