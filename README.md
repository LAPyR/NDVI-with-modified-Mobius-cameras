# Vegetation_indices_with_modified_Mobius_cameras

Here we present the complete process to obtain aerial visible (RGB) and near-infrared (NIR) imagery from a *"dual-spectrum system"* based on: a modified Mobius camera + opensource software. This process is part of a new major version of the research cited as follows:

A. M. de Oca, L. Arreola, A. Flores, J. Sanchez and G. Flores, "Low-cost multispectral imaging system for crop monitoring," 2018 International Conference on Unmanned Aircraft Systems (ICUAS), Dallas, TX, USA, 2018, pp. 443-451, doi: 10.1109/ICUAS.2018.8453426.

The capture process is performed with a Raspberry Pi 3 through the python script "capture.py". Once the imagery is collected we perform the offline following processes:

* Rectification of the imagery to remove distortion: two undistort scripts (one for RGB and other for NIR imagery) are used to rectify the imagery (undistort_inf.py and undistort_nor.py).

* Georeference: the rectified imagery is georeferenced with Mission Planner using the log file of the flight. This process is done extracting GPS coordinates from   the image captures during the flight (https://ardupilot.org/planner/docs/mission-planner-installation.html).

* Orthomosaic reconstruction: we do it uploading the gerectified imagery to OpenDroneMap (https://www.opendronemap.org/webodm/download/).

* Reflectanctance calibration: once the RGB and NIR orthomosaics are obtained through OpenDroneMap, their pixel intensities are converted to reflectance. Specifically for this process, it is needed a Calibration Reflectance Panel (CRP) as the one for the RedEdge-M from Micasense. Such CRP is.used to calibrate imagery with provided reflectance values for each band. The calibration is done individually each bands and saved as new orthomosaics. After that, these orthomosaics are also aligned. (calibration.py)

* Computation of vegetation indices (NDVI, EVI, OSAVI, GCI, GVI, MCARI1) with RGB and NIR imagery from the *dual-spectrum system* (getndvi.py).


Andrés Montes de Oca <br />
PhD. Student. <br />
andresmr@cio.mx 
