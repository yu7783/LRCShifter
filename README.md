# LRCShifter
Adjust timestamps in LRC lyric files with a simple Python GUI

## Features
With LRCShifter, you can easily adjust the timing of lyrics in LRC files.  
You can move timestamps forward or backward by any number of seconds, including fractions of a second.

- Automatically adjusts timestamps in the `[mm:ss.mmm]` format.
- Negative time values are not allowed.
- Simple GUI that allows for easy operation without using the command line.

## How to Use
1. Install Python 3.x if you haven't already.
2. Download `lrc.py`.
3. Run lrc.py
4. Enter the shift value in seconds (e.g., -0.10 or 0.25).
5. Paste your LRC lyrics into the input box on the left.
6. Click the Execute button to shift the timestamps.
7. The adjusted lyrics will appear in the output box on the right.

## Technical Details
- Written in Python 3 using Tkinter for the GUI.
- Uses regular expressions to parse and adjust timestamps.
- Input is accepted via a text box, and the output is displayed in a separate text box.
- Developed with AI (Gemini) assistance and manually optimized logic.
## Benefits
- Quickly correct timing issues in LRC lyric files.
- Improves synchronization with music playback.
- Ideal for Vocaloid and karaoke enthusiasts.

## License
MIT License
