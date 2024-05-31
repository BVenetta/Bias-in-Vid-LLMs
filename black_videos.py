import cv2
import os
import argparse
from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser(description="Black out every other frame of videos and save them to a new directory.")
    parser.add_argument('--input_dir', type=str, required=True, help='Directory containing input video files.')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory to save the augmented video files.')
    return parser.parse_args()

def blackout_every_other_frame(input_video_path, output_video_path):
    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video {input_video_path}")
        return

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % 2 == 0:
            frame[:] = 0  # Black out the frame
        out.write(frame)
        frame_count += 1

    cap.release()
    out.release()

def process_videos(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    video_files = [f for f in os.listdir(input_dir) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]

    for video_file in tqdm(video_files, desc="Processing videos"):
        input_path = os.path.join(input_dir, video_file)
        output_path = os.path.join(output_dir, video_file)
        blackout_every_other_frame(input_path, output_path)

    print(f"Processed {len(video_files)} videos. Augmented videos saved to {output_dir}")

if __name__ == "__main__":
    args = parse_args()
    process_videos(args.input_dir, args.output_dir)
