import sqlite3

# Veritabanına bağlantı kurma
def get_db_connection():
    conn = sqlite3.connect('questions.db')  
    conn.row_factory = sqlite3.Row
    return conn

def add_questions():
    questions = [
        ("Python'da AI geliştirmek için hangi kütüphane yaygın olarak kullanılır?", "Pandas", "NumPy", "TensorFlow", "Matplotlib", 3),
        ("Bilgisayar görüşü (Computer Vision) alanında kullanılan popüler kütüphane nedir?", "OpenCV", "Scikit-learn", "Seaborn", "Flask", 1),
        ("NLP (Doğal Dil İşleme) alanında hangi yöntem, kelime anlamlarını vektörlere dönüştürmek için yaygın olarak kullanılır?", "Bag of Words", "TF-IDF", "Word2Vec", "KMeans", 3),
        ("Python'da AI modelinin eğitilmesi sırasında overfitting (aşırı öğrenme) sorunu nasıl çözülür?", "Daha fazla veri ile model eğitmek", "Modelin hiperparametrelerini artırmak", "Dropout tekniği kullanmak", "Modelin derinliğini artırmak", 3),
        ("Bir yapay zeka modelinde hangi optimizasyon algoritması genellikle kullanılır?", "Stochastic Gradient Descent (SGD)", "KMeans", "DBSCAN", "Linear Regression", 1),
        ("Python'da OpenCV ile bir görüntüdeki yüzleri tespit etmek için hangi fonksiyon kullanılır?", "cv2.findContours()", "cv2.faceCascade.detectMultiScale()", "cv2.faceRecognition()", "cv2.detectFaces()", 2),
        ("Natural Language Processing (NLP) için hangi Python kütüphanesi en yaygın kullanılanlardan biridir?", "Matplotlib", "NLTK", "Flask", "OpenCV", 2),
        ("Bir derin öğrenme modelinin doğruluğunu artırmak için genellikle hangi teknik kullanılır?", "Cross-validation", "Bagging", "Bootstrapping", "Feature engineering", 1)
    ]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.executemany('''
        INSERT INTO questions (question, option1, option2, option3, option4, correct_option)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', questions)

    conn.commit()
    conn.close()

add_questions()
