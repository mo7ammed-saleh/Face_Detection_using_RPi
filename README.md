 # Face Detection using OpenCV with Raspberry Pi 
**This Repository will explain my 4th task in Robotics and AI department at [SMART METHODS](https://github.com/smart-methods) summer training.**

## Task Requirements: 
  - Use OpenCV for making a real time face detection and recognition in Raspberry Pi.
  
## Detailed Steps:
1. Configure the Raspbeery Pi to control the controller remotely [(Click Here).](https://www.youtube.com/watch?v=BpJCAafw2qE&t=1201s)

2. Create your Python virtual environment and install NumPy then Compile OpenCV 4 from source [(Click Here for full installation details).](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/).

3. Test the camera using this [Code](https://github.com/mo7ammed-saleh/Face_Detection_using_RPi/blob/main/Face_Recognition/Face_Detection/Camera_Test.py) in full details with commenet.
  * Run the virtual environment `workon cv`
  * Open the path file if you have saved your .py file in a directory using `cd` command, in my case I will run the folowing command `cd Face_Recognition/Face_Detection` 
  * Run you camera test file by using `python` folowed by your file name, in my case `python Face_Detection.py`
  * I will use a usb camera as shown in the figure: <p align='left'><img width="45%" src="https://github.com/mo7ammed-saleh/Face_Detection_using_RPi/blob/main/img/Camera_usage.jpg"/>
    </p>
  * Tested resut will show an image in a gray and rgb color: <p align='left'><img width="90%" src="https://github.com/mo7ammed-saleh/Face_Detection_using_RPi/blob/main/img/Test_Camera.jpg"/> 

4. 
