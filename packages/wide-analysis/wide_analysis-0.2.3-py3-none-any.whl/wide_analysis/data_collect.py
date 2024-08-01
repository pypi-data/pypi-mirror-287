from datetime import datetime
from wide_analysis.data.process_data import prepare_dataset

def collect(mode, start_date=None, end_date=None, url=None, title=None, output_path=None):
    if mode not in ['date_range', 'date', 'title']:
        raise ValueError("Invalid mode. Choose from ['date_range', 'date', 'title']")

    return prepare_dataset(
        mode=mode,
        start_date=start_date,
        end_date=end_date,
        url=url,
        title=title,
        output_path=output_path
    )