# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:37:01 2024

@author: ADMIN
"""

import re
def is_valid_email(email):
  valid_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
  email_regex = r"^[^@]+@[^@]+\.[^@]+$"
  if not re.match(email_regex, email):
    return False
  username, domain = email.split("@")
  if len(username) < 6 or not username.isalnum():
    return False
  return domain in valid_domains
emails = ["nguyenvana@gmail.com", "abc@123.com", "hoang@gmail", "le.thi@yahoo.com"]
for email in emails:
  if is_valid_email(email):
    print(f"{email} is a valid email.")
  else:
    print(f"{email} is not a valid email.")