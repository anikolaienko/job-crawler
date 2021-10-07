from typing import List

from job_crawler.config import crawlers_config, CrawlerType
from job_crawler.crawlers import JSONCrawler
from job_crawler.notifiers import TelegramNotifier

crawlers: List[JSONCrawler] = []
telegram_notifier = TelegramNotifier()

for crawler_config in crawlers_config:
    if crawler_config.type == CrawlerType.JSON:
        crawlers.append(JSONCrawler(crawler_config))

for crawler in crawlers:
    jobs = crawler.get_jobs()
    for job in jobs:
        telegram_notifier.send(job)
