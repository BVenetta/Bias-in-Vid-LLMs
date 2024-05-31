import os
import cv2
import argparse


def rotate_videos(input_dir, output_dir):
  """
  Rotates all video frames in a directory by 180 degrees vertically and saves them in a new directory.

  Args:
    input_dir: Path to the directory containing the videos.
    output_dir: Path to the directory where the flipped videos will be saved.
  """
  # Create the output directory if it doesn't exist
  os.makedirs(output_dir, exist_ok=True)

  # Get a list of video files in the input directory
  video_files = [f for f in os.listdir(input_dir) if f.lower().endswith((".mp4", ".avi", ".mov", ".mkv"))]

  for filename in video_files:
    video_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, filename)

    # Open the video capture object
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
      print(f"Error opening video: {video_path}")
      continue

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the video writer for the flipped video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Adjust codec if needed
    out = cv2.VideoWriter(output_path, fourcc, cap.get(cv2.CAP_PROP_FPS), (width, height))

    while True:
      ret, frame = cap.read()

      # Exit loop if frame is not read
      if not ret:
        break

      # Flip the frame vertically
      flipped_frame = cv2.flip(frame, 0)  # Flip code 0 for vertical flip

      # Write the flipped frame to the output video
      out.write(flipped_frame)

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"Finished flipping video: {filename}")


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Rotate videos vertically.")
  parser.add_argument("--input_dir", type=str, required=True, help="Path to the directory containing the videos.")
  parser.add_argument("--output_dir", type=str, required=True, help="Path to the directory where the flipped videos will be saved.")
  args = parser.parse_args()

  rotate_videos(args.input_dir, args.output_dir)

print("Flipping videos completed!")
