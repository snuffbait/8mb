import os
import sys
import subprocess

def compress(filez):
    cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', filez]
    duration = float(subprocess.check_output(cmd).decode().strip())

    bits = 7.5 * 8 * 1024 * 1024
    audio = 128 * 1024
    bitrate = max(int(((bits / duration) - audio) / 1024), 100)

    output = filez.replace('.mp4', '_snuff_compressed.mp4')

    subprocess.run([
        'ffmpeg', '-i', filez,
        '-c:v', 'libx264',
        '-b:v', f'{bitrate}k',
        '-preset', 'medium',
        '-c:a', 'aac',
        '-b:a', '128k',
        '-y', output
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

compress(sys.argv[1])
