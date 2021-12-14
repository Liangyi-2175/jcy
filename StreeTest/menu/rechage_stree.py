from locust import HttpUser,User,between,task,HttpLocust
import json

class WebsiteTask(HttpUser):

    def on_start(self):
        pass

    @task(1)
    def index(self):
        url = '/api/order'
        body = {'fee': 1,'return_url': 'https://www.matpool.com/user','title': 'MatPool WEB 官方充值','type': 1}
        headers = {'cookie':'matpool_token=Bearer%20eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzgxNjk1MjUsIm9yaWdfaWF0IjoxNjM3NTY0NzI1LCJ1c2VyX2luZm8iOiJTTTIvaHFRSUJMSVFkaC9ONzdBNVBYWGV6TSs2L1JTdzFJNjJEeFVGMlBPYkJ1QnZLWEJQcEI3WllGR0NIVEZqazNuZXdWK3lIL3ozMVFFYXMydDdzblNMY21FWWNYbFM1VS9ib2oyZm0rSytCQlZPdE5tZ08rWUtKYmlYZUdBayIsInYiOiIwLjE0LjAifQ.DkGA56SQ9ekamKprNYe0-udNo7Jy_GtcdlDEhy1wT2Q; _pk_id.3.5368=65cfca5765f95525.1639105311.; _pk_ses.3.5368=1; token=Bearer%20eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2Mzk3MTAxMjQsIm9yaWdfaWF0IjoxNjM5MTA1MzI0LCJ1c2VyX2luZm8iOiJXV2JNckw3SmdGQjh3SHI1N0Jnb25BbEx0a1BzZjNtSTF0Z2FNL25SY2ZieTUvZFVEeWdXZ2xtbmFpblZ2K2UrV09iQzZ2NzNoWHZWcE1zQlFVNDk1Zk9NZlFFTzlQOUhFNWJ4Q2RXUHJLSW5uU05xdTU0L1ZJTGRGLzRIWTVrNiIsInYiOiIwLjE0LjAifQ.OknSnOtLXLRCpvFJtYOs8Mno5N7jwmiBkYkqTifoIJ4; _mat=Beta',
                   'authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2Mzk3MTAxMjQsIm9yaWdfaWF0IjoxNjM5MTA1MzI0LCJ1c2VyX2luZm8iOiJXV2JNckw3SmdGQjh3SHI1N0Jnb25BbEx0a1BzZjNtSTF0Z2FNL25SY2ZieTUvZFVEeWdXZ2xtbmFpblZ2K2UrV09iQzZ2NzNoWHZWcE1zQlFVNDk1Zk9NZlFFTzlQOUhFNWJ4Q2RXUHJLSW5uU05xdTU0L1ZJTGRGLzRIWTVrNiIsInYiOiIwLjE0LjAifQ.OknSnOtLXLRCpvFJtYOs8Mno5N7jwmiBkYkqTifoIJ4'}
        response = self.client.request('post',url,headers=headers,data=body)
        print(response.text)
        # if response.status_code == 200:
        #     response.success()
        #     print('成功',response.text)
        # else:
        #     response.failure("ss")
        #     print("失败：",response.text)

    def on_stop(self, force=False):
        pass
class WebsiteUser(User):
    task_set = WebsiteTask
    host = 'https://beta.matpool.com/'
    wait_time = between(0.1, 2)