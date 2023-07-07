from flask import Flask, request
import detect_trafficSign
from flask import jsonify


app = Flask(__name__)

@app.route("/detect_image", methods=["POST"])
def detect_image():
    print("detect_image")
    # 指定本地保存路径
    img_Path = "data/img/traffic_sign.jpg"
    # 从请求中获取上传的图片文件
    image_file = request.files["image"]
    # 保存图片到指定路径
    image_file.save(img_Path)
    print("save to local host")
    # 调用检测函数

    traffic_sig = detect_trafficSign.detect_trafficSign(img_Path)
    #result="".join(traffic_sig)
    result_dict = {"result": traffic_sig}

    #返回检测结果的labelc
    return result_dict

def create_app():
    return app

if __name__ == "__main__":
    app.run()
