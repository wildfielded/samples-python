#!/usr/bin/python3

import requests

res = requests.request('GET', 'http://wildfielded.site')

if __name__ == '__main__':
    print(res.text)
    # print(res.headers)

#####=====----- THE END -----=====#########################################