import numpy
import pathlib, sys
import h5py

top_dir = str(pathlib.Path(__file__).parents[2])
sys.path.append(top_dir)
import pyrecon.reconstruct_mlem as reconstruct_mlem
data = numpy.load(top_dir + "/data/mosaic_sysmat.npz")[
            "sysmat"]
#with h5py.File(top_dir + "/data/test_sysmat.hdf5", "r") as f:
#    data = f["sysmat"]
#    print(data.shape)
#    print(type(data))
#    arr=numpy.array(data)
#sysmat = numpy.reshape(
 #       arr, (1280,32400))
data=data.reshape((1,1,1,288,100,100))
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