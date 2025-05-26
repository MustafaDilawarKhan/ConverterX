#!/usr/bin/env python3
"""
Video and Audio Converter Module
Handles conversion between video formats, video to audio, and video to GIF
"""

import os
import logging
from pathlib import Path

try:
    from moviepy.editor import VideoFileClip, AudioFileClip
    MOVIEPY_AVAILABLE = True
except ImportError:
    MOVIEPY_AVAILABLE = False
    logging.warning("MoviePy not available. Video/audio conversion will be limited.")

try:
    import ffmpeg
    FFMPEG_AVAILABLE = True
except ImportError:
    FFMPEG_AVAILABLE = False
    logging.warning("FFmpeg-python not available. Some video conversions may not work.")

# Try to use subprocess with ffmpeg directly as fallback
import subprocess
import shutil

def check_ffmpeg_installed():
    """Check if ffmpeg is available in system PATH"""
    return shutil.which('ffmpeg') is not None

FFMPEG_SYSTEM_AVAILABLE = check_ffmpeg_installed()


class VideoAudioConverter:
    """Handles video and audio file conversions"""

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        # Check dependencies
        if not MOVIEPY_AVAILABLE:
            self.logger.warning("MoviePy not installed. Install with: pip install moviepy")
        if not FFMPEG_AVAILABLE:
            self.logger.warning("FFmpeg-python not installed. Install with: pip install ffmpeg-python")

    def convert_video_to_audio(self, input_file, output_file, audio_format='mp3'):
        """Convert video file to audio format"""
        try:
            # Try MoviePy first
            if MOVIEPY_AVAILABLE:
                return self._convert_video_to_audio_moviepy(input_file, output_file, audio_format)

            # Fallback to system FFmpeg
            elif FFMPEG_SYSTEM_AVAILABLE:
                return self._convert_video_to_audio_ffmpeg(input_file, output_file, audio_format)

            else:
                raise Exception("No video conversion tools available. Please install MoviePy (pip install moviepy) or FFmpeg")

        except Exception as e:
            self.logger.error(f"Video to audio conversion failed: {str(e)}")
            return False

    def _convert_video_to_audio_moviepy(self, input_file, output_file, audio_format='mp3'):
        """Convert video to audio using MoviePy"""
        self.logger.info(f"Converting video to audio using MoviePy: {input_file} -> {output_file}")

        # Check if input file exists
        if not os.path.exists(input_file):
            raise Exception(f"Input file does not exist: {input_file}")

        # Load video file with error handling
        try:
            video = VideoFileClip(input_file)
        except Exception as e:
            raise Exception(f"Failed to load video file. Error: {str(e)}. Make sure FFmpeg is installed.")

        # Extract audio
        audio = video.audio

        if audio is None:
            video.close()
            raise Exception("No audio track found in video file")

        # Set audio parameters based on format
        audio_params = self._get_audio_params(audio_format)

        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        # Write audio file with better error handling
        try:
            audio.write_audiofile(output_file, **audio_params, verbose=False, logger=None, temp_audiofile_path=None)
        except Exception as e:
            audio.close()
            video.close()
            raise Exception(f"Failed to write audio file. Error: {str(e)}")

        # Clean up
        audio.close()
        video.close()

        self.logger.info(f"Successfully converted video to {audio_format.upper()}")
        return True

    def _convert_video_to_audio_ffmpeg(self, input_file, output_file, audio_format='mp3'):
        """Convert video to audio using system FFmpeg"""
        self.logger.info(f"Converting video to audio using FFmpeg: {input_file} -> {output_file}")

        # Check if input file exists
        if not os.path.exists(input_file):
            raise Exception(f"Input file does not exist: {input_file}")

        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        # Build FFmpeg command
        cmd = ['ffmpeg', '-i', input_file, '-vn']  # -vn means no video

        # Add audio codec based on format
        if audio_format.lower() == 'mp3':
            cmd.extend(['-acodec', 'mp3', '-ab', '192k'])
        elif audio_format.lower() == 'wav':
            cmd.extend(['-acodec', 'pcm_s16le'])
        elif audio_format.lower() == 'aac':
            cmd.extend(['-acodec', 'aac', '-ab', '128k'])
        elif audio_format.lower() == 'flac':
            cmd.extend(['-acodec', 'flac'])
        elif audio_format.lower() == 'ogg':
            cmd.extend(['-acodec', 'libvorbis', '-ab', '192k'])
        else:
            cmd.extend(['-acodec', 'mp3', '-ab', '192k'])  # Default to MP3

        cmd.extend(['-y', output_file])  # -y to overwrite output file

        # Run FFmpeg command
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            if result.returncode != 0:
                raise Exception(f"FFmpeg failed: {result.stderr}")

            self.logger.info(f"Successfully converted video to {audio_format.upper()}")
            return True

        except subprocess.TimeoutExpired:
            raise Exception("Conversion timed out after 5 minutes")
        except Exception as e:
            raise Exception(f"FFmpeg conversion failed: {str(e)}")

    def convert_video_format(self, input_file, output_file, target_format):
        """Convert video from one format to another"""
        try:
            # Try MoviePy first
            if MOVIEPY_AVAILABLE:
                return self._convert_video_format_moviepy(input_file, output_file, target_format)

            # Fallback to system FFmpeg
            elif FFMPEG_SYSTEM_AVAILABLE:
                return self._convert_video_format_ffmpeg(input_file, output_file, target_format)

            else:
                raise Exception("No video conversion tools available. Please install MoviePy (pip install moviepy) or FFmpeg")

        except Exception as e:
            self.logger.error(f"Video format conversion failed: {str(e)}")
            return False

    def _convert_video_format_moviepy(self, input_file, output_file, target_format):
        """Convert video format using MoviePy"""
        self.logger.info(f"Converting video format using MoviePy: {input_file} -> {output_file}")

        # Load video file
        video = VideoFileClip(input_file)

        # Get video parameters based on target format
        video_params = self._get_video_params(target_format)

        # Write video file
        video.write_videofile(output_file, **video_params, verbose=False, logger=None)

        # Clean up
        video.close()

        self.logger.info(f"Successfully converted to {target_format.upper()}")
        return True

    def _convert_video_format_ffmpeg(self, input_file, output_file, target_format):
        """Convert video format using system FFmpeg"""
        self.logger.info(f"Converting video format using FFmpeg: {input_file} -> {output_file}")

        # Check if input file exists
        if not os.path.exists(input_file):
            raise Exception(f"Input file does not exist: {input_file}")

        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        # Build FFmpeg command
        cmd = ['ffmpeg', '-i', input_file]

        # Add codec settings based on target format
        if target_format.lower() == 'mp4':
            cmd.extend(['-c:v', 'libx264', '-c:a', 'aac', '-preset', 'medium'])
        elif target_format.lower() == 'avi':
            cmd.extend(['-c:v', 'libx264', '-c:a', 'mp3'])
        elif target_format.lower() == 'mov':
            cmd.extend(['-c:v', 'libx264', '-c:a', 'aac'])
        elif target_format.lower() == 'wmv':
            cmd.extend(['-c:v', 'wmv2', '-c:a', 'wmav2'])
        elif target_format.lower() == 'flv':
            cmd.extend(['-c:v', 'flv1', '-c:a', 'mp3'])
        elif target_format.lower() == 'mkv':
            cmd.extend(['-c:v', 'libx264', '-c:a', 'aac'])
        elif target_format.lower() == 'webm':
            cmd.extend(['-c:v', 'libvpx', '-c:a', 'libvorbis'])
        elif target_format.lower() == 'm4v':
            cmd.extend(['-c:v', 'libx264', '-c:a', 'aac'])
        elif target_format.lower() == '3gp':
            cmd.extend(['-c:v', 'h263', '-c:a', 'aac', '-s', '176x144'])
        else:
            # Default to MP4 settings
            cmd.extend(['-c:v', 'libx264', '-c:a', 'aac'])

        cmd.extend(['-y', output_file])  # -y to overwrite output file

        # Run FFmpeg command
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            if result.returncode != 0:
                raise Exception(f"FFmpeg failed: {result.stderr}")

            self.logger.info(f"Successfully converted video to {target_format.upper()}")
            return True

        except subprocess.TimeoutExpired:
            raise Exception("Conversion timed out after 10 minutes")
        except Exception as e:
            raise Exception(f"FFmpeg conversion failed: {str(e)}")

    def convert_video_to_gif(self, input_file, output_file, max_width=480, fps=10, duration=None):
        """Convert video to GIF with optimization"""
        try:
            # Try MoviePy first
            if MOVIEPY_AVAILABLE:
                return self._convert_video_to_gif_moviepy(input_file, output_file, max_width, fps, duration)

            # Fallback to system FFmpeg
            elif FFMPEG_SYSTEM_AVAILABLE:
                return self._convert_video_to_gif_ffmpeg(input_file, output_file, max_width, fps, duration)

            else:
                raise Exception("No video conversion tools available. Please install MoviePy (pip install moviepy) or FFmpeg")

        except Exception as e:
            self.logger.error(f"Video to GIF conversion failed: {str(e)}")
            return False

    def _convert_video_to_gif_moviepy(self, input_file, output_file, max_width=480, fps=10, duration=None):
        """Convert video to GIF using MoviePy"""
        self.logger.info(f"Converting video to GIF using MoviePy: {input_file} -> {output_file}")

        # Load video file
        video = VideoFileClip(input_file)

        # Limit duration if specified
        if duration and video.duration > duration:
            video = video.subclip(0, duration)

        # Resize video to optimize GIF size
        if video.w > max_width:
            video = video.resize(width=max_width)

        # Write GIF with optimization
        video.write_gif(
            output_file,
            fps=fps,
            opt='OptimizePlus',
            verbose=False,
            logger=None
        )

        # Clean up
        video.close()

        self.logger.info("Successfully converted video to GIF")
        return True

    def _convert_video_to_gif_ffmpeg(self, input_file, output_file, max_width=480, fps=10, duration=None):
        """Convert video to GIF using system FFmpeg"""
        self.logger.info(f"Converting video to GIF using FFmpeg: {input_file} -> {output_file}")

        # Check if input file exists
        if not os.path.exists(input_file):
            raise Exception(f"Input file does not exist: {input_file}")

        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        # Build FFmpeg command for GIF conversion
        cmd = ['ffmpeg', '-i', input_file]

        # Add duration limit if specified
        if duration:
            cmd.extend(['-t', str(duration)])

        # Add video filters for optimization
        filters = []

        # Scale filter to limit width
        filters.append(f'scale={max_width}:-1:flags=lanczos')

        # FPS filter
        filters.append(f'fps={fps}')

        # Palette generation for better quality GIF
        filters.append('split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse')

        cmd.extend(['-vf', ','.join(filters)])
        cmd.extend(['-y', output_file])  # -y to overwrite output file

        # Run FFmpeg command
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            if result.returncode != 0:
                raise Exception(f"FFmpeg failed: {result.stderr}")

            self.logger.info("Successfully converted video to GIF")
            return True

        except subprocess.TimeoutExpired:
            raise Exception("GIF conversion timed out after 5 minutes")
        except Exception as e:
            raise Exception(f"FFmpeg GIF conversion failed: {str(e)}")

    def convert_audio_format(self, input_file, output_file, target_format):
        """Convert audio from one format to another"""
        try:
            # Try MoviePy first
            if MOVIEPY_AVAILABLE:
                return self._convert_audio_format_moviepy(input_file, output_file, target_format)

            # Fallback to system FFmpeg
            elif FFMPEG_SYSTEM_AVAILABLE:
                return self._convert_audio_format_ffmpeg(input_file, output_file, target_format)

            else:
                raise Exception("No audio conversion tools available. Please install MoviePy (pip install moviepy) or FFmpeg")

        except Exception as e:
            self.logger.error(f"Audio format conversion failed: {str(e)}")
            return False

    def _convert_audio_format_moviepy(self, input_file, output_file, target_format):
        """Convert audio format using MoviePy"""
        self.logger.info(f"Converting audio format using MoviePy: {input_file} -> {output_file}")

        # Load audio file
        audio = AudioFileClip(input_file)

        # Get audio parameters based on target format
        audio_params = self._get_audio_params(target_format)

        # Write audio file
        audio.write_audiofile(output_file, **audio_params, verbose=False, logger=None)

        # Clean up
        audio.close()

        self.logger.info(f"Successfully converted to {target_format.upper()}")
        return True

    def _convert_audio_format_ffmpeg(self, input_file, output_file, target_format):
        """Convert audio format using system FFmpeg"""
        self.logger.info(f"Converting audio format using FFmpeg: {input_file} -> {output_file}")

        # Check if input file exists
        if not os.path.exists(input_file):
            raise Exception(f"Input file does not exist: {input_file}")

        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        # Build FFmpeg command
        cmd = ['ffmpeg', '-i', input_file]

        # Add audio codec based on format
        if target_format.lower() == 'mp3':
            cmd.extend(['-acodec', 'mp3', '-ab', '192k'])
        elif target_format.lower() == 'wav':
            cmd.extend(['-acodec', 'pcm_s16le'])
        elif target_format.lower() == 'aac':
            cmd.extend(['-acodec', 'aac', '-ab', '128k'])
        elif target_format.lower() == 'flac':
            cmd.extend(['-acodec', 'flac'])
        elif target_format.lower() == 'ogg':
            cmd.extend(['-acodec', 'libvorbis', '-ab', '192k'])
        elif target_format.lower() == 'm4a':
            cmd.extend(['-acodec', 'aac', '-ab', '128k'])
        elif target_format.lower() == 'wma':
            cmd.extend(['-acodec', 'wmav2', '-ab', '128k'])
        else:
            cmd.extend(['-acodec', 'mp3', '-ab', '192k'])  # Default to MP3

        cmd.extend(['-y', output_file])  # -y to overwrite output file

        # Run FFmpeg command
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            if result.returncode != 0:
                raise Exception(f"FFmpeg failed: {result.stderr}")

            self.logger.info(f"Successfully converted audio to {target_format.upper()}")
            return True

        except subprocess.TimeoutExpired:
            raise Exception("Audio conversion timed out after 5 minutes")
        except Exception as e:
            raise Exception(f"FFmpeg audio conversion failed: {str(e)}")

    def _get_audio_params(self, audio_format):
        """Get audio encoding parameters for different formats"""
        params = {
            'mp3': {'codec': 'mp3', 'bitrate': '192k'},
            'wav': {'codec': 'pcm_s16le'},
            'aac': {'codec': 'aac', 'bitrate': '128k'},
            'flac': {'codec': 'flac'},
            'ogg': {'codec': 'libvorbis', 'bitrate': '192k'},
            'm4a': {'codec': 'aac', 'bitrate': '128k'},
            'wma': {'codec': 'wmav2', 'bitrate': '128k'}
        }
        return params.get(audio_format.lower(), {'codec': 'mp3', 'bitrate': '192k'})

    def _get_video_params(self, video_format):
        """Get video encoding parameters for different formats"""
        params = {
            'mp4': {'codec': 'libx264', 'audio_codec': 'aac'},
            'avi': {'codec': 'libxvid', 'audio_codec': 'mp3'},
            'mov': {'codec': 'libx264', 'audio_codec': 'aac'},
            'wmv': {'codec': 'wmv2', 'audio_codec': 'wmav2'},
            'flv': {'codec': 'flv', 'audio_codec': 'mp3'},
            'mkv': {'codec': 'libx264', 'audio_codec': 'aac'},
            'webm': {'codec': 'libvpx', 'audio_codec': 'libvorbis'},
            'm4v': {'codec': 'libx264', 'audio_codec': 'aac'},
            '3gp': {'codec': 'h263', 'audio_codec': 'aac'}
        }
        return params.get(video_format.lower(), {'codec': 'libx264', 'audio_codec': 'aac'})

    def get_video_info(self, input_file):
        """Get information about a video file"""
        try:
            if not MOVIEPY_AVAILABLE:
                return None

            video = VideoFileClip(input_file)
            info = {
                'duration': video.duration,
                'fps': video.fps,
                'size': (video.w, video.h),
                'has_audio': video.audio is not None
            }
            video.close()
            return info

        except Exception as e:
            self.logger.error(f"Failed to get video info: {str(e)}")
            return None

    def is_video_file(self, file_path):
        """Check if file is a video file"""
        video_extensions = ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.m4v', '.3gp']
        return Path(file_path).suffix.lower() in video_extensions

    def is_audio_file(self, file_path):
        """Check if file is an audio file"""
        audio_extensions = ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a', '.wma']
        return Path(file_path).suffix.lower() in audio_extensions

    def check_dependencies(self):
        """Check if required dependencies are available"""
        status = {
            'moviepy': MOVIEPY_AVAILABLE,
            'ffmpeg': FFMPEG_AVAILABLE
        }

        if not MOVIEPY_AVAILABLE:
            self.logger.warning("MoviePy not available. Install with: pip install moviepy")
        if not FFMPEG_AVAILABLE:
            self.logger.warning("FFmpeg-python not available. Install with: pip install ffmpeg-python")

        return status
