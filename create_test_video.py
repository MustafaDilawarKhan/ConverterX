#!/usr/bin/env python3
"""
Create a simple test video file for testing video conversion
"""

import os
import subprocess

def create_test_video_with_ffmpeg():
    """Create a simple test video using FFmpeg"""
    try:
        # Create a simple 5-second test video with audio
        output_file = "test_video.mp4"
        
        # FFmpeg command to create a test video
        # Creates a 5-second video with:
        # - Red color background (320x240)
        # - 440Hz sine wave audio
        cmd = [
            'ffmpeg',
            '-f', 'lavfi',
            '-i', 'color=red:size=320x240:duration=5',
            '-f', 'lavfi', 
            '-i', 'sine=frequency=440:duration=5',
            '-c:v', 'libx264',
            '-c:a', 'aac',
            '-shortest',
            '-y',  # Overwrite output file
            output_file
        ]
        
        print("Creating test video with FFmpeg...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Test video created: {output_file}")
            print(f"   Duration: 5 seconds")
            print(f"   Resolution: 320x240")
            print(f"   Audio: 440Hz sine wave")
            print(f"   File size: {os.path.getsize(output_file) / 1024:.1f} KB")
            return True
        else:
            print(f"❌ Failed to create test video: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error creating test video: {str(e)}")
        return False

def create_test_audio():
    """Create a simple test audio file"""
    try:
        output_file = "test_audio.wav"
        
        # FFmpeg command to create a test audio file
        cmd = [
            'ffmpeg',
            '-f', 'lavfi',
            '-i', 'sine=frequency=440:duration=3',
            '-c:a', 'pcm_s16le',
            '-y',
            output_file
        ]
        
        print("Creating test audio with FFmpeg...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Test audio created: {output_file}")
            print(f"   Duration: 3 seconds")
            print(f"   Format: WAV (PCM)")
            print(f"   Frequency: 440Hz")
            print(f"   File size: {os.path.getsize(output_file) / 1024:.1f} KB")
            return True
        else:
            print(f"❌ Failed to create test audio: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error creating test audio: {str(e)}")
        return False

if __name__ == "__main__":
    print("🎬 Creating Test Media Files for Video Converter")
    print("=" * 50)
    
    # Check if FFmpeg is available
    try:
        result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ FFmpeg not found. Please install FFmpeg first.")
            exit(1)
        print("✅ FFmpeg is available")
    except FileNotFoundError:
        print("❌ FFmpeg not found. Please install FFmpeg first.")
        exit(1)
    
    print()
    
    # Create test files
    video_success = create_test_video_with_ffmpeg()
    print()
    audio_success = create_test_audio()
    
    print()
    print("📋 Test Results:")
    print(f"   Video: {'✅ Created' if video_success else '❌ Failed'}")
    print(f"   Audio: {'✅ Created' if audio_success else '❌ Failed'}")
    
    if video_success or audio_success:
        print()
        print("🚀 How to test:")
        print("1. Run the Universal File Converter GUI")
        print("2. Drag the test files into the converter")
        print("3. Try these conversions:")
        if video_success:
            print("   • test_video.mp4 → MP3 (extract audio)")
            print("   • test_video.mp4 → GIF (create animation)")
            print("   • test_video.mp4 → AVI (change format)")
        if audio_success:
            print("   • test_audio.wav → MP3 (compress audio)")
            print("   • test_audio.wav → FLAC (lossless)")
        print()
        print("💡 The converter will use FFmpeg for video/audio processing")
