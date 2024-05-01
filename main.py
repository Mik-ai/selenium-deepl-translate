import keyboard
import pyperclip
import time
import selenium_app 

def copy_paste_modify():
    # Получаем выделенный текст
    keyboard.send('ctrl+c')
    time.sleep(0.1)
    selected_text = pyperclip.paste()

    translated_text = selenium_app.translate_text(selected_text)
    print(translated_text)
    
    # Вставляем измененный текст обратно
    pyperclip.copy(translated_text)
    
    # Восстанавливаем выделенный текст
    keyboard.send('ctrl+v')

# Прослушиваем комбинацию клавиш Alt+Ctrl+E
keyboard.add_hotkey('f2', copy_paste_modify)

# Запускаем бесконечный цикл, чтобы скрипт продолжал работать
if __name__ == "__main__":
    keyboard.wait()
