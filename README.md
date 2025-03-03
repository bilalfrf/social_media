# Sosyal Medya Uygulaması

Bu proje, **Flask** framework'ü kullanarak geliştirilmiş temel bir sosyal medya uygulamasıdır. Kullanıcılar, hikayeler paylaşabilir, birbirlerini takip edebilir, beğenme/yorum yapabilir ve profillerini yönetebilir. Ayrıca, güvenlik önlemleri (şifre sıfırlama, e-posta doğrulama) ve kullanıcı deneyimi iyileştirmeleri de eklenmiştir.

---

## İçerik

1. [Uygulama Özellikleri](#uygulama-özellikleri)
2. [Kullanılan Teknolojiler](#kullanılan-teknolojiler)
3. [Kod Yapısı](#kod-yapısı)
4. [Çalışma Mantığı](#çalışma-mantığı)
5. [Kurulum ve Kullanım](#kurulum-ve-kullanım)
6. [English Section](#english-section)

---

## Uygulama Özellikleri

Bu uygulama kullanıcıların aşağıdaki işlemleri gerçekleştirmesine olanak tanır:

### 1. Hesap Oluşturma ve Giriş Yapma:
- Kullanıcılar, **e-posta adresleri** ve **şifreleri**yle kayıt olabilir.
- Kayıt olduktan sonra **e-posta doğrulaması** yapılır.
- Şifre sıfırlama işlevi mevcuttur.

### 2. Hikaye (Story) Paylaşma:
- Kullanıcılar **metin, fotoğraf** veya **video** içeren hikayeler paylaşabilir.
- Paylaşılan hikayeler **düzenlenebilir** veya **silinebilir**.

### 3. Beğenme ve Yorum Yapma:
- Kullanıcılar, hikayelere **beğenme** ve **yorum yapma** işlemleri gerçekleştirebilir.
- Yorumlar **beğenilebilir** veya **beğenilmeyebilir**.

### 4. Takip Etme ve Takipçi Yönetimi:
- Kullanıcılar birbirlerini **takip edebilir** veya **takipten çıkabilir**.
- **Profil sayfalarında** takipçi ve takip edilen kişi listeleri görüntülenebilir.

### 5. Profil Yönetimi:
- Kullanıcılar, kendi profillerini **görüntüleyebilir** ve **düzenleyebilir**.
- Diğer kullanıcıların profillerini ziyaret edebilir.

### 6. Güvenlik ve Doğrulama:
- **Şifreler**, güçlü şifre politikasına uygun olmalıdır.
- **E-posta doğrulama** ve **şifre sıfırlama** işlemleri mevcuttur.

---

## Kullanılan Teknolojiler

Bu proje, aşağıdaki teknolojiler ve kütüphaneler kullanılarak geliştirilmiştir:

- **Python**: Flask uygulamasının yazılım dili.
- **Flask**: Web framework.
- **Flask-Login**: Kullanıcı oturum yönetimi.
- **Flask-PyMongo**: MongoDB veritabanı bağlantısı.
- **Flask-Bcrypt**: Şifrelerin güvenli bir şekilde hash'lenmesi.
- **MongoDB**: Veritabanı olarak MongoDB kullanılmıştır.
- **HTML**: Web sayfalarının yapısı.
- **CSS**: Sayfaların stilini belirlemek için **Bootstrap** kullanıldı.
- **JavaScript**: Dinamik işlevler için kullanıldı.
- **Jinja2**: Flask ile dinamik içerik yerleştirmek için kullanıldı.
- **SMTP**: E-posta gönderme işlevselliği için kullanıldı (Gmail SMTP sunucusu).

---

## Kod Yapısı

### 1. `app.py` (Ana Uygulama Dosyası):
- Flask uygulamasının temel yapılandırmalarını içerir.
- **Blueprint'ler**: `auth` (kimlik doğrulama) ve `main` (ana işlevler) olarak ayrılmıştır.
- **Oturum Yönetimi**: Kullanıcı oturumlarının yönetimi yapılır.
- **MongoDB ve Bcrypt Başlatma**: Veritabanı ve şifre hash'leme işlemleri başlatılır.

### 2. `config.py` (Yapılandırma Dosyası):
- Gizli anahtar (`SECRET_KEY`) ve MongoDB bağlantı URI'si gibi yapılandırma bilgilerini içerir.

### 3. `models.py` (Veritabanı Modelleri):
- **User** sınıfı: Kullanıcı bilgilerini ve işlevlerini yönetir (şifre hash'leme, e-posta doğrulama, takip etme).
- MongoDB işlemleri: Kullanıcı oluşturma, güncelleme, silme ve sorgulama işlemleri yapılır.

### 4. `auth/routes.py` (Kimlik Doğrulama İşlemleri):
- **Kayıt Olma**: Kullanıcıların kaydını ve e-posta doğrulamasını yönetir.
- **Giriş Yapma**: Kullanıcıların giriş yapmasını sağlar.
- **Şifre Sıfırlama**: Kullanıcıların şifrelerini sıfırlamasına olanak tanır.
- **E-posta Doğrulama**: E-posta doğrulama işlemleri yapılır.

### 5. `main/routes.py` (Ana İşlevler):
- **Hikaye Yönetimi**: Kullanıcıların hikaye eklemesi, düzenlemesi ve silinmesi sağlanır.
- **Beğenme ve Yorum Yapma**: Hikayeleri ve yorumları beğenme işlemi yapılır.
- **Takip Etme**: Kullanıcıların birbirini takip etmesi sağlanır.
- **Profil Yönetimi**: Kullanıcı profillerinin düzenlenmesi sağlanır.

### 6. HTML Şablonları:
- `base.html`: Tüm sayfalar için temel şablon.
- `login.html`, `signup.html`: Kullanıcı girişi ve kaydolma sayfaları.
- `story.html`: Hikayelerin listelendiği ve yeni hikayelerin eklenebileceği sayfa.
- `profile.html`: Kullanıcı profillerinin görüntülendiği sayfa.
- `edit_story.html`, `edit_comment.html`: Hikaye ve yorum düzenleme sayfaları.

### 7. JavaScript İşlevleri:
- **Beğenme/Beğenmeme**: Hikayeler ve yorumlar için dinamik işlevsellik.
- **Bağlam Menüsü**: Sağ tıklama ile hikaye ve yorum düzenleme seçenekleri.

### 8. Veritabanı Güncelleme Scriptleri:
- `update_comments.py`: Yorumların benzersiz kimlikler (ID) ile güncellenmesini sağlar.
- `update_likes_dislikes.py`: Beğenilerin ve beğenmeyenlerin sayısal değerlere dönüştürülmesini sağlar.

---

## Çalışma Mantığı

### 1. Kullanıcı Kaydı ve Girişi:
- Kullanıcı kaydolurken **e-posta doğrulaması** yapılır.
- Giriş yaparken **şifre hash'leri** karşılaştırılır.

### 2. Hikaye Paylaşma ve Yönetme:
- Kullanıcılar **metin, fotoğraf** veya **video** içeren hikayeler paylaşabilir.
- Hikayeler **düzenlenebilir** ve **silinebilir**.

### 3. Beğenme ve Yorum Yapma:
- Kullanıcılar, hikayeleri ve yorumları **beğenebilir** veya **beğenmeyebilir**.
- **Beğeniler** ve **yorumlar** dinamik olarak güncellenir.

### 4. Takip Etme ve Profil Yönetimi:
- Kullanıcılar birbirlerini **takip edebilir** veya **takipten çıkabilir**.
- **Profil sayfalarında** takipçi ve takip edilen kişi listeleri görüntülenebilir.

### 5. Güvenlik:
- **Şifreler** güçlü şifre politikasına uygun olmalıdır.
- **E-posta doğrulama** ve **şifre sıfırlama** işlemleri mevcuttur.

---

## Kurulum ve Kullanım

### Gerekli Kütüphaneler:
```bash
pip install flask flask-login flask-pymongo flask-bcrypt
```

# English Section

# Social Media Application

This project is a basic social media application developed using the **Flask** framework. Users can share stories, follow each other, like/comment on posts, and manage their profiles. Additionally, security measures (password reset, email verification) and user experience improvements have been added.

---

## Content

1. [Application Features](#application-features)
2. [Technologies Used](#technologies-used)
3. [Code Structure](#code-structure)
4. [How It Works](#how-it-works)
5. [Installation and Usage](#installation-and-usage)

---

## Application Features

This application allows users to perform the following actions:

### 1. Account Creation and Login:
- Users can register with their **email address** and **password**.
- After registration, **email verification** is required.
- A password reset functionality is available.

### 2. Story Sharing:
- Users can share **text, photo**, or **video** stories.
- Shared stories can be **edited** or **deleted**.

### 3. Liking and Commenting:
- Users can **like** and **comment** on stories.
- Comments can be **liked** or **disliked**.

### 4. Following and Follower Management:
- Users can **follow** or **unfollow** each other.
- **Profile pages** display lists of followers and followees.

### 5. Profile Management:
- Users can **view** and **edit** their own profiles.
- They can also visit other users' profiles.

### 6. Security and Verification:
- **Passwords** must comply with strong password policies.
- **Email verification** and **password reset** processes are available.

---

## Technologies Used

This project is developed using the following technologies and libraries:

- **Python**: Programming language for the Flask application.
- **Flask**: Web framework.
- **Flask-Login**: User session management.
- **Flask-PyMongo**: MongoDB database connection.
- **Flask-Bcrypt**: Secure password hashing.
- **MongoDB**: Database used for data storage.
- **HTML**: Structure of the web pages.
- **CSS**: Styling of pages, with **Bootstrap** used.
- **JavaScript**: Used for dynamic functionality.
- **Jinja2**: Used to embed dynamic content in Flask.
- **SMTP**: Used for email sending functionality (Gmail SMTP server).

---

## Code Structure

### 1. `app.py` (Main Application File):
- Contains the basic configurations for the Flask application.
- **Blueprints**: Divided into `auth` (authentication) and `main` (core functionality).
- **Session Management**: Manages user sessions.
- **MongoDB and Bcrypt Initialization**: Initializes the database and password hashing.

### 2. `config.py` (Configuration File):
- Contains configuration details such as the secret key (`SECRET_KEY`) and MongoDB connection URI.

### 3. `models.py` (Database Models):
- **User** class: Manages user data and functionalities (password hashing, email verification, following).
- MongoDB operations: Create, update, delete, and query user data.

### 4. `auth/routes.py` (Authentication Operations):
- **Sign Up**: Manages user registration and email verification.
- **Login**: Handles user login.
- **Password Reset**: Allows users to reset their passwords.
- **Email Verification**: Handles email verification processes.

### 5. `main/routes.py` (Core Functions):
- **Story Management**: Allows users to add, edit, and delete stories.
- **Liking and Commenting**: Users can like or comment on stories.
- **Following**: Manages user following.
- **Profile Management**: Allows users to manage their profiles.

### 6. HTML Templates:
- `base.html`: Base template for all pages.
- `login.html`, `signup.html`: Pages for user login and registration.
- `story.html`: Page to list stories and allow new story submissions.
- `profile.html`: Page to view user profiles.
- `edit_story.html`, `edit_comment.html`: Pages to edit stories and comments.

### 7. JavaScript Functions:
- **Liking/Disliking**: Dynamic functionality for liking stories and comments.
- **Context Menu**: Right-click to edit or delete stories and comments.

### 8. Database Update Scripts:
- `update_comments.py`: Ensures comments are updated with unique identifiers (IDs).
- `update_likes_dislikes.py`: Converts like/dislike counts into numerical values.

---

## How It Works

### 1. User Registration and Login:
- Upon registration, **email verification** is required.
- During login, **password hashes** are compared.

### 2. Story Sharing and Management:
- Users can share **text, photo**, or **video** stories.
- Stories can be **edited** and **deleted**.

### 3. Liking and Commenting:
- Users can **like** or **dislike** stories and comments.
- **Likes** and **comments** are updated dynamically.

### 4. Following and Profile Management:
- Users can **follow** or **unfollow** other users.
- **Profile pages** display the follower and followee lists.

### 5. Security:
- **Passwords** must comply with a strong password policy.
- **Email verification** and **password reset** processes are included.

---

## Installation and Usage

### Required Libraries:
```bash
pip install flask flask-login flask-pymongo flask-bcrypt
