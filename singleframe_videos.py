import os
import random
import cv2
import argparse

def load_and_augment_video(video_path):
    """
    Load and select a single random frame from the video.

    Args:
        video_path (str): Path to the video file.

    Returns:
        frame: The randomly selected frame.
        frame_rate: The frame rate of the input video.
    """
    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_count = 0

    # Get frame rate of the video
    frame_rate = cap.get(cv2.CAP_PROP_FPS)

    # Read all frames
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
        frame_count += 1

    cap.release()

    # Select a random frame
    if frames:
        random_frame = random.choice(frames)
        return random_frame, frame_rate
    else:
        return None, None

def save_video_frame(frame, output_path, frame_rate):
    """
    Save a single frame as a video file to the output path.

    Args:
        frame (ndarray): The video frame to save.
        output_path (str): Path to save the video.
        frame_rate (float): The frame rate of the output video.
    """
    height, width, layers = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, frame_rate, (width, height))
    out.write(frame)
    out.release()

def process_videos(input_dir, output_dir):
    """
    Process all videos in the input directory, saving a single random frame from each as a video in the output directory.

    Args:
        input_dir (str): Directory containing input videos.
        output_dir (str): Directory to save output videos.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(('.mp4', '.avi', '.mov', '.mkv')):
            video_path = os.path.join(input_dir, filename)
            frame, frame_rate = load_and_augment_video(video_path)
            if frame is not None:
                video_output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_single_frame.mp4")
                save_video_frame(frame, video_output_path, frame_rate)
                print(f"Saved video with single frame from {filename} to {video_output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract a random frame from each video in a directory and save as a new video.")
    parser.add_argument("input_dir", type=str, help="Path to the input directory containing videos.")
    parser.add_argument("output_dir", type=str, help="Path to the output directory to save videos.")

    args = parser.parse_args()

    process_videos(args.input_dir, args.output_dir)
