import cv2 as cv
import numpy as np


class rectDetector:
    def __init__(self, img) -> None:
        self.srcCopy = img.copy()
        # 压缩图片为同一大小
        self.width = 256
        self.height = 128
        # img = cv.resize(img, (self.width, self.height))
        # 将图片进行模糊处理
        self.src = cv.medianBlur(img, 11)
        # 将图片转换为灰度图
        self.src = cv.cvtColor(self.src, cv.COLOR_RGB2GRAY)
        # 自适应阈值化处理(对一个图像采用多个不同的阈值)
        # 当C越大，每个像素点的N*N邻域计算出的阈值就越小，中心点大于这个阈值的可能性也就越大，设置成255的概率就越大，整体图像白色像素就越多，反之亦然。
        # img = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, C=1)

        # TODO: 用颜色掩膜后得到感兴趣的区域（需要数据集）
        # 统一阈值处理(对一个图像采用一个阈值，阈值用OTSU算法计算)
        ret, self.src = cv.threshold(self.src, 100, 255, cv.THRESH_OTSU)

    # 传入处理好的图片，得到检测到的矩形
    def detect(self):
        # 寻找轮廓线
        cnts, hierachy = cv.findContours(
            self.src, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        for cnt in cnts:
            pass
        # TODO: 拟合多边形轮廓，提取矩形轮廓，过滤掉不感兴趣的轮廓，并考虑两个箱子叠在一起的情况
            # 绘制轮廓线
            # cv.drawContours(self.srcCopy, cnt, -1, (255, 0, 0), 4)


def videoDemo():
    cap = cv.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        dtr = rectDetector(frame)
        dtr.detect()
        if frame is None:
            print('--(!) No captured frame -- Break!')
            break
        if cv.waitKey(20) == 27:
            break


# TODO: 命令行运行文件 教程：https://zhuanlan.zhihu.com/p/56922793
# TODO: 和arduino进行串口通信
if __name__ == '__main__':
    videoDemo()
    cv.destroyAllWindows()
