from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from projci import settings
import os
from skimage import io
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
from skimage import io, color
import numpy as np


# Create your views here.
def CompareImage(request):
    ImgOne = os.path.join(settings.BASE_DIR, "images", "01.jpg")
    ImgTwo = os.path.join(settings.BASE_DIR, "images", "02.jpg")
    ImgThree = os.path.join(settings.BASE_DIR, "images", "03.jpg")
    ImgFour = os.path.join(settings.BASE_DIR, "images", "04.jpg")
    ImgFive = os.path.join(settings.BASE_DIR, "images", "05.jpg")

    imageA = io.imread(ImgOne)
    imageB = io.imread(ImgOne)

    # Convert images to grayscale
    imageA_gray = np.dot(imageA[...,:3], [0.2989, 0.5870, 0.1140])
    imageB_gray = np.dot(imageB[...,:3], [0.2989, 0.5870, 0.1140])

    # Compute SSIM
    if imageA_gray.shape != imageB_gray.shape:
        return HttpResponse("Images must have the same dimensions for comparison.")
        # raise ValueError("Images must have the same dimensions for comparison.")

    # Calculate data range
    data_range = imageA_gray.max() - imageA_gray.min()

    # Compute SSIM
    score, diff = ssim(imageA_gray, imageB_gray, full=True, data_range=data_range)

    threshold = 0.9

    if score >= threshold:
        similarity_message = "Similar design"
    else:
        similarity_message = "Not similar design"

    return HttpResponse(similarity_message)

