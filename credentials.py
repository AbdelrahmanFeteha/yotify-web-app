import os
from dotenv import load_dotenv

load_dotenv()

ClientID = os.getenv("SPOTIPY_CLIENT_ID")
ClientSecret = os.getenv("SPOTIPY_CLIENT_SECRET")

#youtube raw request headers
headers = """POST /youtubei/v1/log_event?alt=json&key=AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30 HTTP/3
Host: music.youtube.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br, zstd
Content-Type: application/json
Content-Length: 10668
Referer: https://music.youtube.com/
X-Goog-Request-Time: 1722411516160
X-Goog-Visitor-Id: CgtaSm5NTDhxWi1oTSj406e1BjIKCgJFRxIEGgAgPw%3D%3D
X-Goog-AuthUser: 2
X-Origin: https://music.youtube.com
X-Goog-Event-Time: 1722411514146
Content-Encoding: gzip
X-YouTube-Client-Name: 67
X-YouTube-Client-Version: 1.20240724.00.00
X-YouTube-Device: cbr=Firefox&cbrver=128.0&ceng=Gecko&cengver=128.0&cos=Windows&cosver=10.0&cplatform=DESKTOP
X-Youtube-Identity-Token: QUFFLUhqbmV6R2RmWFpwTnFJR3N1V2RKUi1VTmhvZFlaZ3w=
X-YouTube-Page-CL: 655489373
X-YouTube-Page-Label: youtube.music.web.client_20240724_00_RC00
X-YouTube-Utc-Offset: 180
X-YouTube-Time-Zone: Africa/Cairo
X-YouTube-Ad-Signals: dt=1722411514943&flash=0&frm&u_tz=180&u_his=3&u_h=864&u_w=1382&u_ah=816&u_aw=1382&u_cd=24&bc=31&bih=208&biw=1382&brdim=-6%2C-6%2C-6%2C-6%2C1382%2C0%2C1395%2C829%2C1382%2C207&vis=1&wgl=true&ca_type=image
Origin: https://music.youtube.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Authorization: SAPISIDHASH 1722411514_8fa7abe50ac01b650a632cbbdb83ec6abacd0fd6
Connection: keep-alive
Alt-Used: music.youtube.com
Cookie: VISITOR_INFO1_LIVE=ZJnML8qZ-hM; VISITOR_PRIVACY_METADATA=CgJFRxIEGgAgPw%3D%3D; _gcl_au=1.1.636097211.1722113002; SID=g.a000mQhshVaYJVRz8EJLe4byym5BW-Ndva8rACNhhDdjMyMXlvCG6cp45u7Evp1SnvJ8fe2pTAACgYKASYSARcSFQHGX2Mi7WvpzeiaPq69oqSqMxir4xoVAUF8yKp24v7VMyc-_YL9WfKN0-7c0076; __Secure-1PSIDTS=sidts-CjIB4E2dkRWtvBzAR1HgKlcJmbX_IuYhJ2Tt3vJ3CnoeziTHPJ-eH6BD4QhHN_7VqeuOQRAA; __Secure-3PSIDTS=sidts-CjIB4E2dkRWtvBzAR1HgKlcJmbX_IuYhJ2Tt3vJ3CnoeziTHPJ-eH6BD4QhHN_7VqeuOQRAA; __Secure-1PSID=g.a000mQhshVaYJVRz8EJLe4byym5BW-Ndva8rACNhhDdjMyMXlvCGiFC4WpZ77mjoO3pMTXWqNAACgYKAbcSARcSFQHGX2MiElt0VDAaCARbUO1dYR2YaBoVAUF8yKorfnsn7k8BHYgmvZwxXYDL0076; __Secure-3PSID=g.a000mQhshVaYJVRz8EJLe4byym5BW-Ndva8rACNhhDdjMyMXlvCGbqu22OcvcBq-vfuu7WPDwAACgYKAdQSARcSFQHGX2MiNL7gsPCEP2HnucDR2qlQTxoVAUF8yKpGxY7u-VALGNL3S0Jb9D8U0076; HSID=A0KJs48dM1kq5FyoK; SSID=A9KbKB1vxoembsxO2; APISID=wDX50sX4tSE84SxE/APN75oa_P3fadWzsO; SAPISID=OIli4htGUNS5_aIU/AZ6KwVuS3dcKXaSSw; __Secure-1PAPISID=OIli4htGUNS5_aIU/AZ6KwVuS3dcKXaSSw; __Secure-3PAPISID=OIli4htGUNS5_aIU/AZ6KwVuS3dcKXaSSw; LOGIN_INFO=AFmmF2swRQIgIgUB3-1YdH3m1AI5Asd0k9BKV7JyU2ROD2BV_OzLOtECIQDjLV1chWLnup3FZMHk9SByfUiJD989rjJUjjrxfEpoKw:QUQ3MjNmel9QUnE4blVCZEVhallqMTFuc1BEWHRfc3lNSDlFblNzdjNmYzBmSW54eV9meVFBaTA0YmY0NGRpU0ZaclY4d3ZnYUdQYWNyNGp6RnNTTXptT2t4QnBLUTFfdWQ1SVB2MkN4am9mZktEanQwU0diTi1pM3FWU0hhaHNaSHp6elhaSjQ3RHFEUzBjZlRYVDYxZXhjQllaX1lSeUZR; SIDCC=AKEyXzXUVgP7LfVv2ygShfofNJTXt9VJUMSQRl6t1HPbovZeewz9bD_DzM9PGjeWPy6RjC-cwzY; __Secure-1PSIDCC=AKEyXzVla2e7kZrMHHQzoyH5aOPvLIN17Quwo9vPHq1MClzEgxj4x7U9mwEVJiobS_Tdbv4OmW0; __Secure-3PSIDCC=AKEyXzV9_a6i0Ph8uZ0e0yl7_mX3jr7aNZWQkAGdYnPfVB6EQZzhk6Nn0BpD8ew5f40rxxoAStI; PREF=f4=4000000&tz=Africa.Cairo; YSC=BZnpiE5QeLE
TE: trailers"""