from PIL import Image
from net import Siamese

if __name__ == "__main__":

    model = Siamese()

    image1 = './imgs/4/permu12.png'
    image1 = Image.open(image1)

    image2 = './imgs/4/permu7.png'
    image2 = Image.open(image2)

    probability = model.detect_image(image1,image2)
    print('\nProbability:', probability, '\n')