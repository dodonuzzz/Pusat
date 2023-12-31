# -*- coding: utf-8 -*-
import openai
import os
import sys

def set_api_key():  
  try:
    openai.api_key = os.environ['OPENAI_API_KEY']
  except KeyError:
    sys.stderr.write("""
    You haven't set up your API key yet.
  
    If you don't have an API key yet, visit:
  
    https://platform.openai.com/signup

    1. Make an account or sign in
    2. Click "View API Keys" from the top right menu.
    3. Click "Create new secret key"

    Then, open the Secrets Tool and add OPENAI_API_KEY as a secret.
    """)
    exit(1)

  
text = "Merhaba! Ben Pusat. Evet, Türkçe karakterleri doğru şekilde kullanıyorsunuz. Ç, Ğ, ı, ö, ş, ü harflerini görebiliyorum. Size nasıl yardımcı olabilirim?"

set_api_key()

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", # only available if OpenAI has given you early access, otherwise use: "gpt-3.5-turbo"
  # 32K context gpt-4 model: "gpt-4-32k"
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": " Soru, yorum ve yanıtlarınızı buraya yazınız."}
        # Uygulamayı çalıştırmak için sorularınızı ve yanıtlarınızı role user content sözcüklerinin olduğu iki noktadan sonraki alana tırnak içinde yazınız.
        #{"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        #{"role": "user", "content": "Where was it played?"},
        #{"role": "user", "content": " ?"}
    ]
)
# Uygulamayı Pycharm'dan kullanmanız önerilir.
# Uygulamayı çalıştırmak için Terminal ekranına gelerek PS C:\Users\Doğukan\OneDrive\Masaüstü\BonySpitefulAdministration> python pusat.py (uygulamanın bilgisayarımda bulunduğu yol) şeklinde yazınız.
# Uygulamanın bilgisayarınızda bulunduğu yola terminal ekranınızda ulaştıysanız python pusat.py yazarak uygulamayı çalıştırabilirsiniz.
# Uygulamanın indirilmesi durumunda bilgisayarınızdaki yol (yani pusat.py dosyasının konumu) değişiklik gösterebilir.
#Terminal ekranını temizlemek için terminale (cevabın verildiği ekran) cls yazınız.

print(response['choices'][0]['message']['content'].encode('utf-8').decode('utf-8'))

input("Yeniden çalıştırmak için Enter tuşuna basın.")