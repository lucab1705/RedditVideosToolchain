import os
import random
from tiktokvoice import tts

voices = ['en_au_001',                  # English AU - Female
    'en_au_002',                  # English AU - Male
    'en_uk_001',                  # English UK - Male 1
    'en_uk_003',                  # English UK - Male 2
    'en_us_001',                  # English US - Female (Int. 1)
    'en_us_002',                  # English US - Female (Int. 2)
    'en_us_006',                  # English US - Male 1
    'en_us_007',                  # English US - Male 2
    'en_us_009',                  # English US - Male 3
    'en_us_010',                  # English US - Male 4
    'en_male_narration',           # narrator
    'en_male_funny',               # wacky
    'en_female_emotional',         # peaceful
]
voice = random.choice(voices)

with os.scandir('./in/text/') as dir:
    for file in dir:
        text = open(file, 'r').read()
        tts(text=text, voice=voice, output_filename='./out/audio/'+file.name.split('.')[0]+'.mp3')
        os.remove(file)

print("Finished audio generation.")