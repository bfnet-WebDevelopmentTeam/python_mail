import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
load_dotenv()

send_addresses = ["bfnet.0911@gmail.com", "08010929829@docomo.ne.jp", "honuma596@gmail.com"]
msg = MIMEText("""
<html>
  <body>
    <p>BFネット株式会社<br>
    ご担当者様<br><br>
    突然のご連絡にて失礼いたします<br>
    BFコンシェルジュ合同会社の大沼です<br><br>
    この度、弊社は新サービス「助成金・補助金総合コンシェルジュサービス」の提供を開始いたしました。<br>
    こちらのサービスは成功報酬0円の助成金・補助金のサポートに加えて、ビジネスマッチングや健康管理などその他特典もついてくる究極のコンシェルジュサービスです。<br><br>
    --------------------------------------------------------<br><br>
    【新サービスの概要】<br>
    ▼サービス名<br>
    「助成金・補助金総合コンシェルジュ」<br><br>
    ▼サービス概要<br>
    200社様限定の成功報酬0円の助成金・補助金サポートに加えて、ビジネスマッチングや健康管理などその他特典も付いてくる究極のコンシェルジュサービスとなっております。<br><br>
    --------------------------------------------------------<br><br>
    現在、貴社がご使用できる助成金・補助金の無料診断キャンペーンを実施しております。<br>
    こちらでは受給資格のある助成金や、受給可能な金額が簡単にわかります。<br><br>
    つきましては、「助成金・補助金無料診断シート」と「本サービスの資料」を添付いたしましたので、お手空きの際にご覧いただければ幸いです。<br><br>
    ▼助成金・補助金無料診断シート<br>
    <a href="https://forms.gle/RDFK4TsXshC9BYFj6">https://forms.gle/RDFK4TsXshC9BYFj6</a><br><br>
    ▼本サービス資料<br>
    <a href="https://51.gigafile.nu/0626-cd9e1ae0cd72dec1f9e216f8b54991905">https://51.gigafile.nu/0626-cd9e1ae0cd72dec1f9e216f8b54991905</a><br><br>
    ご不明点などございましたら、下記問い合わせ先までご連絡ください。<br>
    何卒よろしくお願い申し上げます。<br><br>
    ＊--------------------------------------------------------＊<br>
    BFグループ/BFコンシェルジュ合同会社 広報部・営業部　大沼寛<br>
    〒107-0052<br>
    東京都港区赤坂1-1-17<br>
    細川ビル901<br>
    Email: info@bf-concierge.com<br>
    ＊--------------------------------------------------------＊
    </p>
  </body>
</html>""","html","utf-8")
for address in send_addresses:
    msg["From"] = "info@bf-concierge.com"
    msg["To"] = address
    msg["Subject"] = "助成金・補助金無料診断実施中！｜3分簡単入力で受給予想額をお出しします！"
    account = os.getenv('ACCOUNT')
    password = os.getenv('PASSWORD')

    smtp = smtplib.SMTP_SSL(host="mail13.onamae.ne.jp",port=465)
    smtp.login(account,password)
    smtp.send_message(msg)
    if __name__ == "__main__":
        print("Send OK!")
    smtp.quit()

