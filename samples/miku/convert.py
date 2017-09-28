from scipy.io import wavfile
import numpy as np

rate, data = wavfile.read('miku-all-no-head.wav')
data = (np.sum(data, axis = 1) / 2).astype(np.int16)

def note_no2solfege(no):
    lut = {
            0  : 'do',
            1  : 'ga',
            2  : 're',
            3  : 'nu',
            4  : 'mi',
            5  : 'fa',
            6  : 'jur',
            7  : 'so',
            8  : 'ki',
            9  : 'la',
            10 : 'pe',
            11 : 'ti',
    }
    return lut[no % 12]

for id in range(5, 128):
    start = (0 + (id - 5) * 12) * rate
    end = (9.1 + (id - 5) * 12) * rate
    start, end = int(start), int(end)
    wav = data[start:end]
    wav = (wav * (0.8 * 2**15 / np.max(wav))).astype(np.int16) # normalize volume
    wavfile.write('samples/note%03d-%s.wav' % (id, note_no2solfege(id)), rate, wav)
