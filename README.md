<h1><b>Hand-Audio Adjuster (macos) </b></h1>

<h2><b>Overview</b></h2>
<p>The <b>Hand-Audio Adjuster</b> is a project that allows you to control the audio volume of your computer through the movements of your index finger and thumb. By measuring the distance between the thumb and index finger tips, the system adjusts the system's volume in real-time.</p>

<h2><b>Libraries Used</b></h2>
<ul>
    <li><b>OpenCV</b>: Used for hand detection and tracking the position of hand landmarks.</li>
    <li><b>HandTrackingModule</b>: A custom module that provides the ability to detect and track hand landmarks, specifically the thumb and index finger tips, to calculate their distance.</li>
    <li><b>AppleScript & Subprocess</b>: For controlling and adjusting the system volume on macOS through command-line OS commands.</li>
</ul>

<h2><b>Features</b></h2>
<ul>
    <li>Real-time hand gesture-based volume control using the index finger and thumb.</li>
    <li>Displays the <b>FPS</b> (Frames Per Second) of the hand detection system for performance monitoring.</li>
    <li><b>Volume bar</b>: Visual display of the current volume level on the screen.</li>
    <li><b>Distance-based control</b>: As the distance between the index finger and thumb changes, the system volume adjusts dynamically.</li>
    <li><b>OS-level volume control</b>: Instead of using external libraries like PyCaw, the volume is adjusted through AppleScript and subprocess calls, offering a native solution for macOS.</li>
</ul>

<h2><b>How It Works</b></h2>
<p>- <b>Hand Detection</b>: Using <b>OpenCV</b>, the webcam captures the live video feed. The <b>HandTrackingModule</b> is used to detect the position of the thumb and index finger tips in the video frame.</p>
<p>- <b>Distance Measurement</b>: The distance between the thumb and index finger tips is calculated using <b>Euclidean distance</b> (via <code>math.hypot()</code>), which determines how far apart the fingers are.</p>
<p>- <b>Volume Control</b>: The distance between the fingers is mapped to a volume range from 0 to 100. Using <b>AppleScript</b>, a subprocess command is run to set the system volume based on this distance.</p>
<p>- <b>FPS Display</b>: The system also displays the <b>FPS</b> of the webcam feed to show how smoothly the hand detection is running in real-time.</p>

<h2><b>Setup & Installation</b></h2>
<pre><code>
$ git clone https://github.com/vardhanzz/HandAudioAdjuster.git
</code></pre>

<p>Once cloned, navigate into the project folder and install the necessary Python libraries:</p>
<pre><code>
$ pip install opencv-python numpy
</code></pre>

<p><b>Note for macOS Users</b>: This project does not use PyCaw for controlling system volume. Instead, it uses <b>AppleScript</b> through the <b>subprocess</b> module to adjust the system volume. Make sure you have <b>osascript</b> available on your macOS device to control the volume using system-level commands.</p>

<h2><b>Usage</b></h2>
<pre><code>
$ python main.py
</code></pre>

<p>Once the webcam starts, position your hand in front of the camera with your thumb and index finger extended. Move your thumb and index finger closer or farther apart to adjust the volume of your system. The current volume will be displayed on the screen in a visual bar.</p>
