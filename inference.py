import gradio as gr
import torchaudio
import torch
from torchaudio.transforms import Resample
from models import SpeechCommandClassifier
import numpy as np
from preprocess import preprocess_audio, stereo2mono, zero_pad_if_necessary, MelSpectrogram
label = ['ปิดเพลง', 'อื่น ๆ', 'เอคโค่', 'เล่นเพลงต่อ', 'เล่นเพลงถัดไป', 'หยุดเพลง', 'เปิดเพลง', 'เล่นเพลงก่อนหน้า']

target_sr = 48000

def inference(audio_path):
    model = SpeechCommandClassifier(input_shapes=(1, 32, 141), num_classes=8)
    model.load_state_dict(torch.load("best_model.pth"))
    model.eval()
    wav,sr = torchaudio.load(audio_path)
    resampler = Resample(sr, target_sr)
    wav = resampler(wav)
    wav = stereo2mono(wav)
    wav = zero_pad_if_necessary(wav, int(target_sr * 1.5))[0: int(target_sr * 1.5)]
    meler = MelSpectrogram(sample_rate=target_sr, n_mels=32, n_fft=1024, hop_length=512)
    mel = (meler(wav) + torch.tensor(1e-6)).log2()
    pred: torch.Tensor = model(mel.unsqueeze(0).unsqueeze(0))
    y = torch.nn.functional.softmax(pred, dim=1)[0]
    return {label[i]: y[i] for i in range(8)}

demo = gr.Interface(
    fn=inference,
    inputs= gr.Audio(sources=["microphone", "upload"], type="filepath" ),
    outputs=gr.Label(),
    description="This is a demo for speech command classification\n available commands are: ปิดเพลง, อื่น ๆ, เอคโค่, เล่นเพลงต่อ, เล่นเพลงถัดไป, หยุดเพลง, เปิดเพลง, เล่นเพลงก่อนหน้า"
)

demo.launch(share=False)
