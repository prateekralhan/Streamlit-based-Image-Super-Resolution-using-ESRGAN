import cv2
import torch
import numpy as np
import streamlit as st
import RRDBNet_arch as arch

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def instantiate_model(model_name):
    if model_name:
        if model_name == "ESRGAN model ✅":
            model_path = 'models/RRDB_ESRGAN_x4.pth'

        else:
            model_path = 'models/RRDB_PSNR_x4.pth'

        device = torch.device('cuda')
        model = arch.RRDBNet(3, 3, 64, 23, gc=32)
        model.load_state_dict(torch.load(model_path), strict=True)
        model.eval()
        model = model.to(device)
        print('Model path {:s}. \nModel Loaded successfully...'.format(model_path))
        return model
    else:
        st.warning('⚠ Please choose a model !! 😯')


@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def image_super_resolution(uploaded_image, downloaded_image, model):
    device = torch.device('cuda')
    img = cv2.imread(uploaded_image, cv2.IMREAD_COLOR)
    img = img * 1.0 / 255
    img = torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
    img_LR = img.unsqueeze(0)
    img_LR = img_LR.to(device)
    with torch.no_grad():
        output = model(img_LR).data.squeeze().float().cpu().clamp_(0, 1).numpy()
    output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
    output = (output * 255.0).round()
    cv2.imwrite(downloaded_image, output)


@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def download_success():
    st.balloons()
    st.success('✅ Download Successful !!')
