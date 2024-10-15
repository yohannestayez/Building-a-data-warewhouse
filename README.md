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
pip install -r requirements.txt
```

### Running the Notebook
1. Ensure all your JSON files are in the `json_dir` specified in the code.
2. Set up the PostgreSQL database and update the `database_url` variable with the correct credentials.
3. Execute the notebook to load, clean, transform, and store the data.
4. The image resizing function will process all images in the specified directory.


### DBT Integration
As part of the data warehousing initiative, DBT (Data Build Tool) was utilized to facilitate data transformations and create a robust data pipeline. The integration with DBT provides a structured and modular approach to managing data transformations, ensuring high-quality and maintainable SQL code.

**Key Operations with DBT**:
- **Data Modeling**:

Created models that aggregate data from various sources, including cleaned data on Ethiopian medical businesses.
Defined relationships between tables to maintain data integrity and facilitate easier querying.
Transformations:

Developed SQL models for transforming raw data into a structured format suitable for analysis.
Implemented data cleaning processes such as removing duplicates, handling missing values, and standardizing formats directly within DBT.
Materializations:

Configured models to be materialized as tables in the PostgreSQL database, making it easier to query and analyze the data efficiently.
Ensured that transformed data is updated automatically with each run, maintaining the latest insights.
Version Control and Documentation:

Leveraged DBT's built-in version control capabilities to track changes in the data models over time.
Documented the models within the DBT framework to provide clear insights into the data transformation process, making it easier for team members to understand the workflow.
Execution:

The DBT models are executed in conjunction with the data cleaning and transformation processes, ensuring that the warehouse is populated with the latest, cleaned data ready for analysis.

To run the DBT models and update the data warehouse, you can execute the following command:

```bash
dbt run
```
The integration of DBT allows for future enhancements, such as the addition of new data sources and more complex transformations, all while maintaining the integrity and quality of the data warehouse.

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
