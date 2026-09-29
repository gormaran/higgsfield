#!/usr/bin/env bash
# Joins clips/01.mp4..30.mp4 into one 1080p video, laying vo/01.mp3..30.mp3 on their own shot
# (each padded/trimmed to 10 s so voice and picture never drift), plus an optional music bed.
# Usage: ./assemble.sh [output.mp4]
set -euo pipefail
cd "$(dirname "$0")"

OUT="${1:-ia-marketing-5min.mp4}"
MUSIC="music.mp3"   # optional

command -v ffmpeg >/dev/null || { echo "ffmpeg is required"; exit 1; }

# Normalize every clip to 1920x1080, 24 fps, no audio, so concat never breaks on mismatched streams.
mkdir -p .norm
: > .norm/list.txt
: > .norm/alist.txt
for i in $(seq -w 1 30); do
  src="clips/$i.mp4"
  [ -f "$src" ] || { echo "Missing $src"; exit 1; }
  ffmpeg -loglevel error -y -i "$src" \
    -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=24,format=yuv420p" \
    -t 10 -an -c:v libx264 -preset medium -crf 18 ".norm/$i.mp4"
  vo="vo/$i.mp3"
  [ -f "$vo" ] || { echo "Missing $vo"; exit 1; }
  ffmpeg -loglevel error -y -i "$vo" -af "apad=whole_dur=10,atrim=0:10" -ar 48000 -ac 2 ".norm/$i.wav"
  echo "file '$i.mp4'" >> .norm/list.txt
  echo "file '$i.wav'" >> .norm/alist.txt
done

ffmpeg -loglevel error -y -f concat -safe 0 -i .norm/list.txt -c copy .norm/video.mp4
ffmpeg -loglevel error -y -f concat -safe 0 -i .norm/alist.txt -c copy .norm/vo.wav
VO=.norm/vo.wav

if [ -f "$MUSIC" ]; then
  # Music ducked under the voice at -18 dB, faded out over the last 3 s.
  ffmpeg -loglevel error -y -i .norm/video.mp4 -i "$VO" -stream_loop -1 -i "$MUSIC" \
    -filter_complex "[2:a]volume=-18dB,afade=t=out:st=297:d=3[m];[1:a][m]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[a]" \
    -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest "$OUT"
else
  ffmpeg -loglevel error -y -i .norm/video.mp4 -i "$VO" \
    -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest "$OUT"
fi

rm -rf .norm
echo "Done: $OUT"
