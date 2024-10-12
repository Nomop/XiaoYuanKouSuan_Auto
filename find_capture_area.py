from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:  # 仅在按下鼠标时记录位置
        print(f'鼠标点击位置: X={x}, Y={y}')

def test_mouse_click_position():
    print("请点击鼠标以获取位置。按 Esc 退出。")
    
    # 监听鼠标点击事件
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()  # 让监听器保持活动状态，直到用户按下 Esc

if __name__ == "__main__":
    test_mouse_click_position()
