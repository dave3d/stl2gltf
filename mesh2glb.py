#! /usr/bin/env python

import sys
import os
import pymeshlab as ml
import trimesh

def mesh2glb(inname, outname):
    """Convert a mesh file to a GLB file.

    This function converts an input mesh to GLB in a 2 step process.
    First it goes from mesh to PLY using MeshLab.  For input,
    MeshLab supports the following formats:
        PLY, STL, OFF, OBJ, 3DS, VRML 2.0, X3D and COLLADA.

    Then for the second step the PLY mesh is converted to GLB
    using the Trimesh module, since MeshLab does not support GLB.

    Note that in the first step, and scene hierarchy and non-mesh
    data is stripped out.

    """

    # Use meshlab to read the WRL
    ms = ml.MeshSet()
    ms.load_new_mesh(inname)

    # Save a temporary PLY file
    ms.save_current_mesh('tempmesh.ply')

    tmesh = trimesh.load('tempmesh.ply')


    fout = open(outname, "wb")
    tmesh.export(fout, 'glb')
    fout.close()

    # Clean up the temp PLY file
    os.remove('tempmesh.ply')


if __name__ == "__main__":

    inname = "teapot.wrl"
    outname = "teapot.glb"

    if len(sys.argv) > 1:
        inname = sys.argv[1]
        if len(sys.argv) > 2:
            outname = sys.argv[2]
        else:
            outname = inname.replace('.wrl', '.glb')

    print("Converting", inname, "to", outname)
    mesh2glb(inname, outname)
