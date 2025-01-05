import requests

# 文件 URLs 列表
urls = [
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_udp.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_http.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_https.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ws.txt",
    "https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/all.txt",
    "https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/best.txt",
    "https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/http.txt"
]

# 合并内容保存的文件名
output_file = "all.txt"  # Example file name

# 打开输出文件并以追加模式写入内容
with open(output_file, 'w', encoding='utf-8') as file:
    for url in urls:
        try:
            response = requests.get(url, timeout=10)  # 增加超时时间避免长时间卡住
            response.raise_for_status()  # 检查请求是否成功
            # 写入内容，保留换行符，只移除空行
            for line in response.text.splitlines():
                if line.strip():  # 只写入非空行
                    file.write(line + "\n")  # 保留换行符
        except requests.exceptions.RequestException as e:
            print(f"下载失败：{url}，错误信息：{e}")
