import csv
import os  
import time

class SliderLoggerPlacebo:
    def __init__(self, participant_id):
        self.participant_id = participant_id
        self.log_file_path = f"{participant_id}_placebo_logger_002.csv"
        self.setup_logger()

    def setup_logger(self):
        if not os.path.exists(self.log_file_path):
            with open(self.log_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Add other variables here later on when
