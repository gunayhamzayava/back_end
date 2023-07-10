from django import template

register = template.Library()

@register.filter()
def toplama(num,addnum):
    return num + addnum

@register.filter()
def slash(str_):
    end = ""
    for i in str_:
        end += i + "/"
    return end

@register.filter()
def len_(str):
    if len(str)%2 == 0:
        return str[:51]+'...'
    elif len(str) %3== 0:
        return str[:52]+'...'
    else:
        return str[:50]+'...'
    


# for images path
@register.filter()
def lowers(a):
    a=a.lower()
    return a


@register.filter()
def tire(str):
    end = ''
    for i in str:
        end+= i+'-'
    return end