import arcpy
from arcpy import env

env.workspace = r"\\cepfile2\users4\jinwan\Home\Desktop\170033_Building_Footprint_3TM_2D\3d models\data"

neighbourhood_data_file = "Neighbourhoods_2019.shp"

in_features = "170033_Building_Footprint_3TM_2D.shp"
clip_features = "Neighbourhoods_2019.shp"
selected_clip_features = "temp\selected.shp"
out_feature_class = "clip_output\out.shp"
xy_tolerance = ""

field = ["FID", "ID", "NbhdName", "NbhdNo", "SHAPE@X", "SHAPE@Y"]

for row in arcpy.da.SearchCursor(neighbourhood_data_file, field):
    print(row[2])

arcpy.MakeFeatureLayer_management(clip_features, "TempLayer", "ID = 237")
arcpy.CopyFeatures_management("TempLayer",selected_clip_features)

arcpy.Clip_analysis(in_features, selected_clip_features, out_feature_class, xy_tolerance)
