# Identifying Treated Wastewater Discharges to Lough Neagh Catchments
- Python-based analysis of Wastewater Treatment Works (WwTWs) treated effluent discharges into the Lough Neagh catchment.  
- The workflow identifies discharge points within Local Management Areas (LMAs) that drain to Lough Neagh and produces both map and tabular outputs.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/mackinamm-web/Lough-neagh-discharges.git
cd Lough-neagh-discharges
```

### 2. Create the Conda environment
```bash
conda env create -f environment.yml
conda activate loughneagh
```

### 3. Input datasets
All required spatial datasets are included in the `Data/` directory:

- NI_outline.shp  
- Water.shp  
- LMAs.shp  
- treated_discharges.shp  
- WFD_River_Water_Bodies_2016.shp

## Running the notebook

Launch Jupyter Lab:

```bash
jupyter lab
```

Open the Lough_Neagh_Discharge_Analysis.ipynb notebook and run the cells in order.  

The workflow will:

- load and reproject spatial datasets;  
- select LMAs draining to the Lough Neagh catchment;
- identify treated effluent discharges within those LMAs;  
- generate a Cartopy map of discharge points; and
- create Excel output listing all treated effluent discharges within the Lough Neagh wider catchment.

Outputs are saved to the `Outputs/` directory:

- Map of Lough Neagh Treated Discharges.png
- Lough_Neagh_Treated_Discharges.xlsx

## Project structure

```text
├── Data/                 # Input shapefiles used in the analysis
├── Notebooks/            # Jupyter notebook for mapping and tabular analysis
│   └── Lough_Neagh_Discharge_Analysis.ipynb
├── Outputs/              # Generated output map and Excel table
├── Scripts/              # Python scripts for mapping and tabular processing
├── .gitignore            # Ignore rules for temporary, system, and cache files
├── LICENSE               # Project license
├── README.md             # This file
└── environment.yml       # Conda environment specification
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
This means anyone is free to use, copy, modify, merge, publish, distribute, or build upon the code, provided they include the original licence notice.
