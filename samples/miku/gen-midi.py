#!/usr/bin/env python

from midiutil import MIDIFile

def note_no2solfege(no):
    '''
    lut = {
            0  : 'do',
            1  : 'ga',
            2  : 'ray',
            3  : 'nu',
            4  : 'mi',
            5  : 'fa',
            6  : 'jur',
            7  : 'sol',
            8  : 'ki',
            9  : 'la',
            10 : 'pe',
            11 : 'tsi',
    }
    '''
    # modified for vocaloid's lyric system
    lut = {
            0  : 'doe',
            1  : 'ga',
            2  : 'ray',
            3  : 'nu',
            4  : 'mi',
            5  : 'far',
            6  : 'ju',
            7  : 'sol',
            8  : 'ki',
            9  : 'la',
            10 : 'pei',
            11 : 'ti',
    }
    return lut[no % 12]

def c_range(b, e):
    if b <= e:
        return list(range(b, e + 1))
    else:
        return list(range(b, e - 1, -1))

#degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
#degrees  = c_range(60, 72)[:-1] + c_range(72, 55)[:-1] + c_range(55, 72)[:-1] + c_range(72, 60)[:-1]
degrees  = c_range(0, 127)

track    = 0
channel  = 0
duration = 3    # In beats
tempo    = 10   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

time     = 0    # In beats

# lyric
with open("samples.txt", "w") as fo:
    fo.write(note_no2solfege(degrees[0]))
    for pitch in degrees[1:]:
        fo.write(' ')
        fo.write(note_no2solfege(pitch))

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)
for i, pitch in enumerate(degrees):
    MyMIDI.addNote(track, channel, pitch, time + 4 * i, duration, volume)

# midi
with open("samples.mid", "wb") as fo:
    MyMIDI.writeFile(fo)
