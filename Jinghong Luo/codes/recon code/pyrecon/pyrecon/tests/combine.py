import numpy
import pathlib, sys

# import matplotlib.pyplot as plt
import h5py

top_dir = str(pathlib.Path(__file__).parents[2])
sys.path.append(top_dir)
import pyrecon.projector as projector

phantom = numpy.load(str(top_dir) + "/data/" + "2pclose.npz")[
    "phantom"
]
data = numpy.load(str(top_dir) + "/data/" + "5hole_repeater_without_multi.npz")[
    "sysmat"
]
#with h5py.File(top_dir + "/data/test_sysmat.hdf5", "r") as f:
 #   data = f["sysmat"]
  #  print(data.shape)
print(type(data))
arr=numpy.array(data)
sysmat = numpy.reshape(
        arr, (180,10000))
projection = projector.get_forward_projection(sysmat, phantom)
numpy.savez_compressed(
        str(top_dir) + "/data/" + "5hole_projection.npz",
        projection=projection,
    )
top_dir = str(pathlib.Path(__file__).parents[2])
sys.path.append(top_dir)
import pyrecon.reconstruct_mlem as reconstruct_mlem
data = numpy.load(top_dir + "/data/5hole_repeater1.npz")[
            "sysmat"]
#with h5py.File(top_dir + "/data/test_sysmat.hdf5", "r") as f:
#    data = f["sysmat"]
#    print(data.shape)
#    print(type(data))
#    arr=numpy.array(data)
#sysmat = numpy.reshape(
 #       arr, (1280,32400))
data=data.reshape((1,1,1,180,100,100))
        # Load projection data
proj = numpy.load(top_dir + "/data/5hole_projection.npz")[
            "projection"
        ]

        # Perform reconstruction
out = reconstruct_mlem.reconstruct_mlem(data, proj, 10000)
numpy.savez_compressed(
            top_dir + "/data/" + "test_reconstruction.npz",
            reconstructed=out,
        )