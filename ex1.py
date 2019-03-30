from essentia.standard import *

audio = MonoLoader(filename='audio/07 - Don\'t Stop Me Now (Digital Remaster).mp3')()

# Compute beat positions and BPM
rhythm_extractor = RhythmExtractor2013(method="multifeature")
bpm, beats, beats_confidence, _, beats_intervals = rhythm_extractor(audio)

print("BPM:", bpm)
print("Beat positions (sec.):", beats)
print("Beat estimation confidence:", beats_confidence)

# marker = AudioOnsetsMarker(onsets=beats, type='beep')
# marked_audio = marker(audio)
# MonoWriter(filename='audio/dont-stop-beats.mp3')(marked_audio)

# from pylab import plot, show, figure, imshow

import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (30, 12) # set plot sizes to something larger than default

plt.plot(audio, color="black", linewidth=0.7)
plt.title("Audio waveform")
plt.savefig("dont-stop-waveform.png")



for beat in beats:
    plt.axvline(x=beat*44100, color='#2eb1ed    ', linewidth=0.5)



plt.title("Audio waveform and the estimated beat positions")



plt.savefig("dont-stop-beats.png")




