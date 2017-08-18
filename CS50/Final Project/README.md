C. elegans Vital Status Classifier
===

Background
---
This program is a C. elegans live/dead slide classifier. Using curvature measurments of each worm, the program classifies the entire slide as live or dead.

Data was obtained from the [Broad Bioimage Benchmark Collection][1].

Method
---
The program begins by using [OpenCV][2] to read in an slide image as greyscale, applies a [Gaussian blur][3], applies an adaptive Gaussian threshold, binarizes the image, and denoises the slide image. [Canny edge detection][4] is applied to the processed image. The canny edges are then converted into contours.

Using an [approximation to curvature][5], we calculate the curvature between each point for every contour. We then classify the image based on the number of high curvature points based on thresholds established from a training set of prelabeled live and dead image sets.

Benchmark
---
**Training Set**
Live: 20/30 (66.7%)

Dead: 21/26 (80.8%)
**Testing Set**
Live: 14/22 (63.4%)

Dead: 11/19 (57.9%)
**Overall**
Train: 41/56 (73.2%)

Test: 25/41 (61.0%)

[1]: https://data.broadinstitute.org/bbbc/BBBC010/
[2]: http://opencv.org/
[3]: https://en.wikipedia.org/wiki/Gaussian_blur
[4]: https://en.wikipedia.org/wiki/Canny_edge_detector
[5]: https://en.wikipedia.org/wiki/Curvature#Local_expressions
