

"""
  Proje Tanımı:
    Bir yapılacaklar listesi uygulaması oluşturun. Kullanıcı görev ekleyebilir,
    görevleri tamamlandı olarak işaretleyebilir ve tamamlananları silebilir.
  İstenilen Özellikler:
    Görev ekleme.
    Görevleri tamamlama ve tamamlandı olarak işaretleme.
    Görev listesini görüntüleme (tamamlananlar ve tamamlanmayanlar ayrı
    listelerde tutulabilir).
    Görev silme.
    Verileri bir .txt dosyasına kaydetme ve program çalıştığında yeniden yükleme.
  Yönerge:
    Bir Task (Görev) sınıfı oluşturun. Bu sınıf, görev adı ve tamamlanma
    durumunu (True/False) saklasın.
    Bir TaskManager sınıfı oluşturun. Bu sınıf, görevlerin eklenmesi,
    silinmesi ve yönetilmesi için gerekli metotları içersin.
"""
     
import os

class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

    def __str__(self):
        return f"[{ 'x' if self.completed else ' ' }] {self.name}"

class TaskManager:
    def __init__(self, filepath="tasks.txt"):
        self.filepath = filepath
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = not self.tasks[task_index].completed
            self.save_tasks()

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            self.save_tasks()

    def save_tasks(self):
        with open(self.filepath, "w") as f:
            for task in self.tasks:
                f.write(f"{task.name},{task.completed}\n")

    def load_tasks(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                for line in f:
                    name, completed = line.strip().split(",")
                    self.tasks.append(Task(name, completed == "True"))

    def list_tasks(self):
        print("Yapılacaklar:")
        for i, task in enumerate(self.tasks):
            if not task.completed:
                print(f"{i}. {task}")
        print("\nTamamlananlar:")
        for i, task in enumerate(self.tasks):
            if task.completed:
                print(f"{i}. {task}")

     

# Örnek kullanım
manager = TaskManager()

while True:
    print("\n1. Görev Ekle")
    print("2. Görevi Tamamla/İptal Et")
    print("3. Görevi Sil")
    print("4. Görevleri Listele")
    print("5. Çıkış")

    choice = input("Seçiminizi girin: ")

    if choice == "1":
        task_name = input("Görev adını girin: ")
        manager.add_task(Task(task_name))
    elif choice == "2":
        manager.list_tasks()
        task_index = int(input("Tamamlanacak/İptal edilecek görevin numarasını girin: "))
        manager.complete_task(task_index)
    elif choice == "3":
        manager.list_tasks()
        task_index = int(input("Silinecek görevin numarasını girin: "))
        manager.delete_task(task_index)
    elif choice == "4":
        manager.list_tasks()
    elif choice == "5":
        break
    else:
        print("Geçersiz seçim.")
    