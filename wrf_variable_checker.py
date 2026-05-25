import xarray as xr


REQUIRED_VARIABLES = [
    "QICE",
    "QCLOUD",
    "QVAPOR",
    "PBLH",
    "CLDFRA",
    "TSK",
    "HFX",
    "LH"
]


def check_variables(wrf_file):

    ds = xr.open_dataset(wrf_file)

    print("\n[CHECK] Scanning WRF variables...")

    for var in REQUIRED_VARIABLES:

        if var in ds.variables:
            print(f"[OK] {var}")
        else:
            print(f"[MISSING] {var}")
