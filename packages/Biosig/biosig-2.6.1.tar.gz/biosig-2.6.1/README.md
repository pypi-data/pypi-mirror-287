# Biosig Package

Biosig contains tools for processing of biomedical signals
like  EEG, ECG/EKG, EMG, EOG, polysomnograms (PSG). Currently,
it contains import filters of about 50 different file formats
including EDF, GDF, BDF, HL7aECG, SCP (EN1064).

More information is available at
[Biosig project homepage](https://biosig.sourceforge.io)

# Installation:
## GNU/Linux, Unix,
  pip install https://pub.ist.ac.at/~schloegl/biosig/prereleases/Biosig-2.6.1.tar.gz

## MacOSX/Homebrew
  brew install biosig
  pip install numpy
  pip install https://pub.ist.ac.at/~schloegl/biosig/prereleases/Biosig-2.6.1.tar.gz

## MS-Windows
  the biosig extension module is not supported on MS Windoes.
  Instead, it is recommended to use loadgdf.py together with biosig2gdf.exe
  for loading biosig data.

# Usage of the biosig extension module

   import biosig
   import json
   # read header/metainformation
   HDR=json.loads(biosig.header(FILENAME))
   # read data
   DATA=biosig.data(FILENAME)

# Usage of loadgdf (biosig2gdf.exe is strongly recommended)
  loadgdf(filename)

