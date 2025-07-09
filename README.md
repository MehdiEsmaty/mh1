# پروژه mh1

این مخزن شامل یک پروژه نمونه با دو سرویس وب (یکی به زبان Python و دیگری به زبان Rust) و یک استک کامل مانیتورینگ و لاگینگ مبتنی بر Docker Compose است. همچنین، پایپلاین CI/CD با استفاده از GitLab برای تست، بیلد و دیپلوی خودکار پیاده‌سازی شده است.

---

## معرفی اجزای پروژه

### ۱. سرویس Python
- فریم‌ورک: Flask
- مسیر اصلی: `/Python/app.py`
- خروجی: پیام ساده «Hello from Python!» در روت

### ۲. سرویس Rust
- فریم‌ورک: Actix-web
- مسیر اصلی: `/Rust/src/main.rs`
- خروجی: پیام ساده «Hello from Rust!» در روت

### ۳. استک مانیتورینگ و لاگینگ
- **Prometheus**: جمع‌آوری متریک‌ها از سرویس‌ها و سیستم
- **Grafana**: داشبورد گرافیکی برای مشاهده متریک‌ها
- **cAdvisor**: مانیتورینگ کانتینرهای Docker
- **Node Exporter**: جمع‌آوری متریک‌های سیستمی
- **Blackbox Exporter**: تست سلامت endpointها
- **Loki**: ذخیره و جستجوی لاگ‌ها
- **Promtail**: جمع‌آوری و ارسال لاگ‌های کانتینرها به Loki

---

## پایپلاین GitLab CI/CD

در فایل `.gitlab-ci.yml` مراحل زیر تعریف شده است:

1. **تست**: اجرای تست‌های واحد برای هر دو سرویس Python و Rust
2. **بیلد**: ساخت ایمیج Docker برای هر سرویس
3. **دیپلوی**: اجرای اپلیکیشن‌ها و استک مانیتورینگ با استفاده از Docker Compose و بررسی سلامت سرویس‌ها

---

## راهنمای اجرا

### اجرای لوکال با Docker Compose

۱. ابتدا Docker و Docker Compose را نصب کنید.
۲. برای اجرای سرویس‌ها و مانیتورینگ:

```bash
# اجرای اپلیکیشن‌ها
sudo docker-compose up -d

# اجرای استک مانیتورینگ
cd monitoring
sudo docker-compose up -d
```

۳. دسترسی به سرویس‌ها:
- Python: http://localhost:5000
- Rust: http://localhost:8080
- Grafana: http://localhost:3000 (یوزر: admin، پسورد: secret)
- Prometheus: http://localhost:9090

### اجرای تست‌ها

#### Python
```bash
cd Python
python3 -m unittest test_app.py
```

#### Rust
```bash
cd Rust
cargo test
```

---

## وابستگی‌ها

### Python
- flask==2.0.1
- werkzeug<2.1.0

### Rust
- actix-web = "4"
- tokio = { version = "1", features = ["full"] }
- actix-rt = "2" (dev)

---

## نکات مهم
- برای ذخیره‌سازی داده‌های Loki، دایرکتوری‌های `monitoring/loki/chunks`، `monitoring/loki/index`، `monitoring/loki/cache` و ... باید وجود داشته باشند و دسترسی نوشتن داشته باشند.
- پیکربندی کامل سرویس‌ها در فایل‌های دایرکتوری `monitoring/` موجود است.
- برای شخصی‌سازی داشبوردها، می‌توانید به پوشه `monitoring/dashboards/` مراجعه کنید.

---

## توسعه‌دهنده
- این پروژه صرفاً جهت نمونه‌سازی و آموزش DevOps و مانیتورینگ طراحی شده است. 