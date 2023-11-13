import os
import base64
from PIL import Image as PILImage
from io import BytesIO

def resize_image(image_path, output_size):
    with PILImage.open(image_path) as img:
        img_resized = img.resize(output_size)
    return img_resized

def png_to_html(png_path, output_directory, output_size=(200, 200)):
    # Resize the image
    resized_image = resize_image(png_path, output_size)

    # Convert resized image to base64
    with BytesIO() as image_file:
        resized_image.save(image_file, format="PNG")
        encoded_image = base64.b64encode(image_file.getvalue()).decode("utf-8")

    # Create the output HTML file path
    output_html_path = os.path.join(output_directory, os.path.splitext(os.path.basename(png_path))[0] + ".html")

    # Create an HTML file with the embedded image
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Image to HTML</title>
    </head>
    <body>
        <img src="data:image/png;base64,{encoded_image}" alt="PNG Image">
    </body>
    </html>
    """

    # Write the HTML content to the output file
    with open(output_html_path, "w") as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    # Replace 'input_image.png' and '/path/to/output_directory' with your actual paths
    input_png_path = "/Users/diegohiguerasruiz/NO_git_files/Bioinspired_projects/Human_hand/img/version1_6_img1.png"
    output_directory = "/Users/diegohiguerasruiz/NO_git_files/Bioinspired_projects/Human_hand/img/html_versions/"

    # Specify the desired output size (in pixels)
    output_size = (int(7 / 2.54 * 300), int(7 / 2.54 * 300))  # 7 cm converted to pixels at 300 DPI

    # Convert PNG to HTML with resizing
    png_to_html(input_png_path, output_directory, output_size)
