import csv
import os  
import time

class SliderLogger:
    def __init__(self, participant_id):
        self.participant_id = participant_id
        self.log_file_path = f"{participant_id}_test_participant_HiNo_LoOp_027.csv"
        self.setup_logger()

    def setup_logger(self):
        if not os.path.exists(self.log_file_path):
            with open(self.log_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Add other variables here later on when needed.
                writer.writerow(["Timestamp", "Acceleration", "Deceleration", "Lane Offset", "Consider Overtake", "Overtake", "Steer Trq", "Steer Accel", "Steer Veloc", "Speed"])


    def log_value_change(self, values):
        with open(self.log_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([time.strftime("%Y-%m-%d %H: %M:%S"), *values])

