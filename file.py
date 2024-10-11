# The uploaded file appears to be a Power BI file (.pbix). Let's load and inspect the contents to get an overview of the dashboard elements and key metrics.
import os

# Path to the uploaded file
file_path = 'D:/PowerBI projects/HR_ANALYTICS_DASHBOARD1.pbix'

# Checking the file size and type to confirm it's valid for further analysis
file_info = {
    "file_name": os.path.basename(file_path),
    "file_size_MB": os.path.getsize(file_path) / (1024 * 1024),  # size in MB
    "file_type": os.path.splitext(file_path)[-1]  # file extension
}

file_info
