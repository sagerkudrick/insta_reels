from instagrapi import Client
import datetime
from urllib import * 
import imageio
import config

username = config.username
password = config.password
filepath = config.filelocation
post_contents = config.postcontents

cl = Client()
cl.login(username, password)

user_id = cl.user_id_from_username(username)

try:
    media = cl.clip_upload(
        filepath,
        post_contents,
        extra_data={
            "custom_accessibility_caption": "alt text example",
            "like_and_view_counts_disabled": 1,
            "disable_comments": 1,
        }
    )


    media.dict()
    {'pk': 2573347427873726764,
    'id': '2573347427873726764_1903424587',
    'code': 'CO2Xdn6FCEs',
    'taken_at': datetime.datetime(2021, 5, 14, 10, 9, tzinfo=datetime.timezone.utc),
    'media_type': 2,
    'product_type': 'clips',
    'width': 900,
    'height': 900,
    'location': None,
    'user': {'pk': 1903424587,
    'username': username,
    'full_name': username,
    'profile_pic_url': HttpUrl('https://instagram.fhel5-1.fna.fbcdn.net/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg?tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_ohc=EtzrL0pAdg8AX-Xq8yS&edm=ACqnv0EBAAAA&ccb=7-4&oh=e2fd6a9d362f8587ea8123f23b248f1b&oe=60C2CB91&_nc_sid=9ec724', scheme='https', host='instagram.fhel5-1.fna.fbcdn.net', tld='net', host_type='domain', path='/v/t51.2885-19/s150x150/156689363_269505058076642_6448820957073669709_n.jpg', query='tp=1&_nc_ht=instagram.fhel5-1.fna.fbcdn.net&_nc_ohc=EtzrL0pAdg8AX-Xq8yS&edm=ACqnv0EBAAAA&ccb=7-4&oh=e2fd6a9d362f8587ea8123f23b248f1b&oe=60C2CB91&_nc_sid=9ec724'),
    'stories': []},
    'comment_count': 0,
    'like_count': 0,
    'has_liked': None,
    'caption_text': 'Caption text',
    'usertags': [],
    'video_url': None,
    'view_count': 0,
    'video_duration': 0.0,
    'title': '',
    'resources': []}

except imageio.core.NeedDownloadError:
    imageio.plugins.ffmpeg.download()
