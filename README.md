# Sosyal Medya Uygulaması

Bu proje, **Flask** framework'ü kullanarak geliştirilmiş temel bir sosyal medya uygulamasıdır. Kullanıcılar, hikayeler paylaşabilir, birbirlerini takip edebilir, beğenme/yorum yapabilir ve profillerini yönetebilir. Ayrıca, güvenlik önlemleri (şifre sıfırlama, e-posta doğrulama) ve kullanıcı deneyimi iyileştirmeleri de eklenmiştir.

---

## İçerik

1. [Uygulama Özellikleri](#uygulama-özellikleri)
2. [Kullanılan Teknolojiler](#kullanılan-teknolojiler)
3. [Kod Yapısı](#kod-yapısı)
4. [Çalışma Mantığı](#çalışma-mantığı)
5. [Kurulum ve Kullanım](#kurulum-ve-kullanım)

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
