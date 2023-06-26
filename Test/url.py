
"http://github.com/carbonfive/raygun"
'domain name = "github"'

def domain_name(st):
    return  st.split('http://')[-1].split('www.')[-1].split('.')[0]

print(domain_name("www.xakep.ru"))
print(domain_name("http://github.com/carbonfive/raygun"))