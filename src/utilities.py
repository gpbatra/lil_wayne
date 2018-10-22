#!/usr/bin/env python
# coding: utf-8



import librosa, librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pickle
import os


DATA_DIR = os.environ['LW_DATA_DIRECTORY']
notes_file = os.path.join(DATA_DIR, 'notes.p')
notes = pickle.load( open( notes_file, "rb" ) )

def array_statistics(x, sr):
    print x.shape, sr
    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(x, sr=sr)
    plt.show()
    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X), ref=np.max)
    librosa.display.specshow(Xdb, y_axis='log', x_axis='time', sr=sr)
    plt.title('Power spectrogram')
    plt.colorbar(format='%+2.0f dB')
    plt.tight_layout()
    plt.show()

def read_wav(filename):
    x,sr = librosa.core.load(filename, sr=None, mono=True)
    array_statistics(x,sr)
    return x,sr

def append_array(x, sr, total_duration, octave, note_array):
    for (note, hold) in note_array:
        x=np.append(x,librosa.core.tone(notes[note+str(octave)]['hz'],sr=sr, duration= hold * total_duration), axis=0)
    return x, sr
