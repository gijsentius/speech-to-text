import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate

sd.default.samplerate = fs
sd.default.channels = 2

duration = 3  # Duration of recording in seconds

myrecording = sd.rec(int(duration * fs))
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file
