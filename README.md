<img src="/img/logo.png" height="300">
ALF is a virtual line follower vehicle written in python and trained using keras. It uses the pybullet physics engine.

Installation
---------------------
Assuming you already have python3 and pip (pip3 on certain Linux distributions), you'll also need the following packages in order for ALF to work:
+ tensorflow
+ keras
+ pybullet
+ rtree
+ matplotlib

To get them, use the following command
```
pip install tensorflow keras pybullet rtree matplotlib
```
Or, on Linux
```
pip3 install tensorflow keras pybullet rtree matplotlib
```

For the rtree module, you'll also need libspatialindex-c. On __Linux__, you can get it using your package manager. On __Windows__, you can get it from [here](https://libspatialindex.github.io/). Once you've downloaded the files, place them in the Python rtree module folder.

Using Alf
---------------------
In the following examples I'm gonna assume you're using Linux. It works about the same on Windows. 
1. Open a terminal in the alf-ml directory
2. Run `python3 -i training_grounds.py` and drive around a bit in order to gain data. This data will later be used for training, so be careful and drive nice. Be careful: it gets a lot of data very fast, so you might want to tinker with that aswell.
3. Once we have enough data, we can run `python3 process_data.py` in order to get it in a nice format. This does most of the math (calculates which road point is the closest to which sensor, etc). It was done in this fashion because I couldn't get data fast if I processed it on the fly aswell, since my laptop wasn't very fast.
4. Run `python3 network_train.py`. This will train the network, so you want to tinker with this and try out different neural network layouts.
5. Once we're done training, we can check how well the bot is doing using the current network by running `python3 testdrivenet.py`

Using your own road
---------------------

<img src="/img/road_corners.png" height="300">

Using your own road is now easier than ever! In the `road/` directory, you can find an example road file names `blender_road.txt`. The basic layout is:
* First line has a single int indicating the total number of road points
* The rest of the lines are road points

The coordinates must be contained in a box from (-15, -15) to (15, 15) as shown in the image above. You can create the roads in blender aswell, using [this guide](https://blender.stackexchange.com/questions/510/how-can-i-duplicate-a-mesh-along-a-curve) and `road/curve2road.py` script (it needs to be in the Blender folder).
Aditionally, you can create the road in a program of your choice, and just output the coordinates. Put the coordinates (unscaled) in a text file, first line being your number of road points and use `python3 scale_road.py -i <input file> -o <output file>` to scale them in order to fit the map.
