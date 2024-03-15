import cv2
import os

def resize_image(image, width=None, height=None):
    if width is None and height is None:
        return image
    dim = None
    (h, w) = image.shape[:2]

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized

def threshold_image(image, threshold_value=127, max_value=255):
    _, thresholded = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)
    return thresholded

def main():
  
    image_path = "image.jpg"
    if not os.path.isfile(image_path):
        print("Image file not found.")
        return
    image = cv2.imread(image_path)


    resized_image = resize_image(image, width=400)

   
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

  
    thresholded_image = threshold_image(gray_image)

 
    cv2.imshow("Original Image", resized_image)
    cv2.imshow("Thresholded Image", thresholded_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
