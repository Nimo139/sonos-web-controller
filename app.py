from flask import Flask, render_template, request, redirect, url_for, Response  # For flask implementation
from soco import SoCo

app = Flask(__name__)
sonos = SoCo('192.168.178.105')


@app.route("/")
def main():
    track = sonos.get_current_track_info()
    volume = sonos.volume

    return render_template('index.html', track=track, volume=volume, playing=is_playing())


@app.route("/track")
def get_current_track():
    track = sonos.get_current_track_info()
    return track


@app.route("/state")
def get_state():

    state = sonos.get_current_track_info()
    # h:mm:ss to seconds
    state["position"] = time_to_seconds(state["position"])
    state["duration"] = time_to_seconds(state["duration"])

    state["is_playing"] = is_playing()
    state["volume"] = sonos.volume
    state.pop("metadata")

    return state


def time_to_seconds(time):
    time = time.split(":")
    return int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])


@app.route("/play")
def play():
    sonos.play()
    status_code = Response(status=200)
    return status_code


@app.route("/pause")
def pause():
    sonos.pause()
    status_code = Response(status=200)
    return status_code

@app.route("/next")
def next():
    sonos.next()
    status_code = Response(status=200)
    return status_code

@app.route("/previous")
def previous():
    sonos.previous()
    status_code = Response(status=200)
    return status_code

@app.route("/volume")
def volume():
    return str(sonos.volume)


@app.route("/volumeup")
def volumeup():
    sonos.volume += 1
    status_code = Response(status=200)
    return status_code


@app.route("/volumedown")
def volumedown():
    sonos.volume -= 1
    status_code = Response(status=200)
    return status_code


def is_playing():
    """
    Get the playing state (Playing/transitioning or Paused/stopped)
    :return: boolean
    """
    state = sonos.get_current_transport_info()['current_transport_state']
    return state in ['PLAYING', 'TRANSITIONING']


if __name__ == "__main__":
    app.run(host='127.0.0.1')
