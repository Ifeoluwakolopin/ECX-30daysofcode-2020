# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20  08:47:10 2020

@author: TheAre
"""
def intensive_properties(*args):

    '''
    iput format --> intensive_properties((pressure, temperature), (p_unit, t_unit))
    This takes in a tuple of the pressure and temperature values in SI units (N/m 2 and K) 
    and a tuple containing the desired output unit as parameters then returns a tuple of the pressure and
    temperature in the desired units.

    Example:
    intensive_properties((101325,298),(atm, o C)) returns (1,25)
    Note: (Valid output pressure units: ['Pa', 'atm', 'mmHg', 'Bar'] and valid output temperature units: [ 'oC', 'oF', 'oR'] ).'''


    pressure_units = ['Pa', 'atm', 'mmHg', 'Bar']
    temperature_units = ['oC', 'oF', 'oR']

    #Unpacking the arguments
    p = args[0][0]
    t = args[0][1]
    p_unit = args[1][0]
    t_unit = args[1][1]

    if p_unit.lower() == pressure_units[0].lower():
        final_pressure = p              # This is to convert N/m2 to Pascal
        unit1 = pressure_units[0]              
    elif p_unit.lower() == pressure_units[1].lower():
        final_pressure = p / 101325     #This is to convert N/m2 to atm
        final_pressure = round(final_pressure, 3)
        unit1 = pressure_units[1]
    elif p_unit.lower() == pressure_units[2].lower():
        final_pressure = p / 133        #This converts N/m2 to mmHg
        final_pressure = round(final_pressure, 3)
        unit1 = pressure_units[2]
    elif p_unit.lower() == pressure_units[3].lower():
        final_pressure = p / 100000     #This converts N/m2 to bar
        final_pressure = round(final_pressure, 3)
        unit1 = pressure_units[3]
    else:
        return('\nError: Unsupported Unit for Pressure')


    if t_unit.lower() == temperature_units[0].lower():
        final_temperature = t - 273                      # This converts Kelvin to Celcius
        unit2 = temperature_units[0]
    elif t_unit.lower() == temperature_units[1].lower():
        final_temperature = ((t - 273) * 1.8) + 32   #This converts Kelvin to Farenheit
        final_temperature = round(final_temperature, 3)
        unit2 = temperature_units[1]
    elif t_unit.lower() == temperature_units[2].lower():
        final_temperature = t                           #This converts Kelvin to Rankine scale
        final_temperature = round(final_temperature, 3)
        unit2 = temperature_units[2]
    else:
        return('\nError: Unsupported unit for temperature')

    return_statement = '\nFinal pressure: {0} {1}\nFinal Temperature: {2} {3}'.format(final_pressure, unit1, final_temperature, unit2)
    print(return_statement)

    return((final_pressure, final_temperature))


print(intensive_properties((101325,298),('atm', 'oC')))

print(intensive_properties((5874644,367),('bar', 'oF')))

print(intensive_properties((101325,298),('heat', 'oecx')))

print(intensive_properties((345,100),('Pa', 'oR')))

print(intensive_properties((126473,478),('mmHg', 'oC')))



