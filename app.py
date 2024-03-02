from flask import Flask, request, jsonify

app = Flask(__name__)

counter = {"requests made": 0}

@app.route("/count-requests")
def count_requests():
    counter["requests made"] += 1
    return jsonify(counter), 200


# @app.route("/count-requests")
# def count_requests():
#    return jsonify({"requests made": {+=1}}), 200


@app.route("/reset-counter", methods=['POST'])
def reset_requests():
    counter["requests made"] = 0
    return jsonify(counter), 201


if __name__=='__main__':
  app.run()