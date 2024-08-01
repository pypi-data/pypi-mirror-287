"""
Convert auxillary data recorded during WESTPA simulation and stored in west.h5 file
to various probability density datasets.

This script effectively replaces the need to use the native WESTPA plotting pipeline:
west.h5 --w_pdist(with --construct-dataset module.py)--> 
pdist.h5 --plothist(with --postprocess-functions hist_settings.py)--> plot.pdf

TODO: 
    - maybe add option to output pdist as file, this would speed up subsequent plotting
        of the same data. H5_Plot could then use this data.
    - method to return pdist of a single trace, leading into option to plot all succ traces.
"""

# TEMP for trace plot (TODO)
import matplotlib.pyplot as plt
######

import os
import h5py
import numpy as np
from tqdm.auto import tqdm

from warnings import warn

# for copying h5 file
import shutil

# Suppress divide-by-zero in log
np.seterr(divide='ignore', invalid='ignore')

class H5_Pdist():
    """
    These class methods generate probability distributions from a WESTPA H5 file.
    """
    def __init__(self, h5="west.h5", data_type=None, Xname="pcoord", Xindex=0, Yname=None, 
                 Yindex=0, Zname=None, Zindex=0, Cname=None, Cindex=0, 
                 H5save_out=None, Xsave_name=None, Ysave_name=None, Zsave_name=None, 
                 data_proc=None, first_iter=1, last_iter=None, step_iter=1, bins=(100,100), 
                 p_units='kT', T=298, weighted=True, skip_basis=None, succ_only=False,
                 histrange_x=None, histrange_y=None, no_pbar=False, *args, **kwargs):
        """
        Initialize this class with an `h5` file and `data_type`. The `X/Y/Zname` args
        Can be a pcoord or aux dataset name in a west.h5 file, a 1D or 2D numpy array,
        or the path to and name of a file (with a .dat, .txt, .pkl, .npz, .npy ending).

        After instantiating this class, input args are saved as instance attributes.

        These can then be updated if needed. The main method you will call is the
        H5_Pdist.pdist() method, which will return the X, Y, and Z arrays to be plotted.
        The X and Y arrays are 1D and represent the X and Y axis values to be plotted.
        The Z array is empty with 2D output but otherwise will be a 2D array.

        Parameters
        ----------
        h5 : str or list of str
            Path(s) to west.h5 file(s).
        data_type : str
            'evolution' (1 dataset); 'average' or 'instant' (1 or 2 datasets)
        Xname : str or array
            Target data for x axis, default pcoord. Can be a pcoord or aux dataset name 
            in a west.h5 file, a 1D or 2D numpy array, or the path to and name of a file 
            (with a .dat, .txt, .pkl, .npz, .npy ending).
        Xindex : int
            If X.ndim > 2, use this to index.
        Yname : str or array
            Target data for y axis, default None. Can be a pcoord or aux dataset name 
            in a west.h5 file, a 1D or 2D numpy array, or the path to and name of a file 
            (with a .dat, .txt, .pkl, .npz, .npy ending).
        Yindex : int
            If Y.ndim > 2, use this to index.
        Zname : str or array
            Target data for z axis, default None. Can be a pcoord or aux dataset name 
            in a west.h5 file, a 1D or 2D numpy array, or the path to and name of a file 
            (with a .dat, .txt, .pkl, .npz, .npy ending).
            Use this if you want to use a dataset instead of pdist for Z axis.
            This will be best plotted as a scatter plot with Z as the marker color.
            Instead of returning the pdist, only the XYZ datasets will be returned.
            This is becasue the weights/pdist isn't considered.
        Zindex : int
            If Z.ndim > 2, use this to index.
        Cname : str or array
            Target data for cbar axis when using 3d projection scatter, default None. 
            Can be a pcoord or aux dataset name in a west.h5 file, a 1D or 2D numpy array, 
            or the path to and name of a file (with a .dat, .txt, .pkl, .npz, .npy ending).
        Cindex : int
            If C.ndim > 2, use this to index.
        H5save_out : str
            Paths to save a new H5 file with this dataset name.
            Right now it saves the requested X Y or Z data into a new aux_name.
            Note if you use this feature the input data must be the same shape and formatting as the other
            H5 file datasets. (TODO: organization?)
            Also can be name of the outfile h5 file for optionally outputting new skipped basis or succ_only
            h5 dataset with updated weights.
        Xsave_name, Ysave_name, Zsave_name : str
            Respective names to call the new dataset saved into the new H5 file.
        data_proc : function or tuple of functions
            Of the form f(data) where data has rows=segments, columns=frames until tau, depth=data dims.
            The input function must return a processed array of the same shape and formatting.
        first_iter : int
            Default start pdist at iteration 1 data.
        last_iter : int
            Last iteration data to include, default is the last recorded iteration in the west.h5 file. 
            Note that `instant` type pdists only depend on last_iter.
        step_iter : int
            Only use every step_iter size iteration intervals of the input data,
            e.g. step_iter=10 for every 10 iterations.
        bins : tuple of ints (TODO: maybe the tuple isn't user friendly for 1 dim? Could check items like md_pdist)
            Histogram bins in pdist data to be generated for x and y datasets, default both 100.
        p_units : str
            Can be 'kT' (default), 'kcal', 'raw', or 'raw_norm'.
            kT = -lnP, kcal/mol = -RT(lnP), where RT = 0.5922 at `T` Kelvin.
            'raw' is the raw probabilities and 'raw_norm' is the raw probabilities P(max) normalized.
        T : int
            Temperature if using kcal/mol.
        weighted : bool
            Default True, use WE segment weights in pdist calculation.
        skip_basis : list
            List of binaries for each basis state to determine if it is skipped.
            e.g. [0, 0, 1] would only consider the trajectory data from basis 
            states 1 and 2 but would skip basis state 3, applying zero weights.
        succ_only : bool
            Default False, set True to filter weights to show only successfull trajectories.
        histrange_x, histrange_y : list or tuple of 2 floats or ints
            Optionally put custom bin ranges.
        no_pbar : bool
            Optionally do not include the progress bar for pdist generation.
        TODO: maybe also binsfromexpression?
        """
        # standard case where the input h5 file is a single string
        if isinstance(h5, str):
            self.h5_list = [h5]
        # when input is a list one or many h5 files
        elif isinstance(h5, list):
            # save the whole list
            self.h5_list = h5
            # convert to str if input is a single item list
            # or use the first h5 file in the list to initialize (when multiple items)
            h5 = h5[0]
        else:
            raise ValueError(f"Something may be wrong with the h5 file name input: {h5}")

        # save both the name and the h5 file
        self.h5_name = h5
        self.h5 = h5py.File(h5, mode="r")

        if data_type is None or data_type not in ["evolution", "average", "instant"]:
            raise ValueError("Must input valid data_type str: `evolution`, `average`, or `instant`")
        else:
            self.data_type = data_type

        self.p_units = str(p_units)

        self.T = int(T)
        self.weighted = weighted

        # process XYZ names and indicies (TODO: maybe a more efficient way to go about this)
        self.Xname, self.Xindex = self._process_name_and_index(Xname, Xindex, Xname, Yname)
        self.Yname, self.Yindex = self._process_name_and_index(Yname, Yindex, Xname, Yname)
        self.Zname, self.Zindex = self._process_name_and_index(Zname, Zindex, Xname, Yname)

        # for 3d proj plot cbar
        self.Cname, self.Cindex = self._process_name_and_index(Cname, Cindex, Xname, Yname)

        # check to make sure none of the Name / Index pairs are identical
        self._check_duplicate_name_index_pairs()

        # XYZ save into new h5 file options
        self.H5save_out = H5save_out
        self.Xsave_name = Xsave_name
        self.Ysave_name = Ysave_name
        self.Zsave_name = Zsave_name
        # if H5save_out is not None:
        #     shutil.copyfile(self.h5_name, str(H5save_out))
        #     self.H5save_out = h5py.File(H5save_out, "r+")
        
        # raw data processing function
        # TODO: allow for 2-3 functions as tuple input, right now one function only
        self.data_proc = data_proc

        # current iteration variable
        west_current_iteration = self.h5.attrs["west_current_iteration"]

        # default to last
        if last_iter is not None:
            self.last_iter = int(last_iter)
        elif last_iter is None:
            self.last_iter = west_current_iteration - 1
        
        # set first_iter inst attr
        if data_type == "instant":
            self.first_iter = self.last_iter
        else:
            self.first_iter = int(first_iter)

        # check that last_iter is not > current iteration
        if self.last_iter > self.h5.attrs["west_current_iteration"]:
            raise ValueError(f"last_iter of {self.last_iter} > current WE iteration {west_current_iteration}")
        # check that first_iter is not 0 or negative
        if self.first_iter <= 0:
            raise ValueError(f"Using first_iter value of {self.first_iter}, this should be >= 1")

        self.step_iter = step_iter
        
        # standardize bins input
        # case where the input bins is a single int
        if isinstance(bins, int):
            # convert single int to 1 element list to be indexable later
            self.bins = [bins]
            # if there is a 2 dimensional pdist requested, make same int bins each dim
            if Yname is not None:
                self.bins = [bins, bins]
        # when input is already a list of bins with an item for each dimension
        elif isinstance(bins, (list, tuple)):
            self.bins = bins
        else:
            raise ValueError(f"Something may be wrong with bins input: {bins}")

        self.skip_basis = skip_basis

        # initialize weights
        self._init_weights()

        # n_particles for each iteration
        self.n_particles = self.h5["summary"]["n_particles"]

        # TODO: I wonder if both of these attributes are needed (total only used by reshape data array)
        #       I should note somewhere that data array must be for the same length/iters as the west.h5 file
        # the sum of n segments in all specified iterations and all iterations overall
        self.current_particles = np.sum(self.h5["summary"]["n_particles"][self.first_iter-1:self.last_iter])
        # do not include the final (empty) iteration
        self.total_particles = np.sum(self.h5["summary"]["n_particles"][:-1])

        # integer for the amount of frames saved (length) per tau (e.g. 101 for 100 ps tau)
        self.tau = self._get_data_array("pcoord", 0, self.first_iter).shape[1]

        self.histrange_x = histrange_x
        self.histrange_y = histrange_y
        self.no_pbar = no_pbar
        self.succ_only = succ_only

        # accounts for array and filename input XYZnames
        self._check_XYZnames()

    def _process_name_and_index(self, name, index, Xname, Yname):
        """
        Consolidated logic for taking input XYZnames and outputting the 
        corrected name and index.

        Parameters
        ----------
        name : str
            Input XYZ name.
        index : int
            Input XYZ index 
        Xname : str
        Yname : str
        # usingY : bool
        #     Set to True when returning name/index for Yname, default False.
        
        Returns
        -------
        name : str
            Corrected XYZ name.
        index : int
            Corrected XYZ index.
        """
        if name is not None and isinstance(name, str):
            # add auxdata prefix if not using "pcoord" and not using array or filename input
            # instead of checking for '.', check for filename
            #if name != "pcoord" and name[-4] != ".":
            if name != "pcoord" and not os.path.isfile(name):
                name = "auxdata/" + name
            # for common case of evolution with extra Yname input
            if self.data_type == "evolution" and Yname is not None:
                warn("\nDefaulting to evolution plot for --data-type, since you put a --Yname arg.\n"
                    "Did you mean to use --data-type of `average` or `instant`?")
            # for case with "pcoord/aux 0" and "pcoord/aux 0": same name and index will auto change index
            # Note: this didnt really work if you set -xi 1 or other index and -yi 0 
            #       need to actually compare the xindex and yindex within this function
            #       instead, just not going to include this check.
            # elif isinstance(name, str) and usingY and Xname == Yname and index == 0:
            #     index = 1
            #     warn("\nSetting --Yindex to 1 (2nd dimension) since Xname/Yname and Xindex/Yindex were the same.")
        return name, index

    def _check_XYZnames(self):
        """
        Check XYZnames for array and filename input (if found, initialize).
        Replaces self.Xname, self.Yname, and self.Zname attrs as needed.
        """
        XYZnames = ["Xname", "Yname", "Zname", "Cname"]
        for name in XYZnames:
            attr_value = getattr(self, name)
            # reshape 1d input raw data array (if given) into 3d array
            if isinstance(attr_value, np.ndarray):
                setattr(self, name, self.reshape_total_data_array(attr_value))
            # if input isn't an auxname but an allowed filename for input
            # instead of checking for '.', check for filename
            #elif isinstance(attr_value, str) and attr_value[-4] == ".":
            elif isinstance(attr_value, str) and os.path.isfile(attr_value):
                # for .npy binary files or pkl files
                if attr_value[-4:] in [".npy", ".npz", ".pkl"]:
                    data = np.load(attr_value, allow_pickle=True)
                # text files
                elif attr_value[-4:] in [".dat", ".txt"]:
                    data = np.genfromtxt(attr_value)
                else:
                    raise ValueError("File ending must be '.dat', '.txt', '.npy', '.npz', or '.pkl'")
                # need to reshape so that the columns go depth wise
                data = data.reshape(data.shape[0], 1, -1)
                # reshape the array again to fit into current westpa seg per iter shape and set
                setattr(self, name, self.reshape_total_data_array(data))

    def _init_weights(self):
        """
        Initialize the weight array.
        """
        #for iter in range(self.first_iter, self.last_iter + 1):
        # have to make array start from iteration 1 to index well during weighting
        # but only for using skipping basis
        if self.skip_basis is None:
            weight_start = self.first_iter
        elif self.skip_basis:
            weight_start = 1

        # make a (TODO: pre-allocated?) list for each iteration weight array
        #weights = [None] * (self.last_iter - weight_start + 1)
        weights = []
        # fill out the weight list
        # can't use step-iter here since the entire weight array needs to be indexed by step-iter later
        #for iter in range(weight_start, self.last_iter + 1, self.step_iter):
        for iter in range(weight_start, self.last_iter + 1):
            #weights[iter - weight_start] = self.h5[f"iterations/iter_{iter:08d}/seg_index"]["weight"]
            weights.append(self.h5[f"iterations/iter_{iter:08d}/seg_index"]["weight"])
        # 1D array of variably shaped arrays
        self.weights = np.array(weights, dtype=object)

    def _check_duplicate_name_index_pairs(self):
        """
        Warnings if there are duplicate XYZ name/index pairs.
        """
        # only check all of them if Cname is not None
        if self.Cname is not None:
            pairs = [(self.Xname, self.Xindex), (self.Yname, self.Yindex), 
                     (self.Zname, self.Zindex), (self.Cname, self.Cindex)]
        # only check if Zname is not None
        elif self.Zname is not None:
            pairs = [(self.Xname, self.Xindex), (self.Yname, self.Yindex), (self.Zname, self.Zindex)]
        else:
            pairs = [(self.Xname, self.Xindex), (self.Yname, self.Yindex)]
        seen_pairs = set()
        duplicates = set()

        for pair in pairs:
            # for input numpy arrays, skip this checking
            if isinstance(pair[0], np.ndarray):
                pass

            # otherwise check if the pair has been seen before
            elif pair in seen_pairs:
                duplicates.add(pair)
            else:
                seen_pairs.add(pair)

        if duplicates:
            # Handle duplicates
            # For example, you can print a message or perform any desired action
            message = "Duplicate name and index pairs found, "
            message += "check to make sure XYZname and XYZindex values are unique:\n" 
            message += f"Xname: {self.Xname}, Xindex: {self.Xindex}\n"
            message += f"Yname: {self.Yname}, Yindex: {self.Yindex}\n"
            message += f"Zname: {self.Zname}, Zindex: {self.Zindex}\n" 
            warn(message)
            # for pair in duplicates:
            #     print(f"Name: {pair[0]}, Index: {pair[1]}")
        #else:
            # No duplicates found
            #print("No duplicate name and index pairs found")

    def _get_data_array(self, name, index, iteration, h5_create=None, h5_create_name=None):
        """
        Extract, index, and return the aux/data array of interest.
        Rows are segments, columns are frames until tau, depth is ndimensional datasets.

        Parameters
        ----------
        name : str
            Dataset name.
        index : int
            Dataset index.
        iteration : int
            WE iteration.
        h5_create : str
            Name of the h5 file to add the dataset to.
        h5_create_name : str
            Name of the dataset that is being placed into the h5 file.

        Returns
        -------
        data : ndarray
            Dataset of interest from the H5 file.
        """
        # if the user puts in an array object or filename instead of a string dataset name
        # for filename case, should have been converted to an array upon init
        if isinstance(name, np.ndarray):
            # need to parse data for segments only in current iteration
            # segments are each row, but in input they are all concatenated
            n_segs_up_to_iter = np.sum(self.n_particles[self.first_iter-1:iteration-1])
            n_segs_including_iter = np.sum(self.n_particles[self.first_iter-1:iteration])
            data = name[n_segs_up_to_iter:n_segs_including_iter,:,:]

        # name should be a string for the h5 file dataset name
        elif isinstance(name, str):
            # this t/e block is to catch non-existent aux data names
            try:
                #data = np.array(self.h5[f"iterations/iter_{iteration:08d}/{name}"])
                #data = self.h5[f"iterations/iter_{iteration:08d}/{name}"][:]
                # seems like data is okay left as type: <class 'h5py._hl.dataset.Dataset'>
                # doesn't need to be an array, I guess array indexing already works so it's compatible
                # speeds seem pretty similar for both though
                # and the np.atleast_3d will convert to array anyway
                data = self.h5[f"iterations/iter_{iteration:08d}/{name}"]
            except KeyError as e:
                message = f"{e}: {name} is not a valid object in the h5 file. \n" + \
                          f"Available datasets are: 'pcoord' "
                # this t/e block is to catch the case where there are no aux datasets at all
                try:
                    auxnames = list(self.h5[f"iterations/iter_{self.first_iter:08d}/auxdata"])
                    message += f"and the following aux datasets {auxnames}"
                except KeyError:
                    message += "and no aux datasets were found"
                raise ValueError(message)
                
        else:
            raise ValueError("Xname Yname and Zname arguments must be either a string or an array.")

        # standardize the data dimensions to allow 3d indexing
        data = np.atleast_3d(data)

        # run data processing function on raw data if available
        # don't do this for input array data
        if self.data_proc is not None and not isinstance(name, np.ndarray):
            data = self.data_proc(data)

        # option to fill out new h5 file with dataset included here
        # using westpa style compression and scaleoffset 
        # this way it gets repacked into h5 file to update storage
        # could round to 4 decimal places with data=np.around(data, 4)
        if h5_create:
            h5_create.create_dataset(f"iterations/iter_{iteration:08d}/auxdata/{h5_create_name}", 
                                     data=data, compression=4, scaleoffset=6, chunks=True)

        return data[:,:,index]

    # this does add a little overhead at high iteration ranges
    # ~0.5s from 100i to 400i
    # alternatively, can put histrange_x and histrange_y args to skip this
    # TODO: does plothist avoid this?
    def _get_histrange(self, name, index):
        """
        Get the histrange considering the min/max of all iterations considered.

        Parameters
        ----------
        name : str
            Target auxillary data name for range calculation.
        index : int
            Target auxillary data index for range calculation.

        Returns
        -------
        histrange : tuple
            2 item list of min and max bin bounds for hist range of target aux data.
        """
        # set base histrange based on first iteration
        iter_data = self._get_data_array(name, index, self.first_iter)
        #iter_data = self._get_data_array(name, index, self.first_iter)
        global_min = np.amin(iter_data)
        global_max = np.amax(iter_data)

        # loop and update to the max and min for all other iterations considered
        for iter in range(self.first_iter + 1, self.last_iter + 1, self.step_iter):
            iter_data = self._get_data_array(name, index, iter)

            # find minimum and maximum values within the current iter
            iter_min = np.amin(iter_data)
            iter_max = np.amax(iter_data)

            # update global minimum and maximum values
            global_min = min(global_min, iter_min)
            global_max = max(global_max, iter_max)

        # define the common histogram range
        return (global_min, global_max)

    def _normalize(self, hist, p_units):
        """
        Normalize or convert the probabilities.

        Parameters
        ----------
        hist : ndarray
            Array containing the histogram count values to be normalized.
        p_units : str
            Can be 'kT' (default), 'kcal', 'raw', or 'raw_norm'.
            kT = -lnP, kcal/mol = -RT(lnP), where RT = 0.5922 at `T` Kelvin.
            'raw' is the raw probabilities and 'raw_norm' is the raw probabilities P(max) normalized.

        Returns
        -------
        hist : ndarray
            The hist array is normalized according to the p_units argument. 
        """
        # -lnP
        if p_units == "kT":
            hist = -np.log(hist / np.max(hist))
        # -RT*lnP
        elif p_units == "kcal":
            # Gas constant R = 1.9872 cal/K*mol or 0.0019872 kcal/K*mol
            hist = -0.0019872 * self.T * np.log(hist / np.max(hist))
        # raw probability
        elif p_units == "raw":
            hist = hist
        # raw normalized probability (P(x)/P(max))
        elif p_units == "raw_norm":
            hist = hist / np.max(hist)
        else:
            raise ValueError("Invalid p_units value, must be 'kT', 'kcal', 'raw', or 'raw_norm'.")
        return hist

    def _get_children_indices(self, parent):
        """
        For a (iter, seg) pair, look for and return all iter + 1 segment indices.

        Parameters
        ----------
        parent : tuple
            (iteration, segment).

        Returns
        -------
        children : tuple
            The indices of all child segments from the input parent segment.
        """
        children = []
        p_iter, p_seg = parent
        # for all parent_id values of the iter + 1 iteration
        for idx, seg in enumerate(
        self.f[f"iterations/iter_{p_iter+1:08d}/seg_index"]["parent_id"]):
            # match with input parent segment
            if seg == p_seg:
                # put all the parent segment children's indices into list
                children.append(idx)
                
        return children

    def _new_weights_from_skip_basis(self):
        """
        Make a new temp h5 file with zero weights for skipped basis state walkers.

        Returns
        -------
        new_weights : array
            Updated weight array with zero values for skipped basis states.
        """
        # TODO: doesn't work with --first-iter
        
        # copy of weights to edit
        new_weights = self.weights

        # setup a warning for h5 files that have incorrectly recorded bstate pcoords
        # this will all be based off of the first pcoord array (Z index 0)
        # correspondingly, the bstate_pcoord will be the first column
        bs_coords = self.h5[f"ibstates/0/bstate_pcoord"]
        it1_coords = self.h5[f"iterations/iter_00000001/pcoord"][:,0,0]
        # need to second element get the unique indices
        it1_unique_indices = np.unique(it1_coords, return_index=True)[1]
        # then sort to the original bstate ordering
        it1_unique_coords = np.array([it1_coords[index] \
                            for index in sorted(it1_unique_indices)])
        try:
            # make sure that traced unique pcoord elements match the basis state values
            if np.isclose(bs_coords[:,0], it1_unique_coords, rtol=1e-04) is False:
                message = f"The traced pcoord \n{it1_unique_coords} \ndoes not equal " + \
                          f"the basis state coordinates \n{bs_coords}"
                warn(message)
        except ValueError as e:
            message = f"{e}: Not all bstates may have been used in iteration 1."
            warn(message)

        # TODO: print bstate pcoords
        print(f"bstates: {bs_coords[:,0]}")
        print(f"bstates from pcoord: {it1_unique_coords}")
        #import sys ; sys.exit(0)

        # if the basis state binary is a 1 in skip_basis, use weight 0 
        #print("First run skip_basis processing from each initial segment: ")
        for basis, skip in enumerate(self.skip_basis):
            # essentially goes through all initial segments for each skipped basis
            if skip == 1:
                # loop of each initial pcoord value from iteration 1
                for it1_idx, it1_val in enumerate(it1_coords):
                    # so if the pcoord value matches the bstate value to be skipped
                    # needs to both be at the same precision
                    if np.isclose(it1_val, bs_coords[basis,0], rtol=1e-04):
                        # search forward to look for children of basis state 
                        # start at it1_idx, make weight zero 
                        new_weights[0][it1_idx] = 0

                        # list for parent_ids of the current segment skip basis lineage
                        skip_parents_c = [it1_idx]
                        # list for storing the indices to skip for the next iteration
                        skip_parents_n = []

                        # zero the next iteration's children until last_iter
                        for iter in tqdm(range(1, self.last_iter + 1), 
                                         desc="skip_basis", disable=self.no_pbar):
                            for idx in skip_parents_c:
                                # make zero for each child of skip_basis
                                new_weights[iter-1][idx] = 0
                                # then make new skip_parents tuple to loop for next iter
                                skip_parents_n += self._get_children_indices((iter, idx))

                            # make new empty list to store the iteration's skipped
                            skip_parents_c.clear()
                            skip_parents_c += skip_parents_n
                            skip_parents_n.clear()

        # TODO: prob can do better than these print statements
        #print("pdist calculation: ")
        # write new weights into skip_basis_out h5 file
        # TODO: wrap this into h5saveout and include succ_only
        # if self.skip_basis_out is not None:
        #     shutil.copyfile(self.h5_name, self.skip_basis_out)
        #     h5_skip_basis = h5py.File(self.skip_basis_out, "r+")
        #     for idx, weight in enumerate(new_weights):
        #         h5_skip_basis[f"iterations/iter_{idx+1:08d}/seg_index"]["weight"] = weight
            
        # only return portion of weights requested by user
        return new_weights[self.first_iter-1:self.last_iter:self.step_iter]

    ##################### TODO: update or organize this #############################
    def get_parents(self, walker_tuple):
        """
        Get parent of an input (iteration, walker).

        Parameters
        ----------
        walker_tuple : tuple
            (iteration, walker)

        Returns
        -------
        parent : iteration, walker
        """
        it, wlk = walker_tuple
        parent = self.h5[f"iterations/iter_{it:08d}"]["seg_index"]["parent_id"][wlk]
        return it-1, parent

    def trace_walker(self, walker_tuple, first_iter=1):
        """
        Get trace path of an input (iteration, walker).

        Parameters
        ----------
        walker_tuple : tuple
            (iteration, walker)
        first_iter : int
            Iter to trace back to. Default 1.

        Returns
        -------
        trace : list of tuples
            Tuples are (iteration, walker) traces.
        """
        # Unroll the tuple into iteration/walker 
        it, wlk = walker_tuple
        # Initialize our path
        path = [(it,wlk)]
        # And trace it
        while it > first_iter: 
            it, wlk = self.get_parents((it, wlk))
            path.append((it,wlk))
        return np.array(sorted(path, key=lambda x: x[0]))

    def get_coords(self, path, data_name, data_index):
        """
        Get a list of data coordinates for plotting traces.
        Only grabs the last frames.

        Parameters
        ----------
        path : list of tuples
            Tuples are (iteration, walker) traces.
        data_name : str
            Name of dataset.
        data_index : int
            Index of dataset.

        Returns
        -------
        coordinates : 1d array
            Array of coordinates from the list of (iteration, walker) tuples.
        """
        # Initialize an array for the pcoords
        coords = np.zeros((len(path)))
        # Loop over the path and get the pcoords for each walker
        for idx, (it, wlk) in enumerate(path):
            coords[idx] = (self._get_data_array(data_name, data_index, it)[wlk][-1])
        return coords
    
    def get_full_coords(self, walker_tuple, data_name, data_index=0, first_iter=1):
        """
        Returns a full 1D set of data for a single trace (path).
        This will be ordered from the first iter to the last.

        Parameters
        ----------
        walker_tuple : tuple
            (iteration, walker) start point to trace from.
        data_name : str
            Name of dataset.
        data_index : int
            Index of dataset.
        first_iter : int
            Iter to trace back to. Default 1.
            
        Returns
        -------
        coordinates : 1d array
            Array of coordinates from the list of (iteration, walker) tuples.
        """
        # account for non-pcoord input strings
        if data_name != "pcoord":
            data_name = "auxdata/" + data_name

        path = self.trace_walker(walker_tuple, first_iter)
        # Initialize an array for the pcoords (each iter * tau)
        coords = np.zeros((len(path)*self.tau))
        
        # Loop over the path and get the pcoords for each walker
        # path will be ordered from the first iter to the last.
        for idx, (it, wlk) in enumerate(path):
            # fill out the array in self.tau chunks
            coords[idx*self.tau:(idx+1)*self.tau] = self._get_data_array(data_name, data_index, it)[wlk]

        return coords            

    def find_iter_seg_from_xy_vals(self, val_x, val_y):
        """
        Find and return (iter, seg) closest to input data value(s).

        Parameters
        ----------
        val_x : int or float
            X dataset value to search for.
        val_y : int or float
            Y dataset value to search for.

        Returns
        -------
        iter_num, seg_num : int, int
            Iteration, segment number.
        """
        # for evolution plots, only need to search one iteration
        if self.data_type == "evolution":
            # convert to int since it is an iteration number
            val_y = int(val_y)
            # Extract x values for the val_y iteration
            x_data = self._get_data_array(self.Xname, self.Xindex, val_y)[:,-1]
            # Calculate distances between input x values and all data points in the current iteration
            dist = np.abs(x_data - val_x)
            min_dist_idx = np.argmin(dist)
            min_dist = dist[min_dist_idx]
            # iter, seg return: iter is from y value, seg is from min dist
            return val_y, min_dist_idx

        # for e.g. average plots, search all iterations of both x and y values
        distances = []
        # always use iteration 1 to get full trace path
        for i in tqdm(range(1, self.last_iter + 1, self.step_iter), 
                      desc="Trace Search", disable=self.no_pbar): 
            # Extract x and y values for the current iteration
            x_data = self._get_data_array(self.Xname, self.Xindex, i)[:,-1]
            y_data = self._get_data_array(self.Yname, self.Yindex, i)[:,-1]
            # Calculate distances between input values and all data points in the current iteration
            dist = np.sqrt((x_data - val_x)**2 + (y_data - val_y)**2)

            # Find the minimum distance and its index
            min_dist_idx = np.argmin(dist)
            min_dist = dist[min_dist_idx]

            distances.append((min_dist, i, min_dist_idx))

        # Find the iteration and segment with the minimum distance
        min_distance, iter_num, seg_num = min(distances)

        print(f"Tracing ITERATION: {iter_num}, SEGMENT: {seg_num}")
        return iter_num, seg_num

    # TODO: alot of the self refs are not even in h5_pdist, but in h5_plot
    #       need to do some rearrangement and refactoring at some point
    def plot_trace(self, walker_tuple, color="white", linewidth=1.0, linestyle='-', ax=None, 
                   find_iter_seg=False, mark_points=False, 
                   mp_size=80, mp_color=None, mp_markers=('o','v'), **kwargs):
        """
        Plot trace.

        Parameters
        ----------
        walker_tuple : tuple
            (iteration, walker) start point to trace from.
            Can also find the closest iteration/seg using input as (X_value,Y_value).
            `find_iter_seg` must be True to use this setting.
        color : str
        linewidth : int
        linestyle : str
        ax : mpl axes object
        find_iter_seg : bool
            Default False and use walker tuple as (iter, seg). 
            Set True to look for (iter, seg) using walker_tuple input as (X_value,Y_value).
        mark_points : bool
            Default False, set to true to mark the starting and end points of the trace path.
        mp_size : int
            Size of the marked points, default 80.
        mp_color : str
            Color of the marked points, if None, defaults to `color` arg.
        mp_markers : tuple
            Two item tuple: start point marker style, end point marker style.
        **kwargs
            Passed to mpl plt.plot line plots. E.g. alpha parameter.

        Returns
        -------
        aux or aux_x, aux_y : 1D arrays
            The coordinate values at each point in the trace.
        """
        # TODO: update/streamline this
        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = plt.gcf()

        # TODO: temp linestyle check, eventually move this whole method elsewhere
        #       need to be able to use cli and pass linestyle, while being able to use API
        #       where linestyle might not always be available if using h5_pdist and h5_plot separately
        # if object has linestyle specified, use it, otherwise use arg
        if hasattr(self, 'linestyle'):
            linestyle = self.linestyle

        # optional separate marker color
        if mp_color is None:
            mp_color = color

        # search for iter_seg if specified
        if find_iter_seg:
            walker_tuple = self.find_iter_seg_from_xy_vals(walker_tuple[0], walker_tuple[1])

        path = self.trace_walker(walker_tuple)
        # adjustments for plothist evolution of only aux_x data
        if self.data_type == "evolution":
            # split iterations up to provide y-values for each x-value (pcoord)
            aux = self.get_coords(path, self.Xname, self.Xindex)
            iters = np.arange(1, len(aux)+1, self.step_iter)
            ax.plot(aux[::self.step_iter], iters, c="black", lw=linewidth+1, linestyle=linestyle, zorder=1, **kwargs)
            ax.plot(aux[::self.step_iter], iters, c=color, lw=linewidth, linestyle=linestyle, zorder=1, **kwargs)
            # optionally marking start and end
            if mark_points is True:
                # find and plot the starting point
                ax.scatter(aux[0], iters[0], marker=mp_markers[0], color=mp_color, s=mp_size, edgecolor="k", zorder=1)
                # find and plot the end point
                ax.scatter(aux[-1], iters[-1], marker=mp_markers[1], color=mp_color, s=mp_size, edgecolor="k", zorder=1)
            return aux

        # And pull aux_coords for the path calculated
        aux_x = self.get_coords(path, self.Xname, self.Xindex)
        aux_y = self.get_coords(path, self.Yname, self.Yindex)

        ax.plot(aux_x[::self.step_iter], aux_y[::self.step_iter], c="black", lw=linewidth+1, linestyle=linestyle, zorder=1, **kwargs)
        ax.plot(aux_x[::self.step_iter], aux_y[::self.step_iter], c=color, lw=linewidth, linestyle=linestyle, zorder=1, **kwargs)

        # optionally marking start and end
        if mark_points is True:
            # find and plot the starting point
            ax.scatter(aux_x[0], aux_y[0], marker=mp_markers[0], color=mp_color, s=mp_size, edgecolor="k", zorder=1)
            # find and plot the end point
            ax.scatter(aux_x[-1], aux_y[-1], marker=mp_markers[1], color=mp_color, s=mp_size, edgecolor="k", zorder=1)
        
        return aux_x, aux_y

    def w_succ(self):
        """
        Find and return all successfully recycled (iter, seg) pairs.

        Returns
        -------
        succ : list of tuples (iter,wlk)
        """
        succ = []
        for iter in tqdm(range(self.first_iter, self.last_iter + 1), 
                         desc="Running w_succ", disable=self.no_pbar):
            # if the new_weights group exists in the h5 file
            if f"iterations/iter_{iter:08d}/new_weights" in self.h5:
                prev_segs = self.h5[f"iterations/iter_{iter:08d}/new_weights/index"]["prev_seg_id"]
                # append the previous iter and previous seg id recycled
                for seg in prev_segs:
                    succ.append((iter-1, seg))
        # TODO: order this by iter and seg vals? currently segs not sorted but is iter ordered
        return succ
    
    def succ_pdist_weight_filter(self):
        """
        TODO: Filter weights to be zero for all non successfull trajectories.
        Make an array of zero weights and fill out weights for succ trajs only.
        option to output new h5?

        Returns
        -------
        succ_weights : numpy object array
            Updated weight array.
        """
        # start with zero weight array and fill it with succ traj traces
        #succ_weights = np.zeros_like(self.weights, dtype=object)
        #succ_weights = np.vstack((np.zeros_like(w) for w in self.weights), dtype=object)

        # find the per iter n_seg lengths along axis 1 for weights
        seg_lengths = [len(arr) for arr in self.weights]
        #print(seg_lengths)

        # Create a new array filled with zeros with the same variable shape
        succ_weights = np.array([np.zeros(length) for length in seg_lengths], dtype=object)
    
        #print(succ_weights.shape)
        #print(self.weights.shape)

        # trace through each succ traj and fill in weights
        # TODO: there is some redundancy here, no need to fill weight when previously filled
        succ_trajs = self.w_succ()
        for succ in tqdm(succ_trajs, disable=self.no_pbar,
                         desc="Creating succ only weight array"):
            trace_path = self.trace_walker(succ)
            for it, wlk in trace_path:
                #print(succ_weights[it][wlk], self.weights[it][wlk])
                # -1 for indexing iters but regular indexing walkers
                succ_weights[it-1][wlk] = self.weights[it-1][wlk]

        # only return portion of weights requested by user
        return succ_weights[self.first_iter-1:self.last_iter:self.step_iter]

    ###############################################################################

    def aux_to_pdist_1d(self, iteration):
        """
        Take the auxiliary dataset for a single iteration and generate a weighted
        1D probability distribution. 

        Parameters
        ----------
        iteration : int
            Desired iteration to extract timeseries info from.

        Returns
        -------
        midpoints_x : ndarray
            Histogram midpoint bin values for target aux coordinate of dimension 0.
        midpoints_y : ndarray
            Optional histogram midpoint bin values for target aux coordinate of dimension 1.
        histogram : ndarray
            Raw histogram count values of each histogram bin. Can be later normalized as -lnP(x).
        """
        # return 1D aux data: 1D array for histogram and midpoint values
        aux = self._get_data_array(self.Xname, self.Xindex, iteration)

        # make an 1D array to fit the hist values based off of bin count
        histogram = np.zeros((self.bins[0]))
        for seg in range(0, aux.shape[0]):
            counts, bins = np.histogram(aux[seg], bins=self.bins[0], range=self.histrange_x)

            # selectively apply weights
            if self.weighted is True:
                # multiply counts vector by weight scalar from weight array
                counts = np.multiply(counts, self.weights[iteration - self.first_iter][seg])

            # add all of the weighted walkers to total array for the 
            # resulting linear combination
            histogram = np.add(histogram, counts)

        # get bin midpoints
        midpoints_x = (bins[:-1] + bins[1:]) / 2
        
        # TODO: also save as instance attributes?
        return midpoints_x, histogram

    def aux_to_pdist_2d(self, iteration):
        """
        Take the auxiliary dataset for a single iteration and generate a weighted
        2D probability distribution. 

        Parameters
        ----------
        iteration : int
            Desired iteration to extract timeseries info from.

        Returns
        -------
        midpoints_x : ndarray
            Histogram midpoint bin values for target aux coordinate of dimension 0.
        midpoints_y : ndarray
            Optional histogram midpoint bin values for target aux coordinate of dimension 1.
        histogram : ndarray
            Raw histogram count values of each histogram bin. Can be later normalized as -lnP(x).
        """
        # 2D instant histogram and midpoint values for a single specified WE iteration
        X = self._get_data_array(self.Xname, self.Xindex, iteration)
        Y = self._get_data_array(self.Yname, self.Yindex, iteration)

        # 2D array to store hist counts for each timepoint in both dimensions
        histogram = np.zeros(self.bins)
        for seg in range(0, X.shape[0]):
            counts, bins_x, bins_y = np.histogram2d(X[seg], Y[seg], 
                                                    bins=self.bins, 
                                                    range=[self.histrange_x, 
                                                           self.histrange_y]
                                                    )

            if self.weighted is True:
                # multiply counts vector by weight scalar from weight array
                counts = np.multiply(counts, self.weights[iteration - self.first_iter][seg])

            # add all of the weighted walkers to total array for 
            # the resulting linear combination
            histogram = np.add(histogram, counts)

        # get bin midpoints
        midpoints_x = (bins_x[:-1] + bins_x[1:]) / 2
        midpoints_y = (bins_y[:-1] + bins_y[1:]) / 2

        # TODO: save these as instance attributes
        # this will make it easier to save into a text pdist file later

        # save midpoints and transposed histogram (corrected for plotting)
        return midpoints_x, midpoints_y, histogram.T

    def evolution_pdist(self):
        """
        Returns the pdist for 1 coordinate for the range iterations specified.

        Returns
        -------
        x, y, norm_hist : arrays
            x and y axis values, and if using Y or evolution (with only X), 
            also returns norm_hist.
            norm_hist is a 2-D matrix of the normalized histogram values.
        """
        # make array to store hist (-lnP) values for n iterations of X
        evolution_x = np.zeros((self.last_iter - self.first_iter + 1, self.bins[0]))
        positions_x = np.zeros((self.last_iter - self.first_iter + 1, self.bins[0]))

        for iter in tqdm(range(self.first_iter, self.last_iter + 1, self.step_iter), 
                         desc="Evolution", disable=self.no_pbar):
            # account for first_iter arg for array indexing
            iter_index = iter - self.first_iter + 1
            # generate evolution x data
            center_x, counts_total_x = self.aux_to_pdist_1d(iter)
            evolution_x[iter_index - 1] = counts_total_x
            positions_x[iter_index - 1] = center_x

        # 2D evolution plot of X (Y not used if provided) per iteration        
        #evolution_x = self._normalize(evolution_x, self.p_units)

        # bin positions along aux x, WE iteration numbers, z data
        return positions_x, np.arange(self.first_iter, self.last_iter + 1, 1), evolution_x

    # TODO: maybe don't need individual functions, maybe can handle in main
    def instant_pdist_1d(self):
        """
        Returns the x and y pdist datasets for a single iteration.

        Returns
        -------
        Xdata, y : arrays
            x (dataset) and y (pdist) axis values
        """
        center, counts_total = self.aux_to_pdist_1d(self.last_iter)
        #counts_total = self._normalize(counts_total, self.p_units)
        return center, counts_total

    def instant_pdist_2d(self):
        """
        Returns the xyz pdist datasets for a single iteration.

        Returns
        -------
        x, y, norm_hist : arrays
            x and y axis values, and if using Y or evolution (with only X), 
            also returns norm_hist.
            norm_hist is a 2-D matrix of the normalized histogram values.
        """
        center_x, center_y, counts_total = self.aux_to_pdist_2d(self.last_iter)
        #counts_total = self._normalize(counts_total, self.p_units)
        return center_x, center_y, counts_total

    def instant_datasets_3d(self):
        """
        Unique case where `Zname` is specified and the XYZ datasets are returned.
        For single iteration.

        Returns
        -------
        X, Y, Z : arrays 
            Raw data for each named coordinate.
        """
        X = self._get_data_array(self.Xname, self.Xindex, self.last_iter)
        # for the case where Zname is specified but not Yname
        if self.Yname is None:
            warn("`Zname` is defined but not `Yname`, using Yname=`pcoord`")
            Y = self._get_data_array("pcoord", self.Yindex, self.last_iter)
        else:
            Y = self._get_data_array(self.Yname, self.Yindex, self.last_iter)
        Z = self._get_data_array(self.Zname, self.Zindex, self.last_iter)

        return X, Y, Z

    def average_pdist_1d(self):
        """
        1 dataset: average pdist for a range of iterations.

        Returns
        -------
        x, y
            x and y axis values, x is the coordinate values and y is probabilities.
        """
        # make 1D array to sum hist (-lnP) values for n iterations of X
        average_x = np.zeros(self.bins[0])

        for iter in tqdm(range(self.first_iter, self.last_iter + 1, self.step_iter), 
                         desc="Average 1D", disable=self.no_pbar):
            # generate 1d x pdist data
            center_x, counts_total_x = self.aux_to_pdist_1d(iter)
            # summation of counts for all iterations
            average_x += counts_total_x

        # return X positions and normalized 1D average plot data for Y
        #return center_x, self._normalize(average_x, self.p_units)
        return center_x, average_x

    def average_pdist_2d(self):
        """
        2 datasets: average pdist for a range of iterations.

        Returns
        -------
        x, y, norm_hist
            x and y axis values, and if using Y or evolution (with only X), also returns norm_hist.
            norm_hist is a 2-D matrix of the normalized histogram values.
        """
        # empty array for 2D pdist (bins being e.g. (100, 100))
        average_xy = np.zeros(self.bins)

        # 2D avg pdist data generation
        for iter in tqdm(range(self.first_iter, self.last_iter + 1, self.step_iter), 
                         desc="Average 2D", disable=self.no_pbar):
            center_x, center_y, counts_total_xy = self.aux_to_pdist_2d(iter)
            average_xy = np.add(average_xy, counts_total_xy)

        #return center_x, center_y, self._normalize(average_xy, self.p_units)
        return center_x, center_y, average_xy

    def average_datasets_3d(self, interval=1):
        """
        Unique case where `Zname` is specified and the XYZ datasets are returned.
        Averaged over the iteration range.
        
        Returns
        -------
        X, Y, Z : arrays 
            Raw data for each named coordinate.
        """
        if self.Yname is None:
            warn("`Zname` is defined but not `Yname`, using Yname=`pcoord`")
            self.Yname = "pcoord"

        # arrays to be filled with values from each iteration
        # rows are for all segments, columns are each segment datapoint
        X = np.zeros((self.current_particles, self.tau))
        Y = np.zeros((self.current_particles, self.tau))
        Z = np.zeros((self.current_particles, self.tau))

        # loop each iteration
        seg_start = 0
        for iter in tqdm(range(self.first_iter, self.last_iter + 1, self.step_iter), 
                         desc="Data 3D", disable=self.no_pbar):
            # then go through and add all segments/walkers in the iteration
            X[seg_start:seg_start + self.n_particles[iter - 1]] = \
                self._get_data_array(self.Xname, self.Xindex, iter)
            Y[seg_start:seg_start + self.n_particles[iter - 1]] = \
                self._get_data_array(self.Yname, self.Yindex, iter)
            Z[seg_start:seg_start + self.n_particles[iter - 1]] = \
                self._get_data_array(self.Zname, self.Zindex, iter)

            # keeps track of position in the seg_total length based arrays
            seg_start += self.n_particles[iter - 1]

        # 3D datasets using all available data (can be more managable with interval)
        return X[::interval], Y[::interval], Z[::interval]
    
    # TODO: very similar method to avg_datasets_3d, also could combine with code from get_total_dataset
    def average_datasets_4d(self, interval=1):
        """
        Unique case where `Zname` is specified and the XYZ datasets are returned.
        Averaged over the iteration range. With `Cname`, 4d.
        
        Returns
        -------
        X, Y, Z, C : arrays 
            Raw data for each named coordinate.
        """
        if self.Yname is None:
            warn("`Zname` is defined but not `Yname`, using Yname=`pcoord`")
            self.Yname = "pcoord"

        # arrays to be filled with values from each iteration
        # rows are for all segments, columns are each segment datapoint
        X = np.zeros((self.current_particles, self.tau))
        Y = np.zeros((self.current_particles, self.tau))
        Z = np.zeros((self.current_particles, self.tau))
        C = np.zeros((self.current_particles, self.tau))

        # loop each iteration
        seg_start = 0
        for iter in tqdm(range(self.first_iter, self.last_iter + 1, self.step_iter), 
                         desc="Data 4D", disable=self.no_pbar):
            # then go through and add all segments/walkers in the iteration
            X[seg_start:seg_start + self.n_particles[iter - 1]] = \
                self._get_data_array(self.Xname, self.Xindex, iter)
            Y[seg_start:seg_start + self.n_particles[iter - 1]] = \
                self._get_data_array(self.Yname, self.Yindex, iter)
            Z[seg_start:seg_start + self.n_particles[iter - 1]] = \
                self._get_data_array(self.Zname, self.Zindex, iter)
            C[seg_start:seg_start + self.n_particles[iter - 1]] = \
                self._get_data_array(self.Cname, self.Cindex, iter)

            # keeps track of position in the seg_total length based arrays
            seg_start += self.n_particles[iter - 1]

        # 4D datasets using all available data (can be more managable with interval)
        return X[::interval], Y[::interval], Z[::interval], C[::interval]

    def get_all_weights(self):
        """
        Returns an 1D array of the weight for every frame of each tau 
        for all segments of all iterations specified.

        Returns
        -------
        weights_expanded : array
        """
        # weights per seg of each iter, but need for each frame
        weights_1d = np.concatenate(self.weights)

        # need each weight value to be repeated for each tau (e.g. 100 + 1) 
        # will be same shape as X or Y made into 1d shape
        weights_expanded = np.zeros(self.tau * self.current_particles)

        # loop over all ps intervals up to tau in each segment
        weight_index = 0
        for seg in weights_1d:
            # TODO: can I do this without the unused loop?
            for frame in range(self.tau):
                weights_expanded[weight_index] = seg
                weight_index += 1

        return weights_expanded

    # TODO: option for data and weight output for a single iteration (iteration=None)
    # wait, isn't that already available in _get_data_array?
    def get_total_data_array(self, name, index=0, interval=1, reshape=True):
        """
        Loop through all iterations specified and get a 1d raw data array.
        # TODO: this could be organized better with my other methods
        maybe I can separate the helper functions into another class
        for extracting and moving data around, this pdist class could
        be used strictly for making pdists from a nice and standard data
        array input that is handled by the H5_Processing class

        Parameters
        ----------
        name : str
            Name of data from h5 file such as `pcoord` or an aux dataset.
        index : int
            Index of the data from h5 file.
        interval : int
            If more sparse data is needed for efficiency.
        reshape : bool
            Option to reshape into 1d array instead of each seg for all tau values.

        Returns
        -------
        data : 1d array
            Raw (unweighted) data array for the name specified.
        """
        data = np.zeros((self.current_particles, self.tau))
        # account for non-pcoord input strings
        if name != "pcoord":
            name = "auxdata/" + name
    
        # loop each iteration
        seg_start = 0
        for iter in tqdm(range(self.first_iter, self.last_iter + 1, self.step_iter), 
                         desc="Getting Data Array", disable=self.no_pbar):
            # then go through and add all segments/walkers in the iteration
            data[seg_start : seg_start + self.n_particles[iter - 1]] = \
                self._get_data_array(name, index, iter)
            
            # keeps track of position in the seg_total length based arrays
            seg_start += self.n_particles[iter - 1]

        if reshape:
            return data[::interval].reshape(-1,1)
        else:
            return data[::interval]

    def reshape_total_data_array(self, array):
        """
        Take an input 1d array of the data values at every segment for each
        iteration, and reshape them to make pdists.

        Parameters
        ----------
        array : 1d array
            Data values at every segment for each iteration.

        Returns
        -------
        array : ndarray
            Now rows = segments, columns = frame until tau, depth = data dimensions.
        """
        # try except block for input from data array
        # which can be the correct shape if pulled from westpa (e.g. 100 ps + 1)
        # or if from agg MD sim, will just be (e.g. 100 ps)
        # also adding -1 in z dim for extra depth dimension compatibility

        # TODO: change total particles to iteration range to be able to use iter args with data arrays

        try:
            array = array.reshape(self.current_particles, self.tau, -1)
        # e.g. ValueError: cannot reshape array of size 303000 into shape (3000,100,newaxis)
        except ValueError as e:
            try:
                array = array.reshape(self.current_particles, self.tau - 1, -1)
                message = "\nYou may be using an input data array which did not include the rst file datapoints. " + \
                        "\nThis will work, but note that you shouldn't create a new H5 file using this array."
                warn(f"{e} {message}")
                # the case where the array does not have rst data included
                # put the new first column as the first value of each row (segment)
                # TODO: this is a temp hack for the no rst shape data
                # noting that both arrays must have same ndims for hstack
                #print(f"original shape: {array.shape}")
                #print(f"to stack shape: {np.atleast_3d(array[:,0,:]).shape}")
                # make array for all first col vals reshape so that the columns go depth wise
                firstcols = array[:,0,:].reshape(array.shape[0], 1, -1)
                array = np.hstack((firstcols, array))
                #print(f"new shape: {array.shape}")
            # for cases where the WE simulation didn't exit and make next empty iteration
            except ValueError:
                array = array.reshape(np.sum(self.h5["summary"]["n_particles"][self.first_iter-1:self.last_iter-1]), 
                                      self.tau - 1, -1)
                

        # TODO: the above works to solve the shape issue but if I wanted to fill out a new dataset in
        # the h5 file, it would be missing the first value, which links walkers.
        # maybe I can use the parent IDs to link it manually, but note I would have to
        # go through and parse by my self.n_particles array to separate iterations.
        # put conditional if shape[1] = tau vs tau - 1 for creating dataset (to add parent data point)
        # note that the first iteration I need to pull from somewhere else? It's calculated from the
        # original bstate file

        # Note, if the user includes the rst files like WESTPA does, it should look and process fine

        return array

    def make_new_h5(self, new_weights=None):
        """
        TODO: actually make a new h5 file, see bstate filter code, integrate all.
        If self.H5save_out is not None and X/Y/Zsave_name is not None.
        Saves out a new h5 file of name self.H5save_out with the current
        X/Y/Zname data into auxdata of h5 file with name of X/Y/Zsave_name.

        Parameters
        ----------
        new_weights : numpy object array
            Updated weight values, e.g. from skip_basis or succ_only.
        """
        # make copy of h5 file and open copy
        shutil.copyfile(self.h5_name, self.H5save_out)
        self.H5save_out = h5py.File(self.H5save_out, "r+")
        # replace weights
        if new_weights is not None:
            for idx, weight in enumerate(new_weights):
                self.H5save_out[f"iterations/iter_{idx+1:08d}/seg_index"]["weight"] = weight

        # create new dataset based on input XYZ data
        for iter in tqdm(range(self.first_iter, self.last_iter + 1, self.step_iter), 
                         desc="Creating new h5 dataset(s)", disable=self.no_pbar):
            if self.Xsave_name:
                self._get_data_array(self.Xname, self.Xindex, iter, self.H5save_out, self.Xsave_name)
            if self.Ysave_name:
                self._get_data_array(self.Yname, self.Yindex, iter, self.H5save_out, self.Ysave_name)
            if self.Zsave_name:
                self._get_data_array(self.Zname, self.Zindex, iter, self.H5save_out, self.Zsave_name)

    def pdist(self, normalize=True):
        """
        Main public method with pdist generation controls.

        Parameters
        ----------
        normalize : bool
            By default (True), normalizes the output pdist.
            Must be True when using multiple h5 input files.
        
        Returns
        -------
        X, Y, Z : arrays
            Output probability distributions.
        """ 
        # empty object to pass to make_new_h5
        new_weights = None
        # option to zero weight out specific basis states
        if self.skip_basis is not None:
            self.n_bstates = self.h5["ibstates/index"]["n_bstates"]
            try: 
                new_weights = self.weights = self._new_weights_from_skip_basis()
            # if the wrong amount of args are input and != n_bstates
            except IndexError as e:
                message = f"IndexError ({e}) for bstate input ({self.skip_basis}): " + \
                          f"Did you use the correct amount of bstates {self.n_bstates}?"
                warn(message)

        # option to only use weights for succ trajs
        if self.succ_only is True:
            # replace the original weight array with succ only
            new_weights = self.weights = self.succ_pdist_weight_filter()

        # if requested, save out a new H5 file with the input data array in new aux name
        if self.H5save_out is not None:
            self.make_new_h5(new_weights)

        # TODO: need to consolidate the Y 2d vs 1d stuff somehow

        # multi_h5: putting the whole thing in a loop over each h5 file
        # loop histranges to find the best hist range for all input h5 files
        # loop each pdist return, sum and normalize at the end

        # collect each histrange for each file 
        xranges = []
        yranges = []
        # go through each file and find a consistent histrange if histrangeXY is None
        for i, h5 in enumerate(self.h5_list):
            # only needs to be done for non-first dataset in h5_list
            if i != 0:
                # close and re-open, keeping the class attribute for method calls
                # but allowing the loop to propagate through each file
                self.h5.close()
                self.h5 = h5py.File(h5, mode="r")
            if self.histrange_x is None:
                # get the optimal histrange
                xranges.append(self._get_histrange(self.Xname, self.Xindex))
                histrange_x = (min(i[0] for i in xranges),
                               max(i[1] for i in xranges))
            # 2D pdist: needs to handle array input or None input
            if isinstance(self.Yname, (str, np.ndarray)) and self.histrange_y is None:
                yranges.append(self._get_histrange(self.Yname, self.Yindex))
                histrange_y = (min(i[0] for i in yranges),
                               max(i[1] for i in yranges))
        # set final ranges
        if self.histrange_x is None:
            self.histrange_x = histrange_x
        # 2D pdist: needs to handle array input or None input
        if isinstance(self.Yname, (str, np.ndarray)) and self.histrange_y is None:
            self.histrange_y = histrange_y

        # collect each iteration's XYZ arrays for potential summation
        Xs = []
        Ys = []
        Zs = []
        Cs = []
        # same loop but now use the optimized histrange for pdist gen of all h5 files in list
        for i, h5 in enumerate(self.h5_list):
            # only needs to be done for non-first dataset in h5_list
            # at first I thought that was the case, but because the above loop to generate the histrange
            # ends at the last h5 file, we need to reset here
            ### if i != 0:
            # but I can still skip this step, which is redundant when the list is length one
            if len(self.h5_list) > 1:
                # close and re-open, keeping the class attribute for method calls
                # but allowing the loop to propagate through each file
                self.h5.close()
                self.h5 = h5py.File(h5, mode="r")
                self._init_weights()
                
                # TODO: instead of just opening h5 and re-init weights, need to also account for
                # cases like with 3D dataset returns which use self.n_particles (segs per iter)
                # perhaps I can just reinit the entire set of attrs
                #self.h5 = h5
                #self.__init__(self)
                
                # TODO: maybe this could go into a _particle_init method?
                # for now just going to save a new self.n_particles attribute
                self.n_particles = self.h5["summary"]["n_particles"]
                # these may not be needed, 
                self.current_particles = np.sum(self.h5["summary"]["n_particles"][self.first_iter-1:self.last_iter])
                # do not include the final (empty) iteration
                self.total_particles = np.sum(self.h5["summary"]["n_particles"][:-1])

            # scale weights by n h5 files
            self.weights /= len(self.h5_list)

            # TODO: need a better way to always return XYZ (currently using ones)
            #       this is needed for easy testing with uniform XYZ 3 array returns
            #       but maybe a different test strategy would also work
            # TODO: tuple unpacking to deal with variable item return? (this affects super.init of H5_Plot)
            if self.data_type == "evolution":
                x, y, z = self.evolution_pdist()
            elif self.data_type == "instant":
                if self.Yname and self.Zname:
                    x, y, z = self.instant_datasets_3d()
                elif self.Yname:
                    x, y, z = self.instant_pdist_2d()
                else:
                    x, y = self.instant_pdist_1d()
                    z = np.ones((self.first_iter, self.last_iter))
            elif self.data_type == "average":
                # attemts to say, if not None, but has to be compatible with str and arrays
                if isinstance(self.Yname, (str, np.ndarray)) and isinstance(self.Zname, (str, np.ndarray)):
                    # for 4d plots
                    if isinstance(self.Cname, (str, np.ndarray)):
                        x, y, z, c = self.average_datasets_4d()
                    else:
                        x, y, z = self.average_datasets_3d()
                elif isinstance(self.Yname, (str, np.ndarray)):
                    x, y, z = self.average_pdist_2d()
                else:
                    x, y = self.average_pdist_1d()
                    z = np.ones((self.first_iter, self.last_iter))
        
            # append to master lists
            Xs.append(x)
            Ys.append(y)
            Zs.append(z)
            # optional C
            if 'c' in locals():
                Cs.append(c)

        # selectively normalize final probabilities (sometimes Y and sometimes Z)
        # no normalization needed with 3D data returns (Zname) for 3D scatter plots
        if self.data_type == "evolution" or self.Yname is not None and self.Zname is None:
            # for XY, just use the first file array
            X = Xs[0]
            Y = Ys[0]
            # sum each h5 file probability array and return original shape
            Z = np.sum(Zs, axis=0)
            if normalize:
                Z = self._normalize(Z, self.p_units)
        elif self.Yname is None:
            # for XZ, just use the first file array
            X = Xs[0]
            Z = Zs[0]                
            # sum each h5 file probability array and return original shape
            Y = np.sum(Ys, axis=0)
            if normalize:
                Y = self._normalize(Y, self.p_units)
        else:
            # for 3d data returns for scatter3d, stack list of XYZs
            X = np.concatenate(Xs)
            Y = np.concatenate(Ys)
            Z = np.concatenate(Zs)

        # safely close h5 file
        # TODO: not doing this since methods e.g. for tracing need access to h5 file
        #self.h5.close()

        # for optional Cname 4D returns
        if isinstance(self.Cname, (str, np.ndarray)):
            C = np.concatenate(Cs)
            return X, Y, Z, C
        else:
            return X, Y, Z

if __name__ == "__main__":
    # total_array_out = np.loadtxt("p53_X_array.txt")
    # original_array = np.loadtxt("p53_X_array_noreshape.txt")
    # TODO: test Zname with data_array

    #h5pd = H5_Pdist("wedap/data/nacl.h5", data_type="evolution")
    #print(h5pd.w_succ())
    #h5pd.succ_pdist_weight_filter()

    h5pd = H5_Pdist("wedap/data/nacl.h5", data_type="average")
    print(h5pd.get_full_coords((10,1), "pcoord").shape)