A.How to open Gate v9.4:
    You can apply for a node when click on "Quick Launch General-Computer Desktop", and then you will have a 24 hours node;
    Then you can import these codes line by line: 
        module load gcc/11.2.0 geant4/11.2.1 geant4-data/11.2 
        export GEANT4_DATA_DIR=${EBROOTGEANT4MINDATA} 
        module load gcc/11.2.0 openmpi/4.1.1 gate/9.4 geant4-data/11.2
    after that you should go to the top folder of your .mac file,and then use code as follow:
        Gate --qt Yourfilename.mac
    then it will start to run.

B.How to change root file into PDF/npz/hdf5 
    You should use Jupyter Lab/Notebook Advanced Options.After cilck on "Jupyter Lab/Notebook Advanced Options" , import"gcc/11.2.0  openmpi/4.1.1 root/6.26.10 matplotlib/3.5.2" in Extra Modules To Load with Jupyter and then change "QOS" into "general-compute"
    Then look my code "change_root_to_pdf". I recommand all use .npz, because if you want to use hdf5, you should import h5py which will cause more trouble.

C.How to reconstruct by digital picture
    a) open pyrecon file;
    b) put your .npz/.hdf5 file into data file;
    c) use"test_projection_nonmpi.py" to generate projection;
    d) use"test_recon_nonmpi.py" to generate reconstruction picture;
    e) In pyrecon/data file, there is not only hotrod_phantom, but also a file "2p-source-gen.ipynb" to generate digital picture(that code can change the position and size of a point)
    f) you can use "read_projection_npz" and "read_recon_npz" to see the picture result

D.How to reconstruct by MC stimulation
    You can simply change the shape and number of your source and then run the .mac file.
    Then you can use "change_root_to_projection" in Jupyter notebook to get your projection file.

E.Tricks of using Gate to build your machine
    a) http://opengatecollaboration.org/ is the most useful one, and then you find the documentation to get start.
    b) after v9.3 the digitizer code has a big change
    c) only the repeater code applied in the crystal can you get different crystalID
    d) rotate would happen in the axis of your object. For example, if you want to rotate the machine head, please rotate the world.

F.Tricks of using root
    After import:
        module load gcc/11.2.0 geant4/11.2.1 geant4-data/11.2 
        export GEANT4_DATA_DIR=${EBROOTGEANT4MINDATA} 
        module load gcc/11.2.0 openmpi/4.1.1 gate/9.4 geant4-data/11.2
    Your should import 
        "root Yourfilename.root" to open your root file. 
    For me, use .ls to see the file in my root file,
    use "Singles->Print()" to see the list of "Singles"
    "Singles->Draw("Your target name")"to draw the histogram and"Singles->GetEntries()" to know the number of the events
    More code about root is here https://root.cern/learn/ (it is really a big task!!!)


    

