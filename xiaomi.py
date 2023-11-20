import io
import re
import sys
import time

import utils.function as function

from utils.utils import get_config, w_log, s_log


def login(account, password):
    return function.login(account, password)


def info(cookie):
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    function.info(cookie)
    sys.stdout = old_stdout
    w_log(buffer.getvalue().replace('\n', ''))


def check_in(cookie):
    function.check_in(cookie)


def like(cookie):
    function.like(cookie)


def browse(cookie):
    function.browse(cookie)


def carrot(cookie):
    function.carrot(cookie)


def check_status(cookie):
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    function.check_status(cookie)
    sys.stdout = old_stdout
    satus = buffer.getvalue()
    satus_list = re.split(r'\n', satus)
    satus_list.remove('')
    for i in range(len(satus_list)):
        if i == len(satus_list) - 1:
            w_log(satus_list[i] + "\n")
        else:
            w_log(satus_list[i])


def main(account, password, acc_actions):
    for i in range(5):
        cookie = login(account, password)
        if len(cookie) != 0:
            break
        else:
            time.sleep(i)
    if len(cookie) == 0 or cookie == 'Error':
        w_log(f'{account}：登录失败')
    else:
        for action in acc_actions:
            eval(f'{action}(cookie)')


if __name__ == '__main__':
    configs = get_config()
    accounts = []
    passwords = []
    #uas = []
    actions_dict = {
        "check-in": "check_in",
        #"browse-user-page": "",
        "browse-post": "browse",
        "thumb-up": "like",
        #"browse-specialpage": "",
        #"board-follow": "",
        "carrot-pull": "carrot"}
    actions_list = [(key, value) for key, value in actions_dict.items()]
    accounts_actions = []
    for config in configs['accounts']:
        accounts.append(str(config['uid']))
        passwords.append(config['password'])
        #uas.append(config['user-agent'])
        actions = ['info']
        for a in actions_list:
            if config[a[0]]:
                actions.append(a[1])
        actions.append('check_status')
        accounts_actions.append(actions)
    for i in range(len(accounts)):
        #ua = uas[i]
        main(accounts[i], passwords[i], accounts_actions[i])
    s_log(configs.get('logging'))
