wget https://github.com/liamedeiros/ehtplot/archive/refs/heads/master.zip
unzip master.zip -d .
wget https://github.com/achael/eht-imaging/archive/refs/tags/v1.2.7.zip
unzip v1.2.7.zip -d .
pip install pygmo
pip install ehtplot-master
pip install eht-imaging-1.2.7
pip install ./mr_beam/itreg
pip install ./mr_beam/libwise-0.4.7-light
pip install ./mr_beam/MSI
pip install ./mr_beam/imagingbase
pip install ./mr_beam/ga
