import cv2
import pytesseract

# 确保将以下路径替换为你的 Tesseract 安装路径
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def test_tesseract(image_path):
    # 加载图像
    image = cv2.imread(image_path)
    
    if image is None:
        print("无法加载图像，请检查路径是否正确！")
        return

    # 将图像转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 应用阈值处理
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # 使用 Tesseract 进行文本识别
    text = pytesseract.image_to_string(thresh, config='--psm 6')
    
    # 打印识别结果
    print("识别结果:")
    print(text)

# 测试函数
if __name__ == "__main__":
    test_image_path = './a.png'  # 替换为你的图像路径
    test_tesseract(test_image_path)
