import torch

optical_matrix = torch.tensor([[
    [80.0, 85.0, 90.0, 88.0],
    [75.0, 255.0, 250.0, 82.0],
    [78.0, 248.0, 255.0, 85.0],
    [82.0, 88.0, 84.0, 81.0]
]])

print(f"Array Shape: {optical_matrix.shape} | Matrix Type: {optical_matrix.dtype}")

scaled_output_tensor = optical_matrix / 255.0
print(scaled_output_tensor)
