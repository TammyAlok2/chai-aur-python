import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXITS videos (
                   id INTEGER PRIMARY KEY ,
                   name NOT NULL,
                   time TEXT NOT NULL,
                   
               )
               ''')

def list_videos():
    pass

def add_video():
    pass

def main() :
    while True:
        print("\n Youtube mangager app with DB ")
        print ("1. List videos ")
        print("2. Add videos ")
        print("3. Update videos ")
        print("4. Delete videos ")
        print ("5 . Exit app ")
        choice = input("Enter your choice : ") 
        
        if choice =="1":
            list_videos()   
        elif choice =="2":
            input("Enter the video name ")
            input("Enter the video time ")
            add_video(name,time)  
            
        elif choice =="3":
            input("Enter the video name ")
            input("Enter the video time ")
            delete_(name,time)  
            
              


if __name__ == "__main__":
    main()