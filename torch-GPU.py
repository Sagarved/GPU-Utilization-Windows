import torch
print("CUDA Available:", torch.cuda.is_available())
print("Number of GPUs:", torch.cuda.device_count())
print("GPU Name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU found")
"""
As all these torch, tensorflow uses cuda or other GPU libraries, they are not installed in windows client
without actual GPU. This utility check is not working. 
When there is a time one can use to check the driver package of nvidia-smi for windows.
In the ubuntu nvidia-smi without local GPU was able to install the driver package.

"""
