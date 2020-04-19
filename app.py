from flask import Flask, render_template, request

from mbta_finder import find_stop_near

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('static.html')



@app.route('/nearest', methods=['GET', 'POST'])
def find():
    # modify this function so it renders different templates for POST and GET method.
    # aka. it displays the form when the method is 'GET'; it displays the results when
    # the method is 'POST' and the data is correctly processed.
    if request.method == 'POST':
        try:
            result = request.form
            place = result["place"]
            station, wheelchair = find_stop_near(place)
            # return "Nearest Station: " + station + "<br>" + "Number of Accessible Wheelchairs = " + str(wheelchair)
            return render_template('right.html', nearest_station = station, wheelchairs = wheelchair)
        except:
            return render_template('error.html')




