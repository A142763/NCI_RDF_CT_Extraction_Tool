# CDISC Controlled Terminology (CT) RDF/OWL Downloader

This Python script automates the download and extraction of **CDISC Controlled Terminology** RDF/OWL archives from the official **NCI EVS (National Cancer Institute Enterprise Vocabulary Services)** FTP site.

It organizes each downloaded version into a date-stamped directory for easy archival and retrieval.

---

## Features

* Downloads OWL ZIP archives for:

  * **CDASH** (Clinical Data Acquisition Standards Harmonization)
  * **SDTM** (Study Data Tabulation Model)
  * **SEND** (Standard for Exchange of Nonclinical Data)
  * **ADaM** (Analysis Data Model)
  * **Define-XML**
* Creates a structured local directory by standard and release date
* Automatically extracts downloaded ZIP archives and removes the original ZIP file
* Can run for **one standard** or **all standards** in a single execution

---

## Requirements

Python 3.x and the following Python packages:

* `beautifulsoup4`
* `urllib3`
* `certifi`
* `pycurl`

You can install them via:

```bash
pip install beautifulsoup4 urllib3 certifi pycurl
```

---

## Usage

1. **Set your local download location**
   Update the `location` variable inside the script to your desired path:

   ```python
   location = 'D:\\Data\\CT_OWL'
   ```

2. **Run the script**
   By default, the script is set to download **all standards**:

   ```python
   std = 'ALL'
   ```

   To target a single standard, change the value to one of:

   ```
   'CDASH', 'SDTM', 'SEND', 'ADaM', 'Define-XML'
   ```

3. **Execute**:

   ```bash
   python cdisc_ct_downloader.py
   ```

4. **Result**:
   The directory structure will look like:

   ```
   CT_OWL/
   ├── SDTM/
   │   ├── 2024-03-15/
   │   │   ├── sdtm_2024-03-15.owl
   │   └── 2023-12-01/
   ├── ADaM/
   │   └── 2024-01-20/
   └── ...
   ```

---

## Important Notes

* This script uses **web scraping** techniques to list available files. The archive structure could change in the future, breaking the script.
* Ensure you have permission and abide by the [NCI EVS terms of use](https://evs.nci.nih.gov/).
* This was originally written as a **personal learning project** in Python, so while functional, it’s not optimized for performance or error handling.

---

## Author

**Jimmy James**
GitHub: \[your-GitHub-username]

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
