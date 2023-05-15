
ffmpeg -f concat -i ru_en -c copy $1 -y
echo file $1 >> all_list.txt

