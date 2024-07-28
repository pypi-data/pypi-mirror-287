from client import Client
from vytal.adtech import *
import asyncio
import os
import sys
import time
import threading
import numpy as np
b = {
    "camera": "HP Wide Vision HD Camera (30c9:000e)",
    "platform": "Windows NT 10.0; Win64; x64",
    "avg_reprojection_error": 2.0783670841932467,
    "camera_matrix": np.asarray([
        [
            799.8137439399165,
            0,
            576.6573685593131
        ],
        [
            0,
            791.4666396339051,
            347.2948658613477
        ],
        [
            0,
            0,
            1
        ]
    ]),
    "distortion_coefficients": np.asarray([
        0.061920650444799503,
        0.06092457226057464,
        -0.0034758086042474584,
        -0.03328300273410292,
        -0.0793719109712436
    ]),
    "distortion_model": "rectilinear",
    "img_size": [
        1280,
        720
    ],
    "calibration_time": "Sat, 30 Mar 2024 23:13:11 GMT"
}

# Configuration
API_KEY = "sk-3s6r5n64j4u"
IPD = 0.065  # Interpupillary distance in meters

c = Client(API_KEY, IPD)
a = c.start_thread(eye_frames=False)
time.sleep(10)
print(c.preds)
c.end_thread(a)
