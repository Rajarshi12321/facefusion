import os
import sys
import subprocess

def get_test_jobs_directory():
    return os.path.join(os.path.dirname(__file__), 'tests', 'jobs')

def perform_face_swap(
    source_image_path,
    target_video_path,
    output_video_path,
    trim_start=0,
    trim_end=None,
    output_face_swaps_only=True
):
    commands = [
        sys.executable,
        'facefusion.py',
        'headless-run',
        '--jobs-path', get_test_jobs_directory(),
        '--processors', 'face_swapper',
        '-s', source_image_path,
        '-t', target_video_path,
        '-o', output_video_path
    ]

    if trim_start > 0:
        commands += ['--trim-frame-start', str(trim_start)]
    if trim_end is not None:
        commands += ['--trim-frame-end', str(trim_end)]
    if output_face_swaps_only:
        commands += ['--output_face_swaps_only']

    print("Running command:", " ".join(commands))

    # result = subprocess.run(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    result = subprocess.run(commands)

    print("STDOUT:\n", result.stdout)
    print("STDERR:\n", result.stderr)

    if result.returncode != 0:
        raise RuntimeError(f"Face swap failed with return code {result.returncode}")
    else:
        print("✅ Face swap completed successfully.")

# Example usage
if __name__ == "__main__":
    perform_face_swap(
        source_image_path='test_files/input2.jpg',
        target_video_path='test_files/input_video3.mp4',
        output_video_path='test_files/outputs/output_with_update.mp4',
        trim_start=95,
        trim_end=105,
        output_face_swaps_only=True
    )
