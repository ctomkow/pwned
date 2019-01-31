#!/usr/bin/env python3

# core imports
from getpass import getpass
import sys
import logging

# local imports
from .lpass.lpass import LPass
from .haveibeenpwned.haveibeenpwned import HaveIBeenPwned

# 3rd party imports
import click
import click_log

# logging
log = logging.getLogger(__name__)
click_log.basic_config(log)


class Pwned:

    def __init__(self):

        self.main()

    @click.group()
    @click_log.simple_verbosity_option(log)
    @click.pass_context
    def main(self):

        pass

    @main.command()
    @click.argument('lastpass', required=False)
    @click.option('--username', '-u', required=True, help='username/email used for lastpass')
    @click.option('--password', '-p', required=False, help='password used for lastpass')
    @click.option('--mfa', '-m', required=False, help='multi-factor authentication code for lastpass')
    @click.option('--interactive', '-i', required=False, is_flag=True, help='interactive prompts that does not echo secrets')
    @click.option('--haveibeenpwned', '-h', required=False, is_flag=True, help='check if passwords are in haveibeenpwned database')
    def lastpass(lastpass, username, password, mfa, interactive, haveibeenpwned):

        if interactive:
            password = getpass('password:')
            mfa = getpass('mfa code (empty for none):')
            if mfa == '':
                mfa = None

        lpass = LPass(username, password, mfa)
        id_list, username_list, password_list, url_list = lpass.connect()

        if haveibeenpwned:
            haveibeenpwned = HaveIBeenPwned()
            for pass_id, username, password, url in zip(id_list, username_list, password_list, url_list):
                if haveibeenpwned.check_password(password):
                    print(
                        "id:" + pass_id + "---" +
                        "username:" + username + "---" +
                        "password:" + password + "---" +
                        "url:" + url
                    )

    @main.command()
    @click.argument('password', required=False)
    @click.option('--interactive', '-i', required=False, is_flag=True, help='interactive prompts that does not echo secrets when you type')
    def password(password, interactive):

        if interactive:
            password = getpass('password:')

        haveibeenpwned = HaveIBeenPwned()

        try:
            password_exists = haveibeenpwned.check_password(password)
        except ValueError as error:
            log.error(error)
            sys.exit(1)

        if password_exists:
            print('password EXISTS in haveibeenpwned database')
        else:
            print('password DOES NOT EXIST in haveibeenpwned database')

    if __name__ == '__main__':

        Pwned()
