# Identifying Treated Wastewater Discharges to Lough Neagh Catchments
Python-based analysis of Wastewater Treatment Works (WwTWs) treated effluent discharges into the Lough Neagh catchment.  
The workflow identifies discharge points within Local Management Areas (LMAs) that drain to Lough Neagh and produces both map and tabular outputs.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/mackinamm-web/Lough-neagh-discharges.git
cd Lough-neagh-discharges

### 2. Create the Conda environment
```bash
conda env create -f environment.yml
conda activate loughneagh

### 2. Input Datasets
All required spatial datasets are included in the Data/ directory:
-NI_outline.shp
-Water.shp
-LMAs.shp
-treated_discharges.shp
-WFD_River_Water_Bodies_2016.shp
