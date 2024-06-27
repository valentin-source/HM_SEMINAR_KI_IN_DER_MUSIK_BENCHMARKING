import argparse
import subprocess
import time

def run_whisper(audio_file, model, output_dir):
    start_time = time.time()
    command = ["whisper", audio_file, "--model", model, "--output_dir", output_dir]
    try:
        print("Starting transcription")
        result = subprocess.run(command, check=True, capture_output=True)
        end_time = time.time()
        duration = end_time - start_time
        print(result.stdout.decode())
        print(f"Transcription took {duration:.2f} seconds")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python wrapper for Whisper CLI")
    parser.add_argument("audio_file", type=str, help="Path to the audio file to transcribe")
    parser.add_argument("--model", type=str, default="base", help="Model to use for transcription (default: base)")
    parser.add_argument("--output_dir", type=str, default=".", help="WHere the output files should be stored")
    args = parser.parse_args()
    run_whisper(args.audio_file, args.model, args.output_dir)
