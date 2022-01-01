from flask import Flask, render_template, request, redirect, url_for  # For flask implementation
from soco import SoCo

app = Flask(__name__)
sonos = SoCo('192.168.178.105')


@app.route("/")
def main():
    track = sonos.get_current_track_info()
    volume = sonos.volume

    return render_template('index.html', track=track, volume=volume)


@app.route("/track")
def get_current_track():
    track = sonos.get_current_track_info()
    return track


if __name__ == "__main__":
    app.run(host='127.0.0.1')
