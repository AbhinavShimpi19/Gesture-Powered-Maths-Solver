# Hand Gesture Equation Solver
Video Link : https://drive.google.com/file/d/11ciTnVuzuelgZY4KzXl7FPHCpc6KhNR8/view?usp=sharing
## Overview
The **Hand Gesture Equation Solver** is an innovative project that leverages computer vision and machine learning to solve mathematical equations using hand gestures. By capturing gestures in real-time, the system interprets inputs, solves equations, and visualizes results interactively.

---

## Features
- **Real-Time Hand Gesture Detection**: Recognizes hand gestures for mathematical operations and numbers.
- **Equation Solving**: Interprets gestures to form mathematical equations and solves them on the fly.
- **Graph Plotting**: Plots graphs for equations that require visualization.
- **Interactive Interface**: User-friendly interface powered by Streamlit for seamless interaction.

---

## Technology Stack
- **Programming Language**: Python
- **Frameworks**:
  - OpenCV: For real-time gesture recognition
  - Streamlit: For creating an interactive user interface
- **Machine Learning**:
  - MediaPipe: For hand tracking and gesture recognition
  - TensorFlow/Keras: For custom models (if applicable)
- **Visualization**:
  - Matplotlib: For graph plotting
  - NumPy: For mathematical computations

---

## Prerequisites
1. Python 3.8 or higher
2. Libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Webcam or compatible camera for real-time gesture input

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AbhinavShimpi19/Gesture-Powered-Maths-Solver.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Gesture-Powered-Maths-Solver
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. Run the main application:
   ```bash
   streamlit run Socratic.py
   ```
2. Allow access to your camera for real-time hand gesture recognition.
3. Use predefined gestures for:
   - Numbers (e.g., one, two, three...)
   - Operations (e.g., addition, subtraction, multiplication, division)
   - Special commands (e.g., clear, solve, plot)
4. Observe real-time results and visualizations.

---

## Gesture Mapping
| Gesture              | Function                |
|----------------------|-------------------------|
| **One Finger Up**    | Input number `1`       |
| **Two Fingers Up**   | Input number `2`       |
| **Open Hand**        | Addition (`+`)         |
| **Closed Fist**      | Subtraction (`-`)      |
| **Peace Sign**       | Multiplication (`*`)   |
| **Thumbs Up**        | Solve Equation         |
| **Palm Facing Camera** | Clear Input          |

---

## Examples
### Example 1: Solving `3 + 5`
1. Show gestures for `3`, `+`, and `5` in sequence.
2. Gesture `Thumbs Up` to solve.
3. Output:
   - Equation: `3 + 5`
   - Result: `8`

### Example 2: Plotting `y = x^2`
1. Enter equation using gestures.
2. Gesture `Thumbs Up` to solve.
3. Visualize the graph of `y = x^2`.

---

## Contribution
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes and push:
   ```bash
   git push origin feature-branch
   ```
4. Create a Pull Request.


---

## Acknowledgments
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- [Streamlit](https://streamlit.io/)

---

## Contact
For any queries, please reach out to:
- **Author**: Abhinav Shimpi
- **Email**: [abhinavshimpi2005@gmail.com](mailto:abhinavshimpi2005@gmail.com)
- **GitHub**: [AbhinavShimpi19](https://github.com/AbhinavShimpi19)
