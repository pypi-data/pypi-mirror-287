
# Pixi-CLI 🧚

Pixi-CLI is a command-line tool for image conversion and basic image processing tasks.

## Features

- Crop images
- Adjust exposure
- Adjust saturation
- Adjust contrast
- Adjust sharpness
- Apply box blur
- Apply Gaussian blur
- Reduce noise
- Detect edges
- Apply common filters
- Convert images to black and white
- Invert colors
- Rotate images (90, 180, 270 degrees)
- Flip images (horizontally and vertically)
- Create thumbnails
- Compress images
- Get image size
- Fetch image metadata
- Convert between image formats (e.g., jpg, png, bmp, gif, tiff, svg)

## Installation
You can either download Pixi-CLI through PyPI (recommended, requires Python to be installed on your machine) or you can download the executable (more steps, does not requires Python to be installed on your machine)

### Installing via PyPI

1. Ensure you have Python and pip installed on your machine.
2. Install Pixi-CLI using pip:
```sh
pip install pixi-cli
```

### Downloading the Executable

1. Download the latest release of `pixi` from the [Releases](https://github.com/zainkarim/pixi-cli/releases) page.
2. Extract the ZIP file to a desired location on your machine.

## Adding Pixi to Your PATH

### Windows

1. Extract the downloaded ZIP file to a desired location, such as `C:\Program Files\pixi`.
2. Open the Start Menu, search for "Environment Variables", and select "Edit the system environment variables".
3. In the System Properties window, click the "Environment Variables" button.
4. In the Environment Variables window, find the "Path" variable in the "System variables" section and select it, then click "Edit".
5. Click "New" and add the path to the directory where `pixi.exe` is located (e.g., `C:\Program Files\pixi`).
6. Click "OK" to close all dialog boxes.
7. Open Command Prompt and type `pixi --help` to verify that it works from any location.

### macOS and Linux

1. Extract the downloaded ZIP file to a desired location, such as `/usr/local/bin/pixi`.
2. Make the file executable:
   ```sh
   chmod +x /usr/local/bin/pixi
   ```
3. Open a terminal and edit your shell configuration file (`.bashrc`, `.bash_profile`, `.zshrc`, etc.):
   ```sh
   nano ~/.bashrc  # or ~/.bash_profile or ~/.zshrc
   ```
4. Add the following line to include the directory in your PATH:
   ```sh
   export PATH=$PATH:/usr/local/bin
   ```
5. Save the file and source it to apply the changes:
   ```sh
   source ~/.bashrc  # or source ~/.bash_profile or source ~/.zshrc
   ```
6. Open a new terminal and type `pixi --help` to verify that it works from any location.

## Usage

### Basic Usage

1. Open a terminal or Command Prompt.
2. Use the command line to perform various image processing tasks.

### Examples

1. **Get Image Size:**
   ```sh
   pixi /path/to/input.jpg --size
   ```

2. **Get Image Metadata:**
   ```sh
   pixi  /path/to/input.jpg --metadata
   ```

3. **Crop Image:**
   ```sh
   pixi /path/to/input.jpg --output_path /path/to/output.jpg --crop 50 50 200 200
   ```

4. **Adjust Exposure:**
   ```sh
   pixi /path/to/input.jpg --output_path /path/to/output.jpg --exposure 1.2
   ```

5. **Apply Gaussian Blur:**
   ```sh
   pixi /path/to/input.jpg --output_path /path/to/output.jpg --gaussian_blur 2.0
   ```

6. **Convert to Black and White:**
   ```sh
   pixi /path/to/input.jpg --output_path /path/to/output.jpg --bw
   ```

7. **Rotate Image 90 Degrees:**
   ```sh
   pixi /path/to/input.jpg --output_path /path/to/output.jpg --rotate90
   ```

8. **Convert Image Format:**
   ```sh
   pixi /path/to/input.jpg --convert png
   ```

### Full Command-Line Arguments

- `image_path`: Path to the input image (required).
- `--output_path`: Path to save the processed image (required for processing operations).
- `--crop left top right bottom`: Crop the image to the specified box.
- `--exposure factor`: Adjust the exposure by the given factor.
- `--saturation factor`: Adjust the saturation by the given factor.
- `--contrast factor`: Adjust the contrast by the given factor.
- `--sharpness factor`: Adjust the sharpness by the given factor.
- `--box_blur radius`: Apply box blur with the specified radius.
- `--gaussian_blur radius`: Apply Gaussian blur with the specified radius.
- `--reduce_noise`: Reduce noise in the image.
- `--edge_detect`: Detect edges in the image
- `--bw`: Convert the image to black and white.
- `--invert`: Invert the colors of the image.
- `--thumbnail width height`: Create a thumbnail of the specified size.
- `--compression quality`: Compress the image to the specified quality (0-100).
- `--size`: Get the size of the image.
- `--metadata`: Fetch the metadata of the image.
- `--rotate90`: Rotate the image 90 degrees clockwise.
- `--rotate180`: Rotate the image 180 degrees.
- `--rotate270`: Rotate the image 270 degrees clockwise.
- `--flip_horiz`: Flip the image horizontally.
- `--flip_vert`: Flip the image vertically.
- `--convert format`: Convert the image to the specified format.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License.
