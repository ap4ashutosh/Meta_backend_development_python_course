# In this section we will find similarity between if and match
# as we always have to check one condition we may have to check multiple conditions
# error code of http

http_status = 200

if http_status == 200 or http_status == 201:
    print("success!")
elif http_status == 400:
    print("Bad request")
elif http_status == 404:
    print("Not found")
elif http_status == 500 or http_status == 501:
    print("server error")
else:
    print("unknown")

# now do this same using match
# match is similar to switch of c and introduced in version 3.10

# http_status = 200
"""
match http_status:
    case 200|201:
        print("Success!")
    case 400:
        print('Not found')
    case 500|501:
        print("server error")
    case _:
        print("unknown")
"""

# case _: this case is similar to default value in c

