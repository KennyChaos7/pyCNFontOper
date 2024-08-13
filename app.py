from flask import Flask, redirect, url_for, request, render_template, send_from_directory,make_response
import OpecvUtils as opencv_utils
import os, time, datetime, json
BASE_PATH = 'static/'
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('/index.html', utc_dt=datetime.datetime.utcnow())


@app.route('/upload_img', methods=["POST"])
def upload_img():
    try:
        f = request.files['filepond']
        abs_filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ".png"
        filename = os.path.join(BASE_PATH, "", abs_filename)
        f.save(filename)
        print("{0} file upload succcessfully!".format(filename))
        time.sleep(1)
        return json.dumps({'filename':abs_filename}), 200, {'ContentType':'application/json'}
    except Exception as e:
        print(e)
        return e


@app.route('/op_unwrap_n_replace', methods=['GET',])
def unwrap_n_replace():
    filename = request.args.get('filename')
    # print(filename)
    # opencv_utils.unwrap_n_replace('png/20240808161848.png')
    output_filename = opencv_utils.unwrap_n_replace(
        os.path.join(BASE_PATH, "", filename)
    )
    response = make_response(output_filename, 200)
    response.mimetype = "text/plain"
    return response


@app.route('/op_unwrap_n_replace_2', methods=['GET',])
def unwrap_n_replace_2():
    filename = request.args.get('filename')
    # print(filename)
    # opencv_utils.unwrap_n_replace('png/20240808161848.png')
    output_filename = opencv_utils.unwrap_n_replace(
        os.path.join(BASE_PATH, "", filename)
    )
    # return json.dumps({'filename':output_filename}), 200, {'ContentType':'application/json'}
    return send_from_directory(BASE_PATH, output_filename, as_attachment=True)


@app.route('/compare_img', methods=['GET',])
def compare_img():
    filename1 = request.args.get('filename1')
    filename2 = request.args.get('filename2')
    ssim = opencv_utils.compare_img(
        os.path.join(BASE_PATH, "", filename1),
        os.path.join(BASE_PATH, "", filename2)
    )
    # return json.dumps({'filename':output_filename}), 200, {'ContentType':'application/json'}
    return json.dumps({'ssim':ssim}), 200, {'ContentType':'application/json'}


if __name__ == '__main__':
    app.run()
