import teslajson


c = teslajson.Connection('email', 'password')
v = c.vehicles[0]
v.wake_up()
# v.command('auto_conditioning_start')
stat = v.data_request('climate_state')
stat2 = v.data_request('charge_state')

print("charge state:", stat2)

#start_time = datetime.timedelta

#while (datetime.timedelta - start_time) < 5

if stat['inside_temp'] > 37.7:
	v.command('auto_conditioning_start')
	print("TianGong air conditioner started:", stat['inside_temp'])
	v.command('set_temps',27.2)
if stat['inside_temp'] < 32.2:
	v.command('auto_conditioning_stop')
	print("TianGong air conditioner stopped:", stat['inside_temp'])

print(stat['driver_temp_setting'])
	
# v.command('set_temps', 25.0)

# print(stat['driver_temp_setting'])

#print(stat['inside_temp'])

#import struct
#print(dir(v.command.class))
