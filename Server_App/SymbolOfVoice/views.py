from django.shortcuts import render
import os

def record_video(request):
    # print(os.path.exists('./SymbolOfVoice/templates/SymbolOfVoice/video_record.html'))
    return render(request, 'index.html')