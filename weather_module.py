class Weather:
    def __init__(self, fh_array, fl_array, array_lengths, ws, wc):
        self._f_high_array = fh_array
        self._f_low_array = fl_array
        self._ws_mph = ws
        self._number_temperatures = array_lengths
        self._w_code = wc
        self._description = " "
        self.determine_description()

    def load_weekly_weather(self, fh_array, fl_array, ws, wc):
        self._f_high_array = fh_array
        self._f_low_array = fl_array
        self._ws_mph = ws
        self._w_code = wc
        self.determine_description()

    def calculate_average_fahrenheit_high_temp(self):
        return sum(self._f_high_array) / self._number_temperatures

    def calculate_average_fahrenheit_low_temp(self):
        return sum(self._f_low_array) / self._number_temperatures

    def find_weekly_fahrenheit_high_temp(self):
        highest_temp = self._f_high_array[0]
        for temp in self._f_high_array[1:self._number_temperatures]:
            if temp > highest_temp:
                highest_temp = temp
        return highest_temp

    def find_weekly_fahrenheit_low_temp(self):
        lowest_temp = self._f_low_array[0]
        for temp in self._f_low_array[1:self._number_temperatures]:
            if temp < lowest_temp:
                lowest_temp = temp
        return lowest_temp

    def determine_description(self):
        if self._w_code == 'S':
            self._description = "SUNNY"
        elif self._w_code == 'P':
            self._description = "PARTLY CLOUDY"
        elif self._w_code == 'C':
            self._description = "CLOUDY"
        elif self._w_code == 'N':
            self._description = "CLEAR"

    def display_today_weather(self):
        print("SUNDAY FORECAST")
        print(f"High: {self._f_high_array[0]} (F) Low: {self._f_low_array[0]} (F)")
        print(f"Conditions: {self._description}")
        print(f"Wind: {self._ws_mph} MPH")
        print()

    def display_weekly_weather(self):
        days = ["Sunday   ", "Monday   ", "Tuesday  ", "Wednesday",
                "Thursday ", "Friday   ", "Saturday "]

        print("THE WEEKLY FORECAST")
        print(f"Average Hi:  {self.calculate_average_fahrenheit_high_temp():.1f}")
        print(f"Average Low: {self.calculate_average_fahrenheit_low_temp():.1f}")
        print()
        print(f"Highest Weekly Temperature: {self.find_weekly_fahrenheit_high_temp()} (F)")
        print(f"Lowest Weekly Temperature:  {self.find_weekly_fahrenheit_low_temp()} (F)")
        print()

        for i in range(self._number_temperatures):
            print(days[i])
            print(f"High: {self._f_high_array[i]} (F) Low: {self._f_low_array[i]} (F)")
            print()