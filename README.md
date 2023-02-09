# Dynamic Mode Decomposition (DMD) Algorithm

A repository containing the implementation of the Dynamic Mode Decomposition (DMD) algorithm in Python.

###  :file_folder: File Structure

```
.
├── videoframes.py
│   ├── Run this file first to seperate each frame of the video
├── dataimagegray.py
│   ├── Run this file to create an npy dataset from video frames in columns
├── DMD - gray.ipynb
│   ├── Performing Dynamic mode decomposition
├── Fluidosc.mp4
│   ├── sample video
└── README.md
```

### Table of Contents

    Introduction
    Requirements
    Usage
    Parameters
    Output
    Examples
    Conclusion

## Introduction

Dynamic Mode Decomposition (DMD) is a data-driven technique that separates a complex system's dynamic behavior into a set of modes, each of which corresponds to a different underlying physical process. It is a mathematical method that can be applied to a wide range of fields such as fluid dynamics, structural mechanics, and electro-magnetics.
Requirements

The following packages must be installed prior to running the code:

    OpenCV (for creating the dataset)
    Numpy
    Matplotlib (for visualization purposes)
    Scipy
    
## Usage

To use the DMD algorithm, simply import the DMD function and pass in your data matrix X, time-shifted data matrix Xprime, and the number of modes r as input parameters.

## python

from dmd import DMD
Phi, Lambda, b = DMD(X, Xprime, r)

Parameters

    X: A 2D Numpy array representing the data matrix
    Xprime: A 2D Numpy array representing the time-shifted data matrix
    r: An integer representing the number of modes desired for the output

Output

The function returns three outputs:

    Phi: A 2D Numpy array representing the DMD modes
    Lambda: A 2D Numpy array representing the eigenvalues of the system
    b: A 1D Numpy array representing the coefficients of the DMD modes

*** Important: Make sure that your data is 2-D
## Conclusion

This repository provides a simple and easy-to-use implementation of the Dynamic Mode Decomposition (DMD) algorithm in Python. It is intended for researchers, engineers, and students who are interested in exploring the capabilities of this powerful technique for data analysis and system identification.
