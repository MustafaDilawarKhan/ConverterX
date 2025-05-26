#!/usr/bin/env python3
"""
Test script for video conversion functionality
"""

import os
import sys
from video_audio_converter import VideoAudioConverter, FFMPEG_SYSTEM_AVAILABLE, MOVIEPY_AVAILABLE

def test_video_conversion():
    """Test video conversion capabilities"""
    print("🎬 Testing Video Conversion Capabilities")
    print("=" * 50)
    
    # Check dependencies
    print("📋 Dependency Check:")
    print(f"   MoviePy Available: {'✅' if MOVIEPY_AVAILABLE else '❌'}")
    print(f"   FFmpeg Available: {'✅' if FFMPEG_SYSTEM_AVAILABLE else '❌'}")
    
    if not FFMPEG_SYSTEM_AVAILABLE and not MOVIEPY_AVAILABLE:
        print("❌ No video conversion tools available!")
        print("   Please install MoviePy (pip install moviepy) or FFmpeg")
        return False
    
    print()
    
    # Initialize converter
    vc = VideoAudioConverter()
    
    # Check for test video
    test_video = "test_video.mp4"
    if not os.path.exists(test_video):
        print(f"❌ Test video '{test_video}' not found!")
        print("   Run 'python create_test_video.py' first to create test files")
        return False
    
    print(f"✅ Found test video: {test_video}")
    print(f"   File size: {os.path.getsize(test_video) / 1024:.1f} KB")
    print()
    
    # Test conversions
    tests = [
        ("Video → GIF", "test_output.gif", lambda: vc.convert_video_to_gif(test_video, "test_output.gif")),
        ("Video → MP3", "test_output.mp3", lambda: vc.convert_video_to_audio(test_video, "test_output.mp3", "mp3")),
        ("Video → AVI", "test_output.avi", lambda: vc.convert_video_format(test_video, "test_output.avi", "avi")),
        ("Video → WMV", "test_output.wmv", lambda: vc.convert_video_format(test_video, "test_output.wmv", "wmv")),
    ]
    
    results = []
    
    for test_name, output_file, test_func in tests:
        print(f"🔄 Testing {test_name}...")
        
        # Clean up previous output
        if os.path.exists(output_file):
            os.remove(output_file)
        
        try:
            success = test_func()
            
            if success and os.path.exists(output_file):
                file_size = os.path.getsize(output_file) / 1024
                print(f"   ✅ Success! Output: {output_file} ({file_size:.1f} KB)")
                results.append((test_name, True, f"{file_size:.1f} KB"))
            else:
                print(f"   ❌ Failed! No output file created")
                results.append((test_name, False, "No output"))
                
        except Exception as e:
            print(f"   ❌ Failed! Error: {str(e)}")
            results.append((test_name, False, str(e)))
        
        print()
    
    # Summary
    print("📊 Test Results Summary:")
    print("-" * 50)
    successful = 0
    for test_name, success, details in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"   {status} {test_name}: {details}")
        if success:
            successful += 1
    
    print()
    print(f"🎯 Overall: {successful}/{len(tests)} tests passed")
    
    if successful == len(tests):
        print("🎉 All video conversion tests passed!")
        print("   The Universal File Converter is ready for video processing!")
    elif successful > 0:
        print("⚠️  Some video conversions work, others may need troubleshooting")
    else:
        print("❌ All video conversion tests failed")
        print("   Check FFmpeg installation and file permissions")
    
    return successful > 0

def test_ffmpeg_direct():
    """Test FFmpeg directly"""
    print("\n🔧 Testing FFmpeg Direct Access:")
    print("-" * 30)
    
    import subprocess
    import shutil
    
    # Check if FFmpeg is in PATH
    ffmpeg_path = shutil.which('ffmpeg')
    if ffmpeg_path:
        print(f"✅ FFmpeg found at: {ffmpeg_path}")
        
        # Test FFmpeg version
        try:
            result = subprocess.run(['ffmpeg', '-version'], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                version_line = result.stdout.split('\n')[0]
                print(f"✅ FFmpeg version: {version_line}")
                return True
            else:
                print(f"❌ FFmpeg version check failed: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ FFmpeg test failed: {str(e)}")
            return False
    else:
        print("❌ FFmpeg not found in PATH")
        print("   Install FFmpeg from: https://ffmpeg.org/")
        return False

if __name__ == "__main__":
    print("🎬 Universal File Converter - Video Conversion Test")
    print("=" * 60)
    print()
    
    # Test FFmpeg first
    ffmpeg_ok = test_ffmpeg_direct()
    print()
    
    if ffmpeg_ok:
        # Test video conversion
        conversion_ok = test_video_conversion()
        
        if conversion_ok:
            print("\n🚀 Ready to use video conversion in the GUI!")
            print("   Try dragging a video file and converting to GIF or MP3")
        else:
            print("\n🔧 Video conversion needs troubleshooting")
    else:
        print("\n❌ FFmpeg is required for video conversion")
        print("   Please install FFmpeg first")
    
    print("\n" + "=" * 60)
