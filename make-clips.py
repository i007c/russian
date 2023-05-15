

import glob
import json
import os
from pathlib import Path
from string import ascii_letters

BASE_DIR = Path(__file__).parent

MP4_DIR = BASE_DIR / 'mp4'
MP4_DIR.mkdir(exist_ok=True, parents=True)

MP3_DIR = BASE_DIR / 'mp3'

S = 25


def main():
    # print(glob.glob('./mp3/*')[:10])
    with open(BASE_DIR / 'words.json', 'r') as f:
        words = json.load(f)

    n = 0
    for w in words:
        rank, ru, en, wt = w['rank'], w['russian'], w['english'], w['type']

        ru_fn = MP3_DIR / f'{rank}.ru.mp3'
        en_fn = MP3_DIR / f'{rank}.en.mp3'

        n += 1
        # ru_clip = MP4_DIR / f'{n}.mp4'
        # n += 1
        # en_clip = MP4_DIR / f'{n}.mp4'

        if len(en) > S:
            for i in range(1, (len(en) // S)+1):
                en = en[:i*S] + '\n' + en[i*S:]

        if len(ru) > S:
            for i in range(1, (len(ru) // S)+1):
                ru = ru[:i*S] + '\n' + ru[i*S:]

        if not ru_fn.is_file() or not en_fn.is_file():
            continue

        os.system(f'bash get.sh {ru_fn} "[{rank}]" "{ru}" "{wt}" ru.mp4')
        os.system(f'bash get.sh {en_fn} "[{rank}]" "{en}" "{wt}" en.mp4')
        os.system(f'bash con.sh mp4/{n}.mp4')


if __name__ == '__main__':
    main()
