from urls import urls

company_names = ['Orlen Lietuva','Circle', 'Viada', 'Neste', 
                 'Baltic Petroleum', 'Alausa', 'Jozita', 
                 'Emsi', 'Takuras', 'Abromika']

print(company_names)


def choose_company_by_name(company_name):
    for item in urls:
        if item['name'] == company_name.capitalize():
            return item['url']
    else:
        print('Please write correct name of company')


# print(choose_company_by_name(input('select the company: ')))