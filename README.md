Here’s an SEO-optimized rewrite of your CDISC project README that targets phrases like **“CDISC Controlled Terminology Downloader”**, **“CDISC RDF OWL Download”**, and **“CDISC CT Python Script”** so it’s more discoverable on GitHub and Google.

---

# CDISC Controlled Terminology (CT) RDF/OWL Downloader – Python Automation Tool

The **CDISC Controlled Terminology RDF/OWL Downloader** is a Python automation tool that downloads and extracts official **CDISC Controlled Terminology** archives directly from the **NCI EVS (National Cancer Institute Enterprise Vocabulary Services)** FTP repository.

With a single command, you can fetch the latest **CDISC RDF/OWL files** for multiple standards, organize them into date-stamped folders, and keep a clean local archive for easy retrieval.

---

## Key Features

* **Automatic Download** of OWL ZIP archives for:

  * **CDASH** – Clinical Data Acquisition Standards Harmonization
  * **SDTM** – Study Data Tabulation Model
  * **SEND** – Standard for Exchange of Nonclinical Data
  * **ADaM** – Analysis Data Model
  * **Define-XML** – Define Standards for Submission
* **Organized Output** – Saves each release into its own date-stamped directory by standard.
* **Batch or Single Standard** – Download all standards in one go or target a specific one.
* **ZIP Extraction** – Automatically unzips archives and removes the original ZIP.

---

## Requirements

* **Python 3.x**
* Required packages: `beautifulsoup4`, `urllib3`, `certifi`, `pycurl`
  Install via:

  ```bash
  pip install beautifulsoup4 urllib3 certifi pycurl
  ```

---

## Usage Instructions

1. **Set Download Path**
   Update the `location` variable inside the script:

   ```python
   location = 'D:\\Data\\CT_OWL'
   ```

2. **Choose Standards to Download**

   * Default: Download **all** standards

     ```python
     std = 'ALL'
     ```
   * Single standard options: `'CDASH', 'SDTM', 'SEND', 'ADaM', 'Define-XML'`

3. **Run the Script**

   ```bash
   python cdisc_ct_downloader.py
   ```

4. **Resulting Directory Structure**

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

## Notes & Disclaimers

* This script uses **web scraping** to list available files; changes in the NCI EVS site structure could require updates.
* Always review and comply with the [NCI EVS Terms of Use](https://evs.nci.nih.gov/).
* Originally built as a **Python learning project** — functional but not fully optimized for performance or error handling.

---

**Author:** Jimmy James
GitHub: A142763

---


## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
