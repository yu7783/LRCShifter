# LRCShifter

Fix out-of-sync LRC lyrics instantly with a simple GUI tool — no command line required.

## Demo
Before:
[00:10.00]Hello
[00:12.00]World

After (+0.50s):
[00:10.50]Hello
[00:12.50]World

## Features
- Shift all timestamps by any value (e.g. -0.10, +0.25)
- Supports [mm:ss.mmm] format
- Fully GUI-based (no CLI required)
- Fast processing for large LRC files

## Use Cases
- Fix delayed or early lyrics
- Sync Vocaloid / karaoke lyrics
- Adjust downloaded LRC files instantly

## Why LRCShifter?
- Designed for speed and simplicity
- Handles large LRC files smoothly

## How to Use
1. Install Python 3.x if you haven't already.
2. Download `lrc.py`.
3. Run `lrc.py`
4. Enter the shift value (e.g., -0.10 or 0.25)
5. Paste LRC text
6. Click Execute

## Technical Details
- Python 3 + Tkinter GUI
- Regex-based timestamp parsing
- AI-assisted development (Gemini) with manual optimization

## License
MIT License
