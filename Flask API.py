from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True
source = open("rainfall.txt", "r")
update = open("rainfall.txt", "a")
general_info = []

@app.route("/", methods=['GET', 'POST'])
def homepage():
    a = 1
    print("method used is %s" % request.method)
    for i in source.read().split("\n"):
        if i != "":
            dict = {i[0:-6]: i[-6:]}
            full = {a: dict}
            a += 1
            general_info.append(full)
    return jsonify(general_info)

@app.route("/add", methods=["POST"])
def requests():
    data = request.json.items()
    for i in data:
        info = i[0] + ", " + i[1] + "\n"
        update.write(info)
    update.close()
    return str(list(data))


@app.route("/city/<int:id>", methods=['GET', 'POST'])
def city(id):
    for i in general_info:
        for num, info in i.items():
            if id == num:
                return jsonify(info)
    else:
        return "ID not found"


@app.route("/cities", methods=['GET', 'POST'])
def cities():
    cities = []
    for i in general_info:
        for num, info in i.items():
            for t in info.keys():
                cities.append(t)
    return jsonify(cities)

@app.route("/rainfall", methods=['GET', 'POST'])
def rainfall():
    rainfalls = []
    for i in general_info:
        for city, rain in i.items():
            for t in rain.values():
                rainfalls.append(t)
    return jsonify(rainfalls)


app.run()

