from urls import urls


def get_url_by_name(name):
    for item in urls:
        if item['name'] == name:
            return item['url']
    else:
        print('Please write correct name of company')

