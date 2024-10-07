import numpy
import pathlib, sys

# import matplotlib.pyplot as plt
import h5py

top_dir = str(pathlib.Path(__file__).parents[2])
sys.path.append(top_dir)
import pyrecon.projector as projector

phantom = numpy.load(str(top_dir) + "/data/" + "hotrod_phantom_data_100x100.npz")[
    "phantom"
]
data = numpy.load(str(top_dir) + "/data/" + "mosaic_sysmat.npz")[
    "sysmat"
]
#with h5py.File(top_dir + "/data/test_sysmat.hdf5", "r") as f:
 #   data = f["sysmat"]
  #  print(data.shape)
print(type(data))
arr=numpy.array(data)
sysmat = numpy.reshape(
        arr, (288,10000))
projection = projector.get_forward_projection(sysmat, phantom)
numpy.savez_compressed(
        str(top_dir) + "/data/" + "5hole_projection.npz",
        projection=projection,
    )
