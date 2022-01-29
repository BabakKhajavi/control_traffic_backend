import librosa
from FeatureExtaction import ExtractingSoundFeaturse
extract = ExtractingSoundFeaturse()
file = ""
signal = librosa.load(file)
ae_signal = extract.get_amplitude_envelope(signal, 1024, 1024)
t = extract.get_frame_to_time(ae_signal, 512)[0]


def get_avg(length, ae_signal):
    average = []
    iteration = int(len(ae_signal)/length)
    for i in range(0, iteration):
        start = i * length
        finish = start + length
