
# Pixi-CLI 🧚

Pixi-CLI is a command-line tool for basic image processing tasks. It allows users to crop images, adjust exposure, saturation, contrast, and sharpness, apply blur effects, convert images to black and white, invert colors, rotate images, flip images, and fetch image metadata.

## Features

- Crop images
- Adjust exposure
- Adjust saturation
- Adjust contrast
- Adjust sharpness
- Apply box blur
- Apply Gaussian blur
- Convert images to black and white
- Invert colors
- Rotate images (90, 180, 270 degrees)
- Flip images (horizontally and vertically)
- Get image size
- Fetch image metadata

## Installation

### Downloading the Executable

1. Download the latest release of `pixi-cli` from the [Releases](https://github.com/zainkarim/pixi-cli/releases) page.
2. Extract the ZIP file to a desired location on your machine.

## Adding Pixi-CLI to Your PATH

### Windows

1. Extract the downloaded ZIP file to a desired location, such as `C:\Program Files\pixi-cli`.
2. Open the Start Menu, search for "Environment Variables", and select "Edit the system environment variables".
3. In the System Properties window, click the "Environment Variables" button.
4. In the Environment Variables window, find the "Path" variable in the "System variables" section and select it, then click "Edit".
5. Click "New" and add the path to the directory where `pixi-cli.exe` is located (e.g., `C:\Program Files\pixi-cli`).
6. Click "OK" to close all dialog boxes.
7. Open Command Prompt and type `pixi-cli --help` to verify that it works from any location.

### macOS and Linux

1. Extract the downloaded ZIP file to a desired location, such as `/usr/local/bin/pixi-cli`.
2. Make the file executable:
   ```sh
   chmod +x /usr/local/bin/pixi-cli
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
6. Open a new terminal and type `pixi-cli --help` to verify that it works from any location.

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
- `--bw`: Convert the image to black and white.
- `--invert`: Invert the colors of the image.
- `--size`: Get the size of the image.
- `--metadata`: Fetch the metadata of the image.
- `--rotate90`: Rotate the image 90 degrees clockwise.
- `--rotate180`: Rotate the image 180 degrees.
- `--rotate270`: Rotate the image 270 degrees clockwise.
- `--flip_horiz`: Flip the image horizontally.
- `--flip_vert`: Flip the image vertically.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License.
