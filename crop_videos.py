import os
import cv2
import argparse
import torch
from torchvision import transforms
from torchvision.io import read_video, write_video
from torchvision.transforms.functional import to_pil_image, to_tensor
from tqdm import tqdm

def load_and_crop_video(video_path):
    """
    Load a video and perform random crop on each frame.

    Args:
        video_path (str): Path to the video file.

    Returns:
        torch.Tensor: Tensor containing cropped frames.
        float: The frame rate of the input video.
    """
    # Read the video
    frames, _, info = read_video(video_path)
    frame_rate = info["video_fps"]
    height, width = frames.shape[1], frames.shape[2]

    # Calculate crop size as one-third of the original dimensions
    crop_height = height // 3
    crop_width = width // 3
    crop_size = (crop_height, crop_width)

    # Define the random crop transform
    random_crop = transforms.RandomCrop(crop_size)

    # Apply the random crop to each frame
    cropped_frames = torch.stack([to_tensor(random_crop(to_pil_image(frame))) for frame in frames])

    return cropped_frames, frame_rate

def save_cropped_video(frames, output_path, frame_rate):
    """
    Save the cropped frames as a video file.

    Args:
        frames (torch.Tensor): Tensor containing the cropped video frames.
        output_path (str): Path to save the cropped video.
        frame_rate (float): The frame rate of the output video.
    """
    write_video(output_path, frames, fps=frame_rate)

def process_videos(input_dir, output_dir):
    """
    Process all videos in the input directory, performing random crop on each frame and saving as a new video in the output directory.

    Args:
        input_dir (str): Directory containing input videos.
        output_dir (str): Directory to save output videos.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in tqdm(os.listdir(input_dir)):
        if filename.endswith(('.mp4', '.avi', '.mov', '.mkv')):
            video_path = os.path.join(input_dir, filename)
            try:
                cropped_frames, frame_rate = load_and_crop_video(video_path)
                if cropped_frames is not None:
                    video_output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_cropped.mp4")
                    save_cropped_video(cropped_frames, video_output_path, frame_rate)
                    print(f"Saved cropped video from {filename} to {video_output_path}")
            except Exception as e:
                print(f"Error processing file '{filename}': {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform random crop on each frame of videos in a directory and save as new videos.")
    parser.add_argument("input_dir", type=str, help="Path to the input directory containing videos.")
    parser.add_argument("output_dir", type=str, help="Path to the output directory to save cropped videos.")

    args = parser.parse_args()

    process_videos(args.input_dir, args.output_dir)
