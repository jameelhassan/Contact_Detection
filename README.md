# Contact_Detection

This repo is the set of codes for Human-Human and Human-object contact detection. 

You will need to have the images as in the path folders mentioned in the python notebook scripts in order to run the code propoerly. 

The repo makes use of Openpose for pose estimation and [Mannequin depth](https://github.com/google/mannequinchallenge) estimator by Google for depth estimation. 
To use the openpose model, you will need to install openpose [(CMU-openpose)](https://github.com/CMU-Perceptual-Computing-Lab/openpose) and have the models in the folder of the script. This is required only for the notebook "Handkeypoints.ipynb".  

The dataset primarily employed is the [SDHA human interaction dataset](https://cvrc.ece.utexas.edu/SDHA2010/Human_Interaction.html) of human actions. The handshake video sequences are used. One video as a sequence of images is given to test the code in the folder 'seq18'. A trimmed version of this video is available in folder 'new' that contains only frames 650-975 (This was added earlier since generating keypoints using openpose for all 2006 frames takes a long time). This is the video 'seq18.avi' of *set2* in the linked dataset. To test code use the folder of images 'data/new'. This has the following,
- RGB images for each frame in *rgb* folder
- Depth images for each frame in *gray* folder
- Hand keypoints of shape (2,num_ppl,21,3) for each frame in *keypoints* folder as numpy arrays.
  - The shape refers to number of hands(ie: left and right), number of people, number of hand keypoints, (x,y coordinates and confidence).
- Body keypoints of shape (num_ppl,25,3) for each frame in *pose* folder as numpy arrays.

The *results* folder has the handshake detected images for the folder *new*.

Run the notebook "Handshake Detection Full.ipynb" to detect handshakes in the given video stream ie:'data/new'. Please ensure you have changed the paths as necessary. The script requires the RGB, depth images, pose and handkeypoint numpy arrays.
