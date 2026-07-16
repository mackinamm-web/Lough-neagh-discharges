"""

Lough Neagh Treated Effluent Discharges Tabular Analysis Script

This script loads geospatial datasets for Northern Ireland, filters for Local Management Areas (water catchments) connected to Lough Neagh and identifies treated effluent discharges within those LMAs.

The LMAs included in this analysis are: Lough Neagh, River Blackwater, Upper Bann, 
Moyola, Ballinderry, and Six Mile Water.

For each LMA, the script selects all treated discharges that fall within its boundary and performs a spatial join with Water Framework Directive (WFD) river waterbody polygons to retrieve the corresponding waterbody namespace.

The script produces a tabular list of all Wastewater Treatment Works (WwTWs) that have treated discharges within each of the LMAs, alongside the waterbody (Namespace).

The final output table is saved as a Excel in the Outputs folder: Lough_Neagh_Treated_Discharges.xlsx

"""


# IMPORTS FOR GEOSPATIAL DATA ANALYSIS

import geopandas as gpd
import pandas as pd

# LOAD ANALYSIS LAYERS
lmas = gpd.read_file('../Data/LMAs.shp')
discharges = gpd.read_file('../Data/treated_discharges.shp')
waterbodies = gpd.read_file('../Data/WFD_River_Water_Bodies_2016.shp')

# REPROJECT LAYERS TO COMMON CRS
discharges = discharges.to_crs(lmas.crs)
waterbodies = waterbodies.to_crs(lmas.crs)

# DEFINE LMAs IN THE LOUGH NEAGH CATCHMENT

target_lmas = [
    "Lough Neagh",
    "River Blackwater",
    "Upper Bann",
    "Moyola",
    "Ballinderry",
    "Six Mile Water"
]

# LOOP THROUGH LMAs / PREPARE GEOMETRY FOR SPATIAL FILTERING

results = []

for name in target_lmas:
    lma_poly = lmas[lmas["NAME"] == name]

    if lma_poly.empty:
        print(f"WARNING: LMA '{name}' not found.")
        continue
    
    geom = lma_poly.geometry.union_all()

    
# SELECT DISCHARGES INCLUDE THE LMAs
    subset = discharges[discharges.within(geom)].copy()
    subset["LMA"] = name

    results.append(subset)
    

# COMBINE RESULTS INTO A TABLE
if results:
    combined = pd.concat(results, ignore_index=True)

# SPATIAL JOIN TO ADD NAMESPACE AND BUILD OUTPUT TABLE

    combined = gpd.sjoin(
        combined,
        waterbodies[["namespace", "geometry"]],
        how="left",
        predicate="within"
    )

output = pd.DataFrame({
        "Name": combined["Name"],
        "LMA": combined["LMA"],
        "Namespace": combined["namespace"]
})


# SUMMARY OF DISCHARGES
print("\nSummary of discharges inside selected LMAs:")
print(output)

# TOTAL NUMBER OF DISCHARGES
print("\nTotal number of discharges in selected LMAs:", len(combined))

# NUMBER OF DISCHARGES PER LMA
print("\nNumber of discharges per LMA:")
print(combined["LMA"].value_counts())

# NUMBER OF DISCHARGES PER WATERBODY
print("\nTop 10 waterbodies with the most discharges:")
print(combined["namespace"].value_counts().head(10))


# EXPORT TO EXCEL

output.to_excel("../Outputs/Lough_Neagh_Treated_Discharges.xlsx", index=False)
