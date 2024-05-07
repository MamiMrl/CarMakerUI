import csv
import os  
import time

class SliderLogger:
    def __init__(self, participant_id):
        self.participant_id = participant_id
        self.log_file_path = f"{participant_id}_log_data.csv"
        self.setup_logger()

    def setup_logger(self):
        if not os.path.exists(self.log_file_path):
            with open(self.log_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Add other variables here later on when needed.
                writer.writerow(["Timestamp", "Steer Trq", "Acceleration", "Lane Offset", "Deceleration", "Overtake", "Speed"])

    def log_value_change(self, values):
        with open(self.log_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([time.strftime("%Y-%m-%d %H: %M:%S"), *values])

