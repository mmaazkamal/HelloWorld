__author__ = 'HP'

import sys
from wavefile import WaveReader, WaveWriter

with WaveReader(sys.argv[1]) as r :
    with WaveWriter('SignleTone.wav', channels=r.channels, samplerate=r.samplerate,) as w :
        # Just to set the metadata
        w.metadata.title = r.metadata.title + " II"
        w.metadata.artist = r.metadata.artist

        # This is the prodessing loop
        for data in r.read_iter(size=512) :
            data[1] *= .8     # lower volume on the second channel
            w.write(data)
            #"""