# Expected directory structure:

- /
    - 1/
        - original.jpg
    - 2/
        - original.jpg
    - .../
        - original.jpg
    - 40/
        - original.jpg
    - stats.csv
    - test.py

---

# Notes:

- original.jpg contains the image to be processed
- stats.csv contains the stats of each edge detection algorithm performed
- test.py contains the python code to be executed
- ran with `Python 3.6.4`
- this test does not factor the calculation of gaussianBlur

---

# Software deps:

- python
- pip
    - not required, but makes life a lot easier

---

# Python packages:

- numpy
- cv2
- time
- csv

---

# Questions:

- Does our stats need to factor in gaussianBlur for the edge algorithms that use it?
- Do we need to write a project report?
