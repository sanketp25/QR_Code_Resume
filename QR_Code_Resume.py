#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import qrcode


github_resume_url = "https://github.com/sanketp25/Resume/raw/main/SanketPurohit_Resume.pdf"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(github_resume_url)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("/path/to/save/resume_qr_code.png")

