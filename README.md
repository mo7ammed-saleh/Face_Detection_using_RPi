 # Face Detection using OpenCV with Raspberry Pi 
**This Repository will explain my 4th task in Robotics and AI department at [SMART METHODS](https://github.com/smart-methods) summer training.**

## Task Requirements: 
  - Use OpenCV for making a real time face detection and recognition in Raspberry Pi.
  
## Detailed Steps:
1. Configure the Raspbeery Pi to control the controller remotely [(Click Here).](https://www.youtube.com/watch?v=BpJCAafw2qE&t=1201s)

2. Create your Python virtual environment and install NumPy then Compile OpenCV 4 from source [(Click Here for full installation details).](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/)

3. **Camera Test:**
   - Test the camera using this [Code](https://github.com/mo7ammed-saleh/Face_Detection_using_RPi/blob/main/Face_Recognition/Face_Detection/Camera_Test.py) in full details with commenet.
   - Run the virtual environment `workon cv`
   - Open the path file if you have saved your .py file in a directory using `cd` command, in my case I will run the folowing command `cd Face_Recognition/Face_Detection` 
   - Run you camera test file by using `python` folowed by your file name, in my case `python Face_Detection.py`
   - I will use a usb camera as shown in the figure: <p align='left'><img width="45%" src="https://github.com/mo7ammed-saleh/Face_Detection_using_RPi/blob/main/img/Camera_usage.jpg"/>
    </p>
    
   - Tested result will show an image in a Gray and RGB color: <p align='left'><img width="90%" src="https://github.com/mo7ammed-saleh/Face_Detection_using_RPi/blob/main/img/Test_Camera.jpg"/> 

4. **Face Detection:**
   - To recognise a face we should captutre the face (detecte it).The most common way used to detect a face or any objects, is using the ["Haar Cascade classifier"](https://docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html) (It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images).To detect faces the algorithm needs a lot of positive images (images of faces) and negative images (images without faces) to train the classifier. Then we need to extract features from it. OpenCV comes with a trainer as well as a detector. If we want to train our classifier for any object like car, planes etc. we can use OpenCV to create one using ["Cascade Classifier Training"](https://docs.opencv.org/3.3.0/dc/d88/tutorial_traincascade.html).
