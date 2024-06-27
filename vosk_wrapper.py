#!/usr/bin/env python3

import wave
import sys
import time
from vosk import Model, KaldiRecognizer, SetLogLevel
start_time = time.time()
SetLogLevel(0)
wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("Audio file must be WAV format mono PCM.")
    sys.exit(1)
#model = Model(model_name="vosk-model-small-en-us-0.15")
model = Model(model_name="vosk-model-en-us-0.22")
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)
rec.SetPartialWords(True)
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())
print(rec.FinalResult())
print("\n--- %s seconds ---" % (time.time() - start_time))
