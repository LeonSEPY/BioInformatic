import os
import torch
import monai
import nibabel as nib
import numpy as np
from monai.transforms import (
    LoadImaged, AddChanneld, Spacingd, Orientationd, ScaleIntensityd, 
    CropForegroundd, RandCropByPosNegLabeld, RandFlipd, RandRotate90d,
    ToTensord
)
from monai.data import DataLoader, Dataset, CacheDataset
from monai.networks.nets import UNet
from monai.losses import DiceLoss
from monai.metrics import DiceMetric
from monai.inferers import sliding_window_inference

# Directory paths
data_dir = './data/processed'
images_dir = os.path.join(data_dir, 'images')
labels_dir = os.path.join(data_dir, 'labels')

# Get file paths
images = sorted([os.path.join(images_dir, f) for f in os.listdir(images_dir)])
labels = sorted([os.path.join(labels_dir, f) for f in os.listdir(labels_dir)])

# Define dictionary-based dataset
train_files = [{"image": img, "label": lbl} for img, lbl in zip(images, labels)]

# Transforms
train_transforms = monai.transforms.Compose([
    LoadImaged(keys=["image", "label"]),
    AddChanneld(keys=["image", "label"]),
    Spacingd(keys=["image", "label"], pixdim=(1.5, 1.5, 2.0), mode=("bilinear", "nearest")),
    Orientationd(keys=["image", "label"], axcodes="RAS"),
    ScaleIntensityd(keys="image"),
    CropForegroundd(keys=["image", "label"], source_key="image"),
    RandCropByPosNegLabeld(
        keys=["image", "label"],
        label_key="label",
        spatial_size=(96, 96, 96),
        pos=1,
        neg=1,
        num_samples=4,
        image_key="image",
        image_threshold=0
    ),
    RandFlipd(keys=["image", "label"], spatial_axis=[0], prob=0.10),
    RandFlipd(keys=["image", "label"], spatial_axis=[1], prob=0.10),
    RandFlipd(keys=["image", "label"], spatial_axis=[2], prob=0.10),
    RandRotate90d(keys=["image", "label"], prob=0.10, max_k=3),
    ToTensord(keys=["image", "label"]),
])

# Dataset and Dataloader
train_ds = CacheDataset(data=train_files, transform=train_transforms, cache_rate=1.0)
train_loader = DataLoader(train_ds, batch_size=2, shuffle=True, num_workers=2)

# Model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = UNet(
    dimensions=3,
    in_channels=1,
    out_channels=1,
    channels=(16, 32, 64, 128, 256),
    strides=(2, 2, 2, 2),
    num_res_units=2,
).to(device)

# Loss and optimizer
loss_function = DiceLoss(sigmoid=True)
optimizer = torch.optim.Adam(model.parameters(), 1e-4)
dice_metric = DiceMetric(include_background=True, reduction="mean")

# Training loop
max_epochs = 50
val_interval = 5

for epoch in range(max_epochs):
    print(f"Epoch {epoch+1}/{max_epochs}")
    model.train()
    epoch_loss = 0
    step = 0
    for batch_data in train_loader:
        step += 1
        inputs, labels = batch_data["image"].to(device), batch_data["label"].to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = loss_function(outputs, labels)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()
    print(f"Epoch {epoch+1} average loss: {epoch_loss/step:.4f}")

print("Training completed.")
torch.save(model.state_dict(), "./models/segmentation/unet3d_brain_seg.pth")
