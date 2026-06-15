#!/usr/bin/env python3
"""Generate the metronome click WAV files used by the compatibility audio backend.

Run from the repo root:  python tools/gen_sounds.py
Writes mono 16-bit 22.05kHz clicks into ./sounds/.
"""
import math, os, struct, wave

SR = 22050
OUT = os.path.join(os.path.dirname(__file__), "..", "sounds")

# (name, frequency Hz, duration s, peak 0..1, waveform)
CLICKS = [
    ("sam",   1400, 0.075, 1.00, "tri"),
    ("tali",  1050, 0.055, 0.85, "tri"),
    ("khali",  620, 0.065, 0.65, "sine"),
    ("beat",   820, 0.055, 0.60, "tri"),
    ("sub",    492, 0.035, 0.40, "tri"),
]

def sample(freq, t, kind):
    a = 2 * math.pi * freq * t
    if kind == "sine":
        return math.sin(a)
    # band-limited-ish triangle via asin(sin())
    return math.asin(math.sin(a)) * (2 / math.pi)

def write_click(name, freq, dur, peak, kind):
    n = max(1, int(SR * dur))
    frames = bytearray()
    for i in range(n):
        t = i / SR
        env = math.exp(-t * 28)
        v = max(-1.0, min(1.0, sample(freq, t, kind) * env * peak))
        frames += struct.pack("<h", int(v * 32767))
    path = os.path.join(OUT, name + ".wav")
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(bytes(frames))
    print("wrote", path, "(%d frames)" % n)

def main():
    os.makedirs(OUT, exist_ok=True)
    for c in CLICKS:
        write_click(*c)

if __name__ == "__main__":
    main()
