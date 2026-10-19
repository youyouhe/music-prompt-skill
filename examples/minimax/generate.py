#!/usr/bin/env python3
"""Call MiniMax music_generation for the 6 example clips.

Usage: MINIMAX_TOKEN=... python3 generate.py [--only 01-suspense]

Reads prompts.json (same dir), writes mp3 files next to it and raw API
responses to <repo>/../../music-minimax-raw/ (outside the repo, not committed).
The token is read from the environment only — never printed or written anywhere.
"""
import json
import os
import subprocess
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.abspath(os.path.join(HERE, "..", "..", "..", "music-minimax-raw"))
API_URL = "https://api.minimax.cn/v1/music_generation"
MAX_SECONDS = 15


def fail(msg):
    print(f"FATAL: {msg}", file=sys.stderr)
    sys.exit(1)


def main():
    token = os.environ.get("MINIMAX_TOKEN")
    if not token:
        fail("MINIMAX_TOKEN not set in environment")

    only = None
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1]

    with open(os.path.join(HERE, "prompts.json"), encoding="utf-8") as f:
        spec = json.load(f)

    os.makedirs(RAW_DIR, exist_ok=True)

    for clip in spec["clips"]:
        name = clip["file"]
        if only and name != only:
            continue
        out_path = os.path.join(HERE, name)
        if os.path.exists(out_path):
            print(f"[skip] {name} already exists")
            continue

        prompt = clip[clip["use_final"]]
        payload = {
            "model": spec["model"],
            "prompt": prompt,
            "is_instrumental": spec["is_instrumental"],
            "audio_setting": spec["audio_setting"],
            "output_format": spec["output_format"],
        }
        req = urllib.request.Request(
            API_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            },
            method="POST",
        )
        print(f"[call] {name} ...", flush=True)
        try:
            with urllib.request.urlopen(req, timeout=600) as resp:
                body = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", "replace")
            # save error body for the record, then stop hard (brief: any
            # error → record as-is; new-account restriction → stop, no retry)
            with open(os.path.join(RAW_DIR, name + ".error.json"), "w") as f:
                f.write(f"HTTP {e.code}\n{err_body}")
            fail(f"{name}: HTTP {e.code}: {err_body[:500]}")
        except Exception as e:
            fail(f"{name}: {type(e).__name__}: {e}")

        with open(os.path.join(RAW_DIR, name + ".response.json"), "w") as f:
            json.dump(body, f, ensure_ascii=False, indent=2)

        # permission / service-adjustment refusal → stop, no retry, no workaround
        body_str = json.dumps(body, ensure_ascii=False)
        for marker in ("服务调整", "权限", "无权", "forbidden", "not authorized"):
            if marker in body_str and not body.get("data"):
                fail(f"{name}: possible restriction/error in response, stopping: {body_str[:400]}")

        audio_url = (body.get("data") or {}).get("audio") or body.get("audio")
        if not audio_url:
            fail(f"{name}: no audio url in response: {body_str[:400]}")

        extra = body.get("extra_info") or {}
        print(f"[resp] {name}: extra_info keys={sorted(extra.keys()) or 'none'}", flush=True)

        with urllib.request.urlopen(audio_url, timeout=300) as r, open(out_path + ".tmp", "wb") as f:
            f.write(r.read())
        os.rename(out_path + ".tmp", out_path)

        # trim to <= 15 s with stream copy if needed
        dur = float(subprocess.run(
            ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
             "-of", "csv=p=0", out_path],
            capture_output=True, text=True, check=True).stdout.strip())
        if dur > MAX_SECONDS + 0.5:
            subprocess.run(
                ["ffmpeg", "-y", "-v", "error", "-i", out_path,
                 "-t", str(MAX_SECONDS), "-c", "copy", out_path + ".cut"],
                check=True)
            os.replace(out_path + ".cut", out_path)
            dur = float(subprocess.run(
                ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                 "-of", "csv=p=0", out_path],
                capture_output=True, text=True, check=True).stdout.strip())
        print(f"[done] {name}: {dur:.2f}s", flush=True)
        time.sleep(3)


if __name__ == "__main__":
    main()
