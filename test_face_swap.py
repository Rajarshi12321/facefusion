import sys
# from facefusion import get_test_jobs_directory, get_test_example_file, get_test_output_file
import subprocess
import os

import os

def get_test_jobs_directory():
    return os.path.join(os.path.dirname(__file__), 'tests', 'jobs')

def perform_face_swap(source_image_path, target_video_path, output_video_path):
    commands = [
        sys.executable, 
        'facefusion.py', 
        'headless-run', 
        '--jobs-path', get_test_jobs_directory(), 
        '--processors', 'face_swapper', 
        '-s', source_image_path, 
        '-t', target_video_path, 
        '-o', output_video_path, 
        '--trim-frame-start', '95',
        # '--trim-frame-end', '96',
        '--trim-frame-end', '105',
        '--output_face_swaps_only'
        # '--trim-frame-end', '100',
    ]
    print(subprocess.run(commands).returncode)
    # logging.info(f"Command executed with return code: {result.returncode}")
 
    assert subprocess.run(commands).returncode == 0

# Example usage
perform_face_swap('test_files/input2.jpg', 'test_files/input_video3.mp4', 'test_files/outputs/output.mp4')
