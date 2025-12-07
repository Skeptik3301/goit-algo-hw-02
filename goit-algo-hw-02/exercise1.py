from queue import Queue
import time
import random


request_queue = Queue()

def generate_request(request_id):
    """
    Генерує нову заявку та додає її до черги.
    """
    print(f"-> Заявка #{request_id} створена та додана до черги.")
    request_queue.put(request_id)

def process_request():
    """
    Обробляє заявку, видаляючи її з черги.
    """
    if not request_queue.empty():
        
        current_request = request_queue.get()
        print(f"<- Заявка #{current_request} обробляється...")
       
        time.sleep(1) 
        print(f"   Заявка #{current_request} виконана.")
    else:
        print("Черга пуста. Немає заявок для обробки.")

def main():
    """
    Головний цикл програми.
    """
    request_id = 0
    try:
        print("Система запущена. Натисніть Ctrl+C для виходу.")
        while True:
           
            if random.random() > 0.3: 
                request_id += 1
                generate_request(request_id)
            
        
            process_request()
            
           
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("\nРоботу системи завершено користувачем.")

if __name__ == "__main__":
    main()