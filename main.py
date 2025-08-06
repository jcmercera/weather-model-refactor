from weather_module import Weather

def main():
    # Main variables
    # fh = Fahrenheit High
    # fl = Fahrenheit Low
    # ws = Wind Speed in MPH
    # wc = Weather Code
    fh = [78, 76, 80, 82, 85, 79, 75]
    fl = [75, 70, 75, 76, 75, 70, 69]
    ws = 9
    number_temperatures = 7  # The number of temperatures is the same for the high and low temperature array lengths
    wc = 'S'

    # Initialize Weather type
    w = Weather(fh, fl, number_temperatures, ws, wc)

    # Call procedures to determine and display weather information
    w.determine_description()
    w.display_today_weather()
    w.display_weekly_weather()


if __name__ == "__main__":
    main()