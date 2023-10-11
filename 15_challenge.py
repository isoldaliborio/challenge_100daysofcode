"""
Validating Email
Addresses With a
Filter
You are given an integer followed by email addresses. Your task is to print a list containing only
valid email addresses in lexicographical order.
Valid email addresses must follow these rules:
It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores
.
The website name can only have letters and digits .
The extension can only contain letters .
The maximum length of the extension is .
"""


def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, url = s.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False
    if username.replace("-", "").replace("_", "").isalnum() is False:
        return False
    elif website.isalnum() is False:
        return False
    elif extension.isalpha() is False:
        return False
    elif len(extension) > 3:
        return False
    else:
        return True


def filter_mail(x):
    return list(filter(fun, x))


n = 3
emails = ["lara@hackerrank.com", "brian-23@hackerrank.com", "britts_54@hackerrank.com"]

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
