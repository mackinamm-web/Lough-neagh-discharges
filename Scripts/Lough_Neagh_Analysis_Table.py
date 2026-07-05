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
    "Six Mile Water",
    "Braid and Main"
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


print("\nSummary of discharges inside selected LMAs:")
print(output)

# EXPORT TO EXCEL

output.to_excel("../Outputs/Lough_Neagh_Treated_Discharges.xlsx", index=False)
