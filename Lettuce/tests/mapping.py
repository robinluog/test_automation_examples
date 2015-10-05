#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
__author__ = 'Yevhen Vovchuk'

import datetime

email_pref = datetime.datetime.now().strftime("%d%b%Y%I%M%S")

site_mapping = {
    "header": {
        "button login": "//a[contains(text(),'Log in')]",
        "link release": "//img[@alt='Logo']",
        "user name": "//span[@id='user_name'][contains(text(),'Yevhen Vovchuk')]"
    },
    "sign up": {
        "url": "https://my-release.solidopinion.com/signup",
        "button facebook": "//a[contains(text(),'F')]",
        "button twitter": "//a[contains(text(),'T')]",
        "button vk": "//a[contains(text(),'V')]",
        "button google": "//a[contains(text(),'G')]",
        "button yahoo": "//a[contains(text(),'Y')]",
        "input name": "//input[@id='name']",
        "name": "YevhenVovchukYevhenVovchukYevhenVovchuk",
        "true name": "Yevhen Vovchuk",
        "input email": "//input[@id='email']",
        "email": str(email_pref) + "@gmail.com",
        "bad email": "vovchuke@gmailcom",
        "input password": "//input[@id='password']",
        "short password": "1",
        "password": "123456789012345678901234567890",
        "input re-password": "//input[@id='password2']",
        "button signup": "//button[@id='go_signup']",
        "link terms": "//form[contains(concat('',@class,''),'form-signin')]//a[contains(text(),'Terms and Policies')]",
        "link have account": "//div[@id='conteiner-signin']//a[contains(text(),'Already have an account?')]",
        "alert all empty": "//span[contains(text(),'All fields are required.')]",
        "alert empty name": "//span[contains(text(),'Apologies, \"Name\" allows only alphanumeric characters, hyphen, dash, underscores and spaces.')]",
        "alert invalid email": "//span[contains(text(),'Please enter a valid email address.')]",
        "alert empty password": "//span[contains(text(),\"Sorry, password can't be blank.\")]",
        "alert short password": "//span[contains(text(),'Password must have from 6 to 20 characters')]",
        "alert don't match passwords": "//span[contains(text(),'Oops! Your passwords don’t match, try again.')]",
        "button close alert": "//button[@class='close']"
    },
    "sign in": {
        "url": "https://my-release.solidopinion.com/signin",
        "input email": "//input[@id='email']",
        "input password": "//input[@id='password']",
        "button signin": "//button[@id='go_login_page']",
        "email": "vovchuke@gmail.com",
        "password": "123456789012345678901234567890"
    },
    "footer": {
        "link english": "//footer[@id='footer_public_menu']//a[contains(text(),'English')]",
        "link russian": "//footer[@id='footer_public_menu']//a[contains(text(),'Русский')]",
        "text copy right": "//footer[@id='footer_public_menu']//div[contains(text(),'SolidOpinion Inc. © 2015')]",
        "link help": "//footer[@id='footer_public_menu']//a[contains(text(),'Help')]",
        "link terms": "//footer[@id='footer_public_menu']//a[contains(text(),'Terms and Policies')]",
        "link contact us": "//footer[@id='footer_public_menu']//a[contains(text(),'Contact us')]",
    },
    "welcome": {
        "url": "http://my-release.solidopinion.com/welcome",
        "welcome title": "//div[@class='welcome-title'][contains(text(),'Welcome to SolidOpinion!')]"
    }
}
