import requests

def test_baidu_homepage():
    # 发送GET请求到百度主页
    response = requests.get('https://www.baidu.com')
    
    # 验证响应状态码是否为200
    assert response.status_code == 200, "Expected status code 200, but got {}".format(response.status_code)