"""Generate a Seedance 2.5 text-to-video clip with the Higgsfield Python SDK.

Credentials: HF_KEY="key-id:key-secret" in .env.local (git-ignored). The value
is read from the environment by the SDK and is never printed here.
"""
import pathlib
import sys

import httpx
from dotenv import load_dotenv

load_dotenv(pathlib.Path(__file__).with_name('.env.local'))

import higgsfield_client  # noqa: E402  (import after env is loaded)

MODEL = 'bytedance/seedance-2.5/text-to-video'
ARGUMENTS = {
    'prompt': 'A cinematic scene at sunset',
    'duration': 5,
    'resolution': '720p',
    'aspect_ratio': '16:9',
}


def on_queue_update(status: higgsfield_client.Status) -> None:
    print(f'status: {type(status).__name__}', file=sys.stderr)


def video_url(result: dict) -> str | None:
    video = result.get('video')
    if isinstance(video, dict) and video.get('url'):
        return video['url']
    videos = result.get('videos')
    if isinstance(videos, list) and videos and isinstance(videos[0], dict):
        return videos[0].get('url')
    return None


def main() -> int:
    try:
        # subscribe() returns the final status payload; it does not raise when the
        # request ends as failed, nsfw or canceled, so check the status explicitly.
        result = higgsfield_client.subscribe(
            MODEL,
            arguments=ARGUMENTS,
            on_enqueue=lambda request_id: print(f'request_id: {request_id}', file=sys.stderr),
            on_queue_update=on_queue_update,
        )
    except higgsfield_client.CredentialsMissedError:
        print('error: HF_KEY is not set. Add HF_KEY=key-id:key-secret to .env.local.', file=sys.stderr)
        return 2
    except higgsfield_client.HiggsfieldClientError as exc:
        print(f'error: Higgsfield API rejected the request: {exc}', file=sys.stderr)
        return 1
    except httpx.TransportError as exc:
        print(f'error: could not reach the Higgsfield API: {exc}', file=sys.stderr)
        return 1

    status = result.get('status')
    if status == 'nsfw':
        print('error: request was blocked by content moderation (nsfw).', file=sys.stderr)
        return 1
    if status in ('failed', 'canceled'):
        detail = result.get('error') or result.get('detail') or ''
        print(f'error: request {status}. {detail}'.rstrip(), file=sys.stderr)
        return 1
    if status != 'completed':
        print(f'error: unexpected final status: {status!r}', file=sys.stderr)
        return 1

    url = video_url(result)
    if not url:
        print('error: request completed but no video URL was found in the response.', file=sys.stderr)
        return 1

    print(url)
    return 0


if __name__ == '__main__':
    sys.exit(main())
