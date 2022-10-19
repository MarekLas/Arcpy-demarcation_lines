import arcpy
import os

aprx = arcpy.mp.ArcGISProject("CURRENT")
folder = aprx.homeFolder
arcpy.env.workspace = r"{}\brg_mpzp.gdb".format(folder)
arcpy.env.overwriteOutput = True

nr_planu = arcpy.GetParameterAsText(0)

mpzpMap = aprx.listMaps(f"{nr_planu}_MPZP")[0]

folder = aprx.homeFolder
arcpy.env.workspace = r"{}\brg_mpzp.gdb".format(folder)
arcpy.env.overwriteOutput = True

linRoz = mpzpMap.listLayers("LINIE_ROZGR")[0]

# sprawdzamy czy feature class jest pusty
Count = int(arcpy.GetCount_management(linRoz).getOutput(0))

if Count > 0:
    pass
else:
    if arcpy.Exists(mpzpMap.listLayers("PRZEZ_MIX")[0]):
        arcpy.management.Append(r"POWIERZCHNIE\PRZEZNACZENIE\PRZEZ;POWIERZCHNIE\PRZEZNACZENIE\PRZEZ_ULICE;POWIERZCHNIE\PRZEZNACZENIE\PRZEZ_INFR;POWIERZCHNIE\PRZEZNACZENIE\PRZEZ_KOM;POWIERZCHNIE\PRZEZNACZENIE\PRZEZ_MIX", r"{}\brg_mpzp.gdb\BRG_MPZP\LINIE_ROZGR".format(folder), "NO_TEST", 'byt "byt" true true false 255 Text 0 0,First,#', '', '')
    else:
        arcpy.management.Append(r"POWIERZCHNIE\PRZEZNACZENIE\PRZEZ;POWIERZCHNIE\PRZEZNACZENIE\PRZEZ_ULICE;POWIERZCHNIE\PRZEZNACZENIE\PRZEZ_INFR;POWIERZCHNIE\PRZEZNACZENIE\PRZEZ_KOM", r"{}\brg_mpzp.gdb\BRG_MPZP\LINIE_ROZGR".format(folder), "NO_TEST", 'byt "byt" true true false 255 Text 0 0,First,#', '', '')

camera = aprx.activeView.camera
camera.setExtent(arcpy.Describe(linRoz).extent)

linRoz.visible = False

arcpy.AddMessage(nr_planu)
arcpy.AddMessage("Brawo, należy sie medal! Linie rozgraniczajace utworzone")
