import cv2
import subprocess
import torch
from pathlib import Path

# Function to apply CodeFormer SuperResolution
def apply_codeformer_superres(image_path, output_path):
    try:
        # Running CodeFormer superresolution through subprocess
        subprocess.run([
            'python', 'D:\\code\\CodeFormer-master\\inference_codeformer.py',
            '--input_path', image_path,
            '--bg_upsampler', 'realesrgan',
            '--face_upsample', 'True',
            '--w', '1.0',
            '--save_path', output_path
        ], check=True)
        print(f"Superresolution applied and saved to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error running CodeFormer: {e}")

# Function to process the video and enhance the faces
def enhance_video_with_codeformer(input_video, output_video, superres_method):
    # Open the video file
    video_capture = cv2.VideoCapture(input_video)
    if not video_capture.isOpened():
        print("Error: Could not open video file.")
        return

    frame_rate = video_capture.get(cv2.CAP_PROP_FPS)
    frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    # Prepare output video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out_video = cv2.VideoWriter(output_video, fourcc, frame_rate, 
                                (int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)), 
                                 int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    # Load the face detector (Haar Cascade or another model)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    for frame_idx in range(frame_count):
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Failed to read frame.")
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

        if len(faces) > 0:
            # Process faces
            for (x, y, w, h) in faces:
                face_region = frame[y:y+h, x:x+w]
                
                # Save face image temporarily for super-resolution
                face_image_path = 'temp_face.jpg'
                cv2.imwrite(face_image_path, face_region)

                # Enhance face using CodeFormer
                enhanced_face_path = 'enhanced_face.jpg'
                apply_codeformer_superres(face_image_path, enhanced_face_path)

                # Read the enhanced face and replace the original face
                enhanced_face = cv2.imread(enhanced_face_path)
                if enhanced_face is not None:
                    frame[y:y+h, x:x+w] = enhanced_face

        # Write the processed frame to the output video
        out_video.write(frame)
        print(f"Processing frame {frame_idx + 1}/{frame_count}")

    video_capture.release()
    out_video.release()
    print(f"Video saved to {output_video}")

# Example usage
input_video = 'yongen.mp4'
output_video = 'output_yongen.mp4'
superres_method = 'CodeFormer'

enhance_video_with_codeformer(input_video, output_video, superres_method)
