import ollama
import os
with os.scandir('./in/unpol_text/') as texts:
    for txt in texts:
        f = open(f'./in/unpol_text/{txt.name}', encoding="utf-8")
        text = f.read()
        f.close()
        response = ollama.chat(model='llama3', messages=[
          {
            'role': 'user',
            'content': 'Rewrite this text with correct punctuation without modifying its form too much in a format easily readable from a Text-to-speech device: '+text,
          },
        ])
        f = open(f'./in/text/{txt.name}', 'x', encoding="utf-8")
        os.remove(txt)
        f.write('\n'.join(response['message']['content'].split('\n')[1:]))
        f.close()

