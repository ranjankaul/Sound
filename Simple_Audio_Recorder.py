#### Simple Sound Recorder #####

import pyaudio
import wave
import sys

def REC(filename):
    FORMAT = pyaudio.paInt16                     
    CHANNELS = 2                                 ## Number of channels Mono/Stereo
    RATE = 44100                                 ## Sampling rate
    CHUNK = 1024                                 ## Chunk Size
    RECORD_SECONDS = 5                           ## Change the duration
    WAVE_OUTPUT_FILENAME = filename

    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("recording...")
    frames = []
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK, exception_on_overflow = False)
        frames.append(data)
    print("finished recording")
        
        
                                                    ## stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
        
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

filename = str(input("Enter File Name To Be Saved As"))
REC(filename)
