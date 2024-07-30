import base64
import hashlib
import hmac
import logging
import time
import urllib
import requests
from scrapy import signals


class FailedRequestsLogger:
    def __init__(self, crawler):
        self.crawler = crawler
        self.logger = logging.getLogger(__name__)
        self.failed_requests = []

        self.secret = 'SEC702e64e2b79f447dd75eadc5a6d03a38b2096d6e428f565f52800725ff113116'
        self.dd_url = 'https://oapi.dingtalk.com/robot/send?access_token=bea06def58b6ef615c05fee3421c4b6825c550a4186b66e35e49c0ecdb08db91'


    @classmethod
    def from_crawler(cls, crawler):
        ext = cls(crawler)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(ext.spider_error, signal=signals.spider_error)
        return ext

    def spider_closed(self, spider):
        if self.failed_requests:
            self.logger.info("Failed Requests:")
            print(self.failed_requests)
            self.error_to_dd(self.failed_requests)
            for request in self.failed_requests:
                self.logger.info(f"URL: {request.url}, Tag: {request.meta.get('tag')}, retry_times: {request.meta.get('retry_times')}")
        else:
            self.logger.info("No failed requests detected.")


    def spider_error(self, failure, response, spider) -> dict:
        # 记录spider parse中抛出异常会调用
        self.logger.error(failure)
        request = response.request
        print('meta', request.meta)
        request.meta['response_status'] = response.status
        self.failed_requests.append(request)


    def error_to_dd(self, failed_requests):
        total = len(failed_requests)
        spider_name = self.crawler.spider.name
        urls = '、'.join([str(request.meta['request_tag']) for request in failed_requests])

        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": f"{spider_name}爬虫异常",
                "text": "**<font color={}>{}</font>**\n\n爬虫名称：{}\n\n失败请求数：{}\n\n失败请求标志：{}\n\n".format(
                    '#FF0000', f"{spider_name}爬虫异常",
                    spider_name,
                    total,
                    urls,
                )
            }
        }

        timestamp = str(round(time.time() * 1000))
        secret = self.secret
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        headers = {
            "Content-Type": "application/json; charset=utf-8",
        }
        params = {
            "timestamp": timestamp,
            "sign": sign
        }
        requests.post(self.dd_url, params=params, headers=headers, json=data)