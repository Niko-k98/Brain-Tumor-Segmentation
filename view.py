
import h5py
import matplotlib.pyplot as plt
import numpy as np
import glob

img_type= "npz"
# file='data/Synapse/train_npz/case0005_slice020.npz'

data_dir=glob.glob("data/Synapse/train_npz/*.npz")


# Open the HDF5 file
for i,data in enumerate(data_dir):
    npz_file = np.load(data)
    keys=npz_file.files
    dataset = npz_file['image']
    labels=npz_file['label']
    image_data = dataset[:]
    label_data=labels[:]
    
    print("===============================")
    print("image number", i)
    print(data)
    print(label_data.sum())

    # Display the image using matplotlib
    plt.imsave("images/image_{}.png".format(i) ,image_data, cmap='gray')  # Assuming a grayscale image
    plt.imsave("label_viz/label_{}.png".format(i) ,label_data, cmap='gray')  # Assuming a grayscale image
    # plt.axis('off')  # Turn off axis labels
    # plt.show()

# Close the HDF5 file
# h5_file.close()


