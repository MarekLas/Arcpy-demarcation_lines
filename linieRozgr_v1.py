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

arcpy.management.Append(r"POWIERZCHNIE\PRZEZNACZENIE\PRZEZ;POWIERZCHNIE\PRZEZNACZENIE\PRZEZ_ULICE;POWIERZCHNIE\PRZEZNACZENIE\PRZEZ_INFR;POWIERZCHNIE\PRZEZNACZENIE\PRZEZ_KOM", r"{}\brg_mpzp.gdb\BRG_MPZP\LINIE_ROZGR".format(folder), "NO_TEST", 'byt "byt" true true false 255 Text 0 0,First,#', '', '')
linRoz = mpzpMap.listLayers("LINIE_ROZGRANICZAJACE")[0]
linRoz.visible = False

arcpy.AddMessage(nr_planu)
arcpy.AddMessage("Brawo! Linie rozgraniczajace utworzone")
