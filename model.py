from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import os
import glob
import shutil


def get_class(model, labels, image):
  np.set_printoptions(suppress=True)

  model = load_model(model, compile=False)

  class_names = open(labels, "r").readlines()

  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

  image = Image.open(image).convert("RGB")

  size = (224, 224)

  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

  image_array = np.asarray(image)

  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

  data[0] = normalized_image_array

  # Przewiduje model

  prediction = model.predict(data)

  index = np.argmax(prediction)

  class_name = class_names[index]

  confidence_score = prediction[0][index]


  bin = class_name[2:].strip()

  if bin == 'Yellow':

    msg = 'W ciągu ostatnich dziesięciu lat wyprodukowaliśmy więcej plastiku niż w całym ubiegłym stuleciu.'
    
    source="."
    destination = "yellow_bin"

    for jpgFile in glob.glob(os.path.join(source, "*.jpg")):
      if os.path.isfile(jpgFile):
          shutil.move(os.path.abspath(jpgFile), destination)

  if bin == 'Green':

    msg = 'Szkło należy do surowców wtórnych - można je przetwarzać wielokrotnie. Jest to nie tylko ekologiczne, ale i ekonomiczne. Oprócz oszczędności surowców, recykling szkła na dużą skalę oznacza tworzenie miejsc pracy i napędzanie gospodarki. Według szacunków ekonomistów, oddanie do recyklingu 1000 ton szkła oznacza utworzenie około ośmiu miejsc pracy.'
    
    source="."
    destination = "green_bin"

    for jpgFile in glob.glob(os.path.join(source, "*.jpg")):
      if os.path.isfile(jpgFile):
          shutil.move(os.path.abspath(jpgFile), destination)


  if bin == 'Blue':
    
    msg = 'Recykling jednej tony papieru to oszczędność 20 drzew, 20 tysięcy litrów wody i 30 kg zanieczyszczeń powietrza.'
    
    source="."
    destination = "blue_bin"

    for jpgFile in glob.glob(os.path.join(source, "*.jpg")):
      if os.path.isfile(jpgFile):
          shutil.move(os.path.abspath(jpgFile), destination)


  if bin == 'Brown':
    
    msg = 'Odebrane z naszych gospodarstw domowych śmieci biodegradowalne trafiają zazwyczaj do biogazowni lub kompostowni, gdzie zostają przetworzone na energię lub żyzny kompost.'
    
    source="."
    destination = "brown_bin"

    for jpgFile in glob.glob(os.path.join(source, "*.jpg")):
      if os.path.isfile(jpgFile):
          shutil.move(os.path.abspath(jpgFile), destination)

  return bin, confidence_score, msg, jpgFile



