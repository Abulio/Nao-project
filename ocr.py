import pytesseract
import sys
import time
from naoqi import ALProxy
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'E:/Programs/Tesseract-OCR/tesseract'

def SaveImage(IP,Port):
      camProxy = ALProxy("ALVideoDevice", "155.245.20.83", 9559)
      resolution = 2    # VGA
      colorSpace = 11   # RGB

      videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)

      t0 = time.time()

      # Get a camera image.
      # image[6] contains the image data passed as an array of ASCII chars.
      naoImage = camProxy.getImageRemote(videoClient)

      t1 = time.time()

      # Time the image transfer.
      print "acquisition delay ", t1 - t0

      camProxy.unsubscribe(videoClient)


      # Now we work with the image returned and save it as a PNG  using ImageDraw
      # package.

      # Get the image size and pixel array.
      imageWidth = naoImage[0]
      imageHeight = naoImage[1]
      array = naoImage[6]

      # Create a PIL Image from our pixel array.
      im = Image.frombytes("RGB", (imageWidth, imageHeight), array)

      # Save the image.
      im.save("camImage.png", "PNG")

      im.show()
      print(pytesseract.image_to_string(Image.open('camImage.png')))



if __name__ == '__main__':
      IP = "nao.local"  # Replace here with your NaoQi's IP address.
      PORT = 9559

      # Read IP address from first argument if any.
      if len(sys.argv) > 1:
        IP = sys.argv[1]

      naoImage = SaveImage(IP, PORT)

