import json
import os
import time
from pathlib import Path

import gtts

BASE_DIR = Path(__file__).parent
MP3_DIR = BASE_DIR / 'mp3'
MP3_DIR.mkdir(exist_ok=True, parents=True)

MP4_DIR = BASE_DIR / 'mp4'
MP4_DIR.mkdir(exist_ok=True, parents=True)


S = 25


def main():
    with open(BASE_DIR / 'words.json', 'r') as f:
        data = json.load(f)

    n = 0
    for row in data:
        rank = row['rank']
        ru = row['russian']
        en = row['english']
        wt = row['type']
        ref = row.get('ref')
        print(f'[{rank}][{ref}] {ru} :: {en} | {wt}')

        try:
            ru_mp3 = MP3_DIR / f'{rank}.ru.mp3'
            en_mp3 = MP3_DIR / f'{rank}.en.mp3'

            gtts.gTTS(ru, lang='ru').save(ru_mp3)
            time.sleep(2)
            gtts.gTTS(en, lang='en').save(en_mp3)

            n += 1

            if len(en) > S:
                for i in range(1, (len(en) // S)+1):
                    en = en[:i*S] + '\n' + en[i*S:]

            if len(ru) > S:
                for i in range(1, (len(ru) // S)+1):
                    ru = ru[:i*S] + '\n' + ru[i*S:]

            if not ru_mp3.is_file() or not en_mp3.is_file():
                continue

            r = f'[{rank}]'
            if ref:
                r += f'[{ref}]'

            os.system(f'bash get.sh {ru_mp3} "{r}" "{ru}" "{wt}" ru.mp4')
            os.system(f'bash get.sh {en_mp3} "{r}" "{en}" "{wt}" en.mp4')
            os.system(f'bash con.sh mp4/{n}.mp4')

            time.sleep(2)
        except Exception as e:
            print(e)

        print('done', n)


if __name__ == '__main__':
    main()
