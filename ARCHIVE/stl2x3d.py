#!/usr/bin/env python

import sys
import vtk

def stl2x3d(inname, outname):

    reader = vtk.vtkSTLReader()
    reader.SetFileName(inname)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # Create a rendering window and renderer
    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)

    # Assign actor to the renderer
    ren.AddActor(actor)

    writer = vtk.vtkX3DExporter()
    writer.SetFileName(outname)
    #writer.BinaryOn()
    writer.SetRenderWindow(renWin)
    writer.Write()

if __name__ == "__main__":

    inname = "teapot.stl"
    outname = "teapot.x3d"

    if len(sys.argv) > 1:
        inname = sys.argv[1]
        if len(sys.argv) > 2:
            outname = sys.argv[2]
        else:
            outname = inname.replace('.stl', '.x3d')

    print("Converting", inname, "to", outname)
    stl2x3d(inname, outname)
