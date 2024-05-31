import os
import json
import shutil
import argparse

def parse_args():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Select and copy videos corresponding to QA JSON files.")
    parser.add_argument('--video_dir', help='Directory containing video files.', required=True)
    parser.add_argument('--gt_file_question', help='Path to the ground truth file containing questions.', required=True)
    parser.add_argument('--output_dir', help='Directory to save the selected videos.', required=True)
    return parser.parse_args()

def find_video_path(video_dir, video_name, formats):
    """
    Search for a video file that contains the given video_name.

    Args:
        video_dir (str): Directory containing video files.
        video_name (str): The name of the video to find.
        formats (list): List of video file formats to search for.

    Returns:
        str: The path to the video file if found, else None.
    """
    for root, _, files in os.walk(video_dir):
        for file in files:
            if any(file.endswith(fmt) for fmt in formats) and video_name in file:
                return os.path.join(root, file)
    return None

def copy_videos(video_dir, gt_file_question, output_dir):
    """
    Copy videos corresponding to QA JSON files to a separate folder.

    Args:
        video_dir (str): Directory containing video files.
        gt_file_question (str): Path to the ground truth file containing questions.
        output_dir (str): Directory to save the selected videos.
    """
    # Load ground truth questions
    with open(gt_file_question) as file:
        gt_questions = json.load(file)

    video_formats = ['.mp4', '.avi', '.mov', '.mkv']
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for sample in gt_questions:
        video_name = sample['video_name']
        video_path = find_video_path(video_dir, video_name, video_formats)
        
        if video_path and os.path.exists(video_path):
            print(f"Copying video: {video_name}, resolved path: {video_path}")
            shutil.copy(video_path, output_dir)
        else:
            print(f"Video file not found for '{video_name}'")

if __name__ == "__main__":
    args = parse_args()
    copy_videos(args.video_dir, args.gt_file_question, args.output_dir)
