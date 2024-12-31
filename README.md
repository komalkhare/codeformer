# Video Face Enhancement with CodeFormer

This project enhances faces in a video using the CodeFormer model for super-resolution. The script detects faces in each frame of the video, applies face enhancement using CodeFormer, and generates an enhanced video as output.

## Features
- Detects faces in each frame of the video using OpenCV.
- Applies CodeFormer super-resolution to enhance facial regions.
- Outputs a new video with enhanced faces.

## Prerequisites
1. Python 3.7 or higher.
2. Required Python libraries:
   - OpenCV
   - PyTorch
   - Other dependencies specified in the [CodeFormer repository](https://github.com/sczhou/CodeFormer).
3. Pre-trained models for CodeFormer. Download from the CodeFormer repository and place them in the correct directory.

## Installation
1. Clone the CodeFormer repository:
   ```bash
   git clone https://github.com/sczhou/CodeFormer.git
Install the required dependencies:
# Video Face Enhancement with CodeFormer

This guide explains how to set up and use the `x.py` script to enhance faces in a video using CodeFormer super-resolution.

## Installation

### Install the required dependencies:
```bash
pip install -r CodeFormer/requirements.txt
##Usage
Place your input video (e.g., yongen.mp4) in the project directory.

Update the script (x.py) to ensure the paths are correct for:

The inference_codeformer.py script.


The pre-trained models.
python x.py
##Script Description
The script (x.py) processes the input video frame by frame:

1.Detects faces using OpenCV's Haar Cascade.

2.Enhances detected faces using CodeFormer super-resolution.

3.Replaces the original face regions with the enhanced faces in the frame.

4.Saves the enhanced video to the specified output path (e.g., output_yongen.mp4).
Example
Update the script with the input and output video file names:

python
Copy code
input_video = 'yongen.mp4'      # Input video file
output_video = 'output_yongen.mp4'  # Enhanced video output file

Run the script using the following command:

Copy code
python x.py --superres CodeFormer -iv yongen.mp4 -ia input_audio.mp3 -o output_yongen.m
