"""Train CGAN.
python -m mia_vgg.train_generator <fold> <task>
"""

import argparse
import os
import pickle
import random
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
import torch.utils.data
import torchvision.datasets as dset
import torchvision.transforms as transforms
import torchvision.utils as vutils
import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pathlib import Path
#from IPython.display import HTML

cond = True

class Trgtsf:
    def __init__(self, task):
        """Transform a target.
        :param t: Target vector.
        :type t: Vector of size 40
        """
        self.task = task

    def __call__(self, t):
        return t[self.task]

fold = int(sys.argv[1])
task = int(sys.argv[2])

# Set random seed for reproducibility
manualSeed = 999
#manualSeed = random.randint(1, 10000) # use if you want new results
print("Random Seed: ", manualSeed)
random.seed(manualSeed)
torch.manual_seed(manualSeed)
#torch.use_deterministic_algorithms(True) # Needed for reproducible results


# Root directory for dataset
dataroot = "data/celeba"

# Number of workers for dataloader
workers = 2

# Batch size during training
batch_size = 128

# Spatial size of training images. All images will be resized to this
#   size using a transformer.
image_size = 64

# Number of channels in the training images. For color images this is 3
nc = 3

# Size of z latent vector (i.e. size of generator input)
nz = 100

# Size of feature maps in generator
ngf = 64

# Size of feature maps in discriminator
ndf = 64

# Number of training epochs
num_epochs = 5

# Learning rate for optimizers
lr = 0.0002

# Beta1 hyperparameter for Adam optimizers
beta1 = 0.5

# Number of GPUs available. Use 0 for CPU mode.
ngpu = 1


# We can use an image folder dataset the way we have it setup.
# Create the dataset
transform=transforms.Compose([
transforms.Resize(image_size),
transforms.CenterCrop(image_size),
transforms.ToTensor(),
transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])

trgtsf = Trgtsf(task)
celeba = dset.CelebA(root="data", download=True, target_transform=trgtsf, transform=transform, split="all")
#celeba = dset.ImageFolder(root=dataroot,
#                           transform=transforms.Compose([
                           #transforms.Resize(image_size),
                           #transforms.CenterCrop(image_size),
                           #transforms.ToTensor(),
                           #transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                       #]))

path = Path("data", "splits", str(fold), "train.pickle")
with open(path, 'rb') as f:
    train_ids = pickle.load(f)
train_subsampler = torch.utils.data.SubsetRandomSampler(train_ids)
# Create the dataloader
dataloader = torch.utils.data.DataLoader(celeba, batch_size=batch_size, num_workers=workers, sampler=train_subsampler)

# Decide which device we want to run on
device = torch.device("cuda:0" if (torch.cuda.is_available() and ngpu > 0) else "cpu")


# custom weights initialization called on ``netG`` and ``netD``
def weights_init(m):
    classname = m.__class__.__name__
    if classname.find('Conv') != -1:
        nn.init.normal_(m.weight.data, 0.0, 0.02)
    elif classname.find('BatchNorm') != -1:
        nn.init.normal_(m.weight.data, 1.0, 0.02)
        nn.init.constant_(m.bias.data, 0)


# Generator Code

class Generator(nn.Module):
    def __init__(self, ngpu):
        super(Generator, self).__init__()
        self.ngpu = ngpu
        #Conditional gan
        ebd_size = 27
        self.label_embedding = nn.Embedding(2, ebd_size)
        self.cond = cond
        if cond:
            a = nn.ConvTranspose2d(ebd_size + nz, ngf * 8, 4, 1, 0, bias=False),
        else:
            a = nn.ConvTranspose2d(nz, ngf * 8, 4, 1, 0, bias=False),
            
        self.main = nn.Sequential(
            a[0],
            nn.BatchNorm2d(ngf * 8),
            nn.ReLU(True),
            # state size. ``(ngf*8) x 4 x 4``
            nn.ConvTranspose2d(ngf * 8, ngf * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf * 4),
            nn.ReLU(True),
            # state size. ``(ngf*4) x 8 x 8``
            nn.ConvTranspose2d( ngf * 4, ngf * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf * 2),
            nn.ReLU(True),
            # state size. ``(ngf*2) x 16 x 16``
            nn.ConvTranspose2d( ngf * 2, ngf, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ngf),
            nn.ReLU(True),
            # state size. ``(ngf) x 32 x 32``
            nn.ConvTranspose2d( ngf, nc, 4, 2, 1, bias=False),
            nn.Tanh()
            # state size. ``(nc) x 64 x 64``
        )

    def forward(self, input, labels):
        if self.cond:
            label_embeddings = self.label_embedding(labels).unsqueeze(2).unsqueeze(3)
            # Concatenate the noise and the label embeddings
            g_input = torch.cat((input, label_embeddings), 1)
            return self.main(g_input)
        else:
            return self.main(input)

if __name__=="__main__":
    # Create the generator
    netG = Generator(ngpu).to(device)

    # Handle multi-GPU if desired
    if (device.type == 'cuda') and (ngpu > 1):
        netG = nn.DataParallel(netG, list(range(ngpu)))

    # Apply the ``weights_init`` function to randomly initialize all weights
    #  to ``mean=0``, ``stdev=0.02``.
    netG.apply(weights_init)


class Discriminator(nn.Module):
    def __init__(self, ngpu):
        super(Discriminator, self).__init__()
        self.label_embedding = nn.Embedding(2, nz)
        self.label_linear = nn.Linear(nz, 64 * 64)
        
        self.mia_embedding = nn.Embedding(2, nz)
        self.mia_linear = nn.Linear(nz, 64 * 64)

        self.attrib_embedding = nn.Embedding(2, nz)
        self.attrib_linear = nn.Linear(nz, 64 * 64)

        self.ngpu = ngpu
        self.cond = cond
        if cond:
            a = nn.Conv2d(nc+3, ndf, 4, 2, 1, bias=False),
        else:
            a = nn.Conv2d(nc, ndf, 4, 2, 1, bias=False),
        self.main = nn.Sequential(
            # input is ``(nc) x 64 x 64``
            a[0],
            nn.LeakyReLU(0.2, inplace=True),
            # state size. ``(ndf) x 32 x 32``
            nn.Conv2d(ndf, ndf * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 2),
            nn.LeakyReLU(0.2, inplace=True),
            # state size. ``(ndf*2) x 16 x 16``
            nn.Conv2d(ndf * 2, ndf * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 4),
            nn.LeakyReLU(0.2, inplace=True),
            # state size. ``(ndf*4) x 8 x 8``
            nn.Conv2d(ndf * 4, ndf * 8, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 8),
            nn.LeakyReLU(0.2, inplace=True),
            # state size. ``(ndf*8) x 4 x 4``
            nn.Conv2d(ndf * 8, 1, 4, 1, 0, bias=False),
            nn.Sigmoid()
        )

    def forward(self, input, labels):
        if self.cond:
            label_embeddings = self.label_embedding(labels)
            label_map = self.label_linear(label_embeddings).view(labels.size(0), 1, input.size(2), input.size(3))
            # Concatenate images and label map
            d_input = torch.cat((input, label_map), 1)
            return self.main(d_input)
        else:
            return self.main(input)

def attrib_loss(x):
    criterion = nn.CrossEntropyLoss()
    target.eval()
    attack.eval()
    soft = target(x)
    out = attack(soft)
    loss = -criterion(out,label)



if __name__=="__main__":

    # Create the Discriminator
    netD = Discriminator(ngpu).to(device)

    # Handle multi-GPU if desired
    if (device.type == 'cuda') and (ngpu > 1):
        netD = nn.DataParallel(netD, list(range(ngpu)))

    # Apply the ``weights_init`` function to randomly initialize all weights
    # like this: ``to mean=0, stdev=0.2``.
    netD.apply(weights_init)

    # Initialize the ``BCELoss`` function
    criterion = nn.BCELoss()

    # Create batch of latent vectors that we will use to visualize
    #  the progression of the generator
    fixed_noise = torch.randn(64, nz, 1, 1, device=device)

    # Establish convention for real and fake labels during training
    real_label = 1.
    fake_label = 0.

    # Setup Adam optimizers for both G and D
    optimizerD = optim.Adam(netD.parameters(), lr=lr, betas=(beta1, 0.999))
    optimizerG = optim.Adam(netG.parameters(), lr=lr, betas=(beta1, 0.999))

    # Training Loop

    # Lists to keep track of progress
    img_list = []
    G_losses = []
    D_losses = []
    iters = 0

    print("Starting Training Loop...")
    # For each epoch
    for epoch in range(num_epochs):
        # For each batch in the dataloader
        for i, data in enumerate(dataloader, 0):
            #print("in batch")


                ############################
                # (1) Update D network: maximize log(D(x)) + log(1 - D(G(z)))
                ###########################
                ## Train with all-real batch
                netD.zero_grad()
                # Format batch
                real_cpu = data[0].to(device)
                real_lab = data[1].to(device)
                b_size = real_cpu.size(0)
                label = torch.full((b_size,), real_label, dtype=torch.float, device=device)
                # Forward pass real batch through D
                output = netD(real_cpu, real_lab).view(-1)
                # Calculate loss on all-real batch
                errD_real = criterion(output, label)
                # Calculate gradients for D in backward pass
                errD_real.backward()
                D_x = output.mean().item()

                #print("D real batch")

                ## Train with all-fake batch
                # Generate batch of latent vectors
                noise = torch.randn(b_size, nz, 1, 1, device=device)
                # Generate fake image batch with G
                gen_lab = torch.randint(0, 2, (b_size,), device=device)
                fake = netG(noise, gen_lab)

                label.fill_(fake_label)
                # Classify all fake batch with D
                output = netD(fake.detach(),gen_lab).view(-1)
                # Calculate D's loss on the all-fake batch
                errD_fake = criterion(output, label)
                # Calculate the gradients for this batch, accumulated (summed) with previous gradients
                errD_fake.backward()
                D_G_z1 = output.mean().item()
                # Compute error of D as sum over the fake and the real batches
                errD = errD_real + errD_fake
                # Update D
                optimizerD.step()

                #print("D updated")

                ############################
                # (2) Update G network: maximize log(D(G(z)))
                ###########################
                netG.zero_grad()
                label.fill_(real_label)  # fake labels are real for generator cost
                # Since we just updated D, perform another forward pass of all-fake batch through D
                output = netD(fake, gen_lab).view(-1)
                # Calculate G's loss based on this output
                errG = criterion(output, label)
                # Calculate gradients for G
                errG.backward()
                D_G_z2 = output.mean().item()
                # Update G
                optimizerG.step()

                #print("G updated")

                # Output training stats
                if i % 50 == 0:
                    print('[%d/%d][%d/%d]\tLoss_D: %.4f\tLoss_G: %.4f\tD(x): %.4f\tD(G(z)): %.4f / %.4f'
                          % (epoch, num_epochs, i, len(dataloader),
                             errD.item(), errG.item(), D_x, D_G_z1, D_G_z2))

                # Save Losses for plotting later
                G_losses.append(errG.item())
                D_losses.append(errD.item())

                # Check how the generator is doing by saving G's output on fixed_noise
                #if (iters % 500 == 0) or ((epoch == num_epochs-1) and (i == len(dataloader)-1)):
                #    with torch.no_grad():
                #        fake = netG(fixed_noise).detach().cpu()
                #    img_list.append(vutils.make_grid(fake, padding=2, normalize=True))

                iters += 1

    os.makedirs(f"result/{task}/gan/{fold}", exist_ok=True)

    torch.save(netG.state_dict(), f"result/{task}/gan/{fold}/gan_weights")

    with open(f"result/{task}/gan/{fold}/G_losses.pickle", 'wb') as f:
        pickle.dump(G_losses, f)

    with open(f"result/{task}/gan/{fold}/D_losses.pickle", 'wb') as f:
        pickle.dump(D_losses, f)
