# VarStrat

A tool for annotating VCF files using genome stratification files, targeting difficult regions.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install VarStrat.

```bash
pip install varstrat
```

## Usage
To use the tool from the command line:
```bash
varstrat input.vcf output.vcf data_source_dir
```


## Final Notes

1. **Make Sure the Script is Executable:**
   - Ensure `stratify.sh` is executable by running `chmod +x varstrat/stratify.sh`.
   - Also, make sure `stratify.py` is executable by running `chmod +x varstrat/stratify.py`.

2. **Verify the Help Option:**
   - Run your script with the `-h` or `--help` option to verify it displays the help message correctly:
     ```bash
     varstrat -h
     ```
