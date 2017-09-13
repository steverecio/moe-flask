from flask import Flask, render_template
import random

app = Flask(__name__)

RMS_PHOTOS = [
    "https://stallman.org/photos/rms-working/mid/mid_p1000844.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_0554.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_1755.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_3235.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_3658.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_img_4188.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_working-with-the-devil.jpg",
    "https://stallman.org/photos/rms-working/mid/mid_p1000541.jpg",
]

@app.route('/')
def moe():
    moe_src = random.choice(RMS_PHOTOS)
    return render_template('moe.html', moe_src=moe_src)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
