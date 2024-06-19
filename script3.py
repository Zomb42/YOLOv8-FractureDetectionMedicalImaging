import streamlit as st
import cv2 as cv
import numpy as np
from PIL import Image
import detection.detect as detect
import classification.classify as classify
import segmentation.segment as segment
import muscledetect.muscledetect as mfrac

mfrac.train()