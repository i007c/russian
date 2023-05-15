
pad=20

ffmpeg -f lavfi -i \
    color=size=1920x1080:rate=25:color=#040404 \
    -i $1 \
    -vf "
    drawtext=
    fontsize=50:fontcolor=#f2f2f2:x=$pad:y=$pad:
    text='$2',

    drawtext=
    fontsize=120:fontcolor=#f2f2f2:x=(w-text_w)/2:y=(h-text_h-text_h)/2:
    text='$3',

    drawtext=
    fontsize=50:fontcolor=#f2f2f2:x=w-tw-$pad:y=h-th-$pad:
    text='$4'" \
    -c:a copy -shortest $5 -y

