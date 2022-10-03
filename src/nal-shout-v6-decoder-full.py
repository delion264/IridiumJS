#!/usr/bin/env python

#For full message format 30-byte length. Not PECOS or position only (10-bytes)

import struct
import sys

#data = "0600f469cb9c821b73002120c79158b2ca8a607d49c83f42c78a342b8214".decode('hex')
#data = "0600904dd7f0841b730001e9d79158b2ca8a809184a43f42c78a342b8204".decode('hex')
#data = "0600bc16ef98891b730061f8bd9158b2ca8acdfb2c503c42c78a342b8214".decode('hex')

def divide(extract_from, starting_at):
    return extract_from // starting_at, extract_from % starting_at


def strToHex(str): # Used to copy string representation hex bytes to an array. Takes a pair of characters.
    return hex(int(str, 16))


in_string = sys.argv[1]
hex_buffer = [strToHex(in_string[i:i+2]) for i in range(0, len(in_string), 2)]
hex_bytes = bytes([int(i, 0) for i in hex_buffer])
print("Input string: ", in_string)
print("hex_buffer: ", hex_buffer)

type, address, num2, num3, num4, num5, byte1, byte2 = struct.unpack("<BBQQQHBB", hex_bytes[:30])
print(type, address, num2, num3, num4, num5, byte1, byte2)

lat_deg, num2 = divide(num2, 1000000000000000)
lat_min, num2 = divide(num2, 10000000000000)
lat_thmin, num2 = divide(num2, 10000000000)
south, num2 = divide(num2, 1000000000)
lon_deg, num2 = divide(num2, 1000000)
lon_min, num2 = divide(num2, 10000)
lon_thmin, num2 = divide(num2, 10)
west = num2

pos_vervel, num3 = divide(num3, 10000000000000000000)
hour, num3 = divide(num3, 100000000000000000)
vdop_raw, num3 = divide(num3, 10000000000000)
print(num3)
year, num3 = divide(num3, 1000000000)
minute, num3 = divide(num3, 10000000)
secs, num3 = divide(num3, 100000)
millisecs, num3 = divide(num3, 10000)
print(num3)
num19, num3 = divide(num3, 100)
num20 = num3

pos_altitude, num4 = divide(num4, 10000000000000000000)
course_raw, num4 = divide(num4, 100000000000000)
byte3, num4 = divide(num4, 10000000000000)
altitude_raw, num4 = divide(num4, 100000000)
byte4, num4 = divide(num4, 10000000)
ground_vel_raw, num4 = divide(num4, 100)
canned_message_code = num4

month, num5_x = divide(num5, 1000)
day, num5_x = divide(num5_x, 10)
num26 = num5_x

sats = byte1 / 10
num27 = byte1 % 10

print("Canned Message Code:", canned_message_code)

print("Sats:", sats)

print("Time: %d-%02d-%02d %02d:%02d:%02d.%d" %(year, month, day, hour, minute, secs, millisecs * 100))

# Divide by 60 => minutes to degrees
# Divide by 10000 => 
lat = (lat_min + lat_thmin / 10000.) / 60. + lat_deg
if south:
    lat *= -1
print("Latitude:", lat)

lon = (lon_min + lon_thmin / 10000.) / 60. + lon_deg
if (lon_deg >= 180) | west:
    lon = 360 - lon
    lon *= -1
print("Longtitude:", lon)

altitude = altitude_raw/float(10**(5-byte3))
if pos_altitude == 0:
    altitude *= -1
print("Altitude:", altitude)

vervel = num27 * 100 + num26 * 10 + num19/10.
if pos_vervel == 0:
    vervel *= -1
print("Ver Vel:", vervel)

ground_vel = ground_vel_raw / float(10**(5-byte4))
print("Ground Vel:", ground_vel)

course = course_raw / 100.
print("Course:", course)

hdop = (west + num20) / 100.
print("HDOP:", hdop)

vdop = vdop_raw/ 100.
print("VDOP:", vdop)

# Bitwise flags/enum
fix_2d = byte2 & 1 == 1
print("2D Fix:", fix_2d)

routing_included = byte2 & 2 == 2
print("Routing Included", routing_included)

position_fix = byte2 & 4 == 4
print("Position Fix:", position_fix)

free_text_included = byte2 & 8 == 8
print("Free Text Included:", free_text_included)

emergency = byte2 & 16 == 16
print("Emergency:", emergency)

motion = byte2 & 32 == 32
print("Motion:", motion)

emerg_ack = byte2 & 64 == 64
print("Emergency Ack:", emerg_ack)
