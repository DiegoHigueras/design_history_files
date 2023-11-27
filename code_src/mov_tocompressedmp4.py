import os
import subprocess
import tempfile
import shutil

def compress_video(input_path, output_path, target_size_mb, tolerance_percentage=1):
    try:
        # Start with a conservative guess for the bitrate
        target_bitrate = 8 * target_size_mb

        iteration = 1
        while True:
            # Create a temporary file to store the compressed video
            temp_output_path = tempfile.mktemp(suffix=".mp4")

            # Use ffmpeg to compress the video with the current target bitrate
            subprocess.run(["ffmpeg", "-i", input_path, "-c:v", "libx264", "-b:v", f"{target_bitrate}k", temp_output_path])

            # Get the actual file size of the temporary file
            actual_size = os.path.getsize(temp_output_path) / (1024 * 1024)  # Convert to megabytes

            # Calculate the tolerance range
            tolerance_range = target_size_mb * (tolerance_percentage / 100)

            # Print the iteration number and the size of the resulting file
            print(f"Iteration {iteration}: Actual size: {actual_size:.2f} MB")

            # Check if the actual size is within the tolerance range
            if abs(actual_size - target_size_mb) <= tolerance_range:
                # Move the temporary file to the destination path
                shutil.move(temp_output_path, output_path)
                print(f"Video compressed and saved to '{output_path}'. Actual size: {actual_size:.2f} MB")
                break
            elif actual_size > target_size_mb:
                # If the actual size is larger, reduce the bitrate
                target_bitrate *= 0.1
            else:
                # If the actual size is smaller, increase the bitrate
                target_bitrate *= 3

            iteration += 1

        print("Compression completed.")
    except Exception as e:
        print(f"Error compressing video: {e}")

# Example usage
file = "Screen Recording 2023-11-26 at 8.34.15 PM.mov"
input_video_path = "/Users/diegohiguerasruiz/Downloads/"+ file
output_video_path = "./mov_src/" + os.path.splitext(file)[0] + ".mp4"

# Input the desired file size in megabytes
desired_file_size_mb = 1  # Change this to your desired size

compress_video(input_video_path, output_video_path, target_size_mb=desired_file_size_mb, tolerance_percentage=20)
