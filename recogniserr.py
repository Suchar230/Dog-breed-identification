#%%
from fastai.vision import *

from pathlib import Path
import sys
import os.path


if len(sys.argv) > 1:
	scriptPath = Path(os.path.dirname(os.path.realpath(__file__)))

	modelPath = Path(str(scriptPath.parent) + '\\stanford-dogs-dataset-traintest\\cropped') 
    
	data = ImageDataBunch.from_folder(modelPath, train='train', valid_pct=0.2, size=224, num_workers=0)
	data.normalize(imagenet_stats)
	learner = cnn_learner(data, models.resnet34,  metrics=[accuracy, error_rate])

	learner.load("resnet34-fit5-stage2")

	imgPath = Path(sys.argv[1])
	correct = 0
	wrong = 0

	if os.path.isfile(imgPath):
		img = open_image(imgPath)
		pred_class, pred_idx, outputs = learner.predict(img)
		print(pred_class) 
	else:
		print("bad file") 
else:
	print("No filenaMe") 

# %%