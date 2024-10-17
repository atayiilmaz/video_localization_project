
# Video Localization Automation

A Python-based video localization automation tool that overlays images and titles onto a base video, generating localized versions with background music. This tool utilizes the `moviepy` library for video editing and supports various image formats.

## Features

- **Dynamic Image and Title Overlay**: Overlay images and titles on specified areas of the base video.
- **Background Music Integration**: Add corresponding background music for each localized video.
- **Flexible Configuration**: Specify output directory and customize title font size.
- **Automatic Image Conversion**: Convert unsupported image formats to JPEG automatically.
- **Scalability**: Handles a large number of images, titles, and audio tracks efficiently.

## Requirements

- Python 3.6 or higher
- Required libraries:
  - `moviepy`
  - `Pillow`
  - `glob`
  - `openpyxl`
  - `ffmpeg-python`

## Installation

1. **Set Up a Virtual Environment**:
   It is recommended to use a virtual environment to manage dependencies. You can create one using the following command:

   ```bash
   python -m venv env
   ```

   Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

2. **Install Required Libraries**:
   After activating the virtual environment, install the required libraries using pip:

   ```bash
   pip install
   ```

## Usage

You can run the main function to create localized videos by providing command-line arguments for flexibility. Below is an example of how to use the script with command-line parameters:

```bash
python main.py --font_size 30 --output_dir "output_videos"
```

### Command-Line Arguments

- `--font_size`: Font size for the titles (optional, default is 45).
- `--output_dir`: Directory to save the output localized videos (optional, default is `output/`).

### Example Call

Here’s a more detailed example:

```bash
python3 main.py \
--font_size 30 \
--output_dir "output_videos"
```

The localized videos will be saved in the specified output directory with filenames like `localized_video_1.mp4`, `localized_video_2.mp4`, etc.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- [MoviePy](https://zulko.github.io/moviepy/) for video editing capabilities.
- [FFmpeg](https://ffmpeg.org/) for powerful multimedia processing.
