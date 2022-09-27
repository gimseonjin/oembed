# oembed
# readme

# **Application**

퍼플 아이오 사전 과제 oEmbed 사이트 입니다.

### **Development**

```
Based on Python 3.10
```

### **Requirement**

```
beautifulsoup4==4.11.1
certifi==2022.9.14
charset-normalizer==2.1.1
click==8.1.3
Flask==2.2.2
idna==3.4
itsdangerous==2.1.2
Jinja2==3.1.2
lxml==4.9.1
MarkupSafe==2.1.1
pyoembed==0.1.2
python-oembed==0.2.4
requests==2.28.1
soupsieve==2.3.2.post1
urllib3==1.26.12
Werkzeug==2.2.2
```

### **Build Setup**

```
pip3 install -r requirements.txt

python3 app.py
```

### How To Use

1. 메인 페이지로 이동하여 찾기 원하는 site url을 입력하세요


1. 입력 후, 오른쪽에 검색 버튼을 클릭하세요


1. 결과가 modal 형식으로 출력됩니다.


### Demo Site

주의 : flask 내부의 테스트 서버로 돌려서 과하게 사용 시, 서버가 다운될 수 있습니다.

```bash
http://ec2-54-180-138-133.ap-northeast-2.compute.amazonaws.com:5000/
```

### 인스타그램 oEmbed 검색이 되지 않는 이유 & 해결 방법

**인스타그램(meta)의 경우, oEmbed 데이터를 인증 받은 유저, 즉 토큰을 발급 받은 유저에게만 허용**합니다. 그 이유로 몇 가지 가설이 있으나 가장 유력한 것은 **“지적 재산권 침해 방지”, “oEmbed를 요청한 유저의 정확한 통계”** 로 볼 수 있습니다. 따라서 인스타그램 oEmbed를 사용하기 위해서는 토큰을 발급받아야 합니다.

실제 토큰 발급 요청을 보냈으나 아직까지 인증을 받지 못해서 테스트해보지 못했습니다.