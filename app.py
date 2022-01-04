from flask import Flask, render_template, request, redirect, url_for, Response  # For flask implementation
from soco import discover

app = Flask(__name__)
# sonos = SoCo('192.168.178.105')
zones = list(discover())
zone_names = list(map(lambda z: z.player_name, zones))


@app.route("/")
@app.route("/<int:zone_id>/")
def main(zone_id: int = 0):
    track = zones[zone_id].get_current_track_info()
    volume = zones[zone_id].volume

    return render_template('index.html', track=track, volume=volume, playing=is_playing(zone_id), zone_names=zone_names)


@app.route("/<int:zone_id>/track")
def get_current_track(zone_id: int):
    track = zones[zone_id].get_current_track_info()
    return track


@app.route("/<int:zone_id>/state")
def get_state(zone_id: int):
    state = zones[zone_id].get_current_track_info()
    # h:mm:ss to seconds
    state["position"] = time_to_seconds(state["position"])
    state["duration"] = time_to_seconds(state["duration"])

    state["is_playing"] = is_playing(zone_id)
    state["volume"] = zones[zone_id].volume
    state.pop("metadata")

    return state


def time_to_seconds(time):
    time = time.split(":")
    return int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])


@app.route("/<int:zone_id>/play")
def play(zone_id: int):
    zones[zone_id].play()
    status_code = Response(status=200)
    return status_code


@app.route("/<int:zone_id>/pause")
def pause(zone_id: int):
    zones[zone_id].pause()
    status_code = Response(status=200)
    return status_code


@app.route("/<int:zone_id>/next")
def next(zone_id: int):
    zones[zone_id].next()
    status_code = Response(status=200)
    return status_code


@app.route("/<int:zone_id>/previous")
def previous(zone_id: int):
    zones[zone_id].previous()
    status_code = Response(status=200)
    return status_code


@app.route("/<int:zone_id>/volume")
def volume(zone_id: int):
    return str(zones[zone_id].volume)


@app.route("/<int:zone_id>/volumeup")
def volumeup(zone_id: int):
    zones[zone_id].volume += 1
    status_code = Response(status=200)
    return status_code


@app.route("/<int:zone_id>/volumedown")
def volumedown(zone_id: int):
    zones[zone_id].volume -= 1
    status_code = Response(status=200)
    return status_code


def is_playing(zone_id: int):
    """
    Get the playing state (Playing/transitioning or Paused/stopped)
    :return: boolean
    """
    state = zones[zone_id].get_current_transport_info()['current_transport_state']
    return state in ['PLAYING', 'TRANSITIONING']


if __name__ == "__main__":
    app.run(host='0.0.0.0')
