# GanarCRM

![avatar](ganarcrm_imgs/ganarcrm-1.png)
![avatar](ganarcrm_imgs/ganarcrm-2.png)
![avatar](ganarcrm_imgs/ganarcrm-3.png)
![avatar](ganarcrm_imgs/ganarcrm-4.png)
![avatar](ganarcrm_imgs/ganarcrm-5.png)
![avatar](ganarcrm_imgs/ganarcrm-6.png)
![avatar](ganarcrm_imgs/ganarcrm-7.png)
![avatar](ganarcrm_imgs/ganarcrm-8.png)

### For Vue

```
cd ganarcrm_vue
yarn install
yarn serve
yarn build
```

### For Django

```
cd ganarcrm_django
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### For Stripe

```
Install Stripe
cd stripe_folder
./stripe listen --forward-to 127.0.0.1:8000/api/v1/stripe/webhook/
```
