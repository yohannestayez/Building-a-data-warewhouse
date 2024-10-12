# Data Cleaning and Transformation for Ethiopian Medical Businesses

## Project Overview

This projects initiative is to build a **data warehouse** for storing and analyzing data on Ethiopian medical businesses. The data
is collected from web scraping and Telegram channels, and the warehouse will integrate **object detection** capabilities using 
**YOLO**(You Only Look Once). The goal is to enhance data analysis by storing the cleaned, transformed, and standardized data for querying and reporting.

The data warehouse helps provide insights into trends, patterns, and correlations, which are critical for making informed business decisions.

## Notebooks

### Data_Cleaning_and_Transformation.ipynb: 
    This notebook performs the following key operations:
  1. **Data Loading**: Loads JSON data on Ethiopian medical businesses from a local directory.
  2. **Data Cleaning**: 
    - **Remove Duplicates**: Ensures no redundant data.
    - **Handle Missing Values**: Fills missing content and drops rows missing essential information.
    - **Standardize Formats**: Ensures consistent formatting, especially for dates and text fields.
    - **Validation**: Validates cleaned data to ensure it meets expected standards.
  3. **Database Integration**: After cleaning, the data is stored in a PostgreSQL database using SQLAlchemy.
  4. **Image Resizing for YOLO**: Resizes images to 416x416 to ensure they are ready for object detection using YOLO.
  5. **Error Handling and Logging**: Tracks errors and logs progress in a log file (`data_cleaning_task2.log`).

## Project Structure
- **Data Source**: JSON files containing Ethiopian medical business information, stored in `C:\Users\Administrator\Documents\kifiya\Week_7\Data`.
- **Image Data**: Image files associated with the businesses are resized and stored in `C:\Users\Administrator\Documents\kifiya\Week_7\Data\images`.
- **Logging**: All processes are logged, and any errors encountered during data cleaning or image processing are noted.

## Setup Instructions

### Prerequisites
- Python 3.x
- Required Python libraries:
  - `pandas`
  - `os`
  - `logging`
  - `sqlalchemy`
  - `Pillow`
  
Install the dependencies using:

```bash
pip install pandas sqlalchemy Pillow
```

### Running the Notebook
1. Ensure all your JSON files are in the `json_dir` specified in the code.
2. Set up the PostgreSQL database and update the `database_url` variable with the correct credentials.
3. Execute the notebook to load, clean, transform, and store the data.
4. The image resizing function will process all images in the specified directory.

### Logging
Logs will be saved in the `data_cleaning_task2.log` file. This file will contain a record of processed files, errors encountered, and other relevant information.

### Example Usage
To process the JSON files and store them in the database, simply run:

```python
process_json_files(json_dir)
```

To resize images for YOLO object detection:

```python
transform_images(image_folder)
```




## Author
This project was developed by the data engineering team at Kara Solutions as part of a data warehouse initiative for Ethiopian medical businesses.
