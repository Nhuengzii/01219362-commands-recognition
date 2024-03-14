import torch
from torch import nn

class SpeechCommandClassifier(nn.Module):
    def __init__(self, input_shapes,num_classes, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.num_classes = num_classes
        self.conv_layer = nn.Sequential(
            nn.Conv2d(1, 50, 3, 2),
            nn.BatchNorm2d(50),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Conv2d(50, 200, 3, 2),
            nn.ReLU(),
        )

        with torch.no_grad():
            num_elem: torch.Tensor = self.conv_layer(torch.rand(1, *input_shapes))[0].numel()

        self.linear = nn.Sequential(
            nn.Flatten(),
            nn.Linear(int(num_elem), 200),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(200, 200),
            nn.Dropout(0.5),
            nn.ReLU(),
            nn.Linear(200, num_classes),
        )
    def forward(self, x):
        x = self.conv_layer(x)
        x = self.linear(x)
        return x

if __name__ == "__main__":
    model = SpeechCommandClassifier(input_shapes=(1, 32, 141), num_classes=8)
    fake = torch.rand(1, 1, 32, 141)
    print(model.conv_layer(fake).shape)
