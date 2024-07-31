import csv
import requests
from PIL import Image
from io import BytesIO
from typing import Iterator, List


def read_csv(csv_file_path: str, skip_line: int=0) -> Iterator[List[str]]:
    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        # 创建 csv.reader 对象
        csv_reader = csv.reader(csvfile)
    
    for i in range(skip_line):
        next(csv_reader)
    
    return csv_reader

def download_image(url, save_path):
    try:
        # 发送HTTP GET请求获取图片内容
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功

        # 将响应内容转换为字节流
        img_data = BytesIO(response.content)

        # 使用Pillow打开图片
        img = Image.open(img_data)

        # 保存图片到指定路径
        img.save(save_path)
        print(f"Image successfully downloaded and saved to {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
    except IOError as e:
        print(f"Error saving image: {e}")