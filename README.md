# Imbricated Colorful Squares 🎨

This project was created as my **final graphics project** for the [Code In Place](https://codeinplace.stanford.edu/) course, offered by Stanford University. It was built using **Python** and the course's custom `graphics.py` library.

The program generates a series of **nested colorful squares**, giving the illusion of depth and symmetry. It demonstrates:

- Use of **functions** to organize and structure the program
- Repeated drawing logic to simulate loop-like behavior
- Application of **random color selection** from a defined palette
- **Geometric alignment** using precise coordinate manipulation

## 🔧 How it Works

- A canvas of size `400x400` pixels is created.
- Squares (rectangles with equal width and height) are drawn from the outer edge toward the center.
- Each square shrinks by `20` pixels from each side, creating a nested effect.
- Colors are randomly picked from a set of vibrant and soft color names using `random.choice()`.

## 🧠 Key Concepts

- `Canvas`: The drawing surface provided by `graphics.py`
- `create_rectangle(x1, y1, x2, y2, color)`: Draws a rectangle using the given coordinates and fill color
- Random color generation using Python’s `random` module
- Manual spacing via increasing margins

## ▶️ How to Run

Make sure you have the project code (`project.py`) and access to the **Code In Place IDE** (or the course-provided environment that includes the `graphics.py` library).

## 🎯 Try It Yourself

Want to see it in action? Run the project directly in the Code In Place IDE:

👉 [Click here to try the prototype](https://codeinplace.stanford.edu/cip3/share/McylTlErjRhbrGLVtDCS)
