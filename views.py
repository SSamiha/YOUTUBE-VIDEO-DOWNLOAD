import yt_dlp
from django.shortcuts import render
def youtube(request):
    if request.method == 'POST':
        link = request.POST.get('link')

        try:
            ydl_opts = {
                'format': 'best',  # Download best available single stream (no merging)
                'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save to a folder
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=True)

            message = f"Video '{info_dict['title']}' downloaded successfully!"
        
        except Exception as e:
            message = f"An error occurred: {str(e)}"

        return render(request, 'downloader/youtube.html', {'message': message})

    return render(request, 'downloader/youtube.html')