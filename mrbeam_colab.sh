wget https://github.com/liamedeiros/ehtplot/archive/refs/heads/master.zip
unzip master.zip -d .
wget https://github.com/achael/eht-imaging/archive/refs/tags/v1.2.7.zip
unzip v1.2.7.zip -d .
pip install pygmo
pip install ./ehtplot-master
pip install ./eht-imaging-1.2.7
pip install ./mrbeam/mr_beam/itreg
pip install ./mrbeam/mr_beam/libwise-0.4.7-light
pip install ./mrbeam/mr_beam/MSI
pip install ./mrbeam/mr_beam/imagingbase
pip install ./mrbeam/mr_beam/ga
