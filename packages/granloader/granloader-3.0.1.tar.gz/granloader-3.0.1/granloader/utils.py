import os
import re
import subprocess

def install_dependencies():
    return True  # Simplificado já que os pacotes serão instalados via setup.py

def get_video_id(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|live/|.*&v=)?([^&=%\?]{11})')
    youtube_regex_match = re.match(youtube_regex, url)
    if youtube_regex_match:
        return youtube_regex_match.group(6)
    return None

def get_video_title(link):
    try:
        cmd = ['yt-dlp', '--get-title', link]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise Exception(f"Erro ao obter o título do vídeo: {e.stderr}")

def get_video_info(link):
    try:
        cmd = ['yt-dlp', '-F', link]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
        lines = result.stdout.split('\n')
        max_resolution = 0
        for line in lines:
            if "mp4" in line and "video only" in line:
                match = re.search(r'(\d{3,4})p', line)
                if match:
                    resolution = int(match.group(1))
                    max_resolution = max(max_resolution, resolution)
        return max_resolution
    except subprocess.CalledProcessError as e:
        raise Exception(f"Erro ao obter informações do vídeo: {e.stderr}")

def sanitize_filename(title):
    valid_chars = "-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(c for c in title if c in valid_chars)

def start_download(link, folder_path, status_var, progress_var, title_var, resolution_var, eta_var):
    try:
        title = get_video_title(link)
        resolution = get_video_info(link)
        sanitized_title = sanitize_filename(title)
        
        title_var.set(title[:50] + '...' if len(title) > 50 else title)
        resolution_var.set(f"{resolution}p")
        
        output_video = os.path.join(folder_path, "video_temp.mp4")
        output_audio = os.path.join(folder_path, "audio_temp.m4a")
        final_output = os.path.join(folder_path, f"{sanitized_title}.mp4")

        # Download video
        status_var.set("Baixando vídeo")
        video_cmd = ['yt-dlp', '-f', 'bestvideo[ext=mp4]', '-o', output_video, link]
        download_process(video_cmd, status_var, progress_var, eta_var, folder_path)

        # Download audio
        status_var.set("Baixando áudio")
        audio_cmd = ['yt-dlp', '-f', 'bestaudio[ext=m4a]', '-o', output_audio, link]
        download_process(audio_cmd, status_var, progress_var, eta_var, folder_path)

        # Merge video and audio
        status_var.set("Mesclando arquivos")
        merge_cmd = ['ffmpeg', '-i', output_video, '-i', output_audio, '-c', 'copy', final_output]
        download_process(merge_cmd, status_var, progress_var, eta_var, folder_path)

        # Remove temporary files
        os.remove(output_video)
        os.remove(output_audio)

        status_var.set("Download concluído")
        progress_var.set(100)
        eta_var.set("")
    except subprocess.CalledProcessError as e:
        status_var.set(f"Erro durante o download: {str(e)}")
        progress_var.set(0)
    except Exception as e:
        status_var.set(f"Erro inesperado: {str(e)}")
        progress_var.set(0)

def download_process(command, status_var, progress_var, eta_var, folder_path):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    for line in iter(process.stdout.readline, ''):
        update_status(line, status_var, progress_var, eta_var, folder_path)
    process.stdout.close()
    process.wait()

def update_status(output, status_var, progress_var, eta_var, folder_path):
    simplified_folder_path = folder_path.replace(os.path.expanduser("~"), "").replace("\\", "/").lstrip("/")
    
    if "[download]" in output:
        if "Destination" in output:
            status_var.set("Destino: " + simplified_folder_path)
        elif "ETA" in output:
            match = re.search(r'(\d+(\.\d+)?)%', output)
            eta_match = re.search(r'ETA\s(\d+:\d+)', output)
            if match and eta_match:
                progress = float(match.group(1))
                eta = eta_match.group(1)
                progress_var.set(progress)
                eta_var.set(f"ETA: {eta}")
        else:
            status_var.set(output.strip())
    elif "Merging" in output:
        status_var.set("Mesclando arquivos")
