from threading import Thread
from time import sleep
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding= 'utf-8') as f:
        for i in range(1,word_count + 1):
            f.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start_time = datetime.now()

write_words(10, 'exemple1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = datetime.now()
print(f'Работа потоков {end_time - start_time}')

start_thread_time = datetime.now()

threads = []
threading_first = Thread(target=write_words, args=(10, 'example5.txt'))
threading_second = Thread(target=write_words, args=(30, 'example6.txt'))
threading_third = Thread(target=write_words, args=(200, 'example7.txt'))
threading_fourth = Thread(target=write_words, args=(100, 'example8.txt'))

threading_first.start()
threading_second.start()
threading_third.start()
threading_fourth.start()

threading_first.join()
threading_second.join()
threading_third.join()
threading_fourth.join()

end_thread_time = datetime.now()
print(f'Работа потоков {end_thread_time - start_thread_time}')
