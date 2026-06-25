import torch
import torch.nn as nn

class FeatureExtractorCNN(nn.Module):
    def _init_(self):
        super(FeatureExtractorCNN, self)._init_()
        self.conv_node = nn.Conv2d(in_channels=1, out_channels=2, kernel_size=3, padding=1)
        self.pool_node = nn.MaxPool2d(kernel_size=2, stride=2)
        self.linear_node = nn.Linear(2 * 2 * 2, 2)

    def forward(self, input_vector):
        x = self.pool_node(torch.relu(self.conv_node(input_vector)))
        x = x.view(-1, 2 * 2 * 2)
        x = self.linear_node(x)
        return x

classification_net = FeatureExtractorCNN()
mock_data_batch = torch.randn(1, 1, 4, 4)
output_logits = classification_net(mock_data_batch)

print(output_logits.detach().numpy())
