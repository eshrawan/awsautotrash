# awsautotrash

The municipality in my city, Mumbai, India, recently introduced a legislation making the separation of dry and wet waste obligatory in December 2017. Since the citizens have been used to not following this kind of arrangement in years, they are either not aware of the different categories or they do not care enough about it. The way to recitfy this is through awareness campaigns like the government is doing, but it increases the workload for building complexes such as mine.

Each complex within the city has been given the responsibility of composting their own wet waste for domestic use. After investing in the compost machines, because of faulty segregation, the machines have to be constantly repaired. The complex also hired three workers who individually sort through all the waste that the complex produces so that the heavier loss of fixing the machine is not incurred.


      awsautotrash/PHOTO-2018-04-16-19-25-48.jpg
    

At around this time, I was studying building machine learning skills using online services such as TensorFlow and AWS Rekognition. Intially, I began creating the software for recognition of images using TensorFlow but it presented a huge problem. I wanted my setup to be cost effective, and hence I had chosen the RaspberryPi3 to host the code, but it took over 30 seconds for each image to process, and had no scope of increasing density of objects for recognition upon implementation.

(for trial Tensorflow implementation see https://github.com/eshrawan/trash-sorting)

Hence, I decided to use then the AWS Rekognition software, which then porcessed images at an average of 5.6 seconds on repeated testing (files attached in repository). Fo creating a prototype model, I created a conveyor as in the image below. It consists of a motor which can turn clockwise (for wet waste) and anticlockwise (for dry waste). A servo was later attached to classify the reject waste (such as medicinal waste). All the holders for the motor, servo and the conveyor were designed using OpenSCAD and 3D-printed.

The project has further scope in handling a larger density of objects. The image recognition is at its nascent stage, where it cannot recognize the texture of objects, but with repeated testing and learning, it could also be implemented.I also think that instead of holding a databse on the RPi, connecting an online updating database could be made, with which either sofware (TensorFlow or AWS) could work without much change in the implementable code. 
