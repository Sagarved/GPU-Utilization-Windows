import GPUtil
print("Hi 1")

gpus = GPUtil.getGPUs()
print(gpus)
for gpu in gpus:
    print(f"GPU ID: {gpu.id}")
    print(f"Name: {gpu.name}")
    print(f"Load: {gpu.load * 100}%")
    print(f"Memory Free: {gpu.memoryFree}MB")
    print(f"Memory Used: {gpu.memoryUsed}MB")
    print(f"Memory Total: {gpu.memoryTotal}MB")
