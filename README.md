Hello! Thank you for visiting my profile. This repository demonstrates image comparison using Python and the powerful skimage library, ideal for working with image processing tasks. Here, I’ve implemented a comparison of three images to showcase its capabilities. Feel free to explore and try it out—it's a valuable tool for anyone working with image analysis.

skimage (scikit-image) is a Python library designed for image processing, offering a wide range of tools for tasks like image segmentation, filtering, and transformation. It's built on top of NumPy and is widely used in scientific and analytical applications for efficient image analysis.

The complete code is located in the views.py file, as this was part of a Django project I developed for a client. I'm sharing this work as an example of my approach and expertise in Django development.


pip install scikit-image
pip install matplotlib
pip install numpy
------------------------------------------------------------------------------------------------------------------------------------------------
from django.shortcuts import render
from django.http import HttpResponse
from projci import settings
import os
from skimage import io
from skimage.metrics import structural_similarity as ssim
import numpy as np

# View function to compare two images using SSIM (Structural Similarity Index)
def CompareImage(request):
    # Paths to the images
    ImgOne = os.path.join(settings.BASE_DIR, "images", "01.jpg")
    ImgTwo = os.path.join(settings.BASE_DIR, "images", "02.jpg")

    # Load the images
    imageA = io.imread(ImgOne)
    imageB = io.imread(ImgTwo)

    # Convert images to grayscale by applying dot product for each RGB channel
    imageA_gray = np.dot(imageA[...,:3], [0.2989, 0.5870, 0.1140])
    imageB_gray = np.dot(imageB[...,:3], [0.2989, 0.5870, 0.1140])

    # Check if the images have the same dimensions
    if imageA_gray.shape != imageB_gray.shape:
        return HttpResponse("Images must have the same dimensions for comparison.")

    # Calculate data range, used for SSIM computation
    data_range = imageA_gray.max() - imageA_gray.min()

    # Compute SSIM between the two grayscale images
    score, _ = ssim(imageA_gray, imageB_gray, full=True, data_range=data_range)

    # Define a similarity threshold
    threshold = 0.9

    # Determine similarity message based on SSIM score
    similarity_message = "Similar design" if score >= threshold else "Not similar design"

    # Return the result as an HTTP response
    return HttpResponse(similarity_message)
