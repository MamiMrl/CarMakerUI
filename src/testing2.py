import customtkinter as ctk
from tkinter import Tk, font
from pycarmaker import CarMaker, Quantity
import time
from logger import SliderLogger

class TeslaStyleApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Tesla Style Slider')
        self.geometry('1920x1080')

        # Set the Tesla-style color theme
        self.configure(bg='#333333')  # Dark background
        ctk.set_appearance_mode("Dark")  # Dark theme for customtkinter
        ctk.set_default_color_theme("dark-blue")  # Blue accents

        # Verify if Gotham font is available
        available_fonts = list(font.families())
        self.custom_font = ('Gotham', 12) if 'Gotham' in available_fonts else ('Arial', 12)
        
        # Initialize and connect to CarMaker
        self.init_carmaker()

        # Add sliders and labels
        # self.add_slider('brake', 'Brake Level: 0', from_=0, to=1, row=0)
        # self.add_slider('driver_brake', 'Driver Brake: 0 m/s²', from_=-0, to=1, row=1)  # example range
        self.add_slider('steer_trq', 'Steering Torque: 0', from_=-3.0, to=3.0, row=2)  # -π to π radians
        # self.add_slider('long_accel', 'Longitudinal Acceleration: 0 m/s²', from_=-3.0, to=3.0, row=3)  # example range
        self.add_slider('accel', 'Acceleration: 0 m/s²', from_=-3.0, to=3.0, row=4)  # example range
        self.add_slider('lane_change', 'Timing Lane Change: 0²', from_=-2.0, to=2.0, row=5)  # example range
        self.add_slider('speed', 'Speed: 0 km/h', from_=0.0, to=200.0, row=6)  # example range
        # self.add_slider('following_distance', 'Following Distance: 0²', from_=0.0, to=200.0, row=7)  # example range
        self.add_slider('decel', 'Deceleration: 0 m/s²', from_=-3.0, to=3.0, row=8)  # example range
        self.add_slider('overtake', 'Overtake: 0', from_=0.0, to=1.0, row=9)  # example range

        # Change participant id variable each time testing takes place
        self.logger = SliderLogger(participant_id="test")

    def add_slider(self, name, text, from_, to, row):
        slider = ctk.CTkSlider(self, from_=from_, to=to)
        slider.pack(pady=20, padx=20)
        setattr(self, f"{name}_slider", slider)
        
        slider_label = ctk.CTkLabel(self, text=text)
        slider_label.pack(pady=10)
        slider_label.configure(font=self.custom_font)
        setattr(self, f"{name}_slider_label", slider_label)
        
        slider.bind('<Motion>', getattr(self, f"update_{name}_value"))

    # def update_brake_value(self, event):
    #     value = self.brake_slider.get()
    #     self.brake_slider_label.configure(text=f"Brake Level: {value:.2f}")
    #     self.cm.DVA_write(self.qbrake, value)

    def update_steer_trq_value(self, event):
        value = self.steer_trq_slider.get()
        self.steer_trq_slider_label.configure(text=f"Steering Torque: {value:.2f} rad")
        self.cm.DVA_write(self.qsteer_trq, value)
        self.logger.log_value_change([value, None, None, None, None, None])  # Log the value

    def update_accel_value(self, event):
        value = self.accel_slider.get()
        self.accel_slider_label.configure(text=f"Acceleration: {value:.2f} m/s²")
        self.cm.DVA_write(self.qacceleration, value)
        self.logger.log_value_change([None, value, None, None, None, None])  # Log the value

    def update_lane_change_value(self, event):
        value = self.lane_change_slider.get()
        self.lane_change_slider_label.configure(text=f"Timing Lane Change: {value:.2f}")
        self.cm.DVA_write(self.qlane_change_time, value)
        self.logger.log_value_change([None, None, value, None, None, None])  # Log the value

    def update_speed_value(self, event):
        value = self.speed_slider.get()
        self.speed_slider_label.configure(text=f"Timing Lane Change: {value:.2f}")
        self.cm.DVA_write(self.qspeed, value)
        self.logger.log_value_change([None, None, None, None, None, value])

    def update_decel_value(self, event):
        value = self.decel_slider.get()
        self.decel_slider_label.configure(text=f"Deceleration: {value:.2f} m/s²")
        self.cm.DVA_write(self.qdeceleration, value)
        self.logger.log_value_change([None, None, None, value, None, None])  # Log the value

    def update_overtake_value(self, event):
        value = self.overtake_slider.get()
        self.overtake_slider_label.configure(text=f"Overtake: {value:.2f}")
        self.cm.DVA_write(self.qovertake, value) 
        self.logger.log_value_change([None, None, None, None, value, None])  # Log the value

    def init_carmaker(self):
        # Change IP_ADDRESS to 192.168.1.240 in Lab
        IP_ADDRESS = "localhost"
        PORT = 16660
        self.cm = CarMaker(IP_ADDRESS, PORT)
        self.cm.connect()
        # self.qbrake = Quantity("DM.Brake", Quantity.FLOAT)
        # self.qdriver_brake = Quantity("Driver.Brake", Quantity.FLOAT)
        self.qsteer_trq = Quantity("Driver.Steer.Trq", Quantity.FLOAT)
        # self.qlong_accel = Quantity("AccelCtrl.ACC.DesiredAx", Quantity.FLOAT)
        self.qacceleration = Quantity("Driver.ReCon.Accel", Quantity.FLOAT)
        self.qlane_change_time = Quantity("DM.LaneOffset", Quantity.FLOAT)
        self.qspeed = Quantity("Driver.ReCon.Speed", Quantity.FLOAT)
        # self.qfollow_dist = Quantity("AccelCtrl.ACC.DesiredDist", Quantity.FLOAT)
        self.qdeceleration = Quantity("Driver.ReCon.Decel", Quantity.FLOAT)
        self.qovertake = Quantity("Driver.ReCon.Trf_Overtake", Quantity.INT)

# Run the application
if __name__ == "__main__":
    app = TeslaStyleApp()
    app.mainloop()
