# Harris-Corner-Detection
Implementation of Simple Harris Corner Detection Algorithm in Python.\
This script was provided by me to the students during ACM Winter School held at IISER Pune in December 2019 to introduce and demonstrate them the topic of feature detection from the image and how a simple but most important feature like corner is detected using this implementation.\
This is based on paper [A Combined Corner and Edge Detector](http://www.bmva.org/bmvc/1988/avc-88-023.pdf) by Chris Harris.\
The naming convention in the script is as per the equation provided in the paper for easy reference and relatability.

## Usage
''' python find_harris_corners.py ./images/ex1.png --k 0.05 --window_size 5 --threshold 10000 '''

### Input
The script requires one positional argument and 3 optional parameters:
* image_path - Complete path to the image file for corner detection.
* k - Harris corner constant which is usually between 0.04 - 0.06.
* window_size - Size of the sliding window for the windowing function.
* threshold - The value of Harris response function above which to consider as corner candidate.

### Output
The output of the script would be two files:
* corners_list.txt - File containing list of corner position and response value in x, y, r format.
* corners_img.png - Image with corners marked in red color.

## Limitation
As of now the script is able to detect corners formed by perpendicular intersections very effectively but for slant lines as in sample images ex3 to ex7 we detect many unwanted corners due to change in intensities in local neighbourhood.\
A post-processing for calculating local minima and maxima is required to address this issue and detect the corners more effectively.

Sample Input Image             |  Sample Output Image
:-----------------------------:|:-----------------------------:
![Sample Input Image](/images/ex1.png)  |  ![Sample Output Image](/images/output_ex1.png)
:-----------------------------:|:-----------------------------:
![Sample Input Image](/images/ex2.png)  |  ![Sample Output Image](/images/output_ex2.png)
