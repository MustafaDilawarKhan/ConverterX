#!/usr/bin/env python3
"""
Quick test for video conversion
"""

import os
import sys
import subprocess

def test_ffmpeg():
    """Test if FFmpeg works"""
    try:
        result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print("✅ FFmpeg is working")
            return True
        else:
            print("❌ FFmpeg failed")
            return False
    except Exception as e:
        print(f"❌ FFmpeg test failed: {e}")
        return False

def test_video_to_mp3():
    """Test video to MP3 conversion"""
    if not os.path.exists('test_video.mp4'):
        print("❌ test_video.mp4 not found")
        return False
    
    print("🔄 Testing MP4 → MP3 conversion...")
    
    cmd = [
        'ffmpeg', '-i', 'test_video.mp4', 
        '-vn', '-acodec', 'mp3', '-ab', '192k', 
        '-y', 'quick_test.mp3'
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0 and os.path.exists('quick_test.mp3'):
            size = os.path.getsize('quick_test.mp3') / 1024
            print(f"✅ MP3 conversion successful! ({size:.1f} KB)")
            return True
        else:
            print(f"❌ MP3 conversion failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ MP3 conversion error: {e}")
        return False

def test_video_to_gif():
    """Test video to GIF conversion"""
    if not os.path.exists('test_video.mp4'):
        print("❌ test_video.mp4 not found")
        return False
    
    print("🔄 Testing MP4 → GIF conversion...")
    
    cmd = [
        'ffmpeg', '-i', 'test_video.mp4',
        '-vf', 'scale=320:-1:flags=lanczos,fps=10',
        '-y', 'quick_test.gif'
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0 and os.path.exists('quick_test.gif'):
            size = os.path.getsize('quick_test.gif') / 1024
            print(f"✅ GIF conversion successful! ({size:.1f} KB)")
            return True
        else:
            print(f"❌ GIF conversion failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ GIF conversion error: {e}")
        return False

if __name__ == "__main__":
    print("🎬 Quick Video Conversion Test")
    print("=" * 40)
    
    # Test FFmpeg
    if not test_ffmpeg():
        print("\n❌ FFmpeg is not working. Video conversion will fail.")
        sys.exit(1)
    
    print()
    
    # Test conversions
    mp3_ok = test_video_to_mp3()
    print()
    gif_ok = test_video_to_gif()
    
    print()
    print("📊 Results:")
    print(f"   MP3: {'✅' if mp3_ok else '❌'}")
    print(f"   GIF: {'✅' if gif_ok else '❌'}")
    
    if mp3_ok and gif_ok:
        print("\n🎉 Video conversion is working!")
        print("   The GUI should now handle video conversions successfully.")
    else:
        print("\n⚠️  Some video conversions failed.")
        print("   Check FFmpeg installation and codecs.")
    
    # Cleanup
    for file in ['quick_test.mp3', 'quick_test.gif']:
        if os.path.exists(file):
            os.remove(file)
            print(f"🗑️  Cleaned up {file}")
