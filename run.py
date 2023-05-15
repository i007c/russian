import json
import time
from pathlib import Path

import gtts

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'mp3'
DATA_DIR.mkdir(exist_ok=True, parents=True)


def main():
    with open(BASE_DIR / 'words.json', 'r') as f:
        data = json.load(f)

    for row in data:
        rank = row['rank']
        ru = row['russian']
        en = row['english']
        work_type = row['type']

        save_dir = DATA_DIR / work_type
        save_dir.mkdir(exist_ok=True, parents=True)

        ru_save_file = save_dir / f'{rank}.ru.mp3'
        en_save_file = save_dir / f'{rank}.en.mp3'

        gtts.gTTS(ru, lang='ru').save(ru_save_file)
        gtts.gTTS(en, lang='en').save(en_save_file)
        time.sleep(0.1)
        break


if __name__ == '__main__':
    main()
