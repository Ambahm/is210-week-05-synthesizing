#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fahrenheit to Celsius
   Celcius to Kelvin
   Fahrenheit to Kelvin"""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal(273.15)       # deciaml value


def fahrenheit_to_celsius(degrees):
    """This function converts Fahrenheit to Celcisus.

    Args:
        degrees (mixed): Fahrenheit input to be converted to Celsius.

    Returns:
        deci: Farenheit converted to celcisus as a decimal.

    Examples:
        >>> fahrenheit_to_celsius(212)
        Decimal('100')

        >>> fahrenheit_to_celsius(0)
        Decimal('-17.78')

    """
    celcius = (((decimal.Decimal(degrees) - 32) * 5) / 9)
    return celcius


def celsius_to_kelvin(degrees):
    """This function converts Celcisus to Kelvin.

    Args:
        degrees (mixed): Celcius input to be converted to Kelvin.

    Returns:
        deci: Celcius converted Kelvin as decimal.

    Examples:
        >>> celsius_to_kelvin(100)
        Decimal('373.15')

        >>> celsius_to_kelvin(0)
        Decimal('273.15')

    """
    kelvin = ABSOLUTE_DIFFERENCE + degrees
    return kelvin


def fahrenheit_to_kelvin(degrees):
    """This function converts Fahrenheit to Kelvin.

    Args:
        degrees (mixed): Fahrenheit input to be converted to Kelvin

    Returns:
        deci: Farenheit converted to Kelvin as a decimal.

    Examples:
       >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')

        >>> fahrenheit_to_kelvin(0)
        Decimal('255.37')

    """
    celcius = fahrenheit_to_celsius(degrees)        # celcius function

    # Calling Celcius, to get KELVIN using new celcius value

    kelvin = celsius_to_kelvin(celcius)
    return kelvin
