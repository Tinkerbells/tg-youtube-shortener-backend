import subprocess

def download_video(url, output_path, cookies_path):
    """Download audio using yt-dlp"""
    # Динамическое определение абсолютного пути к файлу cookies
    try:
        subprocess.run([
            'yt-dlp',
            '--cookies', cookies_path,  # Use cookies from the specified file
            '--output', output_path,
            '--format', 'ba[ext=m4a]',
            '--extract-audio',
            '--force-overwrites',
            url
        ], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == '__main__':
    download_video('https://www.youtube.com/watch?v=2TL3DgIMY1g', 'temp.m4a', 'cookies.txt')
