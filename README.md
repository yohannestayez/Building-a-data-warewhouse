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

### image_processing.ipynb: 
1. **Data Validation**: The paths for the training images, labels, and data.yaml configuration file are validated to ensure that the directories and files exist before starting the training.
2. **Training Setup**: Training parameters such as epochs, batch_size, and img_size are configured. The notebook uses a subprocess to run the YOLOv5 training script with these parameters.
3. **Running YOLOv5 Training**: The training process is executed using the YOLOv5 train.py script, where the dataset paths and configuration are passed through the data.yaml file.
4. **Post-training Weight Management**: After training, the notebook locates the best and last weights, logs them, and saves the final model weights as labeled_yolov5_model.pt.
5. **Database saving**: finally detectction results are saved to our warehouse database



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
  - `roboflow`
  - `torch`
  - `torchvision`
  
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
Logs will be saved in the `data_cleaning_task2.log` and `yolo_training.log` file. This file will contain a record of processed files, errors encountered, and other relevant information.

### FastAPI CRUD Application
A FastAPI-based app exposing data collected from YOLOv5 object detection, with PostgreSQL as the backend.

**Features**
- CRUD API for detection data.
- PostgreSQL database using SQLAlchemy.
- Pydantic for data validation.

**Steps**
1. Clone the Repository:
  ```
  git clone https://github.com/yohannestayez/Building-a-data-warewhouse.git
  ```
2. Install Dependencies:
  ```
  pip install -r requirements.txt
  ```
3. Configure Database: 
  Update database.py with your PostgreSQL credentials:
  ```
  DATABASE_URL = "postgresql://<username>:<password>@<host>:<port>/<database_name>"
  ```
4. Run the API:
  ```
  uvicorn App.main:app --reload
  ```
**API Endpoints**

- **GET /items/**: Retrieve all items.
- **GET /items/{id}**: Retrieve an item by ID.
- **POST /items/**: Create a new item.
- **PUT /items/{id}**: Update an item.
- **DELETE /items/{id}**: Delete an item.

**Docker Setup**
1. Create Dockerfile:
```bash
docker build -t fastapi-app .
```
2. Run Docker Container:
```bash
docker run -d -p 8000:8000 fastapi-app
```

## Contact
For any inquiries, feel free to reach out!

## Author
This project was developed by the data engineering team at Kara Solutions as part of a data warehouse initiative for Ethiopian medical businesses.
