# Project - Deploy CNN Image Classifier  
Implement the "Project-Deploy CNN Image Classifier" content of the "[Computer Vision with Embedded Machine Learning](https://www.coursera.org/learn/computer-vision-with-embedded-machine-learning)" course on the microAI project. The model file gets from the [OpenMV](https://github.com/on-device-ai/computer-vision-with-embedded-machine-learning/tree/master/2.5.1%20-%20Project%20-%20Live%20CNN%20Inference/OpenMV) deploy directory. However, the MicroPython script between microAI and OpenMV is incompatible, so we need to write another MicroPython script (such as [ei_image_classification.py](https://github.com/on-device-ai/computer-vision-with-embedded-machine-learning/blob/master/2.5.1%20-%20Project%20-%20Live%20CNN%20Inference/microAI/ei_image_classification.py)) for microAI. For further information, please refer to [DeployEdgeImpulseTutorial.md](https://github.com/on-device-ai/microAI/blob/main/DeployEdgeImpulseTutorial.md).   
Then upload the "trained.tflite" and the written script:  
`adb push trained.tflite /userdata`  
`adb push ei_image_classification.py /userdata`  
Use the following command to execute the script:  
`adb shell micropython /userdata/ei_image_classification.py`  
The script running results are as follows:  
![210929](https://user-images.githubusercontent.com/44540872/135217478-59cb082d-2fa7-437d-b75f-a9babe94e51f.gif)  
