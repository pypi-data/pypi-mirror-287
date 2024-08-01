import requests
import time

session = requests.Session


def login(username, password, print='no'):
    timetamp =time.time()
    login_data1 = {"identity":username,"scene":"","pid":"65edCTyg","deviceId":"","timestamp":timetamp}
    requests.post('https://open-service.codemao.cn/captcha/rule/v3',json=login_data1)
    login_data = {"identity":username,"password":password,"pid":"65edCTyg","agreement_ids":[-1]}
    result = requests.post(url='https://api.codemao.cn/tiger/v3/web/accounts/login',json=login_data)
    global co

    co = result.cookies

    code = str(result.status_code)
    global get

    def get():
        return (result.text)

    if code == '201':
        if print == 'yes':
            print("Login Successful[201]")
        else:
            return ('201')
    else:
        if print == 'yes':
            print("Login Failed[" + code + "]")
        else:
            return (code)


def logout(print='no'):

    result = requests.post(
        'https://api.codemao.cn/tiger/v3/web/accounts/loginout',headers=co)
    global get

    def get():
        return (result.text)

    if result.status_code == 204:
        if print == 'yes':
            print("Logout Successful[204]")
        else:
            return ('204')
    else:
        if print == 'yes':
            print("Logout Failed[" + str(result.status_code) + "]")
        else:
            return (str(result.status_code))


def usrinfo(kind, inputstr, inputint: int, print='no'):
    if kind == 'nick':

        change = {'nickname': inputstr}
        result = requests.patch("/tiger/v3/web/accounts/info", data=change,headers=co)

    if kind == 'full':

        change = {'fullname': inputstr}
        result = requests.patch("/tiger/v3/web/accounts/info", data=change,headers=co)

    if kind == 'desc':

        change = {'description': inputstr}
        result = requests.patch("/tiger/v3/web/accounts/info", data=change,headers=co)

    if kind == 'sex':

        change = {'sex': inputint}
        result = requests.patch("/tiger/v3/web/accounts/info", data=change,headers=co)

    if kind == 'birth':

        change = {'birthday	': inputint}
        result = requests.patch("/tiger/v3/web/accounts/info", data=change,headers=co)

    if kind == 'avat':

        change = {'avatar_url': inputstr}
        result = requests.patch("/tiger/v3/web/accounts/info", data=change,headers=co)
    global get

    def get():
        return (result.text)

    if result.status_code == 204:
        if print == 'yes':
            print("Change Info Successful[204]")
        else:
            return ('204')
    else:
        if print == 'yes':
            print("Change Info Failed[" + str(result.status_code) + "]")
        else:
            return (str(result.status_code))


def psc(old_password, new_password, print='no'):

    change = {
        'old_password': old_password,
        'password': new_password,
        'confirm_password': new_password
    }
    result = requests.patch("/tiger/v3/web/accounts/info", data=change,headers=co)

    global get

    def get():
        return (result.text)

    if result.status_code == 204:
        if print == 'yes':
            print("Change Password Successful[204]")
        else:
            return ('204')
    else:
        if print == 'yes':
            print("Change Password Failed[" + str(result.status_code) + "]")
        else:
            return (str(result.status_code))


def like(workid, print='no'):

    result = requests.post("https://api.codemao.cn/nemo/v2/works/" + workid +
                          "/like",headers=co)
    global get

    def get():
        return (result.text)

    if result.status_code == 201:
        if print == 'yes':
            print("Like Successful[201]")
        else:
            return ('201')
    else:
        if print == 'yes':
            print("Like Failed[" + str(result.status_code) + "]")
        else:
            return (str(result.status_code))


def coll(workid, print='no'):

    result = requests.post("https://api.codemao.cn/nemo/v2/works/" + workid +
                          "/collection",headers=co)
    global get

    def get():
        return (result.text)

    if result.status_code == 201:
        if print == 'yes':
            print("Collection Successful[201]")
        else:
            return ('201')
    else:
        if print == 'yes':
            print("Collection Failed[" + str(result.status_code) + "]")
        else:
            return (str(result.status_code))


def fork(workid, print='no'):

    result = requests.post("https://api.codemao.cn/nemo/v2/works/" + workid +
                          "/fork",headers=co)
    global get

    def get():
        return (result.text)

    if result.status_code == 201:
        if print == 'yes':
            print("Fork Successful[201]")
        else:
            return ('201')
    else:
        if print == 'yes':
            print("Fork Failed[" + str(result.status_code) + "]")
        else:
            return (str(result.status_code))


def follow(userid, print='no'):

    result = requests.post("https://api.codemao.cn/nemo/v2/user/" + userid +
                          "/follow",headers=co)
    global get

    def get():
        return (result.text)

    if result.status_code == 204:
        if print == 'yes':
            print("Fork Successful[204]")
        else:
            return ('204')
    else:
        if print == 'yes':
            print("Fork Failed[" + str(result.status_code) + "]")
        else:
            return (str(result.status_code))
        
def comment_w(workid, data, print='no'):

    result = requests.post("https://api.codemao.cn/creation-tools/v1/works/%d/comment" % workid,json=data,headers=co)
    global get

    def get():
        return (result.text)

    if result.status_code == 201:
        if print == 'yes':
            print("Work Comment Successful[201]")
        else:
            return ('201')
    else:
        if print == 'yes':
            print("Work Comment Failed[" + str(result.status_code) + "]")
        else:
            return (str(result.status_code))
