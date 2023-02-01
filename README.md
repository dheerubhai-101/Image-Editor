# Image-Editor

I implemented a menu-driven image scanner using the NumPy library which will execute functions as given below.

* **def crop(image, dist1, dist2, dist3, dist 4)**: To crop the given image and where dist1, dist2, dist3, dist 4 are the
distances from left edge, bottom edge, right edge and top edge
respectively in pixels.

![image](https://user-images.githubusercontent.com/83055325/216031476-a28dbfa5-5d56-4bcc-89ba-2b91cb0f44d5.png)
![reference](https://user-images.githubusercontent.com/83055325/216030403-cd213bcb-538a-404e-8082-518505ca18f9.jpg)


* **def rgb2gray(image)** :
To convert an rgb image to gray

![image](https://user-images.githubusercontent.com/83055325/216031558-146d3a83-5df0-445e-ab25-d3c2b9e482cd.png)

* **def threshold(image, threshold)**:
To perform binary thresholding on an image to only view the dark written
text part.
![image](https://user-images.githubusercontent.com/83055325/216031599-33ecb55c-32dd-4640-b363-fc2af2c6e4b3.png)

* **def resize(image, x_scale, y_scale)**:
To resize the image and where x_scale and y_scale are the scaling factors
along the x and y axes respectively.

![image](https://user-images.githubusercontent.com/83055325/216031650-ae80d8f0-4ecc-4dae-8483-99564310f294.png)

* **def combo(image1, image2, orientation)**:
To combine two images together in an orientation specified by the input.
Orientation should be of two types: the two input images can be combined
in either Left-Right or Top-Bottom manner.
Example: Left-Right - image1 on the left part, image2 on the right part of
the image. Both will combine in this manner and give one single image.
Similarly for Top-Bottom where image1 on top and image2 below.

![image](https://user-images.githubusercontent.com/83055325/216032103-e67336fb-ff2e-4a9b-ba7f-2c0b4d2bdd31.png)

* **def rotate(image, direction)**:
To rotate the image where direction = ‘clockwise’ or ‘anticlockwise
![image](https://user-images.githubusercontent.com/83055325/216031693-eaa48617-c354-4f81-8133-19fef2dc9ed4.png)

* **rotate_at_angle(image, direction, angle)**: rotates the
image at an angle in the given direction.
![image](https://user-images.githubusercontent.com/83055325/216031744-c65f47f0-2de3-46c9-9d76-26c27def7b7c.png)

![image](https://user-images.githubusercontent.com/83055325/216032398-1eb2fa3d-1165-4d32-857a-a7c4530a30b3.png)
