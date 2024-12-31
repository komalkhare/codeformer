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
bash
Copy code
pip install -r CodeFormer/requirements.txt
Install OpenCV:
bash
Copy code
pip install opencv-python
Usage
Place your input video (e.g., yongen.mp4) in the project directory.
Update the script (x.py) to ensure the paths are correct for:
The inference_codeformer.py script.
The pre-trained models.
Run the script:
bash
Copy code
python x.py
Script Description
x.py processes the input video frame by frame:
Detects faces using OpenCV's Haar Cascade.
Enhances detected faces using CodeFormer super-resolution.
Replaces the original face regions with the enhanced faces in the frame.
Saves the enhanced video to the specified output path (e.g., output_yongen.mp4).
Example
python
Copy code
input_video = 'yongen.mp4'      # Input video file
output_video = 'output_yongen.mp4'  # Enhanced video output file
Run the script to process the video:

bash
Copy code
python x.py
Files
x.py: Main script for video processing and face enhancement.
temp_face.jpg: Temporary file to store detected face regions.
enhanced_face.jpg: Temporary file for enhanced face regions.
Notes
Ensure the paths to CodeFormer scripts and pre-trained models are correctly set.
The script currently processes faces sequentially. For performance optimization, consider batch processing.
Troubleshooting
Error: Could not open video file
Verify the input video path.
Error: Failed to read frame
Ensure the video is not corrupted.
Torch warnings
Update PyTorch to the latest version compatible with your system and GPU.
