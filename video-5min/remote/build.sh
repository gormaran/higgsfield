#!/usr/bin/env bash
# Low-budget build of ia-marketing-5min.mp4, meant to run where the Higgsfield CDN is reachable
# (the Higgsfield sandbox). Inputs in the working dir:
#   manifest.tsv  kind<TAB>NN<TAB>url-suffix   (kind: img | vo | ai; suffix is appended to $CDN)
#   captions.tsv  NN<TAB>text                  (optional on-screen label, "\n" = line break)
# Each shot is 10 s: an AI clip if one exists, else a Ken Burns move over the still (0 credits).
set -euo pipefail
CDN="${CDN:-https://d8j0ntlcm91z4.cloudfront.net/user_2zrO9QNNpCetn18kvcsQfnqS5RV/hf_}"
OUT="${1:-ia-marketing-5min.mp4}"
FONT="$(fc-match -f '%{file}' 'Montserrat:black' 2>/dev/null || fc-match -f '%{file}' 'sans:bold')"
mkdir -p src clips norm
while IFS=$'\t' read -r kind n suf; do
  case $kind in img) ext=png;; vo) ext=mp3;; ai) ext=mp4;; esac
  [ -s "src/$kind$n.$ext" ] || curl -sSf --retry 3 -o "src/$kind$n.$ext" "$CDN$suf"
done < manifest.tsv

caption_filter() {  # $1 = shot number -> ",drawtext=..." or ""
  local line; line="$(awk -F'\t' -v n="$1" '$1==n{print $2}' captions.tsv 2>/dev/null || true)"
  [ -n "$line" ] || return 0
  printf '%b' "$line" > "norm/cap$1.txt"
  echo ",drawtext=fontfile='$FONT':textfile=norm/cap$1.txt:fontsize=64:fontcolor=#FFE14D:borderw=6:bordercolor=black:line_spacing=12:x=(w-text_w)/2:y=h-text_h-90:alpha='if(lt(t,0.4),t/0.4,1)'"
}

for i in $(seq -w 1 30); do
  cap="$(caption_filter "$i")"
  if [ -f "src/ai$i.mp4" ]; then
    ffmpeg -loglevel error -y -i "src/ai$i.mp4" -vf "scale=1920:1080:force_original_aspect_ratio=increase:flags=lanczos,crop=1920:1080,fps=24,tpad=stop_mode=clone:stop_duration=10,format=yuv420p$cap" \
      -t 10 -an -c:v libx264 -preset veryfast -crf 19 "clips/$i.mp4"
  else
    # alternate zoom in / zoom out / pan right / pan left so consecutive stills never move the same way
    case $(( 10#$i % 4 )) in
      0) z="1+0.0006*on"; x="iw/2-(iw/zoom/2)"; y="ih/2-(ih/zoom/2)";;
      1) z="1.15-0.0006*on"; x="iw/2-(iw/zoom/2)"; y="ih/2-(ih/zoom/2)";;
      2) z="1.12"; x="(iw-iw/zoom)*on/239"; y="ih/2-(ih/zoom/2)";;
      3) z="1.12"; x="(iw-iw/zoom)*(1-on/239)"; y="ih/2-(ih/zoom/2)";;
    esac
    ffmpeg -loglevel error -y -loop 1 -i "src/img$i.png" -vf "scale=3840:2160:force_original_aspect_ratio=increase:flags=lanczos,crop=3840:2160,zoompan=z='$z':x='$x':y='$y':d=240:s=1920x1080:fps=24,format=yuv420p$cap" \
      -frames:v 240 -an -c:v libx264 -preset veryfast -crf 19 "clips/$i.mp4"
  fi
  ffmpeg -loglevel error -y -i "src/vo$i.mp3" -af "adelay=300|300,apad=whole_dur=10,atrim=0:10" -ar 48000 -ac 2 "norm/$i.wav"
  echo "file '../clips/$i.mp4'" >> norm/list.txt
  echo "file '$i.wav'" >> norm/alist.txt
  echo "shot $i done"
done
ffmpeg -loglevel error -y -f concat -safe 0 -i norm/list.txt -c copy norm/video.mp4
ffmpeg -loglevel error -y -f concat -safe 0 -i norm/alist.txt -c copy norm/vo.wav
ffmpeg -loglevel error -y -i norm/video.mp4 -i norm/vo.wav -map 0:v -map 1:a -af loudnorm=I=-16:TP=-1.5 -ar 48000 -c:v copy -c:a aac -b:a 192k -movflags +faststart -shortest "$OUT"
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate -of compact "$OUT"
echo BUILD_OK
