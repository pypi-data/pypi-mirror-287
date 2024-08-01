import os
import pyopenms as oms
from .filters import set_filter_parameters
from .utils import plot_spectrum

def preprocess_spectrum(file_path, param_combination, output_dir):
    """
    Args:
        file_path (str): Path to the mzML file.
        param_combination (dict): Dictionary of parameters for different filters.
        output_dir (str): Directory to save the processed spectrum.

    Returns:
        oms.MSExperiment: The preprocessed MS experiment.

    Example:
        >>> file_path = "path/to/file.mzML"
        >>> param_combination = {
        ...     "MorphologicalFilter": {"struc_elem_length": 3.0, "struc_elem_unit": "Thomson", "method": "tophat"},
        ...     "SavitzkyGolayFilter": {"polynomial_order": 2, "frame_length": 11},
        ...     "PeakPickerHiRes": {"signal_to_noise": 2.0},
        ...     "Normalizer": {"method": "to_TIC"}
        ... }
        >>> output_dir = "path/to/output"
        >>> preprocess_spectrum(file_path, param_combination, output_dir)
    """
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        exp = oms.MSExperiment()
        oms.MzMLFile().load(file_path, exp)

        # Baseline correction
        if 'MorphologicalFilter' in param_combination:
            morph_filter = oms.MorphologicalFilter()
            set_filter_parameters(morph_filter, param_combination['MorphologicalFilter'])
            morph_filter.filterExperiment(exp)

        # Smoothing
        if 'SavitzkyGolayFilter' in param_combination:
            sg_filter = oms.SavitzkyGolayFilter()
            set_filter_parameters(sg_filter, param_combination['SavitzkyGolayFilter'])
            sg_filter.filterExperiment(exp)

        # Centroiding
        if 'PeakPickerHiRes' in param_combination:
            peak_picker = oms.PeakPickerHiRes()
            picked_exp = oms.MSExperiment()
            set_filter_parameters(peak_picker, param_combination['PeakPickerHiRes'])
            peak_picker.pickExperiment(exp, picked_exp, True)
            exp = picked_exp

        # Normalization
        if 'Normalizer' in param_combination:
            normalizer = oms.Normalizer()
            set_filter_parameters(normalizer, param_combination['Normalizer'])
            normalizer.filterPeakMap(exp)

        return exp
    except Exception as e:
        print(f"Error processing file {file_path} with parameters {param_combination}: {str(e)}")
        return None

def merge_preprocessed_spectra(preprocessed_experiments):
    try:
        merger = oms.SpectraMerger()
        merged_exp = oms.MSExperiment()

        for exp in preprocessed_experiments:
            for spectrum in exp:
                merged_exp.addSpectrum(spectrum)

        # Set parameters for merging
        params = oms.Param()
        params.setValue("block_method:ms_levels", [1])
        params.setValue("block_method:rt_block_size", 1)  # Adjust as necessary
        params.setValue("block_method:rt_max_length", 0.0)  # No RT restriction, should be float
        params.setValue("mz_binning_width", 0.01)  # Adjust as necessary
        params.setValue("mz_binning_width_unit", "Da")
        merger.setParameters(params)

        merger.mergeSpectraBlockWise(merged_exp)

        return merged_exp
    except Exception as e:
        print(f"Error merging spectra: {str(e)}")
        return None
