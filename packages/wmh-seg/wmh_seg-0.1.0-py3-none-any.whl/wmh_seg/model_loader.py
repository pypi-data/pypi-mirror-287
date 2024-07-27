import pkg_resources
import torch
import os

def load_model():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model_dir = pkg_resources.resource_filename('wmh_seg', '')
    model_path = os.path.join(model_dir, 'ChallengeMatched_Unet_mit_b5.pth')

    if not os.path.exists(model_path):
        url = 'https://huggingface.co/jil202/wmh_seg/resolve/main/ChallengeMatched_Unet_mit_b5.pth'  # Replace with your file URL
        print(f'Downloading model from {url}...')
        os.system(f'wget {url} -O {model_path}')

    model_path = pkg_resources.resource_filename('wmh_seg', 'ChallengeMatched_Unet_mit_b5.pth')
    
    model = torch.load(model_path, map_location=device, weights_only=False)
    model.eval()
    model.to(device)
    
    return model

model = load_model()