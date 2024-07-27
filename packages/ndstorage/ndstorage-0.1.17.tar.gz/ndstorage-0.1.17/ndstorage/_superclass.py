import os
from .ndtiff_dataset import NDTiffDataset
from .ndtiff_pyramid_dataset import NDTiffPyramidDataset
from .old_format_version_readers.nd_tiff_v2 import NDTiff_v2_0
from .old_format_version_readers.ndtiff_v1 import NDTiff_v1
import numpy as np
from .file_io import NDTiffFileIO, BUILTIN_FILE_IO

class Dataset:
    """
    Generic class for opening NDTiff datasets. Creating an instance of this class will
    automatically return an instance of the class appropriate to the version and type of NDTiff dataset required
    """
    def __new__(cls, dataset_path=None, file_io: NDTiffFileIO = BUILTIN_FILE_IO, summary_metadata=None):
        ## Datasets currently being collected--must be v3
        if summary_metadata is not None:
            # Check if its a multi-res pyramid or regular
            if "GridPixelOverlapX" in summary_metadata:
                obj = NDTiffPyramidDataset.__new__(NDTiffPyramidDataset)
                obj.__init__(dataset_path=dataset_path, file_io=file_io, summary_metadata=summary_metadata)
            else:
                obj = NDTiffDataset.__new__(NDTiffDataset)
                obj.__init__( dataset_path=dataset_path, file_io=file_io, summary_metadata=summary_metadata)
            return obj

        # Search for Full resolution dir, check for index
        res_dirs = [
            dI for dI in file_io.listdir(dataset_path) if file_io.isdir(file_io.path_join(dataset_path, dI))
        ]
        if "Full resolution" not in res_dirs:
            # Full resolution was removed ND Tiff starting in V3 for non-stitched
            fullres_path = dataset_path
            # but if it doesn't have an index, than something is wrong
            if "NDTiff.index" not in file_io.listdir(fullres_path):
                raise Exception('Cannot find NDTiff index')
            # It must be an NDTiff >= 3.0 non-multi-resolution, loaded from disk
            obj = NDTiffDataset.__new__(NDTiffDataset)
            obj.__init__(dataset_path,  file_io=file_io)
            return obj
        fullres_path = (
                dataset_path + ("" if dataset_path[-1] == os.sep else os.sep) + "Full resolution" + os.sep)
        # It could still be a multi-res v3. Need to parse a Tiff and check major version
        a_tiff_file = [file for file in file_io.listdir(fullres_path) if '.tif' in file][0]
        file = file_io.open(fullres_path + a_tiff_file, "rb")
        file.seek(12)
        major_version = np.frombuffer(file.read(4), dtype=np.uint32)[0]
        file.close()
        if major_version == 3:
            obj = NDTiffPyramidDataset.__new__(NDTiffPyramidDataset)
            obj.__init__(dataset_path=dataset_path, file_io=file_io)
            return obj

        # It's a version 2 or a version 1. Check the name of the index file
        if "NDTiff.index" in file_io.listdir(fullres_path):
            obj = NDTiff_v2_0.__new__(NDTiff_v2_0)
            obj.__init__(dataset_path, full_res_only=True, file_io=file_io)
            return obj
        else:
            obj = NDTiff_v1.__new__(NDTiff_v1)
            obj.__init__(dataset_path, full_res_only=True, file_io=file_io)
            return obj
