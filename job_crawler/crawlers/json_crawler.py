import requests
from typing import Dict, List

from job_crawler.config import CrawlerConfig

class JSONCrawler:
    def __init__(self, config: CrawlerConfig):
        self.url = config.url
        self.base_path_parts = config.base_path_parts
        self.criteria = config.params
        self.result_parts = config.result

    def __isSearchedJob(self, job: Dict[str, str]):
        for key, value in self.criteria.items():
            if value.startswith('%') or value.endswith('%'):
                if value.startswith('%') and value.endswith('%'):
                    if value[1:-1] not in job[key].lower():
                        return False
                else:
                    raise ValueError("Not supported single %% symbol")
            elif job[key].lower() != value:
                return False
        
        return True

    def __toResult(self, job):
        result = []
        for part in self.result_parts:
            result.append(f"{part}!\n{job[part]}")
        return "\n".join(result)

    def get_jobs(self) -> List[str]:
        response = requests.get(self.url)
        
        # navigate down the json to list of jobs
        data = response.json()
        for part in self.base_path_parts:
            data = data[part]
        
        return list(map(self.__toResult, (filter(self.__isSearchedJob, data))))
