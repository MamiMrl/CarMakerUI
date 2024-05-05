import customtkinter as ctk
from tkinter import Tk, font
from pycarmaker import CarMaker, Quantity
import time

# Revising the provided code to improve the UI layout

class TeslaStyleApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Tesla Style Slider')
        self.geometry('700x300')

        # Set the Tesla-style color theme
        self.configure(bg='#333333')  # Dark background
        ctk.set_appearance_mode("Dark")  # Dark theme for customtkinter
        ctk.set_default_color_theme("dark-blue")  # Blue accents
        
        # Verify if Gotham font is available
        available_fonts = list(font.families())
        self.custom_font = ('Gotham', 12) if 'Gotham' in available_fonts else ('Arial', 12)
        
        # Initialize and connect to CarMaker
        self.init_carmaker()

        # Add sliders and labels with improved layout
        self.add_slider('driver_brake', 'Driver Brake: 0 m/s²', from_=-0, to=1, row=0, column=0)
        self.add_slider('steer_trq', 'Steering Torque: 0', from_=-3.0, to=3.0, row=0, column=1)
        self.add_slider('long_accel', 'Longitudinal Acceleration: 0 m/s²', from_=-3.0, to=3.0, row=1, column=0)
        self.add_slider('accel', 'Acceleration: 0 m/s²', from_=-3.0, to=3.0, row=1, column=1)
        self.add_slider('lane_change', 'Timing Lane Change: 0', from_=-300.0, to=300.0, row=2, column=0)
        self.add_slider('desired_speed', 'Speed: 0 km/h', from_=0.0, to=300.0, row=2, column=1)
        self.add_slider('decel', 'Deceleration: 0 m/s²', from_=-3.0, to=3.0, row=3, column=0)
        self.add_slider('overtake', 'Overtake: 0', from_=0.0, to=1.0, row=3, column=1)

    def add_slider(self, name, text, from_, to, row, column):
        # Improved spacing and alignment for UI elements
        grid_base_col = column * 6  # 6 grid cells per column to accommodate labels and slider
        label_width = 10  # Fixed width for Min/Max labels

        min_label = ctk.CTkLabel(self, text=f"Min: {from_}", width=label_width)
        min_label.grid(row=row, column=grid_base_col, pady=10, sticky='w')
        min_label.configure(font=self.custom_font)

        slider_label = ctk.CTkLabel(self, text=text)
        slider_label.grid(row=row, column=grid_base_col + 1, pady=10, columnspan=4, sticky='w')
        slider_label.configure(font=self.custom_font)

        slider = ctk.CTkSlider(self, from_=from_, to=to)
        slider.grid(row=row, column=grid_base_col + 1, pady=50, padx=20, columnspan=4, sticky='ew')
        self.grid_columnconfigure(grid_base_col + 1, weight=1)  # Expand slider

        max_label = ctk.CTkLabel(self, text=f"Max: {to}", width=label_width)
        max_label.grid(row=row, column=grid_base_col + 5, pady=80, sticky='e')
        max_label.configure(font=self.custom_font)

        slider.bind('<Motion>', getattr(self, f"update_{name}_value"))

        # Update the attribute setting to include label for dynamic updates
        setattr(self, f"{name}_slider", slider)
        setattr(self, f"{name}_slider_label", slider_label)

    # ... The rest of the class remains unchanged ...

# Comment out the actual execution part of the code
# if __name__ == "__main__":
#     app = TeslaStyleApp()
#     app.mainloop()




    # def update_brake_value(self, event):
    #     value = self.brake_slider.get()
    #     self.brake_slider_label.configure(text=f"Brake Level: {value:.2f}")
    #     self.cm.DVA_write(self.qbrake, value)

    def update_driver_brake_value(self, event):
        value = self.driver_brake_slider.get()
        self.driver_brake_slider_label.configure(text=f"Brake Level: {value:.2f}")
        self.cm.DVA_write(self.qdriver_brake, value)

    def update_steer_trq_value(self, event):
        value = self.steer_trq_slider.get()
        self.steer_trq_slider_label.configure(text=f"Steering Torque: {value:.2f} rad")
        self.cm.DVA_write(self.qsteer_trq, value)

    def update_long_accel_value(self, event):
        value = self.long_accel_slider.get()
        self.long_accel_slider_label.configure(text=f"Longitudinal Acceleration: {value:.2f} m/s²")
        self.cm.DVA_write(self.qlong_accel, value)

    def update_accel_value(self, event):
        value = self.accel_slider.get()
        self.accel_slider_label.configure(text=f"Acceleration: {value:.2f} m/s²")
        self.cm.DVA_write(self.qacceleration, value)

    def update_lane_change_value(self, event):
        value = self.lane_change_slider.get()
        self.lane_change_slider_label.configure(text=f"Timing Lane Change: {value:.2f}")
        self.cm.DVA_write(self.qlane_change_time, value)
    
    def update_desired_speed_value(self, event):
        value = self.speed_slider.get()
        self.speed_slider_label.configure(text=f"Speed: {value:.2f}")
        self.cm.DVA_write(self.qspeed, value)
    
    # def update_following_distance_value(self, event):
    #     value = self.following_distance_slider.get()
    #     self.following_distance_slider_label.configure(text=f"Following Distance: {value:.2f} m/s²")
    #     self.cm.DVA_write(self.qfollow_dist, value)

    def update_decel_value(self, event):
        value = self.deceleration_slider.get()
        self.deceleration_slider_label.configure(text=f"Deceleration: {value:.2f} m/s²")
        self.cm.DVA_write(self.qdeceleration, value)

    def update_overtake_value(self, event):
        value = self.overtake_slider.get()
        self.overtake_slider_label.configure(text=f"Overtake: {value:.2f}")
        self.cm.DVA_write(self.qovertake, value)

    def init_carmaker(self):
        # Change IP_ADDRESS to 192.168.1.240 in Lab
        IP_ADDRESS = "localhost"
        PORT = 16660
        self.cm = CarMaker(IP_ADDRESS, PORT)
        self.cm.connect()
        # self.qbrake = Quantity("DM.Brake", Quantity.FLOAT)
        self.qdriver_brake = Quantity("Driver.Brake", Quantity.FLOAT)
        self.qsteer_trq = Quantity("Driver.Steer.Trq", Quantity.FLOAT)
        self.qlong_accel = Quantity("AccelCtrl.ACC.DesiredAx", Quantity.FLOAT)
        self.qacceleration = Quantity("Driver.ReCon.Accel", Quantity.FLOAT)
        self.qlane_change_time = Quantity("DM.LaneOffset", Quantity.FLOAT)
        self.qspeed = Quantity("AccelCtrl.ACC.DesiredSpd", Quantity.FLOAT)
        # self.qfollow_dist = Quantity("AccelCtrl.ACC.DesiredDist", Quantity.FLOAT)
        self.qdeceleration = Quantity("Driver.ReCon.Decel", Quantity.FLOAT)
        self.qovertake = Quantity("Driver.ReCon.Trf_Overtake", Quantity.FLOAT)

# Run the application
if __name__ == "__main__":
    app = TeslaStyleApp()
    app.mainloop()
