# Reddit automatized video creation toolchain

## Requirements:
 - Python 3.9+
 - [ollama and llama3 model](https://ollama.com/)
 - run `pip install -r requirements.txt` to install all the necessary python libraries

## Usage
- Set your reddit client datas in `fetchText.py` (make a `secret.py` or whatever you want I'm not your dad)
- Run ollama `ollama run llama3`
- Add reddit links to the queue via addPost [url] {priority}
- Fetch text from links in the queue using fetchText
- Polish the text via llama3 (additional manual work might be required -- llama remarks be damned)
- Generate audio files via TikTok TTS APIs with generateVoice
- Generate the videos through generateVideo
- Enjoy! (looking to integrate with TikTok/Youtube/IG for autopublish)