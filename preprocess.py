import glob
import torchaudio
from torchaudio.transforms import MelSpectrogram
import torch
import random

class RandomClip:
    def __init__(self, sample_rate, clip_length):
        self.clip_length = clip_length

    def __call__(self, audio_data):
        audio_length = audio_data.shape[0]
        if audio_length > self.clip_length:
            offset = random.randint(0, audio_length-self.clip_length)
            audio_data = audio_data[offset:(offset+self.clip_length)]
        return audio_data

class ComposeTransform:
    def __init__(self, transforms):
        self.transforms = transforms

    def __call__(self, audio_data):
        for t in self.transforms:
            audio_data = t(audio_data)
        return audio_data

def stereo2mono(wav: torch.Tensor):
    if wav.shape[0] == 2:
        return wav.mean(dim=0)
    elif wav.shape[0] == 1:
        return wav.squeeze(0)
    else:
        return wav

def zero_pad_if_necessary(wav: torch.Tensor, min_sample_length: int):
    if len(wav) < min_sample_length:
        pad = torch.cat([wav, torch.zeros((min_sample_length - len(wav),))])
        return pad
    else:
        return wav

def preprocess_audio(wav: torch.Tensor, sample_rate: int, clip_length: int):
    composes = ComposeTransform([
        RandomClip(sample_rate, clip_length),
        MelSpectrogram(sample_rate=sample_rate, n_mels=32, n_fft=1024, hop_length=512),
    ])
    wav = stereo2mono(wav)
    wav = zero_pad_if_necessary(wav, sample_rate*clip_length)
    mel = composes(wav)
    mel = (mel + torch.tensor(1e-6)).log2()
    return mel.unsqueeze(0)
