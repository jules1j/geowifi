import folium
import json
from utils import mapper
import os

mapper.create_map()
def map_bssid_output(json_data):
    if json_data['data']['wigle']['lat'] != 'not_found':
        mapper.add_marker(json_data['data']['wigle']['lat'], json_data['data']['wigle']['lon'],
                          json_data['data']['bssid'])
    if json_data['data']['apple']['lat'] != 'not_found':
        mapper.add_marker(json_data['data']['apple']['lat'], json_data['data']['apple']['lon'],
                          json_data['data']['bssid'])
    if json_data['data']['openwifi']['lat'] != 'not_found':
        mapper.add_marker(json_data['data']['openwifi']['lat'], json_data['data']['openwifi']['lon'],
                          json_data['data']['bssid'])
    if json_data['data']['milnikov']['lat'] != 'not_found':
        mapper.add_marker(json_data['data']['milnikov']['lat'], json_data['data']['milnikov']['lon'],
                          json_data['data']['bssid'])
    filename = 'results/{}'.format(str(datetime.timestamp(datetime.now()))).replace('.', '_') + '.html'
    try:
        mapper.save_map(filename)
        print(
            ' [bold white][:world_map: ] Map output saved:[/bold white] [italic bright_green]{0}[/italic bright_green]'.format(
                filename))
    except:
        print(' [bold red][:red_circle:] Error saving output[/bold red]')
        print('')


def map_ssid_output(json_data):
    for result in json_data['results']:
        mapper.add_marker(result['lat'], result['lon'], args.ssid)
    filename = 'results/{}'.format(str(datetime.timestamp(datetime.now()))).replace('.', '_') + '.html'
    try:
        mapper.save_map(filename)
        print(



for dump in json_dumps:
    json.data = json.load(dump)
    map_ssid_output(json.data

