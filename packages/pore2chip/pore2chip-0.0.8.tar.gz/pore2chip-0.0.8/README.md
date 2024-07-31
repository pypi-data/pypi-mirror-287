# Pore2Chip: All-in-One Python Tool for Soil Microstructure Analysis and Micromodel Design

## What is Pore2Chip?
Pore2Chip is a Python module designed to streamline the process of analyzing X-ray computed tomography (XCT) images of soil and creating 2D micromodel designs based on that analysis. It leverages the power of open-source libraries like OpenPNM, PoreSpy, and drawsvg to  extract key information about the soil's porous structure and translate it into a blueprint for microfluidic simulations or physical "lab-on-a-chip" devices developed using additive manufacturing.

### A workflow for model-data-experiment design:

Below is a conceptual figure and vision for this all-in-one Python tool. The working principle starts with XCT imaging files, which will be characterized for soil structure-property relationships and then transformed into a 2D rendering applicable to pore-scale micromodel building. Micromodel experiments will then be used with PFLOTRAN/OpenFOAM/PINNs process models to simulate flow and reactive-transport for calibration and V&V.

## What the module can do? Capability summary:
* Extract pore sizes and pore throat sizes
* Extract pore connectivity numbers
* Get miscellaneous pore information such as feret diameters
* Generate a micromodel design that is representative of input XCT soil data
* Export the design as an SVG file
* Export design as a DXF file (see DXF section)

### Unveiling the Hidden World of Soil: Pore Structure Analysis

Pore2Chip empowers you to delve into the intricate details of soil microstructure by:

* **Quantifying Pore Sizes and Throats:**  It precisely measures the size distribution of pores and pore throats within the soil sample. This information is crucial for understanding fluid flow properties and transport phenomena within the soil.
* **Mapping Pore Connectivity:**  Pore2Chip calculates the number of connections between pores, providing valuable insights into how fluids can move through the soil network.
* **Extracting Diverse Pore Metrics:**  In addition to size and connectivity, Pore2Chip can extract various other pore characteristics, such as feret diameters (the greatest distance a pore can span in a specific direction).

### Bridging the Gap: From Soil Data to Microfluidic Designs

Pore2Chip goes beyond analysis by translating the extracted data into actionable outputs:

* **Micromodel Design Generation:**  Based on the characterization of the soil's pore network, Pore2Chip generates a 2D blueprint that closely resembles the actual pore structure. This design serves as a foundation for microfluidic simulations or the fabrication of physical micromodels using Photolithography or Laser Etching.
* **SVG File Export:**  The micromodel design is exported in a versatile SVG (Scalable Vector Graphics) format, ensuring compatibility with various simulation software and design tools.
* **DXF Export (Optional):**  For users working with computer-aided design (CAD) programs, Pore2Chip can optionally export the design in DXF (Drawing Exchange Format)  facilitating integration into CAD workflows (Note:  DXF export functionality may require additional configuration).

In essence, Pore2Chip offers a comprehensive solution for researchers and engineers working with soil microstructures. It efficiently bridges the gap between XCT data and micromodel development, paving the way for a deeper understanding of soil behavior and the creation of advanced microfluidic devices for diverse applications.

## Getting Started
The OpenPNM and PoreSpy libraries are required to analyze XCT images. PoreSpy is used to generate a pore network that is used to extract pore size distribution, pore throat size distribution, and pore coordination numbers. OpenPNM is used to construct a new 2D pore network that will be used to create the micromodel design.

Example input images can be found in the "bean_bucket_100" folder. Full dataset can be found here: https://github.com/EMSL-MONet/CommSciMtg_Nov23/

Install using PiP:
```
pip install pore2chip
```
Install from source:
```
git clone https://github.com/aramyxt/Pore2Chip.git 
cd Pore2Chip
python3 -m build
python3 -m pip install pore2chip --no-index --find-links dist/
```

Creating a Conda environment:
```
conda create -n pore2chip python=3.8
conda activate pore2chip
pip install pore2chip
```

Building a Docker Image with Jupyter Notebook:
```
git clone https://github.com/aramyxt/Pore2Chip.git 
cd Pore2Chip
docker build -t pore2chip
docker run -p 8888:8888 pore2chip
```
This should output URLs that you can copy and paste into a browser so that you can access the Jupyter Notebook server.

## Example Usage
In the following examples, pore and throat diameters as well as coordination numbers are hard coded values. These values can be extracted from XCT images using the ```metrics``` library.
```
from pore2chip import generate, export

# Shape of the micromodel (number of pores n x n).
n = 5
# Random values for pore, throat diameters and coordination numbers. Can be any length.
arr_pore = [4.0, 9.0, 4.5, 8.4, 14.0, 7.6, 5.0]
arr_throat = [7.0, 5.5, 3.5, 1.4, 5.8, 4.3, 8.8, 8.4, 4.0]
arr_coord = list(range(0, 4))

network = generate.generate_network(n, arr_pore, arr_throat, arr_coord)

design = export.network2svg(network, n, 100)

design.save_svg('network.svg')
```
![output](https://github.com/aramyxt/XCT_to_Micromodel/blob/main/example_outputs/network_from_values.svg)

This package can also generate images without throats and simulate "pores" as "grain" particulates.
```
from pore2chip import generate, export

# Shape of the micromodel (number of "grains" n x n).
n = 5
# Random values for pore, throat diameters and coordination numbers. Can be any length.
arr_grain = [4.0, 3.0, 4.5, 2.4, 14.0, 7.6, 5.0]

network = generate.generate_network(n, arr_grain, None, None)

design = export.network2svg(network, n, 100)

design.save_svg('grain_network.svg')
```
![output2](https://github.com/aramyxt/XCT_to_Micromodel/blob/main/example_outputs/grain_network.svg)

## Converting to PNG
There are many ways to convert an SVG image to a rasterized image format using only Python, such as rendering it using```CairoSVG```.
The recommended way to do this is to use ```svglib``` and ```reportlab```. NOTE: ```reportlab>=4.0.0``` requires ```pycairo```, and by extension, the ```cairo``` library, which cannot be installed by PiP by itself. If you are using Windows, it is recommended to install ```reportlab=3.6.13```.
```
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

rldrawing = svg2rlg('network.svg')
renderPM.drawToFile(rldrawing, 'network.png', fmt='PNG')
```

## Micromodel design -- Getting an STL from the SVG for additive manufacturing 
This is a generalized workflow for getting an SVG to an STL file:

1. Generate the svg using Pore2Chip
2. Use a vector image program such as Inkscape to combine all paths into one path. In Inkscape, this would be ```Paths -> Union```
3. Export the new image as a .DXF file
4. Import the DXF file into the CAD software of your choosing, such as FreeCAD
5. Extrude the shape of the pores and use it as a negative to create the micromodel
6. Export to STL

Example result in Solidworks:
![solidworks_ex](https://github.com/aramyxt/XCT_to_Micromodel/blob/main/example_outputs/cad_mockup2.PNG)

There are many other methods to print the micromodel design onto physical materials.

It is highly recommended to try the Python library ```svglob``` to combine SVG paths without using an external program:
https://github.com/deckar01/svglob/tree/master

Alternatively, ```stl_tools``` can be used to turn a rasterized image into an STL:
https://github.com/thearn/stl_tools

## DXF Exporting
While the ```export``` module can export a DXF file, it can only create pores as circles. It is recommended to export the micromodel as an SVG file and make desired adjustments to it. 
This way, you have more control over the shape and can then convert the SVG to a DXF file.

## For EMSL Tahoma Users
To use the library with Tahoma Open OnDemand:
1. Start a Jupyter Notebook instance in the EMSL OnDemand dashboard
2. Create a Python virtual environment in the terminal
3. Install Pore2Chip in the virtual environment
4. In Jupyter Notebook, set your kernel to your python environment

For more information, see [user guide for EMSL Open OnDemand](https://www.emsl.pnnl.gov/MSC/UserGuide/ood/overview.html)

## Known Issues
* The Feret module will rarely throw an error on some images. Being worked on.

## Work in Progress
* The ability to import and export pore networks in CSV or VTK file formats needed for multi-physics process modeling (e.g., using PFLOTRAN)
* Physics-informed machine learning needed for flow, thermal, and reactive-transport modeling (e.g., physics-informed neural networks)
* Meshfiles needed for CFD modeling (e.g., using OpenFOAM)
* GUI for the Docker container

Example visualization of micromodel with mesh in ParaView:


## Example Jupyter notebooks (basic and advanced usage):
* Example-1: Micromodel Creation from 50 x 50 XCT Data
* Example-2: Micromodel Creation from 100 x 100 XCT Data
* Example-3: Micromodel Pore Stats Using PoreSpy
* Example-4: Flow and transport simulations on micromodels using Physics-informed Neural Network
* Example-5: Flow and transport simulations on micromodels using PoresPy
* Example-6: VTK exports for visualization of micromodel in Paraview

## Authors
* Aramy Truong (lead-developer), EMSL (<aramy.truong@pnnl.gov>)
* Maruti Mudunuru (co-developer), PNNL (<maruti@pnnl.gov>)
* Erin Rooney, USDA (<erin.rooney@usda.gov>)
* Arunima Bhattacharjee, EMSL (<arunimab@pnnl.gov>)
* Tamas Varga, EMSL (<tamas.varga@pnnl.gov>)
* Lal Mamud, PNNL (<lal.mamud@pnnl.gov>)
* Xiaoliang (Bryan) He, PNNL (<xiaoliang.he@pnnl.gov>)
* Anil Krishna Battu, EMSL (<anilkrishna.battu@pnnl.gov>)
* Satish Karra, EMSL (<karra@pnnl.gov>)

## Development and questions
We welcome your contributions to Pore2Chip! This includes bug reports, bug fixes, improvements to the documentation, feature enhancements, and new ideas. 

**Copyright Guidelines:**

To ensure the project's overall licensing remains compatible, please keep the following in mind:

* **Datasets:** Avoid including datasets with restricted licenses that don't allow free use or modification. These can create conflicts with the project's license.
* **Code snippets:** Avoid using code snippets with restricted licenses that don't allow free use or modification.

**Contributing to Pore2Chip:**

We appreciate all contributions, big or small! Here's how to get involved:

* **Fork the repository and create a pull request:** This is the preferred method for contributing code changes.
* **Contact Aramy Truong (<aramy.truong@pnnl.gov>) and/or Maruti Mudunuru (<maruti@pnnl.gov>):** If you have questions or need help getting started.

Additionally, your contributions can be as simple as:

* Fixing typos
* Implementing a new feature calculator
* Developing a novel feature selection process

**No matter your skill level, your help is valuable!**

## Acknowledgements
This research was performed on a project award (Award DOIs: 10.46936/ltds.proj.2024.61069/60012423; 10.46936/intm.proj.2023.60674/60008777; 10.46936/intm.proj.2023.60904/60008965) from the Environmental Molecular Sciences Laboratory, a DOE Office of Science User Facility sponsored by the Biological and Environmental Research program under contract no. DE-AC05-76RL01830.

## Disclaimer
This research work was prepared as an account of work sponsored by an agency of the United States Government. Neither the United States Government nor any agency thereof, nor any of their employees, makes any warranty, express or implied, or assumes any legal liability or responsibility for the accuracy, completeness, or usefulness of any information, apparatus, product, or process disclosed, or represents that its use would not infringe privately owned rights. Reference herein to any specific commercial product, process, or service by trade name, trademark, manufacturer, or otherwise does not necessarily constitute or imply its endorsement, recommendation, or favoring by the United States Government or any agency thereof. The views and opinions of authors expressed herein do not necessarily state or reflect those of the United States Government or any agency thereof.
