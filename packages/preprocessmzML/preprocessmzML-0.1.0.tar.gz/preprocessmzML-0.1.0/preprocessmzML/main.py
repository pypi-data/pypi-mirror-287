import os
import pyopenms as oms
import argparse
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from .preprocess import preprocess_spectrum, merge_preprocessed_spectra
from .utils import get_param_combinations

def process_groups(file_groups, output_base_dir, param_combinations):
    for param_combination in param_combinations:
        # Create a single directory for the given parameter combination
        combination_dir = os.path.join(output_base_dir, "_".join([f"{key}_{value}" for key, value in param_combination.items()]))
        if not os.path.exists(combination_dir):
            os.makedirs(combination_dir)

        for base_name, file_paths in file_groups.items():
            merged_experiments = []
            for fp in file_paths:
                preprocessed_exp = preprocess_spectrum(fp, param_combination, combination_dir)
                if preprocessed_exp is not None:
                    merged_experiments.append(preprocessed_exp)

            if merged_experiments:
                merged_experiment = merge_preprocessed_spectra(merged_experiments)
                if merged_experiment is not None:
                    output_path = os.path.join(combination_dir, f"{base_name}_merged.mzML")
                    oms.MzMLFile().store(output_path, merged_experiment)
                    print(f"Saved merged spectrum to {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Preprocess mzML files with different parameter combinations.')
    parser.add_argument('--data_dir', type=str, required=True, help='Directory containing the mzML files.')
    parser.add_argument('--output_base_dir', type=str, required=True, help='Directory to save the preprocessed files.')

    args = parser.parse_args()
    
    param_grid = {
        'MorphologicalFilter': [
            {"struc_elem_length": 3.0, "struc_elem_unit": "Thomson", "method": "tophat"}
        ],
        'SavitzkyGolayFilter': [
            {'polynomial_order': 2, 'frame_length': 7},
            {'polynomial_order': 2, 'frame_length': 11},
            {'polynomial_order': 3, 'frame_length': 7},
            {'polynomial_order': 3, 'frame_length': 11},
            {'polynomial_order': 4, 'frame_length': 7},
            {'polynomial_order': 4, 'frame_length': 11}
        ],
        'PeakPickerHiRes': [{'signal_to_noise': 1.0}, {'signal_to_noise': 2.0}, {'signal_to_noise': 3.0}],
        'Normalizer': [{'method': 'to_one'}, {'method': 'to_TIC'}]
    }

    param_combinations = get_param_combinations(param_grid)
    
    files_by_base = defaultdict(list)
    for filename in os.listdir(args.data_dir):
        if filename.endswith(".mzML"):
            base_name = "_".join(filename.split("_")[:-1])
            files_by_base[base_name].append(os.path.join(args.data_dir, filename))

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(process_groups, files_by_base, args.output_base_dir, param_combinations)]

        for future in as_completed(futures):
            try:
                future.result()
            except Exception as exc:
                print(f'Generated an exception: {exc}')

    print("Processing completed.")

if __name__ == "__main__":
    main()
