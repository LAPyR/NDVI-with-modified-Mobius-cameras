# NDVI-with-modified-Mobius-cameras

Here is presented scripts for rectification, calibration and computation of NDVI with RGB and NIR imagery from Mobius cameras

* First, two undistort scripts are used to rectify RGB and NIR imagery. (undistort_inf.py and undistort_nor.py)

* Once the RGB and NIR orthomosaics are obtained through OpenDroneMap, these are calibrated. Calibration is done individually to red and near-infrared bands and saved as new orthomosaics (Red and Near-infrared). After that, these orthomosaics are aligned. (calibration.py)

* Finally, the NDVI can be computed. (getndvi.py)

andresmr@cio.mx
Andrés Montes de Oca
PhD student.
CIO.
