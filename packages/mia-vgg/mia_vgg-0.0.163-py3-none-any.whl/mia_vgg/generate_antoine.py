"""Generate synthetic images with matching labels.
python -m mia_vgg.generate <fold> <task>
"""
from .train_generator import Generator, nz
import torch
import matplotlib.pyplot as plt
import torchvision.utils as vutils
import numpy as np
import sys
import pickle
import os
from pathlib import Path
from tqdm import tqdm
from PIL import Image
import csv



ngpu = 0
device = torch.device("cuda:0" if (torch.cuda.is_available() and ngpu > 0) else "cpu")

# Create the generator
netG_0 = Generator(ngpu).to(device)
netG_1 = Generator(ngpu).to(device)

# Handle multi-GPU if desired
if (device.type == 'cuda') and (ngpu > 1):
    netG = torch.nn.DataParallel(netG, list(range(ngpu)))
fold = int(sys.argv[1])
task = int(sys.argv[2])
netG_0.load_state_dict(torch.load(f"result/{task}/gan/{fold}/gan_weights_0", map_location=torch.device(device) ))
netG_1.load_state_dict(torch.load(f"result/{task}/gan/{fold}/gan_weights_1", map_location=torch.device(device) ))
netG.eval()


fixed_noise = torch.randn(50000, nz, 1, 1, device=device)
with torch.no_grad():
    fakes0 = netG_0(fixed_noise).detach().cpu()
fixed_noise = torch.randn(50000, nz, 1, 1, device=device)
with torch.no_grad():
    fakes1 = netG_1(fixed_noise).detach().cpu()
path_img = Path("data", "synthetic", str(task), str(fold), "images")
os.makedirs(path_img, exist_ok=True)
path = Path("data", "synthetic", str(task), str(fold), "attribute.csv")
with open(path, "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    for i,fake in tqdm(enumerate(fakes0)):
        writer.writerow([f"{str(i)}.png", "0"])
        fake = np.transpose(fake, (1,2,0)).numpy()
        fake = (fake+1)/2*255
        fake = fake.astype(np.uint8)
        im = Image.fromarray(fake, 'RGB')
        im.save(Path(path_img, f"{str(i)}.png"), quality=100, subsampling=0)

    ofset = len(fakes0)-1
    for i,fake in tqdm(enumerate(fakes1)):
        writer.writerow([f"{str(ofset+i)}.png", "1"])
        fake = np.transpose(fake, (1,2,0)).numpy()
        fake = (fake+1)/2*255
        fake = fake.astype(np.uint8)
        im = Image.fromarray(fake, 'RGB')
        im.save(Path(path_img, f"{str(ofset+i)}.png"), quality=100, subsampling=0)

