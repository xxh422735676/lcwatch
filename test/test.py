from bs4 import BeautifulSoup
import requests 
import json
import time
headers = {
    'authority': 'leetcode-cn.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'x-timezone': 'Asia/Shanghai',
    'x-operation-name': 'userPublicProfile',
    'accept-language': 'zh-CN',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'x-csrftoken': 'IgPXJvkZFazKMJIZ9jvE0rvSjtvyMLURhluj4ov9WupS1xSwvZGHbv0lUD4xNSlU',
    'dnt': '1',
    'x-definition-name': 'userProfilePublicProfile',
    'sec-ch-ua-platform': '"Android"',
    'origin': 'https://leetcode-cn.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://leetcode-cn.com/u/ycc-ustc/',
    'cookie': '_bl_uid=d7k5exbLahyb0U5esnay6L45U4aX; csrftoken=IgPXJvkZFazKMJIZ9jvE0rvSjtvyMLURhluj4ov9WupS1xSwvZGHbv0lUD4xNSlU; aliyungf_tc=4c4dc24a959cfce2c894f522f00ffe31589e298cb5a9fea83b4690fc1dc32924; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTk4MjM5MSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImRhZTFhMDA0YzE0ZmZlNDQzMTJkODNkNjVmOGVlZTBhZjhkMWNmZTRmZWRlNzFlYjhmYmUyZDZiYTU3YzU3NzgiLCJpZCI6MTk4MjM5MSwiZW1haWwiOiI0MjI3MzU2NzZAcXEuY29tIiwidXNlcm5hbWUiOiJ5aS1rdWFpLXFpYW4tZGUtemhlbmctbHVuIiwidXNlcl9zbHVnIjoieWkta3VhaS1xaWFuLWRlLXpoZW5nLWx1biIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLWNuLmNvbS9hbGl5dW4tbGMtdXBsb2FkL3VzZXJzL3lpLWt1YWktcWlhbi1kZS16aGVuZy1sdW4vYXZhdGFyXzE2MzM4NTM3ODUucG5nIiwicGhvbmVfdmVyaWZpZWQiOnRydWUsIl90aW1lc3RhbXAiOjE2NDA0MDEyODAuMDIxMzM3NSwiZXhwaXJlZF90aW1lXyI6MTY0Mjk2NDQwMCwibGF0ZXN0X3RpbWVzdGFtcF8iOjE2NDI1NTkwNjUsInZlcnNpb25fa2V5XyI6MH0.9RUV4lV4qRZIYQrJzjM0sBO-XBsOeROoQ_kh08NBqgM',
}

data = '{"operationName":"userPublicProfile","variables":{"userSlug":"ycc-ustc"},"query":"query userPublicProfile($userSlug: String!) {\\n  userProfilePublicProfile(userSlug: $userSlug) {\\n    username\\n    haveFollowed\\n    siteRanking\\n    profile {\\n      userSlug\\n      realName\\n      aboutMe\\n      userAvatar\\n      location\\n      gender\\n      websites\\n      skillTags\\n      contestCount\\n      asciiCode\\n      medals {\\n        name\\n        year\\n        month\\n        category\\n        __typename\\n      }\\n      ranking {\\n        rating\\n        ranking\\n        currentLocalRanking\\n        currentGlobalRanking\\n        currentRating\\n        ratingProgress\\n        totalLocalUsers\\n        totalGlobalUsers\\n        __typename\\n      }\\n      skillSet {\\n        langLevels {\\n          langName\\n          langVerboseName\\n          level\\n          __typename\\n        }\\n        topics {\\n          slug\\n          name\\n          translatedName\\n          __typename\\n        }\\n        topicAreaScores {\\n          score\\n          topicArea {\\n            name\\n            slug\\n            __typename\\n          }\\n          __typename\\n        }\\n        __typename\\n      }\\n      socialAccounts {\\n        provider\\n        profileUrl\\n        __typename\\n      }\\n      __typename\\n    }\\n    educationRecordList {\\n      unverifiedOrganizationName\\n      __typename\\n    }\\n    occupationRecordList {\\n      unverifiedOrganizationName\\n      jobTitle\\n      __typename\\n    }\\n    submissionProgress {\\n      totalSubmissions\\n      waSubmissions\\n      acSubmissions\\n      reSubmissions\\n      otherSubmissions\\n      acTotal\\n      questionTotal\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}'
url = 'https://leetcode-cn.com/graphql/'
response = requests.post(url, headers=headers, data=data)
pre = 0 
now = 0
cnt = 0
while(True):
    time.sleep(2)
    cnt = cnt+1
    now = response.json()['data']['userProfilePublicProfile']['submissionProgress']['acTotal']
    if now >  pre or cnt%100==0:
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open("stamp.txt","a") as f:
            f.write(str(date)+" : "+str(now)+"\n")
    pre = now

print('Bye')
