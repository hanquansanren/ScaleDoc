**DocW** Dataset Description Document

**Access Link:** https://drive.google.com/file/d/1-bb7dni9CANLQXznWAXBmbCV0vYtiJ5B/view?usp=drive_link

**Dataset Description:** This dataset currently contains 1000 document images of varying scales. In this project, it is used to train the scale stage network to achieve background removing.
The image naming format is <**DocumentID**>_<**Number1-6**> copy.png. For example: 1_1 copy.png

The meanings of numbers 1-6 are as follows:

+ 1: Warped document image
+ 2: The document occupies almost the entire image (proportion = 1)
+ 3: The document occupies 50% of the entire image (proportion = 0.5)
+ 4: The document occupies 25% of the entire image (proportion = 0.25)
+ 5: The document occupies 12.5% of the entire image (proportion = 0.125)
+ 6: The document occupies 6.25% of the entire image (proportion = 0.0625)
+ gt: The ground truth(scanned document)