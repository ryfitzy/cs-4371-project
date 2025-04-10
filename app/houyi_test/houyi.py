import threading
import time

from flask import Response, render_template, stream_with_context

from original_HouYi import main

from . import bp


def tail_log():
    with open("output.log", "r") as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                yield line
            else:
                time.sleep(0.25)


@bp.route("/log")
def log_stream():
    def generate():
        for line in tail_log():
            yield f"data: {line.strip()}\n\n"

    # return stream_with_context(generate())
    return Response(generate(), mimetype='text/event-stream')


@bp.route("/")
def houyi_log():
    print("test")
    open("output.log", "w").close()
    threading.Thread(target=main.main).start()

    return render_template("test.html")
