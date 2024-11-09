"""
Checks whether a given person is a good influencer, that is, whether the person has at least two
of the following accounts: Facebook, Twitter or Instagram.
"""

facebook = True
twitter = False
instagram = True

if sum((facebook, twitter, instagram)) > 1:
    print("You are a good influencer!")
