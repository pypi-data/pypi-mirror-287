import json
from pathlib import Path

from allotropy.constants import CHARDET_ENCODING
from allotropy.parser_factory import Vendor
from allotropy.to_allotrope import allotrope_from_file

output_files = [
    "connect test 240716.csv",
    "test_utf8.csv",
    "Beckman_Vi-Cell-BLU_example01.csv",
]
vendor = Vendor.BECKMAN_VI_CELL_BLU


if __name__ == "__main__":
    # filename = "Beckman_Vi-Cell-XR_example02_instrumentOutput.xls"
    for filename in output_files:
        # read_mode = "fluorescence"
        # test_filepath = (
        #     f"tests/parsers/agilent_gen5/testdata/{read_mode}/{filename}.txt"
        # )
        # test_filepath = f"tests/parsers/luminex_xponent/testdata/{filename}.csv"
        test_filepath = f"{filename}"

        allotrope_dict = allotrope_from_file(
            test_filepath, vendor, encoding=CHARDET_ENCODING
        )
        target_filename = Path(test_filepath).with_suffix(".json").name
        # print(allotrope_dict)
        with open(target_filename, "w") as fp:
            fp.write(json.dumps(allotrope_dict, indent=4, ensure_ascii=False))
