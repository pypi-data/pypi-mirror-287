import torch
import torchaudio
from torchaudio.transforms import Resample
from torchaudio.functional import resample


COMMON_SAMPLING_RATES = [8000,22050,24000,32000,44100,48000]
RESAMPLERS = {input_sr : {target_sr: Resample(orig_freq=input_sr,new_freq=target_sr) for target_sr in COMMON_SAMPLING_RATES} for input_sr in COMMON_SAMPLING_RATES}



def resample_audio(wav,input_sr,output_sr):
    if input_sr == output_sr:
        return wav
    else:
        if input_sr in RESAMPLERS and output_sr in RESAMPLERS[input_sr]:
            resampled_wav = RESAMPLERS[input_sr][output_sr](wav)
        else:
            resampled_wav = resample(wav,orig_freq=input_sr,new_freq=output_sr)
        return resampled_wav

def convert_to_mono(wav):
    return torch.mean(wav,dim=0,keepdim=True)

def load_and_resample_audio(audio_file,output_sr,mono=True):
    #Input:    path to file on disk (str or Pathlike)
    #Returns:  torch.Tensor with shape [1,T]
    wav, fs = torchaudio.load(audio_file,channels_first=True)
    if mono:
        wav = convert_to_mono(wav)
    return resample_audio(wav,input_sr=fs,output_sr=output_sr)

