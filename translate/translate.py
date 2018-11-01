import json
import requests


def translate(word):
    # 有道词典 api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # key 发送给有道词典服务器的内容
    key = {
        "type": "AUTO",
        "i": word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    response = requests.post(url, data=key)
    # 判断服务器是否响应成功
    if response.status_code == 200:
        return response.text
    else:
        print("调用失败")
        return None


def get_result(response):
    # 通过 json.loads 把返回的结果加载成 json 格式
    result = json.loads(response)
    print("input: %s" % result["translateResult"][0][0]["src"])
    print("output: %s" % result["translateResult"][0][0]["tgt"])


def main():
    word = input("Input the word: ")
    list_trans = translate(word)
    get_result(list_trans)


if __name__ == "__main__":
    main()
