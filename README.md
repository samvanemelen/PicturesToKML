# Pictures to KML

Whether you have an album from a vacation, a field work, a study or any other activity, displaying those images in a spatial context such as Google Earth can be very useful. 

Pictures to KML is a tool that can be placed in a folder and extracts all geo-tagged information from images in that folder. It creates a KML file that can be read by a variety of tools, most commonly Google Earth. The KML Placemarks contain the image itself, the device and the date.

## Files

This repository contains 2 files. The python file constructed to do the operations, and an .exe file. This .exe file is an executable from this python script created with PyInstaller. Just download the .exe file and place it in the folder containing geo-tagged images. Run the file and a KML file will be created.
The python file works in the same way but requires the right modules to be present in your environment. The executable file does not has dependencies.

## Updates and contributions

Feel free to contribute with issues, remarks, improvements of forking this repository. It is not actively being developed but occurring issues or proposed improvements might be incorporated anyway.

## Users guide
![ExeInFolder](https://user-images.githubusercontent.com/36103001/58802011-5f69a780-860c-11e9-9791-34a18d22c3e8.JPG)
First of all, place the executable (or the python script) in the folder containing your images.
![Give a name window](https://user-images.githubusercontent.com/36103001/58802012-5f69a780-860c-11e9-91a0-02a037c28b61.JPG)
When opening the exe file (or running the python script) You are prompted to give a name. This is not the name of the file (Always Output.kml) but the name of the feature group.

![Placing images](https://user-images.githubusercontent.com/36103001/58802009-5ed11100-860c-11e9-9270-d6eb7807bad5.JPG)
after that the code will check all images with geodata and adds those with a location to the KML.

![Done](https://user-images.githubusercontent.com/36103001/58802010-5f69a780-860c-11e9-84b1-e3474e87928f.JPG)
At the end you will see a confirmation and a line telling you how many images were added to the KML file.


![GoogleEarth](https://user-images.githubusercontent.com/36103001/58802013-5f69a780-860c-11e9-88cf-5307bf92c2c3.JPG)
The final result looks something like this. A map with a placemark for each image, with a short description and the image itself.