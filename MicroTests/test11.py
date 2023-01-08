#!/usr/bin/python3

def domain_name(url_str: str) -> str:
    ''' Returns the "effective" domain name from URL string
    Arguments:
        url_str [str] -- URL string
    Returns:
        [str] -- Effective domain name
    '''
    subdom_list = ['co', 'com', 'org', 'edu', 'gov']
    doms_list = url_str.replace('http://', '')\
                       .replace('https://', '')\
                       .split('/', maxsplit=1)[0]\
                       .split('.')
    return doms_list[-2] if doms_list[-2] not in subdom_list else doms_list[-3]

''' =====----- MAIN -----===== '''
if __name__ == '__main__':
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
    assert domain_name('http://github.com/carbonfive/raygun') == "github"

#####=====----- THE END -----=====#########################################