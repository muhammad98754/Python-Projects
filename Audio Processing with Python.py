# For Audio Processing, Python provides Pydub, which is a very simple, and well-designed module.

#AudioSegment is the parent class in Pydub. It plays the role of a container that can load, manipulate, and save audio files. Let’s create our first audio with python. For this, we will need a test file, which could be in any format like WAV, MP3, or anyone. In this article, I will download an audio file just like we scrape data from the web:

import urllib.request
from pydub import AudioSegment
from pydub.playback import play
# Download an audio file
urllib.request.urlretrieve("https://tinyurl.com/wx9amev", "metallic-drums.wav")
# Load into PyDub
loop = AudioSegment.from_wav("metallic-drums.wav")
# Play the result
play(loop)

#As we have loaded our audio, now we can perform various types of audio processing, let’s start from some necessary steps by repeating an audio file:

# Repeat 2 times
loop2 = loop * 2
# Get length in milliseconds
length = len(loop2)
# Set fade time
fade_time = int(length * 0.5)
# Fade in and out
faded = loop2.fade_in(fade_time).fade_out(fade_time)

#Above we simply repeated the audio, now let’s layer and mix different audio segments with different levels of manipulation:

# Download another loop
urllib.request.urlretrieve("https://tinyurl.com/yx3k5kw5", "beat.wav")
# Load into PyDub
beat = AudioSegment.from_wav("beat.wav")
# Mix with our original loop
mixed = beat[:length].overlay(loop2)

#Now, let’s move further with bringing everything together by applying filters and reversing audio effects:

# Filter the beat at 3kHz
filtered = beat.low_pass_filter(3000)
# Mix loop2 with a reversed, panned version
loop = loop2.reverse().pan(-0.5).overlay(loop2.pan(0.5))
# Mix our filtered beat with the new loop at -3dB
final = filtered.overlay(loop2 - 3, loop=True)

#Now if you want to save your audio file, you can easily do it as below:

final.export("final.mp3", format="mp3")

#Apart from all the steps of manipulating the sound we have covered above, we can also synthesize new tones. These tones can be sine, square, manipulating waves at any frequency. We can also perform white noise. In the example below, I will show the sine method to produce sine tuning for the initial 15 intervals in a harmonic way:

# Create an empty AudioSegment
result = AudioSegment.silent(duration=0)
# Loop over 0-14
for n in range(15):
    # Generate a sine tone with frequency 200 * n
    gen = Sine(200 * n)
    # AudioSegment with duration 200ms, gain -3
    sine  = gen.to_audio_segment(duration=200).apply_gain(-3)
    # Fade in / out
    sine = sine.fade_in(50).fade_out(100)
    # Append the sine to our result
    result += sine
# Play the result
play(result)

