# Multi-Scale Document Dewarping via an End-to-End Deep Neural Network Approach
ScaleDoc: A Two Stage Approach for Scale Aware Document Dewarping

# Introduction
Document dewarping has been studied for many years but remains unresolved, particularly for multi-scale documents where the background occupies a large proportion. To enhance the multi-scale awareness of document dewarping algorithms, we propose a two-stage framework with explicit scale-aware capabilities, named ScaleDoc, which consists of a scale-aware stage and a dewarping stage.
In the scale-aware stage, we propose a convolutional network with self-attention mechanisms to explicitly remove the document background. In the dewarping stage, we introduce a lightweight method that dewarps warped documents by predicting document edges using sparse control points. 
To verify the performance of the proposed ScaleDoc, we collect a new real document dataset named DocW, which comprises 1k images of varying scales and warping levels. In the DocW, all documents are authentically captured rather than generated.
We conduct extensive experiments on our DocW and another benchmark dataset DocUnet. The experimental results demonstrate the effectiveness of our proposed ScaleDoc, outperforming the current state-of-the-art (SOTA) models on both pixel
alignment metrics (i.e., MS-SSIM and LD) and OCR metrics (i.e., CER and ED) for multi-scale documents. 

# Dataset
![samples_and_name.png](imgs%2Fsamples_and_name.png)
More information about dataset **DocW** could be found in [dataset.md](dataset.md)

# Results
Test result on DocW:
![docWresult.png](imgs%2FdocWresult.png)

Test result on DocUnet Benchmark:
![docunetresult.png](imgs%2Fdocunetresult.png)

# Poster
![SURF-2023-0121-Poster.jpg](imgs%2FSURF-2023-0121-Poster.jpg)