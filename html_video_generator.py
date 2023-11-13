import os
import base64

def video_to_html(video_path, output_directory):
    # Read the video file as binary
    with open(video_path, "rb") as video_file:
        # Encode the binary data as base64
        encoded_video = base64.b64encode(video_file.read()).decode("utf-8")

    # Create the output HTML file path
    output_html_path = os.path.join(output_directory, os.path.splitext(os.path.basename(video_path))[0] + ".html")

    # Create an HTML file with the embedded video
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Video to HTML</title>
    </head>
    <body>
        <video width="640" height="480" controls>
            <source src="data:video/mp4;base64,{encoded_video}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </body>
    </html>
    """

    # Write the HTML content to the output file
    with open(output_html_path, "w") as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    # Replace 'input_video.mov' and '/path/to/output_directory' with your actual paths
    input_video_path = "/Users/diegohiguerasruiz/NO_git_files/Bioinspired_projects/Human_hand/mov_src/Screen Recording 2023-11-13 at 10.52.52 AM.mov"
    output_directory = "/Users/diegohiguerasruiz/NO_git_files/Bioinspired_projects/Human_hand/mov_src/mov_html_versions/"

    # Convert MOV to HTML with MP4
    video_to_html(input_video_path, output_directory)
