# intellectus-emotion-detection

# Added new files from https://github.com/muxspace/facial_expressions

# data3.py
# I used pandas to open legend.csv from https://github.com/muxspace/facial_expressions and sorted the data by emotion

# data3png.py
# The imgages from https://github.com/muxspace/facial_expressions were all jpgs, but I needed them to be pngs, so I used opencv to rewrite each image as a png


# sortdata3.py
# The images from https://github.com/muxspace/facial_expressions were all 350 x 350px, and some were not in grayscale, so I used opencv v4.5 to resize them to 48 x 48px and to convert them into grayscale, then added them to the training part of the original dataset, FER-2013 dataset [80/20 train test split]


# If I were to do this project again, I would have used a function in sortdata3.py rather than copy and pasting the same lines of code out a few times
# Further improvements will involve the following: for epoch 50/50 after training, the accuracy for training was  0.8626. whereas the accuracy for validation was 0.9701 which is noticeably higher, and based on this, I suspect that it is overfitting

# Limitations on research
# In order to perfect this project, I will be leveraging the following techniques: https://www.kdnuggets.com/2019/12/5-techniques-prevent-overfitting-neural-networks.html
# Simplifying the model
# Stopping earlier - won't work on this program since from epoch 1, the accuracy for validation was already higher than the accuracy for training
# Augmenting the dataset - I added more images, but did not augment the images themselves
# Use Regularization
# Use dropouts
