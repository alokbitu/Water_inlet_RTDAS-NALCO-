import os.path
import datetime, time
import pytz
import zipfile
from aesencrypt import *
from cfasf import *
from config import *
import math
import serial
import binascii

# Global variables
n = manningcoefficent
s = shgl
zip_data = ''
datfln = ''
zipfln = ''
lst = {}
add_to_dict = []
final_value = []

parameters = ["Discharge"]

iso_codes = ['12']

no_of_params = len(parameters)


class GetTime:
    def __init__(self):
        now_utc = datetime.datetime.utcnow()
        local_tz = pytz.timezone('Asia/Kolkata')  # Local timezone which we want to convert the UTC time
        now_utc = pytz.utc.localize(now_utc)  # Add timezone information to UTC time
        x = now_utc.astimezone(local_tz)  # Convert to local time

        self.timestamp = x.strftime('%Y-%m-%dT%H:%M:00Z')
        self.year = x.strftime('%Y')
        self.month = x.strftime('%m')
        self.date = x.strftime('%d')
        self.hour = x.strftime('%H')
        self.min_t = x.strftime('%M')
        self.seconds = x.strftime('%S')
        self.monthYear = x.strftime('%b%Y')
        self.flnts = x.strftime('%Y%m%d%H%M00')


def create_text_file(mon_folder, filename):
    text_filepath = os.path.join(mon_folder, filename)
    is_file = os.path.isfile(text_filepath)
    if is_file:
        # print("File Exists")
        pass
    else:
        text_filepath = os.path.join(mon_folder, filename)
        f = open(text_filepath, "a")
        f.write(plant_name + "\n")
        f.write(plant_address1 + "\n")
        f.write(plant_address2 + "\n")
        f.write(plant_country + "\n\n")
        heading = "{:<12}{:<15}{:<15}{:<25}{:<15}\n".format("plantid", "station_id", "parameters", "value",
                                                            "TimeStamp")
        f.write(heading)
        f.close()
        print("New Text File Created")


def add_data_to_bkpfile(mon_folder, filename, data):
    text_filepath = os.path.join(mon_folder, filename)
    f = open(text_filepath, "a")
    f.write(data)
    f.close()


def sensor_data():
    A9lv = [0x80, 0x04, 0x00, 0x01, 0x00, 0x09, 0x7F, 0xDD]  # A9lv---all 9 parameter value
    # gblv = [0x80, 0x03, 0x00, 0x06, 0x00, 0x01, 0x7A, 0x1A]  # gblv---gauge to bottom level

    ser = serial.Serial(port=comport, baudrate='9600', timeout=1)
    if not ser.is_open:
        ser.open()

    ser.flush()
    ser.flushInput()
    ser.flushOutput()
    ser.write(serial.to_bytes(A9lv))
    print(" Total command sent to Flow meter.")
    A9lv = ser.readall()
    ser.flush()
    ser.flushInput()
    ser.flushOutput()
    print(A9lv)
    hexstr1 = binascii.hexlify(A9lv).decode('utf-8')
    print(hexstr1)

    # hexstr1 = "08041200b6053a1f590000000002230000000000007777"
    water_hex = hexstr1[6:10]
    water_int = int(water_hex, 16) / 1000
    print("water_value is:" + ' ' + str(water_int))
    air_height = hexstr1[10:14]
    air_value = int(air_height, 16) / 1000
    print('air distance is:' + ' ' + str(air_value))

    #air_value = 1.484
    '''
    ser.write(serial.to_bytes(gblv))
    print("guage to bottom level command sent to Flow meter.")
    gblv = ser.readall()
    ser.flush()
    ser.flushInput()
    ser.flushOutput()
    print(gblv)
    hexstr2 = binascii.hexlify(gblv).decode('utf-8')
    print(hexstr2)



    # hexstr2 = '800302009885f0'

    gb_distance = hexstr2[6:10]
    #gb_value = int(gb_distance,16)/100
    print('total distance is:' + ' ' + str(gb_value))
    '''

    gb_value = 1.390  # height from the wall
    if air_value >= 1.5:
      water_level = 0
    else:

      water_level = gb_value - air_value

    print(gb_value)
    print(water_level)
    if water_level <= 0:
        water_level = 0
    return water_level


def calculate_data():
    height = float(sensor_data())   # converting string to float

    discharge = ((1.84 * width * ((height) ** 1.5)) * 3600) - 8.31
    print(discharge)
    # velocity = discharge / area

    print("height of water in tank:" + str(round(height, 6)) + " " + units_dict['height'])
    print("water Discharge to the tank is:" + str(round(discharge, 6)) + ' ' + units_dict['discharge'])

    final_value.append(round(discharge, 6))
    # print(final_value)

    dictionary = dict(zip(parameters, final_value))
    print(dictionary)

    file1 = open("current_discharge.txt", "w+")
    file1.write(str(round(discharge, 2)))
    file1.close()


def create_rawdata():
    parameter_codes = []
    for i in range(0, len(parameters)):
        index_of_parameter = parameters.index(parameters[i])
        iso_code = iso_codes[index_of_parameter]
        parameter_codes.append(iso_code)
    # print(parameter_codes)

    no_of_params = len(parameters)

    site_buff = site_id[5:]
    zip_data1 = ''
    zip_data2 = ''
    global zip_data
    zip_data = ''

    g = GetTime()
    yyyy = g.year
    yy = yyyy[2:]
    month = g.month
    date = g.date
    hour = g.hour
    min_t = g.min_t
    fts = g.flnts
    monyear = g.monthYear
    timestamp = g.timestamp

    global datfln
    datfln = site_id + "_" + station_name + "_" + fts + ".dat"
    global zipfln
    zipfln = site_id + "_" + station_name + "_" + fts + ".zip"

    textfln = fsw + date + month + yy + ".txt"

    month_folder = os.path.join(bkpfld_path, monyear)
    isdir1 = os.path.isdir(month_folder)
    if isdir1 == 0:
        os.mkdir(month_folder)

    create_text_file(month_folder, textfln)

    data1 = plant_name + '\n' + plant_address1 + '\n' + plant_address2 + '\n' + plant_country + '\n'
    data2 = "{:5d}    1\n".format(no_of_params)

    for param in range(no_of_params):
        data3 = "  1{}{:<16} {:<10}{:<18}3         0     0     \n".format(parameter_codes[param], parameters[param],
                                                                          units[param], analyzers[param])
        data4 = " {}{:<24}{:<10}{:<21}\n".format(site_buff, station_name, iso_latitude, iso_longtitude)
        zip_data1 = zip_data1 + data3 + data4

    for param in range(no_of_params):
        d0 = str("{:.6f}".format(final_value[param], 6))
        data5 = " {:<3}{:<5}   1{}{}{}{}{} 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1   1   0    1\nU {}\n". \
            format(parameter_codes[param], site_buff, yy, month, date, hour, min_t, d0)
        zip_data2 = zip_data2 + data5
    zip_data = data1 + data2 + zip_data1 + zip_data2
    print(zip_data)

    for i in range(0, no_of_params):
        d0 = str("{:.6f}".format(final_value[i], 6))
        bkp_data = "{:<12}{:<15}{:<15}{:<25}{:<15}{}\n".format(site_id, analyzers[i], station_name, parameters[i], d0,
                                                               timestamp)
        add_data_to_bkpfile(month_folder, textfln, bkp_data)
    add_data_to_bkpfile(month_folder, textfln, "\n")


# Create raw file with zip_data.
# This function is mainly written to check file format.
# This function is not needed to execute.
def create_rawfile():
    f = open('rawfile.txt', 'w')
    f.write(zip_data)
    f.close()


# Creates dat file with zip_data.
def create_datfile():
    enc_data = aes256cbc_encrypt(zip_data)
    f = open(datfln, 'wb')
    f.write(enc_data)
    f.close()


# Zips dat file.
def create_zipfile():
    with zipfile.ZipFile(zipfln, 'a', compression=zipfile.ZIP_DEFLATED) as my_zip:
        my_zip.write(datfln)
        my_zip.close()
    try:
        os.unlink(datfln)
    except:
        print("Error while deleting dat file: ", datfln)


def save_zipfile():
    # shutil.copy(zipfln, spcbdir)
    # shutil.copy(zipfln, spcb_realtime_path)
    shutil.copy(zipfln, cpcbdir)
    os.unlink(zipfln)


# Main function of this file
# Combine all functions in this file for simplicity
def zfgen_main():
    g = GetTime()
    secs = int(g.seconds)
    if secs % 30 == 0:
        sensor_data()
        calculate_data()
        if secs == 0:
            create_rawdata()
            create_datfile()
            create_zipfile()
            save_zipfile()
            final_value.clear()
    time.sleep(1)


if __name__ == "__main__":
    while True:
        zfgen_main()








