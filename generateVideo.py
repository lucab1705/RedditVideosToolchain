from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import whisper
from whisper.utils import get_writer 
import ffmpeg
import os
import random

#TODO: Fix SRT file extension save

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
def extract_audio(a):
    extracted_audio = f"audio-tmp.wav"
    stream = ffmpeg.input('./out/audio/'+audio.name)
    stream = ffmpeg.output(stream, extracted_audio)
    ffmpeg.run(stream, overwrite_output=True)
    return extracted_audio

with os.scandir('./out/audio/') as dir:
    for audio in dir:
        audioclip = AudioFileClip('./out/audio/'+audio.name)
        ad = extract_audio(audioclip)
        model = whisper.load_model('small')
        result = model.transcribe(audio=ad, language='en', word_timestamps=True, task="transcribe")
        word_options = {
            "max_line_count": 1,
            "max_line_width": 18
        }
        srt_writer = get_writer(output_format='srt', output_dir='./out/subs/')
        srt_writer(result, audio, word_options)
        vd =  os.listdir('./in/videos/')
        video = random.choice(vd)
        videoclip = VideoFileClip('./in/videos/'+video)
        while audioclip.duration > videoclip.duration:
            video = random.choice(vd)
            videoclip = VideoFileClip('./in/videos/'+video)
        start = random.randrange(int(videoclip.duration) - int(audioclip.duration))
        bg =  os.listdir('./in/bgMusic/')
        bgmusic = random.choice(bg)
        bgaudio = AudioFileClip('./in/bgMusic/'+bgmusic)
        bgaudio = bgaudio.fx(afx.volumex, 0.1)
        bgaudio = afx.audio_loop(bgaudio, duration = audioclip.duration)
        new_audioclip = CompositeAudioClip([audioclip, bgaudio]).set_duration(audioclip.duration - .1)
        videoclip = videoclip.subclip(start, start + audioclip.duration)
        videoclip = videoclip.set_audio(new_audioclip)
        (w, h) = videoclip.size
        if w > h:
            crop_width = h * 9/16
            x1, x2 = (w - crop_width)//2, (w+crop_width)//2
            y1, y2 = 0, h
            videoclip = videoclip.crop(x1=x1, y1=y1, x2=x2, y2=y2)
        generator = lambda txt: TextClip(txt.upper(), font='Montserrat-ExtraBold', fontsize=42, color='white', stroke_color='black', stroke_width=2, method='caption', align='center', size=videoclip.size)
        subtitles = SubtitlesClip('./out/subs/'+audio.name.split('.')[0]+'.txt.srt', generator)
        videoclip = CompositeVideoClip((videoclip, subtitles), size=videoclip.size)
        videoclip.write_videofile('./out/toPublish/'+audio.name.split('.')[0]+'.mp4', remove_temp=True, codec="libx264")
