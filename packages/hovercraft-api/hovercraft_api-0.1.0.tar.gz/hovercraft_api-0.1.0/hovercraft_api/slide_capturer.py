import os
import time
import threading
import http.server
import socketserver
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
import cv2
import numpy as np

from art import *
from .utils import logger

# HTTPサーバーの設定
PORT = 8000

class SlideCapturer:
    def __init__(self, output_dir, port=PORT):
        self.output_dir = output_dir
        self.port = port

    def start_server(self):
        DIRECTORY = self.output_dir  # Hovercraftの出力ディレクトリをクラス変数として使用

        class Handler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=DIRECTORY, **kwargs)

        with socketserver.TCPServer(("", self.port), Handler) as httpd:
            logger.info(f"サーバーが http://localhost:{self.port} で起動しました")
            httpd.serve_forever()

    def capture_slides_as_png(self, fps=30, duration=5):
        server_thread = threading.Thread(target=self.start_server)
        server_thread.daemon = True
        server_thread.start()

        time.sleep(2)  # サーバーの起動を待つ

        options = Options()
        # options.add_argument('-headless')  # ヘッドレスモードを有効にする場合はコメントを外す
        driver = webdriver.Firefox(options=options)

        try:
            driver.get(f'http://localhost:{self.port}/index.html')

            slides = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'step'))
            )

            frame_count = 0
            for i in tqdm(range(len(slides)), desc="スライドのキャプチャ"):
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, f".step:nth-child({i+1})"))
                )

                # 各スライドをfps * duration回キャプチャ
                for j in range(fps * duration):
                    driver.save_screenshot(f'{self.output_dir}/slide_{frame_count:05d}.png')
                    frame_count += 1
                    time.sleep(1 / fps)

                if i < len(slides) - 1:
                    # トランジション中のフレームもキャプチャ
                    webdriver.ActionChains(driver).send_keys(Keys.RIGHT).perform()
                    for j in range(fps):  # 1秒間のトランジションを仮定
                        driver.save_screenshot(f'{self.output_dir}/slide_{frame_count:05d}.png')
                        frame_count += 1
                        time.sleep(1 / fps)

            logger.success("全てのスライドのキャプチャが完了しました。")
        except Exception as e:
            logger.error(f"キャプチャ中にエラーが発生しました: {str(e)}")
        finally:
            driver.quit()

    def create_video_from_images(self, image_folder, output_video_name, fps=30):
        images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
        images.sort()

        if not images:
            logger.error("画像ファイルが見つかりません。")
            return

        frame = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, layers = frame.shape

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video = cv2.VideoWriter(output_video_name, fourcc, fps, (width, height))

        for image in tqdm(images, desc="動画の作成"):
            video.write(cv2.imread(os.path.join(image_folder, image)))

        cv2.destroyAllWindows()
        video.release()
        logger.success(f"動画の作成が完了しました: {output_video_name}")
