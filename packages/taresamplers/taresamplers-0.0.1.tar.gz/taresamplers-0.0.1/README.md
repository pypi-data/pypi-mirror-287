##taresamplers - A Utility Wrapper for TorchAudio Resamplers

`torchaudio` has very efficient resamplers. This is a code snippet that I use so often that I decided to package for my convenience, instead of adding it to every utils.py of every project.
Resampling kernels are cached in the background for you, so computation will be much faster after the first few calls.

Simply do:

```
from torchaudioresamplers import load_and_resample_audio, resample_audio

target_sr = 22050
audio_path = "/tmp/audio.wav"
wav = load_and_resample_audio(audio_path,target_sr)

wav_16k = resample_audio(wav,target_sr,16000)

```

