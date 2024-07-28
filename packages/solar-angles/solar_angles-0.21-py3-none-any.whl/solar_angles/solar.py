import math
from datetime import datetime


# The calculations here are based on Chapter 6 of
# '   McQuiston, F.C. and J.D. Parker.  1998.
# '   Heating, Ventilating, and Air Conditioning Analysis and Design, Third Edition.
# '   John Wiley and Sons, New York.

# This was originally a class called SolarPosition, but that was actually a poor design
# The location is capable of moving each call, as well as the date/time.
# So there wasn't anything that needed to persist, and the arguments got funny between instantiation and function calls
# Thus it is just a little library of functions


class AngularValueType:
    """
    This class combines a numeric value with an angular measurement unit.

    Proper construction should call constructor with either radians=x or degrees=y; not both.
    The constructor will calculate the complementary.
    The value of the angle can then be retrieved from the .degrees or .radians value as needed.

    Another class member, called .valued is available to determine if the class members contain meaningful values.

    If the constructor is called without either argument, the .valued variable is False, and the numeric vars are None.

    If the constructor is called with both arguments, they will be assigned if they agree to within a small tolerance;
    otherwise a ValueError is thrown.
    """

    def __init__(self, radians=None, degrees=None):
        """
        Constructor for the class.  Call it with either radians or degrees, not both.

        >>> a = AngularValueType(radians=math.pi)
        >>> b = AngularValueType(degrees=180)
        """

        if not radians and not degrees:
            self.valued = False
            self.radians = None
            self.degrees = None
        elif radians and not degrees:
            self.valued = True
            self.radians = radians
            self.degrees = math.degrees(radians)
        elif degrees and not radians:
            self.valued = True
            self.radians = math.radians(degrees)
            self.degrees = degrees
        else:  # degrees and radians
            if abs(math.degrees(radians) - degrees) > 0.01:
                raise ValueError("Radians and Degrees both given but don't agree")
            self.valued = True
            self.radians = radians
            self.degrees = degrees

    def __str__(self) -> str:
        return f"{self.valued=}, {self.radians=}, {self.degrees=}"


def day_of_year(time_stamp: datetime) -> int:
    """
    Calculates the day of year (1-366) given a Python datetime.datetime instance.
    Basically a wrapper to ensure it is a full datetime instance .
    in subsequent calculations. If the type is *not* datetime.datetime, this will throw a TypeError.

    :param time_stamp: [Python datetime] The current date and time to be used in calculating day of year
    :returns: [Integer] [dimensionless] The day of year, from 1 to 365 for non-leap years and 1-366 for leap years.
    """
    if not type(time_stamp) is datetime:
        raise TypeError("Expected datetime.datetime type")
    return time_stamp.timetuple().tm_yday


def equation_of_time(time_stamp: datetime) -> float:
    """
    Calculates the Equation of Time for a given date.
    I wasn't able to get the McQuiston equation to match the values in the given table.
    I ended up using a different formulation here: http://holbert.faculty.asu.edu/eee463/SolarCalcs.pdf.

    :param time_stamp: [Python datetime] The current date and time to be used in this calculation of day of year.
    :returns: [Float] The equation of time, which is the difference between local civil time and local solar_angles time
    """
    degrees = (day_of_year(time_stamp) - 81.0) * (360.0 / 365.0)
    radians = math.radians(degrees)
    return 9.87 * math.sin(2 * radians) - 7.53 * math.cos(radians) - 1.5 * math.sin(radians)


def declination_angle(time_stamp: datetime) -> AngularValueType:
    """
    Calculates the Solar Declination Angle for a given date.
    The solar_angles declination angle is the angle between a line connecting the center of the sun and earth and the
    projection of that line on the equatorial plane. Calculation is based on McQuiston.

    :param time_stamp: [Python datetime] The current date and time to be used in this calculation of day of year.
    :returns: [AngularValueType] The solar_angles declination angle in an AngularValueType with both radian and degree versions
    """
    radians = math.radians((day_of_year(time_stamp) - 1.0) * (360.0 / 365.0))
    dec_angle_deg = 0.3963723 - 22.9132745 * math.cos(radians) + 4.0254304 * math.sin(radians) - 0.387205 * math.cos(
        2.0 * radians) + 0.05196728 * math.sin(2.0 * radians) - 0.1545267 * math.cos(
        3.0 * radians) + 0.08479777 * math.sin(3.0 * radians)
    return AngularValueType(degrees=dec_angle_deg)


def local_civil_time(time_stamp: datetime, daylight_savings_on: bool, longitude: float,
                     standard_meridian: float) -> float:
    """
    Calculates the local civil time for a given set of time and location conditions.
    The local civil time is the local time based on prime meridian and longitude.

    :param time_stamp: [Python datetime] The current date and time to be used in this calculation of day of year.
    :param daylight_savings_on: [Boolean] A flag if the current time is a daylight savings number.
                                If True, the hour is decremented.
    :param longitude: [Float] [degrees west] The current longitude in degrees west of the prime meridian.
                      For Golden, CO, the variable should be = 105.2.
    :param standard_meridian: [Float] [degrees west] The local standard meridian for the location, in degrees west
                              of the prime meridian.  For Golden, CO, the variable should be = 105.

    :returns: [Float] [hours] Returns the local civil time in hours for the given date/time/location
    """
    civil_hour = time_stamp.time().hour
    if daylight_savings_on:
        civil_hour -= 1
    local_civil_time_hours = civil_hour + time_stamp.time().minute / 60.0 + time_stamp.time().second / 3600.0 - 4 * (
            longitude - standard_meridian) / 60.0
    return local_civil_time_hours


def local_solar_time(time_stamp: datetime, daylight_savings_on: bool, longitude: float,
                     standard_meridian: float) -> float:
    """
    Calculates the local solar_angles time for a given set of time and location conditions.
    The local solar_angles time is the local civil time that has been corrected by the equation of time.

    :param time_stamp: [Python datetime] The current date and time to be used in this calculation of day of year.
    :param daylight_savings_on: [Boolean] A flag if the current time is a daylight savings number.
                                If True, the hour is decremented.
    :param longitude: [Float] [degrees west] The current longitude in degrees west of the prime meridian.
                      For Golden, CO, the variable should be = 105.2.
    :param standard_meridian: [Float] [degrees west] The local standard meridian for the location, in degrees west
                              of the prime meridian.  For Golden, CO, the variable should be = 105.

    :returns: [Float] [hours] Returns the local solar_angles time in hours for the given date/time/location
    """

    return local_civil_time(
        time_stamp, daylight_savings_on, longitude, standard_meridian
    ) + equation_of_time(time_stamp) / 60.0


def hour_angle(time_stamp: datetime, daylight_savings_on: bool, longitude: float,
               standard_meridian: float) -> AngularValueType:
    """
    Calculates the current hour angle for a given set of time and location conditions.
    The hour angle is the angle between solar_angles noon and the current solar_angles angle, so at local solar_angles noon the value
    is zero, in the morning it is below zero, and in the afternoon it is positive.

    :param time_stamp: [Python datetime] The current date and time to be used in this calculation of day of year.
    :param daylight_savings_on: [Boolean] A flag if the current time is a daylight savings number.
                                If True, the hour is decremented.
    :param longitude: [Float] [degrees west] The current longitude in degrees west of the prime meridian.
                      For Golden, CO, the variable should be = 105.2.
    :param standard_meridian: [Float] [degrees west] The local standard meridian for the location, in degrees west
                              of the prime meridian.  For Golden, CO, the variable should be = 105.

    :returns: [AngularValueType] The hour angle in an AngularValueType with both radian and degree versions
    """
    local_solar_time_hours = local_solar_time(time_stamp, daylight_savings_on, longitude, standard_meridian)
    hour_angle_deg = 15.0 * (local_solar_time_hours - 12)
    return AngularValueType(degrees=hour_angle_deg)


def altitude_angle(time_stamp: datetime, daylight_savings_on: bool, longitude: float, standard_meridian: float,
                   latitude: float) -> AngularValueType:
    """
    Calculates the current solar_angles altitude angle for a given set of time and location conditions.
    The solar_angles altitude angle is the angle between the sun rays and the horizontal plane.

    :param time_stamp: [Python datetime] The current date and time to be used in this calculation of day of year.
    :param daylight_savings_on: [Boolean] A flag if the current time is a daylight savings number.
                                If True, the hour is decremented.
    :param longitude: [Float] [degrees west] The current longitude in degrees west of the prime meridian.
                      For Golden, CO, the variable should be = 105.2.
    :param standard_meridian: [Float] [degrees west] The local standard meridian for the location, in degrees west
                              of the prime meridian.  For Golden, CO, the variable should be = 105.
    :param latitude: [Float] [degrees north] The local latitude for the location, in degrees north of the equator.
                     For Golden, CO, the variable should be = 39.75.

    :returns: [AngularValueType] The solar_angles altitude angle in an AngularValueType with both radian and degree versions
    """
    declination_radians = declination_angle(time_stamp).radians
    hour_radians = hour_angle(time_stamp, daylight_savings_on, longitude, standard_meridian).radians
    latitude_radians = math.radians(latitude)
    altitude_radians = math.asin(
        math.cos(latitude_radians) * math.cos(declination_radians) * math.cos(hour_radians) + math.sin(
            latitude_radians) * math.sin(
            declination_radians))
    return AngularValueType(radians=altitude_radians)


def azimuth_angle(time_stamp: datetime, daylight_savings_on: bool, longitude: float, standard_meridian: float,
                  latitude: float) -> AngularValueType:
    """
    Calculates the current solar_angles azimuth angle for a given set of time and location conditions.
    The solar_angles azimuth angle is the angle in the horizontal plane between due north and the sun.
    It is measured clockwise, so that east is +90 degrees and west is +270 degrees.

    :param time_stamp: [Python datetime] The current date and time to be used in this calculation of day of year.
    :param daylight_savings_on: [Boolean] A flag if the current time is a daylight savings number.
                                If True, the hour is decremented.
    :param longitude: [Float] [degrees west] The current longitude in degrees west of the prime meridian.
                      For Golden, CO, the variable should be = 105.2.
    :param standard_meridian: [Float] [degrees west] The local standard meridian for the location, in degrees west
                              of the prime meridian.  For Golden, CO, the variable should be = 105.
    :param latitude: [Float] [degrees north] The local latitude for the location, in degrees north of the equator.
                     For Golden, CO, the variable should be = 39.75.

    :returns: [AngularValueType] The solar_angles azimuth angle in an AngularValueType with both radian and degree versions.
              NOTE: If the sun is down, the Float values in the dictionary are None.
    """
    declination_radians = declination_angle(time_stamp).radians
    altitude_degrees = altitude_angle(time_stamp, daylight_savings_on, longitude, standard_meridian, latitude).degrees
    altitude_radians = math.radians(altitude_degrees)
    if altitude_degrees < 0:  # sun is down
        return AngularValueType()
    latitude_radians = math.radians(latitude)
    hour_radians = hour_angle(time_stamp, daylight_savings_on, longitude, standard_meridian).radians
    acos_from_south = math.acos(
        (math.sin(altitude_radians) * math.sin(latitude_radians) - math.sin(declination_radians)) / (
                math.cos(altitude_radians) * math.cos(latitude_radians)))
    if hour_radians < 0:
        azimuth_from_south = acos_from_south
    else:
        azimuth_from_south = -acos_from_south
    azimuth_angle_radians = math.radians(180) - azimuth_from_south
    return AngularValueType(radians=azimuth_angle_radians)


def wall_azimuth_angle(time_stamp: datetime, daylight_savings_on: bool, longitude: float, standard_meridian: float,
                       latitude: float, surface_azimuth_deg: float) -> AngularValueType:
    """
    Calculates the current wall azimuth angle for a given set of time/location conditions, and a surface orientation.
    The wall azimuth angle is the angle in the horizontal plane between the solar_angles azimuth
    and the vertical wall's outward facing normal vector.

    :param time_stamp: [Python datetime] The current date and time to be used in this calculation of day of year.
    :param daylight_savings_on: [Boolean] A flag if the current time is a daylight savings number.
                                If True, the hour is decremented.
    :param longitude: [Float] [degrees west] The current longitude in degrees west of the prime meridian.
                      For Golden, CO, the variable should be = 105.2.
    :param standard_meridian: [Float] [degrees west] The local standard meridian for the location, in degrees west
                              of the prime meridian.  For Golden, CO, the variable should be = 105.
    :param latitude: [Float] [degrees north] The local latitude for the location, in degrees north of the equator.
                     For Golden, CO, the variable should be = 39.75.
    :param surface_azimuth_deg: [Float] [degrees CW from North] The angle between north and the outward facing
                                normal vector of the wall, measured as positive clockwise from south
                                (southwest facing surface: 225, northwest facing surface: 315)

    :returns: [AngularValueType] The wall azimuth angle in an AngularValueType with both radian and degree versions.
              NOTE: If the sun is behind the surface, the Float values in the dictionary are None.
    """
    this_surface_azimuth_deg = surface_azimuth_deg % 360
    solar_azimuth = azimuth_angle(time_stamp, daylight_savings_on, longitude, standard_meridian, latitude).degrees
    if solar_azimuth is None:  # sun is down
        return AngularValueType()
    wall_azimuth_degrees = solar_azimuth - this_surface_azimuth_deg
    if wall_azimuth_degrees > 90 or wall_azimuth_degrees < -90:
        return AngularValueType()
    return AngularValueType(degrees=wall_azimuth_degrees)


def solar_angle_of_incidence(time_stamp: datetime, daylight_savings_on: bool, longitude: float,
                             standard_meridian: float, latitude: float,
                             surface_azimuth_deg: float) -> AngularValueType:
    """
    Calculates the solar_angles angle of incidence for a given set of time and location conditions, and a surface orientation.
    The solar_angles angle of incidence is the angle between the solar_angles ray vector incident on the surface,
    and the outward facing surface normal vector.

    :param time_stamp: [Python datetime] The current date and time to be used in this calculation of day of year.
    :param daylight_savings_on: [Boolean] A flag if the current time is a daylight savings number.
                                If True, the hour is decremented.
    :param longitude: [Float] [degrees west] The current longitude in degrees west of the prime meridian.
                      For Golden, CO, the variable should be = 105.2.
    :param standard_meridian: [Float] [degrees west] The local standard meridian for the location, in degrees west
                              of the prime meridian.  For Golden, CO, the variable should be = 105.
    :param latitude: [Float] [degrees north] The local latitude for the location, in degrees north of the equator.
                     For Golden, CO, the variable should be = 39.75.
    :param surface_azimuth_deg: [Float] [degrees CW from North] The angle between north and the outward facing
                                normal vector of the wall, measured as positive clockwise from south
                                (southwest facing surface: 225, northwest facing surface: 315)

    :returns: [AngularValueType] The solar_angles angle of incidence in an AngularValueType with both radian & degree versions.
              NOTE: If the sun is down, or behind the surface, the Float values in the dictionary are None.
    """
    wall_azimuth_rad = wall_azimuth_angle(time_stamp, daylight_savings_on, longitude, standard_meridian, latitude,
                                          surface_azimuth_deg).radians
    if wall_azimuth_rad is None:
        return AngularValueType()
    altitude_rad = altitude_angle(time_stamp, daylight_savings_on, longitude, standard_meridian, latitude).radians
    incidence_angle_radians = math.acos(math.cos(altitude_rad) * math.cos(wall_azimuth_rad))
    return AngularValueType(radians=incidence_angle_radians)


def direct_radiation_on_surface(time_stamp: datetime, daylight_savings_on: bool, longitude: float,
                                standard_meridian: float, latitude: float,
                                surface_azimuth_deg: float, horizontal_direct_irradiation: float) -> float:
    """
    Calculates the amount of direct solar_angles radiation incident on a surface for a set of time and location conditions,
    a surface orientation, and a total global horizontal direct irradiation. This is merely the global horizontal
    direct solar_angles irradiation times the angle of incidence on the surface.

    :param time_stamp: [Python datetime] The current date and time to be used in this calculation of day of year.
    :param daylight_savings_on: [Boolean] A flag if the current time is a daylight savings number.
                                If True, the hour is decremented.
    :param longitude: [Float] [degrees west] The current longitude in degrees west of the prime meridian.
                      For Golden, CO, the variable should be = 105.2.
    :param standard_meridian: [Float] [degrees west] The local standard meridian for the location, in degrees west
                              of the prime meridian.  For Golden, CO, the variable should be = 105.
    :param latitude: [Float] [degrees north] The local latitude for the location, in degrees north of the equator.
                     For Golden, CO, the variable should be = 39.75.
    :param surface_azimuth_deg: [Float] [degrees CW from North] The angle between north and the outward facing
                                normal vector of the wall, measured as positive clockwise from south
                                (southwest facing surface: 225, northwest facing surface: 315)
    :param horizontal_direct_irradiation: [Float] [any] The global horizontal direct irradiation at the location.

    :returns: [Float] The incident direct radiation on the surface.
              The units of this return value match the units of the parameter :horizontalDirectIrradiation:
    """
    theta = solar_angle_of_incidence(time_stamp, daylight_savings_on, longitude, standard_meridian, latitude,
                                     surface_azimuth_deg).radians
    return horizontal_direct_irradiation * math.cos(theta)
