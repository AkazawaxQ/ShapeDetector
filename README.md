# Real-Time Shape, Color, Area & Perimeter Detection using OpenCV
This project is a Python-based real-time computer vision application that detects the shape, color, area, and perimeter of objects using a standard webcam. Leveraging the power of OpenCV and NumPy, the system analyzes live video frames to identify geometric features and display them directly on screen with visual feedback.

📸 **Features**  
✅ Real-time object detection from webcam feed  
🟢 Shape recognition: Triangle, Rectangle, Square, Pentagon, Hexagon, Circle  
🎨 Color identification: Red, Yellow, Green, Blue, Purple  
📐 Geometric calculations: Area and perimeter of each detected object  
🧾 Annotates each object with its:
  - Shape
  - Color
  - Area (in pixels)
  - Perimeter (in pixels)

🔧 **Technologies Used**
- Python 3.x
- OpenCV for image processing and contour detection
- NumPy for array and numerical operations
- HSV color space for more accurate color detection

🖥️ How It Works  
1.Webcam Capture:  
  - The program reads video frames using cv2.VideoCapture(0).  

2.Preprocessing:  
  - Converts frames to grayscale, applies Gaussian Blur, then performs Canny Edge Detection.  
  - Converts original frame to HSV color space for color analysis.

3.Contour Detection:  
  - Uses cv2.findContours to detect external shapes.  
  - Ignores small contours using an area threshold.

4.Shape Classification:  
  - Analyzes the number of edges using cv2.approxPolyDP.  
  - Uses aspect ratio to differentiate between squares and rectangles.  

5.Color Classification:  
  - Uses the hue component of HSV to classify general color families.  

6.Visual Output:  
  - Annotates detected shapes with their name, color, area, and perimeter.  
  - Displays everything in a separate window titled "Shape".  

📌 Notes
-  The program uses basic thresholding and heuristics, and is designed as a simple educational prototype.
-  The accuracy can vary depending on lighting, object positioning, and camera resolution.
-  For more robust detection, future improvements could include:
  - Deep learning models
  - More advanced color classification (LAB color space, clustering)
  - Object tracking between frames
